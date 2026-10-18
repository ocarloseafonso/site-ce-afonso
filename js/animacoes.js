/* ==========================================================================
   ANIMAÇÕES PDL 3.0 — C.E. Afonso Soluções Digitais
   Craft-Finishing: Smart Header, Barra Progresso, Scroll Reveal
   ========================================================================== */

(function () {
  'use strict';

  /* ─── 1. SMART HEADER — Transparente no topo, vidro no scroll ─────────── */
  const cabecalho = document.getElementById('cabecalho');
  const topbar = document.querySelector('.topbar');
  const TOPBAR_H = topbar ? topbar.offsetHeight : 38;

  function atualizarCabecalho() {
    if (!cabecalho) return;
    if (window.scrollY > 40) {
      cabecalho.classList.add('cabecalho--scrolled');
    } else {
      cabecalho.classList.remove('cabecalho--scrolled');
    }
  }

  // Ajustar posição inicial do cabeçalho com base na topbar
  function ajustarTopCabecalho() {
    if (!cabecalho) return;
    const topH = topbar ? topbar.offsetHeight : 0;
    if (!cabecalho.classList.contains('cabecalho--scrolled')) {
      cabecalho.style.top = topH + 'px';
    }
  }

  window.addEventListener('scroll', atualizarCabecalho, { passive: true });
  window.addEventListener('resize', ajustarTopCabecalho, { passive: true });
  atualizarCabecalho();

  /* ─── 2. BARRA DE PROGRESSO DE LEITURA ────────────────────────────────── */
  const barraProgresso = document.getElementById('barra-progresso');

  function atualizarProgresso() {
    if (!barraProgresso) return;
    const scrollTotal = document.documentElement.scrollHeight - window.innerHeight;
    if (scrollTotal <= 0) return;
    const progresso = (window.scrollY / scrollTotal) * 100;
    barraProgresso.style.width = Math.min(progresso, 100) + '%';
  }

  window.addEventListener('scroll', atualizarProgresso, { passive: true });

  /* ─── 3. SCROLL REVEAL ARTESANAL COM CASCATA (CRAFT-FINISHING) ─────────── */
  const elementosRevelar = document.querySelectorAll('.revelar');

  if (elementosRevelar.length > 0) {
    // Se IntersectionObserver disponível (todos os browsers modernos):
    if ('IntersectionObserver' in window) {
      const observadorReveal = new IntersectionObserver(
        function (entradas) {
          entradas.forEach(function (entrada) {
            if (entrada.isIntersecting) {
              entrada.target.classList.add('ativo');
              observadorReveal.unobserve(entrada.target);
            }
          });
        },
        {
          threshold: 0.12,
          rootMargin: '0px 0px -40px 0px'
        }
      );

      elementosRevelar.forEach(function (el) {
        observadorReveal.observe(el);
      });
    } else {
      // Fallback: revelar tudo imediatamente
      elementosRevelar.forEach(function (el) {
        el.classList.add('ativo');
      });
    }
  }

  /* ─── 4. DIVISOR ORNAMENTAL — Entrada suave ao cruzar viewport ─────────── */
  const divisores = document.querySelectorAll('.divisor-ornamental');
  if (divisores.length > 0 && 'IntersectionObserver' in window) {
    const obsDivisor = new IntersectionObserver(
      function (entradas) {
        entradas.forEach(function (entrada) {
          if (entrada.isIntersecting) {
            entrada.target.style.opacity = '1';
            entrada.target.style.transform = 'scale(1)';
            obsDivisor.unobserve(entrada.target);
          }
        });
      },
      { threshold: 0.5 }
    );

    divisores.forEach(function (div) {
      div.style.opacity = '0';
      div.style.transform = 'scale(0.92)';
      div.style.transition = 'opacity 0.6s ease, transform 0.6s cubic-bezier(0.16,1,0.3,1)';
      obsDivisor.observe(div);
    });
  }

  /* ─── 5. HERO FOTO — Parallax suave na rolagem ─────────────────────────── */
  const heroFoto = document.querySelector('.hero__bg-foto');
  function parallaxHero() {
    if (!heroFoto) return;
    const offset = window.scrollY * 0.25;
    heroFoto.style.transform = 'translateY(' + offset + 'px)';
  }
  window.addEventListener('scroll', parallaxHero, { passive: true });

})();
