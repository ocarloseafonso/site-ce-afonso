/* ============================================
   C.E. AFONSO SOLUÇÕES DIGITAIS
   JavaScript Principal
   ============================================ */

document.addEventListener('DOMContentLoaded', function () {

  // --- Mobile Menu ---
  const hamburger = document.querySelector('.hamburger');
  const nav = document.querySelector('.nav');
  const overlay = document.querySelector('.nav-overlay');

  if (hamburger && nav) {
    hamburger.addEventListener('click', function () {
      hamburger.classList.toggle('active');
      nav.classList.toggle('open');
      if (overlay) overlay.classList.toggle('active');
      document.body.style.overflow = nav.classList.contains('open') ? 'hidden' : '';
    });

    if (overlay) {
      overlay.addEventListener('click', function () {
        hamburger.classList.remove('active');
        nav.classList.remove('open');
        overlay.classList.remove('active');
        document.body.style.overflow = '';
      });
    }

    // Close menu on link click (excluding dropdown toggles for the first click)
    nav.querySelectorAll('a:not(.nav-dropdown-toggle)').forEach(function (link) {
      link.addEventListener('click', function () {
        hamburger.classList.remove('active');
        nav.classList.remove('open');
        if (overlay) overlay.classList.remove('active');
        document.body.style.overflow = '';
      });
    });

    // Mobile dropdown toggle
    document.querySelectorAll('.nav-dropdown-toggle').forEach(function (toggle) {
      toggle.addEventListener('click', function (e) {
        if (window.innerWidth <= 1024) {
          if (!this.parentElement.classList.contains('open')) {
            // First click: expand submenu, do not navigate
            e.preventDefault();
            this.parentElement.classList.add('open');
          } else {
            // Second click: close mobile menu and let default navigation occur
            hamburger.classList.remove('active');
            nav.classList.remove('open');
            if (overlay) overlay.classList.remove('active');
            document.body.style.overflow = '';
          }
        }
      });
    });
  }

  // --- Header Scroll Effect ---
  const header = document.querySelector('.header');
  if (header) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 50) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }

  // --- FAQ Filtering & Accordion ---
  const filterBtns = document.querySelectorAll('.filter-btn');
  const faqItems = document.querySelectorAll('.faq-item');

  if (filterBtns.length > 0 && faqItems.length > 0) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const filterValue = btn.getAttribute('data-filter');

        faqItems.forEach(item => {
          item.classList.remove('open'); // Fecha os abertos ao trocar de filtro

          if (filterValue === 'todas') {
            item.classList.remove('hide');
          } else {
            const categories = item.getAttribute('data-category');
            if (categories && categories.split(' ').includes(filterValue)) {
              item.classList.remove('hide');
            } else {
              item.classList.add('hide');
            }
          }
        });
      });
    });
  }

  document.querySelectorAll('.faq-question').forEach(function (btn) {
    btn.addEventListener('click', function () {
      const item = this.parentElement;
      const isOpen = item.classList.contains('open');

      // Close all in the same list
      const list = item.closest('.faq-list');
      if (list) {
        list.querySelectorAll('.faq-item').forEach(function (faq) {
          faq.classList.remove('open');
        });
      }

      if (!isOpen) {
        item.classList.add('open');
      }
    });
  });

  // --- Smooth Scroll for Anchor Links ---
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  // --- Active Nav Link ---
  const currentPath = window.location.pathname;
  document.querySelectorAll('.nav-link, .nav-dropdown-menu a').forEach(function (link) {
    const href = link.getAttribute('href');
    if (href && href !== '/' && href !== '#') {
      if (currentPath.endsWith(href) || currentPath.includes(href)) {
        link.classList.add('active');
        // Open parent dropdown if applicable
        const parentDropdown = link.closest('.nav-dropdown');
        if (parentDropdown && window.innerWidth <= 1024) {
          parentDropdown.classList.add('open');
        }
      }
    } else if (href === '/' && (currentPath === '/' || currentPath === '' || currentPath.endsWith('index.html'))) {
      link.classList.add('active');
    }
  });

  // --- WhatsApp Float - Dynamic Message ---
  const whatsappFloat = document.querySelector('.whatsapp-float');
  if (whatsappFloat) {
    const pageType = document.body.getAttribute('data-page');
    let message = '';

    switch (pageType) {
      case 'home':
        message = 'Olá! Gostaria de saber mais sobre o Protocolo de Destaque Local (PDL).';
        break;
      case 'sobre':
        message = 'Olá! Gostaria de conhecer mais sobre a C.E. Afonso Soluções Digitais.';
        break;
      case 'servicos':
        message = 'Olá! Gostaria de saber mais sobre os pilares do Protocolo de Destaque Local (PDL).';
        break;
      case 'blog':
        message = 'Olá! Vi o blog da C.E. Afonso e gostaria de tirar uma dúvida.';
        break;
      case 'faq':
        message = 'Olá! Tenho uma dúvida sobre o Protocolo de Destaque Local (PDL).';
        break;
      case 'contato':
        message = 'Olá! Gostaria de uma consultoria estratégica para o meu negócio.';
        break;
      default:
        message = 'Olá! Gostaria de saber mais sobre as soluções digitais.';
    }

    const encodedMessage = encodeURIComponent(message);
    whatsappFloat.setAttribute('href', 'https://wa.me/5524992074661?text=' + encodedMessage);
    whatsappFloat.setAttribute('target', '_blank');
    whatsappFloat.setAttribute('rel', 'noopener noreferrer');
  }

  // --- Lazy Loading Images (fallback for older browsers) ---
  if ('IntersectionObserver' in window) {
    const lazyImages = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.getAttribute('data-src');
          img.removeAttribute('data-src');
          imageObserver.unobserve(img);
        }
      });
    });

    lazyImages.forEach(function (img) {
      imageObserver.observe(img);
    });
  }

  // --- Services Slider (Home) Infinite ---
  const servicesSlider = document.querySelector('.services-slider');
  const prevServiceBtn = document.querySelector('.slider-arrow.prev');
  const nextServiceBtn = document.querySelector('.slider-arrow.next');

  if (servicesSlider && prevServiceBtn && nextServiceBtn) {
    prevServiceBtn.style.display = 'none';

    // To create a flawless infinite scroll without visual bugs or DOM shifting jumps:
    // We duplicate the existing 4 cards exactly 15 times (60 cards).
    // This allows the user to click the next arrow dozens of times continuously!
    const originalCards = Array.from(servicesSlider.children);
    for (let i = 0; i < 15; i++) {
      originalCards.forEach(card => {
        const clone = card.cloneNode(true);
        servicesSlider.appendChild(clone);
      });
    }

    let isAnimating = false;

    nextServiceBtn.addEventListener('click', () => {
      if (isAnimating) return;
      isAnimating = true;

      // Show left arrow permanently once they click right
      prevServiceBtn.style.display = 'flex';

      const firstCard = servicesSlider.firstElementChild;
      const offset = firstCard.offsetWidth + 28;

      servicesSlider.scrollBy({ left: offset, behavior: 'smooth' });

      setTimeout(() => { isAnimating = false; }, 400); // Debounce clicks slightly
    });

    prevServiceBtn.addEventListener('click', () => {
      if (isAnimating) return;
      isAnimating = true;

      const firstCard = servicesSlider.firstElementChild;
      const offset = firstCard.offsetWidth + 28;

      servicesSlider.scrollBy({ left: -offset, behavior: 'smooth' });

      setTimeout(() => { isAnimating = false; }, 400);
    });
  }

  // --- Manual Gallery Slider (Details Page) ---
  const galleryTracks = document.querySelectorAll('.gallery-slider-track');
  galleryTracks.forEach(track => {
    // Buttons live inside .gallery-slider-wrapper, the direct parent of the track
    const wrapper = track.closest('.gallery-slider-wrapper');
    if (!wrapper) return;

    const prevBtn = wrapper.querySelector('.gallery-arrow.prev');
    const nextBtn = wrapper.querySelector('.gallery-arrow.next');

    // Remove old duplicated content logic to make it a standard manual slider
    let isGalleryAnimating = false;

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        if (isGalleryAnimating) return;
        isGalleryAnimating = true;
        const firstCard = track.firstElementChild;
        if (firstCard) {
          const offset = firstCard.offsetWidth + 16;
          track.scrollBy({ left: offset, behavior: 'smooth' });
        }
        setTimeout(() => { isGalleryAnimating = false; }, 400);
      });
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        if (isGalleryAnimating) return;
        isGalleryAnimating = true;
        const firstCard = track.firstElementChild;
        if (firstCard) {
          const offset = firstCard.offsetWidth + 16;
          track.scrollBy({ left: -offset, behavior: 'smooth' });
        }
        setTimeout(() => { isGalleryAnimating = false; }, 400);
      });
    }
  });

  // --- Lightbox Premium ---
  // Event Delegation: .lightbox-trigger is on the wrapper div, so get the img inside
  document.body.addEventListener('click', function (e) {
    const trigger = e.target.closest('.lightbox-trigger');
    if (trigger) {
      // If clicked directly on the img, use it; otherwise find the img inside the wrapper
      const img = trigger.tagName === 'IMG' ? trigger : trigger.querySelector('img');
      if (img) openLightbox(img.src, img.alt);
    }
  });

  function openLightbox(src, alt) {
    // Determine if lightbox already exists
    let overlay = document.querySelector('.lightbox-overlay');
    if (!overlay) {
      // Build HTML
      overlay = document.createElement('div');
      overlay.className = 'lightbox-overlay';
      overlay.innerHTML = `
        <div class="lightbox-content">
          <button class="lightbox-close" aria-label="Fechar">&times;</button>
          <img src="" alt="Imagem Ampliada">
        </div>
      `;
      document.body.appendChild(overlay);

      // Bind close events
      const closeBtn = overlay.querySelector('.lightbox-close');
      closeBtn.addEventListener('click', closeLightbox);
      overlay.addEventListener('click', (e) => {
        if (e.target === overlay) {
          closeLightbox();
        }
      });
      // Esc key
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && overlay.classList.contains('active')) {
          closeLightbox();
        }
      });
    }

    // Set Image
    const contentImg = overlay.querySelector('img');
    contentImg.src = src;
    contentImg.alt = alt || 'Imagem Ampliada';

    // Show Lightbox overlay
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    const overlay = document.querySelector('.lightbox-overlay');
    if (overlay) {
      overlay.classList.remove('active');
      document.body.style.overflow = '';
      setTimeout(() => {
        if (overlay) overlay.remove(); // Clean up DOM if desired
      }, 300);
    }
  }

  // --- Cookie Consent (LGPD) ---
  if (window.cookieconsent) {
    window.cookieconsent.initialise({
      palette: {
        popup: { background: "#0D0D0D", text: "rgba(255,255,255,0.85)" },
        button: { background: "#C8005A", text: "#fff" }
      },
      theme: "classic",
      position: "bottom",
      revokable: false,
      type: "info",
      content: {
        message: "Utilizamos cookies para melhorar sua experiência e analisar o tráfego do site. Ao continuar navegando, você concorda com nossa política de privacidade.",
        dismiss: "Aceitar e Continuar",
        link: "Política de Privacidade",
        href: "privacy",
        policy: "Política de Cookies"
      }
    });
  }

});
