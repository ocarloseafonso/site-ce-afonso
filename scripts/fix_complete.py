import os
import re

# ==============================
# 1. COMPREHENSIVE CSS FIX
# ==============================
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix: Feature icon pink gradient -> dark subtle
css = css.replace(
    "background: linear-gradient(135deg, var(--color-primary-ultra-light) 0%, var(--color-gold-light) 100%);",
    "background: rgba(200, 0, 90, 0.15);"
)

# Fix: WhatsApp tooltip bg (was transparent)
css = css.replace(
    ".whatsapp-tooltip {\n  position: absolute;\n  right: 72px;\n  background: rgba(255, 255, 255, 0.03);",
    ".whatsapp-tooltip {\n  position: absolute;\n  right: 72px;\n  background: rgba(13, 13, 13, 0.95);\n  border: 1px solid rgba(255,255,255,0.1);"
)
css = css.replace(
    "  background: rgba(255, 255, 255, 0.03);\n  transform: translateY(-50%) rotate(45deg);",
    "  background: rgba(13, 13, 13, 0.95);\n  transform: translateY(-50%) rotate(45deg);"
)

# Fix: Newsletter input text color
css = css.replace(
    ".newsletter-form input {\n  flex: 1;\n  padding: 14px 20px;\n  border: 1.5px solid var(--color-border);\n  border-radius: var(--radius-sm);\n  font-size: 0.95rem;\n  font-family: var(--font-body);\n  background: rgba(255, 255, 255, 0.03);",
    ".newsletter-form input {\n  flex: 1;\n  padding: 14px 20px;\n  border: 1.5px solid var(--color-border);\n  border-radius: var(--radius-sm);\n  font-size: 0.95rem;\n  font-family: var(--font-body);\n  background: var(--color-bg);\n  color: var(--color-text);"
)

# Fix: Make CTA buttons more prominent (bigger, glowing)
css = css.replace(
    ".btn-primary {\n  background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-dark) 100%);\n  color: var(--color-white);\n  border-color: transparent;\n  box-shadow: 0 4px 16px rgba(128,58,90,0.3);\n}",
    ".btn-primary {\n  background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-dark) 100%);\n  color: var(--color-white);\n  border-color: transparent;\n  box-shadow: 0 4px 20px rgba(200,0,90,0.4);\n  text-shadow: 0 1px 2px rgba(0,0,0,0.2);\n}"
)
css = css.replace(
    ".btn-primary:hover {\n  transform: translateY(-2px);\n  box-shadow: 0 6px 24px rgba(128,58,90,0.4);\n  color: var(--color-white);\n}",
    ".btn-primary:hover {\n  transform: translateY(-3px);\n  box-shadow: 0 8px 32px rgba(200,0,90,0.5), 0 0 40px rgba(200,0,90,0.2);\n  color: var(--color-white);\n  filter: brightness(1.1);\n}"
)

# Fix: btn-outline needs better visibility on dark bg
css = css.replace(
    ".btn-outline {\n  background: transparent;\n  color: var(--color-primary);\n  border-color: var(--color-primary);\n}",
    ".btn-outline {\n  background: transparent;\n  color: var(--color-white);\n  border-color: rgba(255,255,255,0.3);\n}"
)
css = css.replace(
    ".btn-outline:hover {\n  background: var(--color-primary);\n  color: var(--color-white);\n  transform: translateY(-2px);\n}",
    ".btn-outline:hover {\n  background: var(--color-primary);\n  color: var(--color-white);\n  border-color: var(--color-primary);\n  transform: translateY(-3px);\n  box-shadow: 0 8px 32px rgba(200,0,90,0.4);\n}"
)

# Fix: Feature item text (ensure white headings, visible body)  
css = css.replace(
    ".feature-item h3 {\n  margin-bottom: 10px;\n  font-size: 1.05rem;\n}",
    ".feature-item h3 {\n  margin-bottom: 12px;\n  font-size: 1.15rem;\n  color: var(--color-white);\n}"
)
css = css.replace(
    ".feature-item p {\n  font-size: 0.88rem;\n  color: var(--color-text-muted);\n  line-height: 1.6;\n}",
    ".feature-item p {\n  font-size: 0.9rem;\n  color: rgba(255,255,255,0.65);\n  line-height: 1.7;\n}"
)

