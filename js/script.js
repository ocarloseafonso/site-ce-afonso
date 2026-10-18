/* ==========================================================================
   SCRIPT PRINCIPAL PDL 3.0 — C.E. Afonso Soluções Digitais
   Menu Mobile, FAQ Acordeão, Formulário WhatsApp, LGPD Cookies
   ========================================================================== */

(function () {
  'use strict';

  /* ─── DADOS CANÔNICOS DA AGÊNCIA ────────────────────────────────────────── */
  var WHATSAPP_NUM = '5524999555644';
  var WHATSAPP_BASE = 'https://wa.me/' + WHATSAPP_NUM;

  /* ─── 1. MENU DRAWER MOBILE ─────────────────────────────────────────────── */
  var navToggle   = document.getElementById('navToggle');
  var navDrawer   = document.getElementById('navDrawer');
  var navOverlay  = document.getElementById('navOverlay');

  function abrirMenu() {
    if (!navDrawer) return;
    navDrawer.classList.add('ativo');
    navOverlay && navOverlay.classList.add('ativo');
    navToggle && navToggle.classList.add('aberto');
    navToggle && navToggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden'; // trava de scroll dupla
    document.documentElement.style.overflow = 'hidden';
  }

  function fecharMenu() {
    if (!navDrawer) return;
    navDrawer.classList.remove('ativo');
    navOverlay && navOverlay.classList.remove('ativo');
    navToggle && navToggle.classList.remove('aberto');
    navToggle && navToggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
    document.documentElement.style.overflow = '';
  }

  if (navToggle) {
    navToggle.addEventListener('click', function () {
      var estaAberto = navDrawer && navDrawer.classList.contains('ativo');
      estaAberto ? fecharMenu() : abrirMenu();
    });
  }

  if (navOverlay) {
    navOverlay.addEventListener('click', fecharMenu);
  }

  // Fechar ao clicar em link do drawer
  if (navDrawer) {
    var linksDrawer = navDrawer.querySelectorAll('a');
    linksDrawer.forEach(function (link) {
      link.addEventListener('click', fecharMenu);
    });
  }

  // Fechar com ESC
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') fecharMenu();
  });

  /* ─── 2. FAQ — ACORDEÃO COM FÍSICA SUAVE ─────────────────────────────────── */
  var faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(function (item) {
    var pergunta = item.querySelector('.faq-pergunta') || item.querySelector('.faq-question');
    var resposta = item.querySelector('.faq-resposta') || item.querySelector('.faq-answer');

    if (!pergunta || !resposta) return;

    pergunta.addEventListener('click', function () {
      var estaAberto = item.classList.contains('aberto') || item.classList.contains('open');

      // Fechar todos os outros
      faqItems.forEach(function (outroItem) {
        if (outroItem !== item) {
          fecharFAQ(outroItem);
        }
      });

      if (estaAberto) {
        fecharFAQ(item);
      } else {
        abrirFAQ(item);
      }
    });
  });

  function abrirFAQ(item) {
    var resposta = item.querySelector('.faq-resposta') || item.querySelector('.faq-answer');
    if (!resposta) return;
    item.classList.add('aberto');
    item.classList.add('open');
    // Física suave com scrollHeight real
    resposta.style.maxHeight = (resposta.scrollHeight + 40) + 'px';
    resposta.style.opacity = '1';
    resposta.style.transform = 'translateY(0)';
    var btn = item.querySelector('.faq-pergunta') || item.querySelector('.faq-question');
    if (btn) btn.setAttribute('aria-expanded', 'true');
  }

  function fecharFAQ(item) {
    var resposta = item.querySelector('.faq-resposta') || item.querySelector('.faq-answer');
    if (!resposta) return;
    item.classList.remove('aberto');
    item.classList.remove('open');
    resposta.style.maxHeight = '0';
    resposta.style.opacity = '0';
    resposta.style.transform = 'translateY(-4px)';
    var btn = item.querySelector('.faq-pergunta') || item.querySelector('.faq-question');
    if (btn) btn.setAttribute('aria-expanded', 'false');
  }

  /* ─── FILTROS DE CATEGORIA FAQ ───────────────────────────────────────────── */
  var filterBtns = document.querySelectorAll('.faq-filters .filter-btn');
  if (filterBtns.length > 0) {
    filterBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        filterBtns.forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        var filtro = btn.getAttribute('data-filter');
        faqItems.forEach(function (item) {
          var cat = item.getAttribute('data-category');
          if (filtro === 'todas' || !cat || cat === filtro) {
            item.classList.remove('hide');
          } else {
            item.classList.add('hide');
            fecharFAQ(item);
          }
        });
      });
    });
  }

  /* ─── 3. FORMULÁRIO COM ENVIO DINÂMICO PARA WHATSAPP ─────────────────────── */
  var form = document.getElementById('form-contato');

  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      var nome    = (form.querySelector('[name="nome"]') || {}).value || '';
      var empresa = (form.querySelector('[name="empresa"]') || {}).value || '';
      var cidade  = (form.querySelector('[name="cidade"]') || {}).value || '';
      var telefone= (form.querySelector('[name="telefone"]') || {}).value || '';
      var servico = (form.querySelector('[name="servico"]') || {}).value || '';
      var mensagem= (form.querySelector('[name="mensagem"]') || {}).value || '';

      var textoWpp = '';
      textoWpp += 'Olá, Carlos Eduardo! Vim pelo site da C.E. Afonso Soluções Digitais.\n\n';
      if (nome)     textoWpp += '*Nome:* ' + nome + '\n';
      if (empresa)  textoWpp += '*Empresa:* ' + empresa + '\n';
      if (cidade)   textoWpp += '*Cidade:* ' + cidade + '\n';
      if (telefone) textoWpp += '*Telefone:* ' + telefone + '\n';
      if (servico)  textoWpp += '*Interesse:* ' + servico + '\n';
      if (mensagem) textoWpp += '*Mensagem:* ' + mensagem + '\n';

      var url = WHATSAPP_BASE + '?text=' + encodeURIComponent(textoWpp);
      window.open(url, '_blank', 'noopener,noreferrer');
    });
  }

  /* ─── 4. LGPD — BANNER COOKIES & MODAL ──────────────────────────────────── */
  var avisoCookies     = document.getElementById('aviso-cookies');
  var btnAceitarCook   = document.getElementById('btn-aceitar-cookies');
  var modalLGPD        = document.getElementById('modal-lgpd');
  var btnAceitarLGPD   = document.getElementById('btn-aceitar-lgpd');
  var btnFecharModal   = modalLGPD && modalLGPD.querySelector('.modal-lgpd-fechar');
  var linkPrivacidade  = document.querySelectorAll('.link-privacidade');

  var STORAGE_KEY = 'cea_cookies_aceitos';

  function mostrarAviso() {
    if (!avisoCookies) return;
    setTimeout(function () {
      avisoCookies.classList.add('ativo');
    }, 1200);
  }

  function aceitarCookies() {
    localStorage.setItem(STORAGE_KEY, '1');
    if (avisoCookies) {
      avisoCookies.classList.remove('ativo');
      avisoCookies.classList.remove('visivel');
    }
    fecharModalLGPD();
  }

  function abrirModalLGPD(e) {
    if (e) e.preventDefault();
    if (!modalLGPD) return;
    modalLGPD.classList.add('ativo');
    document.body.style.overflow = 'hidden';
  }

  function fecharModalLGPD() {
    if (!modalLGPD) return;
    modalLGPD.classList.remove('ativo');
    document.body.style.overflow = '';
  }

  // Verificar se já aceitou
  if (!localStorage.getItem(STORAGE_KEY)) {
    mostrarAviso();
  }

  if (btnAceitarCook) {
    btnAceitarCook.addEventListener('click', aceitarCookies);
  }

  if (btnAceitarLGPD) {
    btnAceitarLGPD.addEventListener('click', aceitarCookies);
  }

  if (btnFecharModal) {
    btnFecharModal.addEventListener('click', fecharModalLGPD);
  }

  // Abrir modal ao clicar nos links de privacidade dentro do banner
  linkPrivacidade.forEach(function (link) {
    link.addEventListener('click', function (e) {
      // Se o link está dentro do banner de cookies, abre modal em vez de navegar
      if (avisoCookies && avisoCookies.contains(link)) {
        abrirModalLGPD(e);
      }
    });
  });

  // Fechar modal com ESC ou clicando fora
  if (modalLGPD) {
    modalLGPD.addEventListener('click', function (e) {
      if (e.target === modalLGPD) fecharModalLGPD();
    });
  }

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') fecharModalLGPD();
  });

  /* ─── 5. LINKS DO CABEÇALHO — Estado ATIVO por página atual ──────────────── */
  var paginaAtual = window.location.pathname.split('/').pop() || 'index.html';
  var linksNav = document.querySelectorAll('.nav-link, .nav-mobile-link');

  linksNav.forEach(function (link) {
    var href = (link.getAttribute('href') || '').split('#')[0].split('?')[0];
    var nome = href.split('/').pop() || 'index.html';
    // Remover ativo de todos primeiro
    link.classList.remove('ativo');
    // Aplicar ativo no link correto
    if (nome === paginaAtual) {
      link.classList.add('ativo');
    }
  });

  /* ─── 6. SCROLL SUAVE PARA ÂNCORAS INTERNAS ────────────────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var id = link.getAttribute('href').substring(1);
      var alvo = document.getElementById(id);
      if (alvo) {
        e.preventDefault();
        alvo.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  /* ─── 7. COPIAR LINK DO ARTIGO (COMPARTILHAMENTO FÁCIL) ─────────────────── */
  window.copiarLinkArtigo = function (btn) {
    var url = window.location.href;
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(url).then(function () {
        exibirFeedbackCopia(btn);
      }).catch(function () {
        fallbackCopiar(url, btn);
      });
    } else {
      fallbackCopiar(url, btn);
    }
  };

  function fallbackCopiar(url, btn) {
    var input = document.createElement('input');
    input.value = url;
    document.body.appendChild(input);
    input.select();
    try {
      document.execCommand('copy');
      exibirFeedbackCopia(btn);
    } catch (e) {
      prompt('Copie o link abaixo:', url);
    }
    document.body.removeChild(input);
  }

  function exibirFeedbackCopia(btn) {
    if (!btn) return;
    var span = btn.querySelector('span');
    var textoOriginal = btn.getAttribute('data-original-text') || (span ? span.textContent : 'Copiar Link');
    btn.setAttribute('data-original-text', textoOriginal);
    if (span) {
      span.textContent = 'Copiado!';
    }
    btn.classList.add('copiado');
    setTimeout(function () {
      if (span) {
        span.textContent = textoOriginal;
      }
      btn.classList.remove('copiado');
    }, 2500);
  }

})();
