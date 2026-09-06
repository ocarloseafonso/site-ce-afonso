# Documento 05 — Template de Produção
### Blog institucional — Carlos Eduardo Afonso | Volta Redonda

---

## 1. Objetivo deste documento

Esta é a ficha que o agente monta **para cada artigo individual**, antes de escrever. Ela reúne, num único lugar, tudo que vem espalhado nos Documentos 01 a 04 e 07 — assim o agente não precisa reconsultar todos os arquivos toda vez, e Carlos consegue revisar o plano do artigo antes do texto ser gerado, se quiser.

**[OBRIGATÓRIO]** O agente preenche esta ficha ANTES de escrever o artigo, não depois. Se algum campo não puder ser preenchido com confiança, o agente sinaliza a lacuna em vez de inventar a informação.

---

## 2. Fluxo de preenchimento

```
1. Ler Documento 04 → selecionar a pauta (regra de fila)
2. Copiar dados da pauta para os campos 3.1 e 3.2 abaixo
3. Ler Documento 03 → identificar o serviço relacionado e preencher 3.3
4. Ler Documento 07 → verificar se algum caso se aplica, preencher 3.4
5. Preencher 3.5 (plano de estrutura) com base no Documento 01
6. Preencher 3.6 (checagem SEO) com base no Documento 02
7. Escrever o artigo
8. Preencher 3.7 (autoavaliação) após escrever
9. Encaminhar para revisão humana (Documento 06)
```

---

## 3. Ficha de produção — modelo

```
=====================================================
FICHA DE PRODUÇÃO — ARTIGO
=====================================================

3.1 — IDENTIFICAÇÃO
ID da pauta:
Título de trabalho:
Data de início da produção:

3.2 — DADOS DE BUSCA (origem: Documento 04)
Keyword principal:
Termos secundários:
Variações semânticas:
Intenção de busca:
Nicho:
Perguntas relacionadas a responder:

3.3 — CONEXÃO COM SERVIÇO (origem: Documento 03)
Serviço relacionado:
Este serviço deve ser citado neste artigo? (sim/não, conforme critério QUANDO INDICAR / QUANDO NÃO INDICAR)
Página interna para linkar:
Outros artigos publicados para linkar (verificar Documento 04):

3.4 — CASO DE APOIO (origem: Documento 07 — opcional)
Existe caso aplicável a este problema? (sim/não)
Se sim, qual ID do caso:
Nível de anonimização permitido:
Onde no texto o caso se encaixa naturalmente:

3.5 — PLANO DE ESTRUTURA (origem: Documento 01)
Problema central do leitor:
Por que esse problema acontece (resumo):
Solução central a apresentar:
Passo a passo aplicável? (sim/não)
Erros comuns a mencionar:
Faixa de tamanho estimada (curto/médio/guia completo):
Proporção de voz pessoal x institucional prevista: (padrão 75/25)

3.6 — CHECAGEM SEO (origem: Documento 02)
Título (H1) proposto:
Title tag (até 60 caracteres):
Meta description (140–160 caracteres):
URL proposta:
Headings (H2) planejados:
Schema aplicável: (Article/BlogPosting + FAQPage se pertinente)

3.6b — IMAGEM DE CAPA E MINIATURA (origem: Documentos 09 e 10)
Conceito visual (Diretor de Fotografia IA):
Prompt em inglês (Pixazo FLUX Schnell):
Negative prompt:
Formato e Proporção: 16:9 (horizontal, sem texto/logos)
Caminho do arquivo: assets/images/blog/[slug].webp
Alt text da imagem:

3.7 — AUTOAVALIAÇÃO PÓS-ESCRITA (preenchida após o rascunho)
O artigo passou no "teste da cidade trocada"? (sim/não)
O artigo evitou todos os itens da lista anti-padrão-IA (Documento 01, item 6)? (sim/não)
A imagem de capa/miniatura foi gerada via Pixazo e validada sem texto/marcas? (sim/não)
A citação de serviço (se houve) ficou natural, não forçada? (sim/não)
Links internos inseridos: (quantidade e destinos)
Palavra-chave principal presente em: título / H2 / primeiro parágrafo / meta description (marcar todos que se aplicam)

=====================================================
```

---

## 4. Regras de preenchimento

- **[OBRIGATÓRIO]** Nenhum campo de 3.2 e 3.3 pode ficar vazio — vêm diretamente dos Documentos 04 e 03, que já devem estar preenchidos antes da produção começar.
- **[PADRÃO]** O campo 3.4 (caso de apoio) pode ficar em branco. Forçar um caso que não se encaixa é pior do que não citar nenhum.
- **[OBRIGATÓRIO]** O campo 3.7 é preenchido de forma honesta — se alguma resposta for "não", o artigo volta para ajuste antes de seguir para o Documento 06.

---

## 5. O que este documento não cobre

- As regras em si (o que significa "voz pessoal", o que é "padrão anti-IA") → **Documento 01**
- As regras técnicas em si (o que é uma meta description boa) → **Documento 02**
- Critério detalhado de quando citar um serviço → **Documento 03**
- Origem da pauta e das keywords → **Documento 04**
- Validação final antes do deploy → **Documento 06**
