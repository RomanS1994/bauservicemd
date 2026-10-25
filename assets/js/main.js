/* Small progressive enhancements. No cookies, tracking or persistent browser storage. */
(() => {
  'use strict';
  document.documentElement.classList.add('js');
  const toggle = document.querySelector('[data-menu-toggle]');
  const panel = document.querySelector('[data-mobile-drawer]');
  const desktop = window.matchMedia('(min-width: 1024px)');
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (toggle && panel && typeof panel.showModal === 'function') {
    let animation;
    let closing = false;
    let scrollY = 0;
    let bodyStyles;
    const lockedProperties = ['position', 'top', 'left', 'right', 'width', 'overflow'];
    const lockScroll = () => {
      scrollY = window.scrollY;
      bodyStyles = Object.fromEntries(lockedProperties.map((key) => [key, document.body.style[key]]));
      Object.assign(document.body.style, { position: 'fixed', top: `-${scrollY}px`, left: '0', right: '0', width: '100%', overflow: 'hidden' });
      document.documentElement.classList.add('mobile-menu-open');
    };
    const unlockScroll = () => {
      if (!bodyStyles) return;
      Object.assign(document.body.style, bodyStyles);
      bodyStyles = null;
      document.documentElement.classList.remove('mobile-menu-open');
      const previous = document.documentElement.style.scrollBehavior;
      document.documentElement.style.scrollBehavior = 'auto';
      window.scrollTo(0, scrollY);
      document.documentElement.style.scrollBehavior = previous;
    };
    const finishClose = () => {
      animation?.cancel();
      animation = null;
      if (panel.open) panel.close();
      toggle.setAttribute('aria-expanded', 'false');
      closing = false;
      unlockScroll();
      if (!desktop.matches) toggle.focus({ preventScroll: true });
    };
    const closeMenu = (immediate = false) => {
      if (!panel.open) return;
      if (immediate || reduced.matches || typeof panel.animate !== 'function') {
        finishClose();
        return;
      }
      if (closing) return;
      closing = true;
      animation?.cancel();
      animation = panel.animate([
        { transform: 'translateX(0)' },
        { transform: 'translateX(-100%)' }
      ], { duration: 340, easing: 'cubic-bezier(.4, 0, .2, 1)', fill: 'forwards' });
      animation.addEventListener('finish', finishClose, { once: true });
    };
    toggle.addEventListener('click', () => {
      if (desktop.matches || panel.open) return;
      lockScroll();
      panel.showModal();
      toggle.setAttribute('aria-expanded', 'true');
      if (!reduced.matches && typeof panel.animate === 'function') {
        animation = panel.animate([
          { transform: 'translateX(-100%)' },
          { transform: 'translateX(0)' }
        ], { duration: 480, easing: 'cubic-bezier(.22, 1, .36, 1)' });
      }
    });
    panel.querySelector('[data-menu-close]')?.addEventListener('click', () => closeMenu());
    panel.addEventListener('cancel', (event) => { event.preventDefault(); closeMenu(); });
    panel.addEventListener('click', (event) => { if (event.target.closest('a')) closeMenu(true); });
    panel.addEventListener('close', () => {
      toggle.setAttribute('aria-expanded', 'false');
      unlockScroll();
    });
    desktop.addEventListener('change', () => { if (desktop.matches) closeMenu(true); });
    reduced.addEventListener('change', () => {
      if (!reduced.matches) return;
      if (closing) finishClose();
      else animation?.cancel();
    });
    window.addEventListener('pagehide', () => closeMenu(true));
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