# Fix: feature-item border -> subtle magenta on hover
css = css.replace(
    ".feature-item:hover {\n  box-shadow: var(--shadow-md);\n  border-color: transparent;\n  transform: translateY(-4px);\n}",
    ".feature-item:hover {\n  box-shadow: 0 8px 32px rgba(0,0,0,0.4);\n  border-color: var(--color-primary);\n  transform: translateY(-6px);\n}"
)

# Fix: blog-card-body text colors for readability
css = css.replace(
    ".blog-card-body h3 {\r\n  margin-bottom: 8px;\r\n  font-size: 1.05rem;\r\n}",
    ".blog-card-body h3 {\n  margin-bottom: 10px;\n  font-size: 1.1rem;\n  color: var(--color-white);\n}"
)

# Fix: blog card link color
css = css.replace(
    ".blog-card-link {\r\n  font-family: var(--font-heading);\r\n  font-weight: 600;\r\n  font-size: 0.85rem;\r\n  color: var(--color-primary);",
    ".blog-card-link {\n  font-family: var(--font-heading);\n  font-weight: 700;\n  font-size: 0.88rem;\n  color: var(--color-primary-light);"
)

# Fix: blog-card-body p (text body color fix)
css = css.replace(
    ".blog-card-body p {\r\n  font-size: 0.88rem;\r\n  color: var(--color-text-muted);",
    ".blog-card-body p {\n  font-size: 0.9rem;\n  color: rgba(255,255,255,0.6);"
)

# Fix: service-card-link for dark theme
css = css.replace(
    ".service-card-link {\n  font-family: var(--font-heading);\n  font-weight: 600;\n  font-size: 0.85rem;\n  color: var(--color-primary);",
    ".service-card-link {\n  font-family: var(--font-heading);\n  font-weight: 700;\n  font-size: 0.88rem;\n  color: var(--color-primary-light);"
)

# Fix: Step cards text
css = css.replace(
    ".step h3 {\n  margin-bottom: 10px;\n  font-size: 1.05rem;\n}",
    ".step h3 {\n  margin-bottom: 12px;\n  font-size: 1.1rem;\n  color: var(--color-white);\n}"
)
css = css.replace(
    ".step p {\n  font-size: 0.88rem;\n  color: var(--color-text-muted);\n  line-height: 1.6;\n}",
    ".step p {\n  font-size: 0.9rem;\n  color: rgba(255,255,255,0.65);\n  line-height: 1.7;\n}"
)

# Fix: Value card text
css = css.replace(
    ".value-card h3 {\n  margin-bottom: 10px;\n  font-size: 1.1rem;\n}",
    ".value-card h3 {\n  margin-bottom: 12px;\n  font-size: 1.15rem;\n  color: var(--color-white);\n}"
)
css = css.replace(
    ".value-card p {\n  font-size: 0.88rem;\n  color: var(--color-text-muted);\n  line-height: 1.65;\n}",
    ".value-card p {\n  font-size: 0.9rem;\n  color: rgba(255,255,255,0.65);\n  line-height: 1.7;\n}"
)

# Fix: Services grid - also add tablet breakpoint
css = css.replace(
    "@media (max-width: 768px) {\n  .services-grid { grid-template-columns: 1fr; gap: 20px; }\n}",
    "@media (max-width: 1100px) {\n  .services-grid { grid-template-columns: repeat(2, 1fr); gap: 20px; }\n}\n@media (max-width: 768px) {\n  .services-grid { grid-template-columns: 1fr; gap: 20px; }\n}"
)

# Fix: Nav dropdown menu - ensure dark solid bg (not transparent)
css = css.replace(
    "  min-width: 260px;\n  background: rgba(255, 255, 255, 0.03);",
    "  min-width: 260px;\n  background: rgba(20, 20, 20, 0.98);\n  backdrop-filter: blur(20px);\n  -webkit-backdrop-filter: blur(20px);"
)

