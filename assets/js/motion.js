/* Native, once-only motion. No dependencies, tracking, or persistent state. */
(() => {
  'use strict';
  const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (typeof Element.prototype.animate !== 'function') return;

  const active = new Set();
  const seen = new WeakSet();
  let observer;
  let progress;
  let frame = 0;
  const ease = 'cubic-bezier(.22, 1, .36, 1)';
  const animateMotion = (element, frames, duration = 750, delay = 0, easing = ease) => {
    if (!element || preference.matches) return;
    const animation = element.animate(frames, { duration, delay, easing, fill: 'backwards' });
    active.add(animation);
    const finish = () => active.delete(animation);
    animation.addEventListener('finish', finish, { once: true });
    animation.addEventListener('cancel', finish, { once: true });
  };
  const play = (element, frames, duration = 750, delay = 0, easing = ease) => {
    if (!element || preference.matches || seen.has(element)) return;
    seen.add(element);
    animateMotion(element, frames, duration, delay, easing);
  };
  const rise = (element, delay = 0) => play(element, [
    { transform: 'translateY(14px)' },
    { transform: 'translateY(0)' }
  ], 1100, delay);
  const revealImage = (image, delay = 0) => play(image, [
    { transform: 'scale(1.025)' },
    { transform: 'scale(1)' }
  ], 1500, delay);

  const updateProgress = () => {
    frame = 0;
    if (!progress || preference.matches) return;
    const page = document.documentElement;
    const distance = page.scrollHeight - page.clientHeight;
    const value = distance > 0 ? Math.min(1, Math.max(0, window.scrollY / distance)) : 0;
    progress.style.transform = `scaleX(${value})`;
  };
  const requestProgress = () => {
    if (!preference.matches && !frame) frame = requestAnimationFrame(updateProgress);
  };

  const start = () => {
    if (preference.matches) return;
    const hero = document.querySelector('.hero-copy');
    if (hero) {
      const heroEase = 'cubic-bezier(.25, .1, .25, 1)';
      ['.eyebrow', '.hero-title', '.hero-description', '.hero-actions'].forEach((selector, index) => {
        play(hero.querySelector(selector), [
          { transform: 'translateY(12px)' },
          { transform: 'translateY(0)' }
        ], 1200, index * 100, heroEase);
      });
      const photo = document.querySelector('.hero-media img');
      const revealHeroPhoto = () => play(photo, [
        { transform: 'scale(1.025)' },
        { transform: 'scale(1)' }
      ], 3000, 0, heroEase);
      // Start the gentle zoom when the photograph is actually visible.
      if (photo?.complete && photo.naturalWidth) revealHeroPhoto();
      else photo?.addEventListener('load', revealHeroPhoto, { once: true });
    } else {
      document.querySelectorAll('.page-hero h1, .page-hero .section-intro').forEach((element, index) => rise(element, index * 100));
    }

    if ('IntersectionObserver' in window) {
      observer = new IntersectionObserver((entries) => {
        entries.forEach(({ target, isIntersecting }) => {
          if (!isIntersecting) return;
          observer.unobserve(target);
          target.classList.add('is-in-view');
          const staggered = target.matches('.service-row, .step, .preparation-list li, .faq-list > details, .footer-grid > *');
          const index = staggered ? Array.from(target.parentElement.children).indexOf(target) : 0;
          const delay = Math.min(index, 3) * 75;
          if (target.matches('figure')) {
            revealImage(target.querySelector('img'));
          } else {
            rise(target, delay);
            if (target.matches('.project-card')) revealImage(target.querySelector('img'), 90);
            if (target.matches('.step')) play(target.querySelector('.step-number'), [
              { transform: 'translateY(8px) scale(.96)' },
              { transform: 'translateY(0) scale(1)' }
            ], 850, delay + 80);
          }
        });
      }, { threshold: .08, rootMargin: '0px 0px -28px 0px' });
      // Animate each outer unit once: nested targets otherwise move twice.
      // Keep painted content visible when the observer starts, even on slow loads.
      const targets = Array.from(document.querySelectorAll('.services-intro, .service-row, .section-top, .project-card, .about-band-grid > *, .step, .preparation-grid > div, .preparation-list li, .faq-layout > div, .contact-copy, .contact-form, .services-intro figure, .preparation-grid figure, .page-grid figure, .service-detail-grid figure, .example-hero, .section .section-label, .section h2, .faq-list > details, .footer-grid > *'));
      const units = new Set(targets);
      targets.forEach((element) => {
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
  document.querySelectorAll('.faq-list details').forEach((details) => {
    details.addEventListener('toggle', () => {
      requestProgress();
      if (!details.open || preference.matches) return;
      const content = details.querySelector('p');
      if (!content) return;
      const animation = content.animate([{ transform: 'translateY(-4px)' }, { transform: 'translateY(0)' }], { duration: 450, easing: ease });
      active.add(animation);
      const finish = () => active.delete(animation);
      animation.addEventListener('finish', finish, { once: true });
      animation.addEventListener('cancel', finish, { once: true });
    });
  });
  document.querySelectorAll('.faq-more').forEach((more) => {
    more.addEventListener('toggle', () => {
      requestProgress();
      if (!more.open) return;
      animateMotion(more.querySelector('.faq-list'), [
        { transform: 'translateY(6px)' },
        { transform: 'translateY(0)' }
      ], 450);
    });
  });
  const galleryPhoto = document.querySelector('[data-gallery-photo]');
  galleryPhoto?.addEventListener('load', () => {
    if (!galleryPhoto.closest('dialog')?.open) return;
    animateMotion(galleryPhoto, [
      { opacity: .5, transform: 'scale(.985)' },
      { opacity: 1, transform: 'scale(1)' }
    ], 400);
  });
  preference.addEventListener('change', () => {
    observer?.disconnect();
    active.forEach((animation) => animation.cancel());
    active.clear();
    if (frame) cancelAnimationFrame(frame);
    frame = 0;
    if (!preference.matches) start();
  });
  start();
})();
