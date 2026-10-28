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
      const currentTransform = getComputedStyle(panel).transform;
      animation?.cancel();
      animation = panel.animate([
        { transform: currentTransform === 'none' ? 'translateX(0)' : currentTransform },
        { transform: 'translateX(-100%)' }
      ], { duration: 600, easing: 'cubic-bezier(.65, 0, .35, 1)', fill: 'forwards' });
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
        ], { duration: 800, easing: 'cubic-bezier(.65, 0, .35, 1)' });
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
  if (!photos.length || !image) return;
  let current = 0;
  let requested = 0;
  let requestVersion = 0;
  let opener;
  let previousOverflow;
  const counter = dialog.querySelector('[data-gallery-counter]');
  const caption = dialog.querySelector('[data-gallery-caption]');
  const loadError = {
    uk: 'Не вдалося завантажити фото. Спробуйте ще раз.',
    de: 'Das Foto konnte nicht geladen werden. Bitte erneut versuchen.',
    en: 'The photo could not be loaded. Please try again.'
  }[document.documentElement.lang] || 'The photo could not be loaded. Please try again.';
  const show = async (index) => {
    requested = (index + photos.length) % photos.length;
    const next = requested;
    const photo = photos[next];
    const version = ++requestVersion;
    dialog.setAttribute('aria-busy', 'true');
    // Keep the previous photograph painted until its replacement is decoded.
    const candidate = new Image();
    try {
      if (typeof candidate.decode === 'function') {
        candidate.src = photo.href;
        await candidate.decode();
      } else {
        await new Promise((resolve, reject) => {
          candidate.onload = resolve;
          candidate.onerror = reject;
          candidate.src = photo.href;
        });
      }
      if (version !== requestVersion) return null;
      image.src = candidate.src;
      image.alt = photo.dataset.caption;
      caption.textContent = photo.dataset.caption;
      current = next;
      counter.textContent = `${current + 1} / ${photos.length}`;
      return true;
    } catch {
      if (version !== requestVersion) return null;
      if (version === requestVersion) {
        requested = current;
        counter.textContent = loadError;
      }
      return false;
    } finally {
      if (version === requestVersion) dialog.removeAttribute('aria-busy');
    }
  };
  links.forEach((link) => link.addEventListener('click', async (event) => {
    if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || event.button !== 0) return;
    event.preventDefault();
    opener = link;
    const loaded = await show(photos.findIndex((photo) => photo.href === link.href));
    if (loaded === null) return;
    if (!loaded) {
      // Native links retain a useful fallback if the first image cannot decode.
      if (!dialog.open && opener === link && !dialog.hasAttribute('aria-busy')) window.location.assign(link.href);
      return;
    }
    if (dialog.open) return;
    previousOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    dialog.showModal();
  }));
  dialog.querySelector('[data-gallery-close]').addEventListener('click', () => dialog.close());
  dialog.querySelector('[data-gallery-prev]').addEventListener('click', () => show(requested - 1));
  dialog.querySelector('[data-gallery-next]').addEventListener('click', () => show(requested + 1));
  dialog.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
      event.preventDefault();
      show(requested + (event.key === 'ArrowLeft' ? -1 : 1));
    }
  });
  dialog.addEventListener('click', (event) => { if (event.target === dialog) dialog.close(); });
  dialog.addEventListener('close', () => {
    ++requestVersion;
    requested = current;
    dialog.removeAttribute('aria-busy');
    document.body.style.overflow = previousOverflow || '';
    opener?.focus({ preventScroll: true });
  });
  window.addEventListener('pagehide', () => {
    ++requestVersion;
    dialog.removeAttribute('aria-busy');
    if (dialog.open) dialog.close();
  });
  let touchX;
  let touchY;
  image.addEventListener('touchstart', (event) => {
    touchX = event.changedTouches[0].clientX;
    touchY = event.changedTouches[0].clientY;
  }, { passive: true });
  image.addEventListener('touchend', (event) => {
    const delta = event.changedTouches[0].clientX - touchX;
    const vertical = event.changedTouches[0].clientY - touchY;
    if (Math.abs(delta) > 55 && Math.abs(delta) > Math.abs(vertical)) show(requested + (delta < 0 ? 1 : -1));
  }, { passive: true });
})();
