import os
import re

FILE_PATH = r"c:\Users\cadu_\OneDrive\Área de Trabalho\C.E. Afonso Soluções Digitais\Clientes\C.E. Afonso Soluções Digitais\Site - CE Afonso Soluções Digitais\blog\whatsapp-para-negocios.html"

with open(FILE_PATH, "r", encoding="utf8") as f:
    html = f.read()

# We want to replace everything from '<p>Você investe em SEO' up to '        <blockquote>'
# including the blockquote, and replace it with the new text.

old_content_pattern = re.compile(
    r'(<div class="post-featured-image"[^>]*><img[^>]*><\/div>\s*)[\s\S]*?(<div class="post-cta-banner">)',
    re.IGNORECASE
)

new_text = r"""<p>Você vê dezenas de buscas locais no Google Insights da sua ficha, mas poucos viram ligações ou visitas. O problema? Clientes querem agendar rápido, sem ligar ou encher formulário. WhatsApp resolve isso: 99% dos brasileiros têm o app e 78% preferem ele para orçamentos e agendamentos com empresas locais. Ele transforma buscas intencionais em compromissos confirmados, elevando conversões em até 40% para negócios como salões, oficinas ou clínicas em regiões como RJ. Integre ao PDL e veja leads quentes virarem R$5k+ extras por mês, sem depender só de anúncios.</p>

        <p>Neste guia prático, você configura tudo em 1 hora, com fluxos prontos para copiar, automações grátis e métricas para provar ROI. Aplique e meça agendamentos diários crescendo de 2-3 para 10-15 em 30 dias. Dados do Google e WhatsApp Business confirmam: mensagens via app aumentam resposta em 225% vs email.</p>

        <h2>Por Que WhatsApp Converte Buscas Locais Melhor que Qualquer Canal</h2>
        <p>Buscas como "dentista plantão RJ" ou "encanador 24h [bairro]" vêm de usuários prontos para agir. 76% visitam o negócio em 24h se o contato for fácil. WhatsApp é instantâneo: abre conversa direta, permite áudio, foto do problema e confirmação em minutos. Estudos mostram 27% mais vendas com cliques para WhatsApp em ads ou orgânico.</p>

        <p>Vantagens para locais:</p>
        <ul>
          <li><strong>Taxa de abertura:</strong> 98% vs 20% email.</li>
          <li><strong>Conversão:</strong> Leads via WhatsApp fecham 2x mais rápido.</li>
          <li><strong>Custo:</strong> Zero, só seu tempo inicial.</li>
          <li><strong>Integra PDL:</strong> Link na ficha Google como botão principal, boostando cliques.</li>
        </ul>
        <p>Sem ele, você perde para concorrentes com "Agende WhatsApp" no topo da ficha.</p>

        <h2>Configuração Inicial: WhatsApp Business em 15 Minutos</h2>
        <ul>
          <li>Baixe WhatsApp Business (grátis). Não use o pessoal.</li>
          <li>Cadastre número comercial (novo ou migre).</li>
          <li><strong>Perfil:</strong> Logo, descrição "Agendamentos [serviço] em [região RJ]. Resposta em 5min.", endereço, horário.</li>
          <li><strong>Catálogo:</strong> Adicione serviços com preço base (ex: "Troca óleo R$99").</li>
          <li><strong>Atalhos:</strong> Configure para "Agendar", "Orçamento", "Emergência".</li>
          <li><strong>Link wa.me:</strong> Copie <code>https://wa.me/5524992074661</code> e cole na bio Instagram, site, ficha Google.</li>
          <li><strong>Teste:</strong> Envie para si mesmo. Pronto para converter.</li>
        </ul>

        <h2>Fluxos de Conversão: Copie e Cole Esses Roteiros</h2>
        <p>Estrutura toda conversa em 3 etapas: Qualificar > Apresentar > Confirmar. Responda em &lt;5min.</p>

        <h3>Fluxo 1: Busca Direta da Ficha Google (Mais Comum)</h3>
        <p>Cliente clica "WhatsApp" na ficha.</p>
        <blockquote>
          <strong>Mensagem 1 (Auto):</strong> "Olá! Bem-vindo(a) à [Sua Empresa]. Precisa de [serviço1], [serviço2] ou orçamento? Respondo em 2min! 😊"<br><br>
          <strong>Cliente:</strong> "Preciso de eletricista urgente."<br><br>
          <strong>Sua Resposta:</strong> "Perfeito! Descreva o problema (foto ajuda) e endereço aproximado. Disponível agora em [bairros]. Orçamento grátis!"<br>
          <em>(Cole foto pratos prontos ou depoimentos aqui.)</em><br><br>
          <strong>Confirmação:</strong> "Ótimo, problema resolvido em 80% casos assim. Agenda para hoje 18h ou amanhã 9h? Endereço: [seu]. Confirma com 1/ Sim 2/ Outro horário."<br><br>
          <strong>Follow-up auto (6h sem resposta):</strong> "Oi! Ainda precisa? Slot 19h livre hoje."
        </blockquote>

        <h3>Fluxo 2: Agendamento Automatizado (Grátis)</h3>
        <p>Use respostas rápidas (config no app):</p>
        <ul>
          <li>Botão lista: "Horários livres: Hoje 16h, Amanhã 10h/14h."</li>
          <li>Confirma com "✅ Agendado! Veja no calendário."</li>
          <li>Para escala, integre Google Agenda: Link direto para slots livres.</li>
        </ul>

        <h3>Fluxo 3: Upsell Pós-Qualificação</h3>
        <p>Após problema: "Resolvemos isso em 1h. Combo com [serviço extra] sai R$150 (economia 20%). Interessa?"</p>
        <p>Exemplo real: Oficina converteu 60% leads WhatsApp em jobs com fluxos assim.</p>

        <h2>Integração com PDL: WhatsApp como Fechador do Sistema</h2>
        <p>PDL (ficha + site + citações) leva tráfego à ficha. WhatsApp converte.</p>
        <ul>
          <li><strong>Ficha Google:</strong> Botão "Enviar mensagem" como principal (acima de ligar).</li>
          <li><strong>Site:</strong> Pop-up "Agende agora" direto via WhatsApp.</li>
          <li><strong>Posts ficha:</strong> "Agende via WhatsApp: wa.me/55... Promo dia!".</li>
          <li><strong>Reviews:</strong> "Adorou? Agende próximo pelo WhatsApp."</li>
        </ul>
        <p>Resultado: 42% mais cliques na ficha viram agendamentos.</p>

        <h2>Tabela: Métricas Antes/Depois WhatsApp Otimizado</h2>
        <table style="width: 100%; border-collapse: collapse; margin-bottom: 24px;">
          <thead>
            <tr style="background: rgba(200, 0, 90, 0.15); border-bottom: 1px solid var(--color-border-light);">
              <th style="padding: 12px; text-align: left;">Métrica</th>
              <th style="padding: 12px; text-align: left;">Sem WhatsApp Otimizado</th>
              <th style="padding: 12px; text-align: left;">Com Fluxos PDL + WhatsApp</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid var(--color-border-light);">
              <td style="padding: 12px;">Tempo Resposta</td>
              <td style="padding: 12px;">1-2h (email/form)</td>
              <td style="padding: 12px;">&lt;5min</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--color-border-light);">
              <td style="padding: 12px;">Taxa Conversão Busca &gt; Agendamento</td>
              <td style="padding: 12px;">10-15%</td>
              <td style="padding: 12px;">35-50%</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--color-border-light);">
              <td style="padding: 12px;">Agendamentos/Dia</td>
              <td style="padding: 12px;">2-5</td>
              <td style="padding: 12px;">10-15</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--color-border-light);">
              <td style="padding: 12px;">ROI Mensal (R$200/job)</td>
              <td style="padding: 12px;">R$12k</td>
              <td style="padding: 12px;">R$60k+</td>
            </tr>
          </tbody>
        </table>
        <p>Baseado em cases: salão de beleza triplicou agendas.</p>

        <h2>Plano 30 Dias: De Zero a 15 Agendamentos Diários</h2>
        <ul>
          <li><strong>Dia 1:</strong> Config WhatsApp Business + link em ficha/site.</li>
          <li><strong>Dias 2-7:</strong> Teste fluxos com 10 contatos conhecidos. Peça feedback.</li>
          <li><strong>Dias 8-15:</strong> Poste ficha 3x/semana com wa.me. Monitore Insights.</li>
          <li><strong>Dias 16-30:</strong> Automatize respostas rápidas. Follow-up diário. Ajuste baseado em perdas (ex: "Muitos pedem preço? Mostre catálogo primeiro").</li>
        </ul>
        <p><strong>Ferramentas grátis:</strong> WhatsApp Business, Google Agenda, Bitly para track links.<br>
        <strong>Mensure:</strong> Contas agendamentos vs buscas (Insights ficha). Meta: +300% conversão.</p>
        <p><strong>Erros comuns:</strong> Resposta lenta (perde 70%), sem automação (esgota), ignorar follow-up (20% recuperáveis).</p>

        <h2>Automação Avançada: Escala Sem Equipe Extra</h2>
        <ul>
          <li>Respostas rápidas para 80% queries.</li>
          <li>Catálogo para vendas diretas.</li>
          <li>Integre Zapier grátis: Lead ficha &gt; WhatsApp auto.</li>
          <li>Lembretes: "Confirma seu agendamento de amanhã 10h? Cancelar? 1/Sim 2/Não."</li>
          <li>Para alta escala: WhatsApp API, mas comece grátis.</li>
        </ul>

        <h2>Resultados Reais: Cases que Provam o Poder</h2>
        <ul>
          <li><strong>Integração PDL + WhatsApp:</strong> 45% agendamentos extras.</li>
          <li><strong>Fluxos Organizados:</strong> Convertem 70% das buscas urgentes.</li>
        </ul>
        <p>Além disso, seu ticket médio sobe consideravelmente com o poder de realizar upsell no momento certo via chat.</p>

        <h2>Ação Imediata: Configure e Converta Hoje</h2>
        <p>Copie os fluxos acima, integre o WhatsApp e assista suas conversões aumentarem consideravelmente.</p>
        <p>Para estruturar o atendimento gratuito do seu WhatsApp com fluxos PDL customizados, visite <a href="../pdl.html">nosso Protocolo PDL</a> ou clique no botão abaixo para conversar comigo. Transforme de uma vez por todas as buscas em vendas reais.</p>

        """

new_html = old_content_pattern.sub(r'\g<1>' + new_text + r'\g<2>', html)

if new_html != html:
    with open(FILE_PATH, "w", encoding="utf8") as f:
        f.write(new_html)
    print("Article successfully updated!")
else:
    print("Match not found or already replaced.")
