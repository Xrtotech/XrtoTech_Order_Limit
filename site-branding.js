// Mintlify has one global site name; localize the shared chrome on language changes.
(() => {
  const brands = {
    zh: { name: '订单限购帮助中心', logo: '/logo/order-limit.svg' },
    en: { name: 'Order Limits Help Center', logo: '/logo/order-limit-en.svg' },
    ja: { name: '注文制限ヘルプセンター', logo: '/logo/order-limit-ja.svg' },
  };
  const updateBrand = () => {
    const language = document.documentElement.lang.split('-')[0];
    const brand = brands[language] || brands.zh;
    document.querySelectorAll('img.nav-logo').forEach((logo) => {
      if (logo.getAttribute('src') !== brand.logo) logo.setAttribute('src', brand.logo);
      if (logo.alt !== brand.name) logo.alt = brand.name;
      const link = logo.closest('a');
      if (link && link.getAttribute('aria-label') !== brand.name) {
        link.setAttribute('aria-label', brand.name);
      }
    });
    const title = document.title.replace(/ - (订单限购帮助中心|Order Limits Help Center|注文制限ヘルプセンター)$/, ` - ${brand.name}`);
    if (document.title !== title) document.title = title;
  };
  let scheduled = false;
  new MutationObserver(() => {
    if (scheduled) return;
    scheduled = true;
    requestAnimationFrame(() => { scheduled = false; updateBrand(); });
  }).observe(document.documentElement, {
    subtree: true, childList: true, characterData: true,
    attributes: true, attributeFilter: ['lang'],
  });
  updateBrand();
})();
