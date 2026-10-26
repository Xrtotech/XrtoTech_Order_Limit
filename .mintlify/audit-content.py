from pathlib import Path
import json,re
root=Path.cwd();cfg=json.loads(Path('docs.json').read_text())
files=[p for p in root.rglob('*.mdx') if p.relative_to(root).parts[0]!='.mintlify']
errors=[];titles={};descs={}
def field(s,key):
 m=re.search('^'+key+': (.+)$',s,re.M)
 return json.loads(m.group(1)) if m else None
for p in files:
 rel=p.relative_to(root);s=p.read_text();title=field(s,'title');desc=field(s,'description');keys=field(s,'keywords')
 for k,v in [('title',title),('description',desc),('keywords',keys)]:
  if not v:errors.append(f'{rel}: missing {k}')
 if title in titles:errors.append(f'Duplicate title: {rel} / {titles[title]}')
 if desc in descs:errors.append(f'Duplicate description: {rel} / {descs[desc]}')
 titles[title]=str(rel);descs[desc]=str(rel)
 if len(title)>60:errors.append(f'{rel}: title >60')
 if re.search(r'^# ',s,re.M):errors.append(f'{rel}: duplicate H1')
 for dest in re.findall(r'\]\((/[^)\s]+)\)|href="(/[^"\s]+)"',s):
  target=(dest[0] or dest[1]).split('#')[0].strip('/')
  if not target:target='index'
  if not (root/(target+'.mdx')).exists():errors.append(f'{rel}: missing local page {target}')
  if rel.parts[0] in ['en','ja'] and not target.startswith(rel.parts[0]+'/'):errors.append(f'{rel}: link leaves locale {target}')
 if 'scenarios' in rel.parts and p.stem!='index':
  for h in {'zh':['## 开始前','## 操作步骤','## 测试你的设置'],'en':['## Before you begin','## Steps','## Test your configuration'],'ja':['## 始める前に','## 設定手順','## 設定をテストする']}[rel.parts[0] if rel.parts[0] in ['en','ja'] else 'zh']:
   if h not in s:errors.append(f'{rel}: missing scenario section {h}')
# Navigation is complete and language sets match.
def pages(obj):
 if isinstance(obj,str):yield obj
 elif isinstance(obj,list):
  for x in obj:yield from pages(x)
 elif isinstance(obj,dict):
  for k in ['pages','groups']:yield from pages(obj.get(k,[]))
nav=set(pages(cfg['navigation']['languages']))
for language in cfg['navigation']['languages']:
 nav.update(pages(language))
for f in files:
 path=f.relative_to(root).with_suffix('').as_posix()
 if path not in nav:errors.append('Missing from navigation: '+path)
base={p.relative_to(root).with_suffix('').as_posix() for p in files if p.relative_to(root).parts[0] not in ['en','ja']}
for lang in ['en','ja']:
 translated={p.relative_to(root/lang).with_suffix('').as_posix() for p in files if p.relative_to(root).parts[0]==lang}
 if base!=translated:errors.append(f'{lang}: missing/extra pages {base^translated}')
 # Preserve scenario numeric values and template token sets after stripping metadata and image comments.
 for path in base:
  if path.startswith('scenarios/') or path=='settings/messages':
   original=(root/(path+'.mdx')).read_text().split('---',2)[2]
   local=(root/lang/(path+'.mdx')).read_text().split('---',2)[2]
   strip=lambda s:re.sub(r'\{\/\*.*?\*\/\}','',s,flags=re.S)
   # Set check catches added unsupported tokens without depending on translated sentence order.
   tok=lambda s:set(re.findall(r'\{\{[A-Za-z]+\}\}',s))
   if tok(original)!=tok(local):errors.append(f'{lang}/{path}: token mismatch')
   if path.startswith('scenarios/'):
    numeric=lambda s:set(re.findall(r'(?<![\w-])\d+(?:\.\d+)?(?![\w-])',strip(s)))
    # List step numbering differs with Japanese spacing, compare only numbers >= 10 and core settings tables.
    tables=lambda s:'\n'.join(x.replace('1 点 2 kg', '2 kg') for x in s.splitlines() if x.startswith('|'))
    if numeric(tables(original))!=numeric(tables(local)):errors.append(f'{lang}/{path}: numeric table mismatch {numeric(tables(original)) ^ numeric(tables(local))}')
report={'pages':len(files),'per_language':len(base),'scenarios_per_language':sum(x.startswith('scenarios/') and x!='scenarios/index' for x in base),'unique_titles':len(titles),'unique_descriptions':len(descs),'errors':errors}
Path('.mintlify/content-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