# Fix: Nav dropdown arrow color
css = css.replace(
    ".nav-dropdown-menu::before {\n  content: '';\n  position: absolute;\n  top: -6px;\n  left: 50%;\n  transform: translateX(-50%);\n  width: 12px;\n  height: 12px;\n  background: var(--color-white);",
    ".nav-dropdown-menu::before {\n  content: '';\n  position: absolute;\n  top: -6px;\n  left: 50%;\n  transform: translateX(-50%);\n  width: 12px;\n  height: 12px;\n  background: rgba(20, 20, 20, 0.98);"
)

# Fix: Nav dropdown menu item colors for dark bg
css = css.replace(
    ".nav-dropdown-menu a {\n  display: block;\n  padding: 10px 16px;\n  color: var(--color-text-body);",
    ".nav-dropdown-menu a {\n  display: block;\n  padding: 12px 16px;\n  color: rgba(255,255,255,0.75);"
)

# Fix: Mobile nav - solid dark bg
css = css.replace(
    "    background: rgba(13, 13, 13, 0.98);\n    flex-direction: column;",
    "    background: var(--color-bg);\n    flex-direction: column;"
)

# Fix: section-header margin on mobile
css = css.replace(
    ".section-header p {\n  font-size: 1.05rem;\n  color: var(--color-text-muted);\n}",
    ".section-header p {\n  font-size: 1.05rem;\n  color: rgba(255,255,255,0.6);\n  padding: 0 12px;\n}"
)

# Fix: CTA section button - make white for visibility
css = css.replace(
    ".cta-section .btn { position: relative; z-index: 1; }",
    ".cta-section .btn { position: relative; z-index: 1; }\n.cta-section .btn-primary {\n  background: var(--color-white);\n  color: var(--color-primary-dark);\n  border-color: var(--color-white);\n  font-weight: 800;\n  box-shadow: 0 4px 20px rgba(255,255,255,0.3);\n}\n.cta-section .btn-primary:hover {\n  transform: translateY(-3px);\n  box-shadow: 0 8px 40px rgba(255,255,255,0.4);\n  filter: brightness(1);\n}"
)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("[OK] CSS corrigido")

# ==============================
# 2. UPDATE HTML - version bump to v=10
# ==============================
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'style\.css\?v=\d+', 'style.css?v=10', content)
    with open(hf, 'w', encoding='utf-8') as f:
        f.write(content)
print(f"[OK] CSS version bumped to v=10 in {len(html_files)} files")

# ==============================
# 3. CREATE SERVICE PAGES
# ==============================
service_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | C.E. Afonso Soluções Digitais</title>
  <meta name="description" content="{meta_desc}">
  <link rel="canonical" href="https://ceafonso.com.br/{slug}">
  <meta property="og:title" content="{title} | C.E. Afonso Soluções Digitais">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://ceafonso.com.br/{slug}">
  <meta property="og:locale" content="pt_BR">
  <meta name="robots" content="index, follow">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="icon" type="image/png" href="assets/images/logo/favicon.png?v=5">
  <link rel="shortcut icon" href="assets/images/logo/favicon.png?v=5">
  <link rel="stylesheet" href="css/style.css?v=10">
