/* Small progressive enhancements. No cookies, tracking or persistent browser storage. */
(() => {
  'use strict';
  document.documentElement.classList.add('js');
  const toggle = document.querySelector('[data-menu-toggle]');
  const menu = document.querySelector('[data-menu]');
  if (toggle && menu) {
    const setOpen = (open) => {
      toggle.setAttribute('aria-expanded', String(open));
      menu.classList.toggle('is-open', open);
      menu.setAttribute('data-open', String(open));
    };
    toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
    menu.addEventListener('click', (event) => {
      if (event.target.closest('a')) setOpen(false);
    });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        toggle.focus();
      }
    });
    document.addEventListener('click', (event) => {
      if (!event.target.closest('.site-header')) setOpen(false);
    });
    window.matchMedia('(min-width: 1024px)').addEventListener('change', () => setOpen(false));
  }


})();

// A single accessible image viewer; ordinary image links remain usable without JavaScript.
(() => {
  const dialog = document.querySelector('[data-gallery-dialog]');
  if (!dialog || typeof dialog.showModal !== 'function') return;
  const links = [...document.querySelectorAll('[data-gallery-image]')];
  const photos = links.filter((link, index) => links.findIndex((item) => item.href === link.href) === index);
  const image = dialog.querySelector('[data-gallery-photo]');
  let current = 0;
  let opener;
  let previousOverflow;
  const show = (index) => {
    current = (index + photos.length) % photos.length;
    const photo = photos[current];
    image.src = photo.href;
    image.alt = photo.dataset.caption;
    dialog.querySelector('[data-gallery-caption]').textContent = photo.dataset.caption;
    dialog.querySelector('[data-gallery-counter]').textContent = `${current + 1} / ${photos.length}`;
  };
  links.forEach((link) => link.addEventListener('click', (event) => {
    if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || event.button !== 0) return;
    event.preventDefault();
    opener = link;
    show(photos.findIndex((photo) => photo.href === link.href));
    previousOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    dialog.showModal();
  }));
  dialog.querySelector('[data-gallery-close]').addEventListener('click', () => dialog.close());
  dialog.querySelector('[data-gallery-prev]').addEventListener('click', () => show(current - 1));
  dialog.querySelector('[data-gallery-next]').addEventListener('click', () => show(current + 1));
  dialog.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
      event.preventDefault();
      show(current + (event.key === 'ArrowLeft' ? -1 : 1));
    }
  });
  dialog.addEventListener('click', (event) => { if (event.target === dialog) dialog.close(); });
  dialog.addEventListener('close', () => {
    document.body.style.overflow = previousOverflow || '';
    opener?.focus();
  });
  let touchX;
  image.addEventListener('touchstart', (event) => { touchX = event.changedTouches[0].clientX; }, { passive: true });
  image.addEventListener('touchend', (event) => {
    const delta = event.changedTouches[0].clientX - touchX;
    if (Math.abs(delta) > 55) show(current + (delta < 0 ? 1 : -1));
  }, { passive: true });
})();
