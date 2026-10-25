/* Motion belongs to text and accents. Image pixels never fade or restart on load. */
(() => {
  'use strict';
  const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
  const active = new Set();
  const seen = new WeakSet();
  const ease = 'cubic-bezier(.16, 1, .3, 1)';
  let observer;
  let progress;
  let frame = 0;
  const move = (element, offset = 18, delay = 0) => {
    if (!element || preference.matches || typeof element.animate !== 'function') return;
    // Never promote a photograph, or one of its ancestors, to an animated layer.
    if (element.matches('img, picture, figure') || element.querySelector('img, picture')) return;
    const animation = element.animate([
      { transform: `translateY(${offset}px)` },
      { transform: 'translateY(0)' }
    ], { duration: 1300, delay, easing: ease });
    active.add(animation);
    const finish = () => active.delete(animation);
    animation.addEventListener('finish', finish, { once: true });
    animation.addEventListener('cancel', finish, { once: true });
  };
  const updateProgress = () => {
    frame = 0;
    if (!progress || preference.matches) return;
    const page = document.documentElement;
    const distance = page.scrollHeight - page.clientHeight;
    progress.style.transform = `scaleX(${distance > 0 ? Math.min(1, Math.max(0, window.scrollY / distance)) : 0})`;
  };
  const requestProgress = () => {
    if (!preference.matches && !frame) frame = requestAnimationFrame(updateProgress);
  };
  const start = () => {
    if (preference.matches) return;
    if ('IntersectionObserver' in window) {
      observer = new IntersectionObserver((entries) => {
        entries.forEach(({ target, isIntersecting }) => {
          if (!isIntersecting) return;
          observer.unobserve(target);
          if (seen.has(target)) return;
          seen.add(target);
          target.classList.add('is-in-view');
          if (target.matches('figure, .project-card, .step')) return;
          const group = target.closest('.service-list, .preparation-list, .faq-list, .steps');
          const siblings = group ? Array.from(group.children) : [];
          const unit = group ? target.closest('.service-row, li, details') : null;
          move(target, target.matches('.eyebrow') ? 8 : 18, Math.max(0, Math.min(siblings.indexOf(unit), 3)) * 110);
        });
      }, { threshold: .12, rootMargin: '0px 0px 40px 0px' });
      const targets = Array.from(document.querySelectorAll('.section .eyebrow, .section h2, .services-intro > p:not(.eyebrow), .service-content, .section-intro, .section-top > .text-link, .project-card, .project-card h3, .project-card > .text-link, .about-band-grid > div > p:not(.eyebrow), .about-band-grid > div > .text-link, .step, .step h3, .step p, .preparation-list li, .faq-list > details, .contact-copy > p:not(.eyebrow), .contact-options, .form-heading, .contact-form, .services-intro figure, .preparation-grid figure, .page-grid figure, .service-detail-grid figure, .about-band-grid figure, .example-hero'));
      const units = new Set(targets.filter(el => !el.matches('figure, .project-card, .step')));
      targets.forEach(element => {
        for (let parent = element.parentElement; parent; parent = parent.parentElement) {
          if (units.has(parent)) return;
        }
        observer.observe(element);
      });
    }
    if (!progress) {
      progress = document.createElement('div');
      progress.className = 'reading-progress';
      progress.setAttribute('aria-hidden', 'true');
      document.body.append(progress);
    }
    updateProgress();
  };
  window.addEventListener('scroll', requestProgress, { passive: true });
  window.addEventListener('resize', requestProgress, { passive: true });
  window.addEventListener('load', requestProgress, { once: true });
  window.addEventListener('pageshow', requestProgress);
  document.querySelectorAll('.faq-list details').forEach(details => {
    details.addEventListener('toggle', () => {
      requestProgress();
      if (details.open) move(details.querySelector('p'), -6);
    });
  });
  document.querySelectorAll('.faq-more').forEach(more => more.addEventListener('toggle', requestProgress));
  preference.addEventListener('change', () => {
    observer?.disconnect();
    active.forEach(animation => animation.cancel());
    active.clear();
    if (frame) cancelAnimationFrame(frame);
    frame = 0;
    if (!preference.matches) start();
  });
  start();
})();