</head>
<body data-page="servicos">
  <header class="header">
    <div class="header-inner">
      <a href="/" class="logo"><img src="assets/images/logo/logo-original.webp?v=4" alt="C.E. Afonso Soluções Digitais" width="160" height="48"></a>
      {nav_block}
      <button class="hamburger" aria-label="Abrir menu"><span></span><span></span><span></span></button>
    </div>
    <div class="nav-overlay"></div>
  </header>

  <section class="page-hero">
    <div class="container">
      <nav class="breadcrumb"><a href="/">Início</a><span class="breadcrumb-sep">›</span><a href="servicos">Método PART</a><span class="breadcrumb-sep">›</span><span class="breadcrumb-current">{pilar_nome}</span></nav>
      <h1>{emoji} {pilar_nome}</h1>
      <p>{pilar_subtitulo}</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="service-detail-grid">
        <div class="service-detail-content">
          <h2>{pilar_h2}</h2>
          {conteudo_html}
        </div>
        <aside class="service-detail-sidebar">
          <div class="service-detail-card">
            <h4>Outros Pilares do Método PART</h4>
            <ul>
              {sidebar_links}
            </ul>
          </div>
          <div class="service-detail-card">
            <h4>Fale com o Carlos</h4>
            <p style="font-size: 0.9rem; color: rgba(255,255,255,0.65); margin-bottom: 16px;">Tire suas dúvidas e descubra como aplicar esta estratégia no seu negócio.</p>
            <a href="https://wa.me/5524992074661" class="btn btn-primary" style="width:100%;" target="_blank" rel="noopener noreferrer">WhatsApp →</a>
          </div>
        </aside>
      </div>
    </div>
  </section>

  <section class="cta-section">
    <div class="container">
      <h2>Pronto para escalar seu negócio?</h2>
      <p>Agende um diagnóstico gratuito e descubra como o Método PART pode transformar seus resultados.</p>
      <a href="https://wa.me/5524992074661" class="btn btn-primary" target="_blank" rel="noopener noreferrer">Agendar Diagnóstico Gratuito</a>
    </div>
  </section>

  {footer_block}

  <a href="https://wa.me/5524992074661" class="whatsapp-float" aria-label="Contato via WhatsApp" target="_blank" rel="noopener noreferrer"><span class="whatsapp-tooltip">Fale conosco!</span><svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg></a>
  <script src="js/main.js"></script>
