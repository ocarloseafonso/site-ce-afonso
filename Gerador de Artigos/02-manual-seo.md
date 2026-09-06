# Documento 02 — Manual SEO
### Blog institucional — Carlos Eduardo Afonso | Volta Redonda

---

## 1. Objetivo deste documento

Define como estruturar tecnicamente cada artigo para maximizar a chance de aparecer nas buscas. Trabalha junto com o Documento 01 (Manual Editorial) — aqui não se decide *o que* escrever, se decide *como estruturar* o que já foi decidido.

Convenção de marcação: **[OBRIGATÓRIO]**, **[PADRÃO]**, **[VARIÁVEL]** — mesmo critério do Documento 01.

---

## 2. Princípio geral

**[OBRIGATÓRIO]** Não existe fórmula de "repetir a palavra-chave X vezes". Isso é prática ultrapassada e pode até prejudicar. O critério real é: o Google entende do que a página trata e para quem ela é relevante quando o conteúdo usa naturalmente os termos que as pessoas realmente buscam, principalmente em título, headings e primeiros parágrafos.

**[OBRIGATÓRIO]** Desde 2024 o antigo "sistema de conteúdo útil" do Google foi incorporado ao algoritmo de busca principal — não é mais um filtro separado, é parte de como toda página é avaliada. Na prática isso não muda a regra de ouro: conteúdo original, completo, que resolve o problema de quem chegou até ali.

---

## 3. Estrutura técnica por artigo

Cada artigo precisa definir, antes de ser escrito (essa definição vem do Documento 04, ficha de pauta):

```
KEYWORD PRINCIPAL:
TERMOS SECUNDÁRIOS:
VARIAÇÕES SEMÂNTICAS:
INTENÇÃO DE BUSCA: (informacional / comercial / transacional)
LOCALIZAÇÃO:
PERGUNTAS RELACIONADAS:
SERVIÇO RELACIONADO:
PÁGINA INTERNA PARA LINKAR:
```

**[OBRIGATÓRIO]** A keyword principal deve aparecer:
- No título (H1)
- Em pelo menos um subtítulo (H2)
- No primeiro parágrafo, de forma natural
- Na meta description

**[OBRIGATÓRIO]** Não forçar a keyword de forma antinatural. Se a frase ficar estranha para incluir o termo exato, usar uma variação semântica.

---

## 4. Título (H1) e title tag

- **[OBRIGATÓRIO]** O H1 do artigo é único e diferente da title tag (meta título), mas ambos devem conter a keyword principal.
- **[PADRÃO]** Title tag entre 50–60 caracteres, para não ser cortada nos resultados de busca.
- **[PADRÃO]** Priorizar títulos que respondem a uma pergunta real ou nomeiam um problema real, não títulos genéricos de "dicas".
- **[VARIÁVEL]** Incluir "Volta Redonda" no título quando a busca real inclui a cidade (validar no Documento 04). Não inserir a cidade no título só por hábito.

---

## 5. Meta description

- **[OBRIGATÓRIO]** Toda página tem meta description própria, entre 140–160 caracteres.
- **[OBRIGATÓRIO]** Resume o problema que o artigo resolve e menciona a keyword principal, escrita para convidar o clique, não para repetir o título.

---

## 6. Estrutura de headings (H2/H3)

- **[OBRIGATÓRIO]** Um H1 por artigo. H2 para as seções principais (que seguem a estrutura do Documento 01: problema, causa, solução, passo a passo, erros comuns, quando buscar ajuda). H3 apenas quando uma seção precisa de subdivisão real.
- **[PADRÃO]** Evitar headings artificiais criados só para "parecer bem estruturado" — cada heading precisa corresponder a uma divisão real de conteúdo.

---

## 7. URL

- **[OBRIGATÓRIO]** Padrão de URL: `/blog/titulo-resumido-sem-acentos-e-sem-stopwords-desnecessarias`
- **[PADRÃO]** Priorizar incluir a keyword principal na URL, de forma curta. Exemplo: para "Como colocar uma empresa no Google Maps em Volta Redonda", URL sugerida: `/blog/como-colocar-empresa-no-google-maps-volta-redonda`
- **[OBRIGATÓRIO]** Nunca alterar a URL de um artigo já publicado e indexado sem redirecionamento 301 configurado — isso derruba posicionamento.

---

## 8. Links internos (detalhamento técnico)

Complementa a regra editorial do Documento 01.

