> For Mintlify product knowledge (components, configuration, writing standards),
> install the Mintlify skill: `npx skills add https://mintlify.com/docs`

# Documentation project instructions

## About this project

- This is a documentation site built on [Mintlify](https://mintlify.com)
- Pages are MDX files with YAML frontmatter
- Configuration lives in `docs.json`
- Use the Mintlify MCP server, `https://mcp.mintlify.com`, to edit content and settings via MCP
- Use the Mintlify docs MCP server, `https://www.mintlify.com/docs/mcp`, to query information about using Mintlify via MCP

## Terminology

- Site names: 订单限制帮助中心 / Order Limits Help Center / 注文制限ヘルプセンター. Do not show the vendor brand.
- Chinese app display name: 订单限购. Preserve actual UI labels when explaining app settings.
- Write for Shopify merchants and store operators.
- Keep product-level, variant-level, individual, combined, and cumulative limits distinct.

## Style preferences

- Chinese is the primary and default documentation language. Provide complete Japanese and English versions.
- Keep Chinese pages at the existing root paths, Japanese under `ja/`, and English under `en/`.
- Keep page structure, scenario values, supported template tokens, and feature boundaries aligned across all three languages.
- Localize internal links and navigation. Do not link translated pages back to Chinese by default.
- App UI labels currently come from Chinese source. Translated instructions must include a way to find the actual labels.
- Use the supplied logo, brand purple `#A07EC8`, and a strict light-only theme.

- Use active voice and second person ("you")
- Keep sentences concise — one idea per sentence
- Use sentence case for headings
- Bold for UI elements: Click **Settings**
- Code formatting for file names, commands, paths, and code references

## Content boundaries

- Document verified merchant-facing capabilities from the adjacent `xiangou` source.
- Prioritize scenario recipes with settings, steps, expected allowed/blocked cases, and limitations.
- Do not infer capabilities from competitor documentation.
- Do not invent plans, prices, support contacts, compatibility guarantees, or app UI translations.
- Keep internal implementation and source-review notes in `.mintlify/`, outside merchant guides.