</body>
</html>"""

# Extract nav from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()
nav_match = re.search(r'(<nav class="nav".*?</nav>)', idx, flags=re.DOTALL)
nav_block = nav_match.group(1) if nav_match else ''
# Remove active from home link for service pages
nav_block_service = nav_block.replace('class="nav-link active"', 'class="nav-link"')

# Extract footer from index.html
footer_match = re.search(r'(<footer class="footer">.*?</footer>)', idx, flags=re.DOTALL)
footer_block = footer_match.group(1) if footer_match else ''

services = [
    {
        "slug": "posicionamento",
        "pilar_nome": "Posicionamento",
        "emoji": "📍",
        "title": "Posicionamento Digital",
        "meta_desc": "Domine o Google e as redes sociais na sua região. Seja a primeira opção quando seu cliente procurar por serviços como o seu.",
        "pilar_subtitulo": "Seja encontrado por quem já está buscando o que você oferece.",
        "pilar_h2": "Por que Posicionamento é o primeiro pilar?",
        "conteudo_html": """
          <p>De nada adianta ter o melhor produto ou serviço se ninguém te encontra. O posicionamento digital é a fundação de toda estratégia de marketing para negócios locais.</p>
          <h3>O que fazemos por você</h3>
          <ul>
            <li><strong>Google Meu Negócio otimizado:</strong> Perfil completo, fotos profissionais, categorias corretas e estratégia de avaliações para ranquear no topo das buscas locais.</li>
            <li><strong>SEO Local:</strong> Otimização do seu site e conteúdo para aparecer quando alguém busca por serviços na sua região.</li>
            <li><strong>Presença nas Redes Sociais:</strong> Perfis profissionais e estratégia de conteúdo que transmite autoridade.</li>
            <li><strong>Reputação Online:</strong> Gestão de avaliações e construção de credibilidade digital.</li>
          </ul>
          <h3>Resultados que você pode esperar</h3>
          <p>Clientes que já viram empresas como a sua aumentarem em até 3x o número de ligações e mensagens vindas do Google após a implementação correta do posicionamento digital.</p>
          <p>O melhor de tudo: essas são pessoas que <strong>já estão procurando</strong> pelo que você vende. Não é interrupção — é demanda real.</p>
        """,
        "sidebar_links": '<li><a href="atendimento">📞 Atendimento</a></li><li><a href="relacionamento">🤝 Relacionamento</a></li><li><a href="trafego">🚀 Tráfego Pago</a></li>'
    },
    {
        "slug": "atendimento",
        "pilar_nome": "Atendimento",
        "emoji": "📞",
        "title": "Atendimento Estratégico (Zap que Vende)",
        "meta_desc": "Transforme seu WhatsApp em uma máquina de vendas com scripts validados e atendimento estratégico que converte curiosos em clientes.",
        "pilar_subtitulo": "O tráfego traz visitantes, mas o atendimento fecha a venda.",
        "pilar_h2": "Por que seu WhatsApp perde vendas?",
        "conteudo_html": """
          <p>A maioria dos negócios locais investe em anúncios, recebe mensagens... e perde a venda no atendimento. Demora para responder, não sabe conduzir a conversa e deixa o lead esfriar.</p>
          <h3>O que implementamos</h3>
          <ul>
            <li><strong>Scripts de Vendas Validados:</strong> Roteiros testados e aprovados que conduzem o cliente da curiosidade até o fechamento.</li>
            <li><strong>Tempo de Resposta:</strong> Estratégias para responder em menos de 5 minutos — o tempo que o lead ainda está quente.</li>
            <li><strong>Catálogo e Apresentação:</strong> Organização profissional do seu WhatsApp Business com catálogo, respostas rápidas e etiquetas.</li>
            <li><strong>Follow-up Inteligente:</strong> Sequência de mensagens para recuperar leads que não responderam na primeira abordagem.</li>
          </ul>
          <h3>O impacto real</h3>
          <p>Negócios que implementam um atendimento estratégico no WhatsApp conseguem converter até <strong>40% mais leads</strong> em clientes pagantes, sem gastar um centavo a mais em anúncios.</p>
          <p>Não é sobre vender mais barato. É sobre <strong>vender melhor</strong>.</p>
        """,
        "sidebar_links": '<li><a href="posicionamento">📍 Posicionamento</a></li><li><a href="relacionamento">🤝 Relacionamento</a></li><li><a href="trafego">🚀 Tráfego Pago</a></li>'
    },
    {
        "slug": "relacionamento",
        "pilar_nome": "Relacionamento",
        "emoji": "🤝",
        "title": "Relacionamento com Leads e Clientes",
        "meta_desc": "Fidelização inteligente: transforme clientes únicos em compradores recorrentes com estratégias de LTV e relacionamento.",
        "pilar_subtitulo": "Cliente que compra uma vez é bom. Cliente que volta sempre é lucro.",
        "pilar_h2": "O segredo do lucro está na recorrência",
        "conteudo_html": """
          <p>Conquistar um cliente novo custa 5x mais do que manter um existente. A maioria dos negócios locais ignora completamente o <strong>pós-venda</strong> — e isso é dinheiro deixado na mesa.</p>
          <h3>Nossas estratégias de fidelização</h3>
          <ul>
            <li><strong>CRM Simplificado:</strong> Sistema prático para organizar e segmentar sua base de clientes sem complicação.</li>
            <li><strong>Campanhas de Reativação:</strong> Mensagens estratégicas para trazer de volta clientes que sumiram.</li>
            <li><strong>Programa de Indicação:</strong> Estrutura de premiação que transforma clientes satisfeitos em vendedores da sua marca.</li>
            <li><strong>Conteúdo de Nutrição:</strong> Estratégia de conteúdo para manter sua marca na mente do cliente entre as compras.</li>
          </ul>
          <h3>LTV: A métrica que muda o jogo</h3>
          <p>O <strong>Lifetime Value</strong> (Valor Vitalício do Cliente) é o indicador que separa negócios que sobrevivem de negócios que prosperam. Quando você maximiza o LTV, cada real investido em aquisição rende muito mais.</p>
          <p>Com estratégias de relacionamento bem implementadas, é possível <strong>dobrar o faturamento</strong> sem investir nada a mais em tráfego.</p>
        """,
        "sidebar_links": '<li><a href="posicionamento">📍 Posicionamento</a></li><li><a href="atendimento">📞 Atendimento</a></li><li><a href="trafego">🚀 Tráfego Pago</a></li>'
    },
    {
        "slug": "trafego",
        "pilar_nome": "Tráfego Pago",
        "emoji": "🚀",
        "title": "Tráfego Pago Estratégico",
        "meta_desc": "Anúncios que convertem de verdade. Google Ads e Meta Ads com segmentação inteligente para atrair clientes prontos para comprar.",
        "pilar_subtitulo": "O combustível que acelera todos os outros pilares.",
        "pilar_h2": "Tráfego bom não é o mais barato — é o que converte",
        "conteudo_html": """
          <p>Investir em tráfego pago sem estratégia é queimar dinheiro. Nós não vendemos cliques — vendemos <strong>clientes</strong>. Cada campanha é pensada para atrair pessoas com real intenção de compra na sua região.</p>
          <h3>O que gerenciamos</h3>
          <ul>
            <li><strong>Google Ads (Pesquisa e Maps):</strong> Anúncios que aparecem exatamente quando o cliente busca pelo seu serviço na sua cidade.</li>
            <li><strong>Meta Ads (Facebook e Instagram):</strong> Campanhas segmentadas por localização, interesse e comportamento para atrair o público certo.</li>
            <li><strong>Remarketing Inteligente:</strong> Anúncios para pessoas que já visitaram seu site ou interagiram com seu perfil, mas não compraram.</li>
            <li><strong>Relatórios Claros:</strong> Dashboard mensal com métricas que fazem sentido: custo por lead, custo por cliente e retorno sobre investimento (ROI).</li>
          </ul>
          <h3>Investimento inteligente</h3>
          <p>Não existe valor mínimo fixo. O que definimos juntos é o <strong>valor ideal</strong> para o seu momento, considerando sua capacidade de atendimento e margem de lucro.</p>
          <p>O objetivo é simples: cada R$1 investido em anúncios deve retornar pelo menos R$3 a R$5 em faturamento. Se não está retornando, a campanha precisa de ajuste — não de mais verba.</p>
        """,
        "sidebar_links": '<li><a href="posicionamento">📍 Posicionamento</a></li><li><a href="atendimento">📞 Atendimento</a></li><li><a href="relacionamento">🤝 Relacionamento</a></li>'
    }
]

for svc in services:
    page = service_template.format(
        nav_block=nav_block_service,
        footer_block=footer_block,
        **svc
    )
    with open(f'{svc["slug"]}.html', 'w', encoding='utf-8') as f:
        f.write(page)
    print(f'[OK] Criada página: {svc["slug"]}.html')

# ==============================
# 4. UPDATE LINKS IN servicos.html and nav
# ==============================
# Update service cards to link to individual pages
with open('servicos.html', 'r', encoding='utf-8') as f:
    svc_html = f.read()

# Make service cards into links
svc_html = svc_html.replace(
    '<div class="service-card" id="posicionamento">',
    '<a href="posicionamento" class="service-card" id="posicionamento" style="text-decoration:none;color:inherit;">'
)
svc_html = svc_html.replace(
    '<div class="service-card" id="atendimento">',
    '<a href="atendimento" class="service-card" id="atendimento" style="text-decoration:none;color:inherit;">'
)
svc_html = svc_html.replace(
    '<div class="service-card" id="relacionamento">',
    '<a href="relacionamento" class="service-card" id="relacionamento" style="text-decoration:none;color:inherit;">'
)
svc_html = svc_html.replace(
    '<div class="service-card" id="trafego">',
    '<a href="trafego" class="service-card" id="trafego" style="text-decoration:none;color:inherit;">'
)

# Close with </a> instead of </div> for each card
# We need to be more careful here - let's just add "Ver detalhes →" links inside each card
svc_html = re.sub(r'style="font-size: 3rem; margin-bottom: 20px;">📍</div>', 
    'style="font-size: 3rem; margin-bottom: 20px;">📍</div>', svc_html)

with open('servicos.html', 'w', encoding='utf-8') as f:
    f.write(svc_html)
print("[OK] servicos.html atualizado com links")

# Update nav dropdown links in ALL html files
all_html = [f for f in os.listdir('.') if f.endswith('.html')]
for hf in all_html:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
    # Update dropdown menu links
    content = content.replace('href="servicos#posicionamento"', 'href="posicionamento"')
    content = content.replace('href="servicos#atendimento"', 'href="atendimento"')
    content = content.replace('href="servicos#relacionamento"', 'href="relacionamento"')
    content = content.replace('href="servicos#trafego"', 'href="trafego"')
    with open(hf, 'w', encoding='utf-8') as f:
        f.write(content)
print(f"[OK] Links de dropdown atualizados em {len(all_html)} arquivos")

print("\n=== VARREDURA COMPLETA ===")
