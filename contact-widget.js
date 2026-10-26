// Use the same contact QR code as the app, on every documentation page.
(() => {
  if (document.getElementById('contact-widget')) return;

  const copy = {
    zh: {
      button: '有问题？联系我们', title: '微信联系我们',
      hint: '微信扫一扫，添加微信沟通', qr: '微信联系二维码', close: '关闭',
    },
    ja: {
      button: 'お困りですか？お問い合わせ', title: 'WeChat でお問い合わせ',
      hint: 'WeChat でコードをスキャンしてお問い合わせください', qr: 'WeChat お問い合わせ用 QR コード', close: '閉じる',
    },
    en: {
      button: 'Questions? Contact us', title: 'Contact us on WeChat',
      hint: 'Scan with WeChat to get in touch', qr: 'WeChat contact QR code', close: 'Close',
    },
  };
  const widget = document.createElement('div');
  widget.id = 'contact-widget';
  widget.innerHTML = `
    <section id="contact-widget-panel" aria-labelledby="contact-widget-title" hidden>
      <div class="contact-widget-header">
        <h2 id="contact-widget-title"></h2>
        <button class="contact-widget-close" type="button">×</button>
      </div>
      <img class="contact-widget-qr" src="/images/wechat-contact-qr.svg" width="205" height="205" alt="">
      <p class="contact-widget-hint"></p>
    </section>
    <button class="contact-widget-trigger" type="button" aria-expanded="false" aria-controls="contact-widget-panel">
      <img src="/images/wechat-logo.png" width="28" height="28" alt="">
      <span></span>
    </button>`;
  const panel = widget.querySelector('section');
  const trigger = widget.querySelector('.contact-widget-trigger');
  const close = widget.querySelector('.contact-widget-close');
  const setOpen = (open, restoreFocus = false) => {
    panel.hidden = !open;
    trigger.setAttribute('aria-expanded', String(open));
    if (open) close.focus();
    if (restoreFocus) trigger.focus();
  };
  const localize = () => {
    const pathLanguage = location.pathname.split('/')[1];
    const text = copy[pathLanguage] || copy.zh;
    trigger.querySelector('span').textContent = text.button;
    trigger.setAttribute('aria-label', text.button);
    widget.querySelector('h2').textContent = text.title;
    widget.querySelector('.contact-widget-hint').textContent = text.hint;
    widget.querySelector('.contact-widget-qr').alt = text.qr;
    close.setAttribute('aria-label', text.close);
  };
  trigger.addEventListener('click', () => setOpen(panel.hidden));
  close.addEventListener('click', () => setOpen(false, true));
  document.addEventListener('pointerdown', (event) => {
    if (!panel.hidden && !widget.contains(event.target)) setOpen(false);
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && !panel.hidden) setOpen(false, widget.contains(document.activeElement));
  });
  window.addEventListener('mintlify:navigate', () => {
    setOpen(false);
    localize();
    if (!widget.isConnected) document.body.append(widget);
  });
  localize();
  document.body.append(widget);
})();