- **[OBRIGATÓRIO]** Cada artigo linka para no mínimo 1 e no máximo 4 outros conteúdos internos (outros artigos + página de serviço).
- **[OBRIGATÓRIO]** Texto âncora deve ser descritivo do destino, nunca genérico ("clique aqui", "saiba mais"). Exemplo correto: "veja como funciona a criação de Google Meu Negócio".
- **[PADRÃO]** Quando um artigo novo for publicado, verificar se artigos antigos relacionados podem receber um link para ele também — isso distribui relevância pela estrutura toda, não só do artigo novo para os antigos.
- **[VARIÁVEL]** Densidade de links aumenta em artigos mais longos (guias completos podem ter mais pontos de link que respostas diretas).

---

## 9. Dados estruturados (schema markup)

Isso não estava no plano original, mas é importante para negócio local — ajuda o Google a entender a página de forma estruturada, além do texto.

- **[PADRÃO]** Toda página de serviço deve ter schema `LocalBusiness`, com nome, endereço, telefone, área de atendimento e categoria consistentes com o Google Perfil da Empresa.
- **[PADRÃO]** Todo artigo do blog deve ter schema `Article` ou `BlogPosting`, incluindo autor (Carlos Eduardo Afonso), data de publicação e data de atualização.
- **[VARIÁVEL]** Artigos estruturados como pergunta-resposta (ex: "Quanto custa um site?") podem usar schema `FAQPage` quando fizer sentido, mas isso deve ser avaliado caso a caso — uso excessivo ou incorreto de FAQ schema pode ser penalizado.
- Nota: implementação técnica do schema é responsabilidade do deploy no Antigravity — este documento define **o que** precisa estar presente, não o código.

---

## 10. Consistência NAP (Nome, Endereço, Telefone)

- **[OBRIGATÓRIO]** Nome da empresa, endereço e telefone devem ser idênticos, caractere por caractere, em: site, Google Perfil da Empresa, e qualquer diretório ou rede social onde a empresa apareça. Inconsistência aqui prejudica SEO local de forma direta.
- Esse controle não é parte do conteúdo do blog, mas deve ser verificado como parte da base de SEO local geral (fora do escopo deste manual, mas registrado aqui como lembrete operacional).

---

## 11. Imagens de Capa e Miniaturas (origem: Documentos 09 e 10)

- **[OBRIGATÓRIO]** Toda publicação de artigo possui imagem de capa e miniatura gerada automaticamente via Pixazo API (FLUX Schnell), seguindo as diretrizes do Diretor de Fotografia IA.
- **[OBRIGATÓRIO]** Proporção 16:9 horizontal, salva no formato otimizado `.webp` na pasta `assets/images/blog/[slug].webp`.
- **[OBRIGATÓRIO]** Texto alternativo (`alt`) contextualizado e descritivo da cena fotográfica, sem keyword stuffing.
- **[OBRIGATÓRIO]** Ausência absoluta de textos, logotipos ou marcas d'água na imagem (o texto pertence ao HTML e ao SEO, não à fotografia).
- **[PADRÃO]** Referenciada no Schema.org `BlogPosting` como propriedade `"image": "https://www.ceafonso.com.br/assets/images/blog/[slug].webp"` e na meta tag OpenGraph `og:image`.

---

## 12. Prevenção de canibalização (camada técnica)

Complementa o controle editorial do Banco de Pautas (Documento 04).

- **[OBRIGATÓRIO]** Antes de criar uma pauta nova, o agente verifica a keyword principal e as variações semânticas contra todas as pautas já publicadas. Se a sobreposição de intenção for alta, a pauta nova deve ser descartada ou reformulada para atacar um ângulo genuinamente diferente.
- **[PADRÃO]** Quando dois artigos tratam de temas próximos por necessidade (ex: "SEO Local para clínicas" e "SEO Local para salões"), a diferenciação deve estar clara já no título e na keyword principal, e ambos devem linkar um para o outro.

---

## 13. Search Console como parte do ciclo

Você já tem o Search Console ativo — isso deve virar retroalimentação do sistema, não só relatório:

- **[PADRÃO]** Revisão periódica (sugestão: mensal) de quais artigos estão recebendo impressão mas pouco clique — candidatos a ajuste de título/meta description.
- **[PADRÃO]** Identificar buscas reais que estão levando tráfego a um artigo e que não foram previstas na keyword original — isso vira insumo para o Banco de Palavras-chave (Documento 04).
- **[PADRÃO]** Artigos com queda de posição ao longo do tempo entram como candidatos a atualização, não só artigos novos entram no ciclo de produção.

---

## 14. O que este documento não cobre

- Tom, estrutura narrativa e regras de voz → **Documento 01 (Manual Editorial)**
- Lista de keywords por serviço → **Documento 04 (Banco de Pautas e Palavras-chave)**
- Ficha de produção artigo a artigo → **Documento 05 (Template de Produção)**
- Checklist final antes do deploy → **Documento 06 (Checklist de Publicação)**
