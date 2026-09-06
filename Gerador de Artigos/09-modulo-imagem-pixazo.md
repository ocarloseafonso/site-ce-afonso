# Documento 09 — Módulo de Geração de Imagem com Pixazo API
### Blog institucional — Carlos Eduardo Afonso | Volta Redonda

---

## 1. Objetivo
Sempre que o sistema criar um novo artigo, depois de definir o tema e finalizar a copy, ele deverá automaticamente criar uma imagem de capa e miniatura relacionada ao assunto central do artigo.

A imagem deve ser criada:
- **Sem qualquer texto, palavra, letra, número, logotipo, marca ou elemento tipográfico.**
- Com aparência de **fotografia profissional produzida por um fotógrafo real**, e não uma imagem artificial de IA.
- **Diretriz de Representatividade Obrigatória:** Sempre retratar pessoas pretas (Black / Afro-Brazilian people). Quando houver múltiplas pessoas, a maioria absoluta deve ser de pessoas pretas, contemplando homens e mulheres de variados biotipos e faixas etárias.
- Formato **horizontal 16:9** (ou 3:2), otimizada para capa e miniatura de blog.

---

## 2. Fluxo de Execução
```
1. Sistema seleciona o tema do artigo e escreve a copy (Documentos 04 e 05).
2. Sistema identifica o assunto central do artigo.
3. Diretor de Fotografia IA (Documento 10) cria o conceito visual e o prompt fotográfico em inglês.
4. Sistema envia o prompt para a API da Pixazo (Flux Schnell).
5. A imagem é gerada na Pixazo.
6. O sistema baixa a imagem, converte/otimiza para formato WebP.
7. A imagem recebe o nome padronizado: assets/images/blog/{slug}.webp.
8. A imagem é vinculada ao artigo (capa interna) e ao blog.html (card/miniatura).
9. O processo de deploy continua normalmente.
```

---

## 3. Configuração da API Pixazo

### Variável de Ambiente
- Variável: `PIXAZO_API_KEY`
- **Segurança**: NUNCA colocar a API Key diretamente no código-fonte, frontend, HTML, JavaScript público ou repositório Git. Salvar exclusivamente no arquivo local `.env` (ignorado no Git).

### Endpoint Flux 1 Schnell
- **Método**: `POST`
- **URL**: `https://gateway.pixazo.ai/flux-1-schnell/v1/getData`
- **Headers**:
  ```http
  Content-Type: application/json
  Cache-Control: no-cache
  Ocp-Apim-Subscription-Key: ${PIXAZO_API_KEY}
  ```
- **Payload**:
  ```json
  {
    "prompt": "PROMPT_GERADO_PELO_DIRETOR_DE_FOTOGRAFIA",
    "num_steps": 4,
    "width": 1024,
    "height": 576
  }
  ```
- **Resposta**:
  ```json
  {
    "output": "https://pub-....r2.dev/flux-schnell-cf/prompt-....png"
  }
  ```

---

## 4. Regras do Prompt Fotográfico

O sistema não deve simplesmente colocar o título do artigo no prompt. Deve interpretar semanticamente o tema e transformá-lo em uma cena visual concreta do mundo real.

### Exemplo:
- **Artigo**: "Como escolher uma empresa de criação de sites em Volta Redonda"
- **Não gerar**: "Uma imagem sobre criação de sites em Volta Redonda."
- **Gerar**:
  > *"Natural editorial photograph of a small Brazilian business owner sitting at a desk in a modest modern office, reviewing a website project on a laptop with a professional web designer beside him, authentic everyday Brazilian business environment, realistic human expressions, natural posture, subtle imperfections, practical working atmosphere, soft daylight coming through a window, realistic skin texture, natural skin tones, believable clothing, documentary photography, photographed with a professional full-frame camera, 50mm lens, shallow but realistic depth of field, soft natural shadows, slightly imperfect real-world composition, restrained color grading, realistic exposure, subtle film grain, authentic commercial photography, no staged stock-photo appearance"*

### Estilo Fotográfico Prioritário:
- natural editorial photography
- documentary photography
- authentic commercial photography
- real-world environment
- natural daylight / soft natural shadows
- realistic skin texture and natural skin tones
- subtle imperfections and natural body posture
- moderate depth of field
- restrained color grading and neutral white balance

### Evitar Excesso de Estética (Anti-padrão IA):
Não usar termos que forçam artificialismo:
- `8K`, `ultra detailed`, `hyper realistic`, `unreal engine`, `cinematic masterpiece`, `perfect lighting`, `perfect skin`, `glowing skin`, `dramatic lighting`, `oversaturated`, `HDR`, `fantasy lighting`, `plastic skin`, `CGI`, `3D render`, `digital art`.

---

## 5. Tratamento de Erros e Fallback
1. Se a API não retornar uma URL válida na primeira tentativa, o sistema tenta novamente **uma vez** com um prompt simplificado.
2. Se a segunda tentativa falhar, registra o erro no log e NÃO interrompe a publicação do artigo, utilizando uma imagem de fallback padrão do acervo institucional.
