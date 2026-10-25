/* Small progressive enhancements. No cookies, tracking, storage or network requests. */
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

  const language = document.documentElement.lang;
  const labels = {
    uk: { name: 'Ім’я', contact: 'Контакт для відповіді', message: 'Завдання', required: 'Будь ласка, заповніть це поле.', invalid: 'Вкажіть email або номер телефону.' },
    de: { name: 'Name', contact: 'Kontakt für die Antwort', message: 'Vorhaben', required: 'Bitte füllen Sie dieses Feld aus.', invalid: 'Bitte geben Sie eine E-Mail-Adresse oder Telefonnummer ein.' },
    en: { name: 'Name', contact: 'Reply contact', message: 'Project', required: 'Please complete this field.', invalid: 'Enter an email address or phone number.' }
  }[language] || { name: 'Name', contact: 'Contact', message: 'Project', required: 'Please complete this field.', invalid: 'Enter an email address or phone number.' };

  document.querySelectorAll('[data-contact-form]').forEach((form) => {
    const fields = ['name', 'contact', 'message'].map((name) => form.elements.namedItem(name));
    fields.forEach((field) => field.addEventListener('input', () => field.setCustomValidity('')));
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      fields.forEach((field) => field.setCustomValidity(field.value.trim() ? '' : labels.required));
      const contact = form.elements.namedItem('contact');
      if (contact.value.trim()) {
        const value = contact.value.trim();
        const emailValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
        const phoneValid = /^[+\d\s()./-]+$/.test(value) && value.replace(/\D/g, '').length >= 7;
        contact.setCustomValidity(emailValid || phoneValid ? '' : labels.invalid);
      }
      if (!form.reportValidity()) return;
      const body = `${labels.name}: ${fields[0].value.trim()}\n${labels.contact}: ${fields[1].value.trim()}\n\n${labels.message}:\n${fields[2].value.trim()}`;
      const subject = form.dataset.subject || 'BauServiceMD';
      const status = form.querySelector('[data-form-status]');
      if (status) status.textContent = form.dataset.fallback || '';
      window.location.href = `mailto:renovierungsservicedima@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    });
  });
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
