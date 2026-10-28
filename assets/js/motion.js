/* Hero typography animates on first paint. Scroll effects leave text positions stable. */
(() => {
  'use strict';
  const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
  const seen = new WeakSet();
  let observer;
  let progress;
  let frame = 0;
  const photoSeen = new WeakSet();
  const photoJobs = new Map();
  let photoObserver;
  let heroAttempted = false;
  let textObserver;
  const textSeen = new WeakSet();
  const startText = () => {
    if (!('IntersectionObserver' in window)) return;
    textObserver = new IntersectionObserver(entries => {
      entries.forEach(({ target, isIntersecting }) => {
        if (!isIntersecting) return;
        textObserver.unobserve(target);
        target.classList.add('text-revealed');
      });
    }, { threshold: 0, rootMargin: '0px 0px 100px 0px' });
    document.querySelectorAll('.text-motion').forEach(heading => {
      if (textSeen.has(heading)) return;
      textSeen.add(heading);
      // Only prepare headings still below the screen. Visible text stays untouched.
      if (heading.getBoundingClientRect().top <= window.innerHeight + 120) return;
      heading.classList.add('text-armed');
      textObserver.observe(heading);
    });
  };
  const settlePhoto = (wrapper) => {
    const timer = photoJobs.get(wrapper);
    if (timer) clearTimeout(timer);
    photoJobs.delete(wrapper);
    wrapper.classList.remove('photo-reveal-armed', 'photo-reveal-running', 'is-preparing');
    wrapper.classList.add('photo-reveal-done');
  };
  const revealHeroWhenReady = () => {
    if (preference.matches || heroAttempted) return;
    heroAttempted = true;
    const hero = document.querySelector('.hero-background');
    const image = hero?.querySelector('.hero-media img');
    if (!hero || !image) return;
    // A cached/painted picture must never be covered again by a delayed decode.
    if (image.complete || image.naturalWidth > 0) return;
    hero.classList.add('is-preparing');
    photoJobs.set(hero, setTimeout(() => settlePhoto(hero), 3500));
    const reveal = () => {
      if (!hero.classList.contains('is-preparing') || preference.matches) return;
      if (!image.naturalWidth) { settlePhoto(hero); return; }
      hero.classList.add('is-ready');
      clearTimeout(photoJobs.get(hero));
      photoJobs.set(hero, setTimeout(() => settlePhoto(hero), 1600));
    };
    image.addEventListener('load', reveal, { once: true });
    image.addEventListener('error', () => settlePhoto(hero), { once: true });
  };
  const startPhotos = () => {
    if (!('IntersectionObserver' in window)) return;
    photoObserver = new IntersectionObserver(entries => {
      entries.forEach(({ target, isIntersecting }) => {
        if (!isIntersecting) return;
        photoObserver.unobserve(target);
        const image = target.querySelector('img');
        if (!image) { settlePhoto(target); return; }
        const reveal = () => {
          if (preference.matches || !target.classList.contains('photo-reveal-armed') || target.classList.contains('photo-reveal-running')) return;
          if (!image.naturalWidth) { settlePhoto(target); return; }
          target.classList.add('photo-reveal-running');
          clearTimeout(photoJobs.get(target));
          photoJobs.set(target, setTimeout(() => settlePhoto(target), 1500));
        };
        if (image.complete) reveal();
        else {
          photoJobs.set(target, setTimeout(() => settlePhoto(target), 2500));
          image.addEventListener('load', reveal, { once: true });
          image.addEventListener('error', () => settlePhoto(target), { once: true });
        }
      });
    }, { threshold: .08 });
    document.querySelectorAll('[data-photo-reveal]').forEach(wrapper => {
      if (photoSeen.has(wrapper)) return;
      photoSeen.add(wrapper);
      // Only cover images before they enter the viewport, never after first paint.
      if (wrapper.getBoundingClientRect().top < window.innerHeight + 24) {
        settlePhoto(wrapper);
        return;
      }
      wrapper.classList.add('photo-reveal-armed');
      photoObserver.observe(wrapper);
    });
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
    revealHeroWhenReady();
    startPhotos();
    startText();
    if ('IntersectionObserver' in window) {
      observer = new IntersectionObserver((entries) => {
        entries.forEach(({ target, isIntersecting }) => {
          if (!isIntersecting) return;
          observer.unobserve(target);
          if (seen.has(target)) return;
          seen.add(target);
          target.classList.add('is-in-view');
          // Scroll callbacks can arrive after a fast swipe has painted the text.
          // Only decorative pseudo-elements react; text never changes position.
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
    });
  });
  document.querySelectorAll('.faq-more').forEach(more => more.addEventListener('toggle', requestProgress));
  preference.addEventListener('change', () => {
    observer?.disconnect();
    photoObserver?.disconnect();
    textObserver?.disconnect();
    document.querySelectorAll('.text-armed').forEach(heading => heading.classList.remove('text-armed', 'text-revealed'));
    Array.from(photoJobs.keys()).forEach(settlePhoto);
    document.querySelectorAll('[data-photo-reveal].photo-reveal-armed').forEach(settlePhoto);
    if (frame) cancelAnimationFrame(frame);
    frame = 0;
    if (!preference.matches) start();
  });
  start();
})();
