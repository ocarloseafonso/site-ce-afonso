# Documento 06 — Checklist de Publicação
### Blog institucional — Carlos Eduardo Afonso | Volta Redonda

---

## 1. Objetivo deste documento

Última validação antes de um artigo virar TXT final e seguir para deploy no Antigravity. Nada é publicado sem passar por este checklist inteiro.

**[OBRIGATÓRIO]** Se qualquer item marcado como obrigatório falhar, o artigo NÃO segue para deploy — volta para ajuste.

---

## 2. Checklist — Conteúdo e voz (Documento 01)

```
[ ] Estrutura segue a lógica: problema → causa → solução → passo a passo → 
    erros comuns → quando buscar ajuda → próximo passo
[ ] Escrito em primeira pessoa, voz de Carlos
[ ] Proporção pessoal/institucional próxima de 75/25
[ ] Nenhuma comparação depreciativa com concorrentes
[ ] Passou no "teste da cidade trocada" (não é genérico, tem elementos 
    reais de Volta Redonda)
[ ] Tamanho do texto condiz com a complexidade do problema (não foi 
    estufado nem cortado artificialmente)
```

## 3. Checklist — Anti-padrão-IA (Documento 01, item 6)

```
[ ] Sem emojis
[ ] Sem travessão usado como recurso estilístico recorrente
[ ] Sem abertura genérica
[ ] Sem "não é X, é Y" como recurso de estilo
[ ] Sem conclusão do tipo "esperamos que este artigo tenha ajudado"
[ ] Sem afirmação estatística sem fonte real
[ ] Sem excesso de "além disso / nesse sentido / dessa forma / é importante 
    destacar"
[ ] Sem excesso de listas ou headings artificiais
[ ] Frases com ritmo variado, não uniformes
```

## 4. Checklist — SEO técnico (Documento 02)

```
[ ] Keyword principal presente em: H1, pelo menos um H2, primeiro parágrafo, 
    meta description
[ ] Title tag entre 50–60 caracteres
[ ] Meta description entre 140–160 caracteres
[ ] URL curta, sem acento, contendo a keyword principal
[ ] Estrutura de headings corresponde a divisões reais de conteúdo
[ ] Entre 1 e 4 links internos, com âncora descritiva (nunca "clique aqui")
[ ] Link para a página de serviço presente, se o critério do Documento 03 
    indicar que sim
[ ] Imagens (se houver) com alt text descritivo e nome de arquivo adequado
[ ] Schema Article/BlogPosting definido, com autoria de Carlos Eduardo Afonso
```

## 4.1 Checklist — Imagem de Capa e Miniatura (Documentos 09 e 10)

```
[ ] Prompt fotográfico gerado pelo Diretor de Fotografia IA em inglês
[ ] Imagem gerada via Pixazo API (FLUX Schnell)
[ ] ZERO texto, palavras, números, legendas ou letras visíveis
[ ] ZERO marcas comerciais, logotipos ou marcas d'água
[ ] Aparência de fotografia real e documental (evitou termos de 3D/CGI/8K)
[ ] Formato horizontal 16:9, salvo em assets/images/blog/[slug].webp
[ ] Imagem configurada como capa do post (<div class="post-featured-image">)
[ ] Imagem configurada como miniatura do card no blog.html (<div class="blog-card-img">)
[ ] Alt text preenchido com descrição natural do conteúdo da cena
```

## 5. Checklist — Uso de serviço e casos (Documentos 03 e 07)

```
[ ] Citação de serviço (se houver) é natural, não parece propaganda inserida 
    à força
[ ] Serviço citado é o correto segundo o critério QUANDO INDICAR do 
    Documento 03
[ ] Caso de apoio (se usado) respeita o nível de anonimização definido na 
    ficha do caso
[ ] Nenhuma afirmação de resultado inventada ou não verificável
```

## 6. Checklist — Controle de duplicidade (Documento 04)

```
[ ] Keyword principal e intenção verificadas contra todas as pautas já 
    publicadas — sem sobreposição significativa
[ ] Status da pauta atualizado para PUBLICADO após deploy
[ ] URL e data de publicação preenchidas no Documento 04
[ ] Se aplicável, artigos antigos relacionados foram atualizados com link 
    para o novo artigo
```

## 7. Checklist — Revisão humana final

```
[ ] Carlos leu o artigo completo antes do deploy
[ ] Nenhuma informação factual incorreta ou desatualizada
[ ] Texto soa como algo que Carlos escreveria de fato
[ ] Aprovado para publicação
```

---

## 8. Após a publicação

```
[ ] Artigo gerado em TXT na pasta de publicados
[ ] Deploy realizado no Antigravity
[ ] Registro atualizado no Documento 04
[ ] (Periodicamente, não a cada artigo) Verificar no Search Console se o 
    artigo está sendo indexado e recebendo impressões nas semanas seguintes
```

---

## 9. O que este documento não cobre

- As regras em si, apenas a validação delas → **Documentos 01, 02, 03, 04 e 07**
