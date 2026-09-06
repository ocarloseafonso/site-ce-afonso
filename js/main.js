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

  // --- Blog Sidebar Filtering & Pagination (3 per page) ---
  const blogList = document.querySelector('.blog-articles-list');
  const sidebarCatBtns = document.querySelectorAll('.sidebar-cat-btn');
  const blogPagination = document.querySelector('.blog-pagination');
  const blogStatusInfo = document.querySelector('.blog-status-info');

  if (blogList) {
    const allArticles = Array.from(blogList.querySelectorAll('.blog-card-horizontal'));
    const ITEMS_PER_PAGE = 3;
    let currentCategory = 'all';
    let currentPage = 1;

    function renderBlogPage() {
      const filteredArticles = allArticles.filter(article => {
        if (currentCategory === 'all') return true;
        const cats = article.getAttribute('data-category') || '';
        return cats.split(' ').includes(currentCategory);
      });

      const totalItems = filteredArticles.length;
      const totalPages = Math.ceil(totalItems / ITEMS_PER_PAGE) || 1;

      if (currentPage > totalPages) currentPage = 1;

      const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
      const endIndex = startIndex + ITEMS_PER_PAGE;

      allArticles.forEach(article => {
        article.style.display = 'none';
      });

      filteredArticles.slice(startIndex, endIndex).forEach(article => {
        article.style.display = '';
      });

      if (blogStatusInfo) {
        if (totalItems === 0) {
          blogStatusInfo.textContent = 'Nenhum artigo encontrado nesta categoria.';
        } else {
          blogStatusInfo.textContent = `Mostrando ${startIndex + 1}–${Math.min(endIndex, totalItems)} de ${totalItems} artigo${totalItems > 1 ? 's' : ''}`;
        }
      }

      if (blogPagination) {
        if (totalPages <= 1) {
          blogPagination.innerHTML = '';
        } else {
          let html = '';
          html += `<button class="pagination-btn" ${currentPage === 1 ? 'disabled' : ''} data-page="${currentPage - 1}">← Anterior</button>`;

          for (let p = 1; p <= totalPages; p++) {
            html += `<button class="pagination-btn ${p === currentPage ? 'active' : ''}" data-page="${p}">${p}</button>`;
          }

          html += `<button class="pagination-btn" ${currentPage === totalPages ? 'disabled' : ''} data-page="${currentPage + 1}">Próxima →</button>`;

          blogPagination.innerHTML = html;

          blogPagination.querySelectorAll('.pagination-btn').forEach(btn => {
            btn.addEventListener('click', () => {
              const targetPage = parseInt(btn.getAttribute('data-page'), 10);
              if (targetPage && targetPage !== currentPage && targetPage >= 1 && targetPage <= totalPages) {
                currentPage = targetPage;
                renderBlogPage();
                blogList.scrollIntoView({ behavior: 'smooth', block: 'start' });
              }
            });
          });
        }
      }
    }

    sidebarCatBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        sidebarCatBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentCategory = btn.getAttribute('data-filter') || 'all';
        currentPage = 1;
        renderBlogPage();
      });
    });

    renderBlogPage();
  }

  // Fallback for legacy blog filter buttons if present
  const blogFilterBtns = document.querySelectorAll('.blog-filter-btn');
  const legacyBlogCards = document.querySelectorAll('.blog-grid .blog-card');

  if (blogFilterBtns.length > 0 && legacyBlogCards.length > 0) {
    blogFilterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        blogFilterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const filterValue = btn.getAttribute('data-filter');

        legacyBlogCards.forEach(card => {
          if (filterValue === 'all') {
            card.style.display = '';
          } else {
            const categories = card.getAttribute('data-category');
            if (categories && categories.split(' ').includes(filterValue)) {
              card.style.display = '';
            } else {
              card.style.display = 'none';
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

  // --- WhatsApp Tracking - Dynamic Contextual Messages ---
  function resolveWhatsAppMessage() {
    const path = window.location.pathname.toLowerCase();
    const pageType = document.body.getAttribute('data-page') || '';

    // Mapeamento semântico por artigo do Blog
    const articleMessages = {
      'seo-local-para-clinicas': 'Olá, vim do artigo sobre SEO local para Clinicas em Volta Redonda e gostaria de saber mais!',
      'topo-google-volta-redonda': 'Olá, vim do artigo falando sobre colocar a empresa no topo do Google e gostaria de saber como funciona.',
      'erros-mapa-google': 'Olá, vim do artigo sobre os 7 erros que somem com sua empresa do Google Maps e gostaria de saber mais!',
      'guia-google-meu-negocio': 'Olá, vim do artigo Guia Prático de Google Meu Negócio e gostaria de otimizar minha empresa.',
      'importancia-seo-local': 'Olá, vim do artigo sobre a importância do SEO local e gostaria de saber mais!',
      'poder-das-avaliacoes': 'Olá, vim do artigo sobre o poder das avaliações no Google e gostaria de saber mais!',
      'por-que-sistema-posicionamento': 'Olá, vim do artigo sobre por que você precisa de um sistema de posicionamento e gostaria de saber mais!',
      'posicionamento-google': 'Olá, vim do artigo sobre posicionamento no Google e gostaria de solicitar uma auditoria gratuita.',
      'protocolo-destaque-local': 'Olá, vim do artigo sobre o Protocolo de Destaque Local e gostaria de saber mais!',
      'site-para-negocio-local': 'Olá, vim do artigo sobre sites para negócios locais e gostaria de saber mais!',
      'trafego-vs-organico': 'Olá, vim do artigo sobre Tráfego Pago vs Orgânico e gostaria de saber mais!',
      'anuncios-vs-organico': 'Olá, vim do artigo sobre Anúncios vs Tráfego Orgânico e gostaria de saber mais!',
      'whatsapp-maquina-vendas': 'Olá, vim do artigo sobre transformar o WhatsApp em máquina de vendas e gostaria de saber mais!',
      'whatsapp-para-negocios': 'Olá, vim do artigo sobre WhatsApp para Negócios e gostaria de saber mais!'
    };

    // Verifica se está dentro de um artigo específico do blog pelo slug da URL
    for (const [slug, msg] of Object.entries(articleMessages)) {
      if (path.includes(slug)) {
        return msg;
      }
    }

    // Fallback dinâmico para novos artigos do blog
    if (path.includes('/blog/') && !path.endsWith('/blog/') && !path.endsWith('/blog') && !path.endsWith('blog.html')) {
      const heading = document.querySelector('article h1') || document.querySelector('h1');
      if (heading && heading.textContent.trim()) {
        const title = heading.textContent.trim().replace(/\s+/g, ' ');
        return `Olá, vim do artigo "${title}" e gostaria de saber mais!`;
      }
      return 'Olá, vim de um artigo do blog da C.E. Afonso e gostaria de saber mais!';
    }

    // Mapeamento semântico por página institucional
    switch (pageType) {
      case 'home':
        return 'Olá! Gostaria de saber mais sobre os serviços da C.E. Afonso Soluções Digitais.';
      case 'sobre':
        return 'Olá! Vim da página Sobre e gostaria de conhecer mais sobre a C.E. Afonso Soluções Digitais.';
      case 'servicos':
        return 'Olá! Vim da página de Serviços e gostaria de entender qual solução é ideal para minha empresa.';
      case 'blog':
        return 'Olá! Vim do Blog da C.E. Afonso e gostaria de saber mais sobre os conteúdos e serviços.';
      case 'faq':
        return 'Olá! Vim da página de Perguntas Frequentes (FAQ) e gostaria de tirar uma dúvida sobre os serviços.';
      case 'contato':
        return 'Olá! Vim da página de Contato e gostaria de solicitar uma análise estratégica.';
      default:
        if (path.includes('sobre')) return 'Olá! Vim da página Sobre e gostaria de conhecer mais sobre a C.E. Afonso Soluções Digitais.';
        if (path.includes('servicos')) return 'Olá! Vim da página de Serviços e gostaria de saber mais.';
        if (path.includes('faq')) return 'Olá! Vim da página de Dúvidas Frequentes e gostaria de tirar uma dúvida.';
        if (path.includes('contato')) return 'Olá! Gostaria de solicitar uma análise estratégica para o meu negócio.';
        return 'Olá! Gostaria de saber mais sobre as soluções digitais da C.E. Afonso.';
    }
  }

  const defaultTrackedMsg = resolveWhatsAppMessage();
  const encodedTrackedMsg = encodeURIComponent(defaultTrackedMsg);

  // Atualiza o botão flutuante do WhatsApp
  const whatsappFloat = document.querySelector('.whatsapp-float');
  if (whatsappFloat) {
    whatsappFloat.setAttribute('href', 'https://wa.me/5524992074661?text=' + encodedTrackedMsg);
    whatsappFloat.setAttribute('target', '_blank');
    whatsappFloat.setAttribute('rel', 'noopener noreferrer');
  }

  // Atualiza links de WhatsApp genéricos (sem texto pré-definido) para carregar o rastreio da página
  const genericWaLinks = document.querySelectorAll('a[href^="https://wa.me/5524992074661"]');
  genericWaLinks.forEach(function (link) {
    const currentHref = link.getAttribute('href');
    if (currentHref && !currentHref.includes('?text=')) {
      link.setAttribute('href', 'https://wa.me/5524992074661?text=' + encodedTrackedMsg);
    }
  });

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
