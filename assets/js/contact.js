/* Contact submissions are sent only after an explicit form submission. */
(() => {
  'use strict';
  const validation = {
    uk: { required: 'Будь ласка, заповніть це поле.', invalid: 'Вкажіть email або номер телефону.' },
    de: { required: 'Bitte füllen Sie dieses Feld aus.', invalid: 'Bitte geben Sie eine E-Mail-Adresse oder Telefonnummer ein.' },
    en: { required: 'Please complete this field.', invalid: 'Enter an email address or phone number.' }
  };
  const labels = validation[document.documentElement.lang] || validation.en;
  document.querySelectorAll('[data-contact-form]').forEach((form) => {
    const fields = ['name', 'contact', 'message'].map((name) => form.elements.namedItem(name));
    const button = form.querySelector('[type="submit"]');
    const buttonLabel = form.querySelector('[data-submit-label]');
    const initialLabel = buttonLabel.textContent;
    const status = form.querySelector('[data-form-status]');
    let pending = false;
    const report = (state, message) => {
      status.dataset.state = state;
      status.textContent = message;
    };
    fields.forEach((field) => field.addEventListener('input', () => field.setCustomValidity('')));
    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      if (pending) return;
      fields.forEach((field) => field.setCustomValidity(field.value.trim() ? '' : labels.required));
      const contact = fields[1].value.trim();
      const isEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(contact);
      const isPhone = /^[+\d\s()./-]+$/.test(contact) && contact.replace(/\D/g, '').length >= 7;
      if (contact && !isEmail && !isPhone) fields[1].setCustomValidity(labels.invalid);
      if (!form.reportValidity()) return;
      // Do not send or display a false success for the anti-spam trap.
      if (form.elements.namedItem('_honey').value) return;
      pending = true;
      button.disabled = true;
      form.setAttribute('aria-busy', 'true');
      buttonLabel.textContent = form.dataset.loading;
      report('loading', form.dataset.loading);
      const controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), 20000);
      const payload = {
        name: fields[0].value.trim(),
        contact,
        message: fields[2].value.trim(),
        _subject: form.dataset.subject,
        _template: 'table',
        _url: window.location.origin + window.location.pathname,
        _honey: ''
      };
      if (isEmail) payload.email = contact;
      try {
        const endpoint = new URL(form.action);
        // Restrict transport to the intended form service, including on misconfiguration.
        if (endpoint.origin !== 'https://formsubmit.co') throw new Error('Invalid endpoint');
        endpoint.pathname = '/ajax' + endpoint.pathname;
        const response = await fetch(endpoint.href, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          credentials: 'omit',
          body: JSON.stringify(payload),
          signal: controller.signal
        });
        const result = await response.json();
        if (/activat|confirm.{0,40}email|verif.{0,40}email/i.test(String(result.message || ''))) {
          report('error', form.dataset.activation);
          return;
        }
        if (!response.ok || (result.success !== true && result.success !== 'true')) throw new Error('Submission not accepted');
        report('success', form.dataset.success);
        // Preserve the original entries if the visitor edits while the request is pending.
        if (fields[0].value.trim() === payload.name && fields[1].value.trim() === contact && fields[2].value.trim() === payload.message) form.reset();
      } catch {
        report('error', form.dataset.error);
      } finally {
        clearTimeout(timeout);
        pending = false;
        button.disabled = false;
        buttonLabel.textContent = initialLabel;
        form.removeAttribute('aria-busy');
      }
    });
  });
})();
