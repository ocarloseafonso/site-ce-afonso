# Documento 08 — Gerador de Base Editorial por Cliente
### Motor de personalização para novos clientes de gestão de blog

---

## 1. Objetivo deste documento

Este documento transforma os Documentos 01 a 07 (feitos originalmente para Carlos Eduardo Afonso / Volta Redonda) em uma base editorial personalizada para qualquer cliente novo de gestão de blog.

**Como usar:**

1. Criar uma pasta nova para o cliente.
2. Copiar para dentro dela os Documentos 01 a 07 originais (sem alterar) + este Documento 08.
3. Preencher a **Parte A — Ficha de Briefing** abaixo com as informações do cliente.
4. O agente lê este documento preenchido e reescreve os Documentos 01 a 07 dentro da pasta do cliente, seguindo o **Mapa de Transformação** (Parte B) e as **Regras Invariáveis** (Parte C).
5. Rodar o **Checklist de Validação** (Parte D) antes de considerar a base pronta para uso.

**[OBRIGATÓRIO]** O agente nunca reescreve os Documentos 01–07 originais (os de Carlos). Sempre trabalha sobre as cópias dentro da pasta do cliente novo.

---

## PARTE A — Ficha de Briefing do Cliente

```
=====================================================
FICHA DE BRIEFING — CLIENTE NOVO
=====================================================

A.1 — IDENTIDADE
Nome do cliente (pessoa ou marca que assina o blog):
Nome do negócio:
Cidade/região de atuação:
Segmento do negócio: (clínica, salão, restaurante, oficina, e-commerce, 
outro — descrever)

A.2 — AUTORIDADE E VOZ
Quem assina os artigos: (dono do negócio / equipe / marca institucional)
O cliente quer construir autoridade pessoal ou institucional?
Tom desejado: (ex: pessoal e próximo / técnico e formal / misto — 
especificar proporção se souber)
Existe alguma restrição de tom? (ex: setor regulado, como saúde, exige 
cautela em promessas de resultado)
Há alguma política de menção a concorrentes diferente da padrão 
(nunca comparar diretamente)?

A.3 — CATÁLOGO DE SERVIÇOS/PRODUTOS DO CLIENTE
(Repetir o bloco abaixo para cada serviço/produto do negócio do cliente 
— isso substitui INTEIRAMENTE o Documento 03 original, que era sobre os 
serviços do Carlos)

  SERVIÇO/PRODUTO:
  CATEGORIA:
  PROBLEMA QUE RESOLVE:
  PÚBLICO:
  ENTREGÁVEIS:
  BENEFÍCIOS:
  QUANDO INDICAR (em qual tipo de artigo mencionar):
  QUANDO NÃO INDICAR:
  TERMOS RELACIONADOS DE BUSCA:

A.4 — NICHOS/PÚBLICOS PRIORITÁRIOS DO CLIENTE
(Se o negócio atende mais de um público ou tipo de cliente, listar em 
ordem de prioridade — equivalente ao que fizemos com "clínicas" para 
o Carlos)
1.
2.
3.

A.5 — DADOS TÉCNICOS
Domínio do site do cliente:
Estrutura de URL do blog (ex: /blog/ ou outro caminho):
Perfil da Empresa no Google configurado? (sim/não)
Nome, endereço e telefone exatos (para consistência de NAP):
Search Console já configurado? (sim/não)

A.6 — CASOS E RESULTADOS INICIAIS (se houver)
(Se o cliente já tiver algum caso ou resultado para citar desde o início 
— senão, o Documento 07 do cliente começa vazio, igual ao do Carlos)

A.7 — RESTRIÇÕES ESPECÍFICAS
(Qualquer regra particular deste cliente que não existia no modelo 
original — ex: não pode citar preços, não pode citar nome de paciente 
nem anonimizado, setor exige aviso legal em determinados temas)

=====================================================
```

---

## PARTE B — Mapa de transformação

Define, documento por documento, o que muda com base no briefing.

### Documento 01 (Manual Editorial) →
- Seção "Autoria e voz": substituir nome, tipo de assinatura (pessoal/marca) pelos dados de A.2.
- Seção "Tom de voz": ajustar proporção pessoal/institucional conforme A.2. Se o segmento for regulado (ex: saúde, direito, finanças), adicionar regra extra de cautela em promessas de resultado.
- Seção "Prioridade de nicho": substituir pela lista de A.4.
- Demais seções (estrutura do artigo, regras anti-padrão-IA, teste da cidade trocada) permanecem — são metodologia, não conteúdo específico.

### Documento 02 (Manual SEO) →
- Substituir todas as referências a "Volta Redonda" pela cidade/região de A.1.
- Ajustar exemplo de URL para o domínio de A.5.
- Ajustar seção de NAP com os dados reais de A.5.
- Estrutura técnica (headings, schema, meta description, links internos) permanece — é metodologia.

### Documento 03 (Catálogo de Serviços) →
- **Substituição integral.** Este documento é recriado do zero usando os blocos preenchidos em A.3, seguindo exatamente o mesmo formato (SERVIÇO, CATEGORIA, PROBLEMA QUE RESOLVE, PÚBLICO, ENTREGÁVEIS, BENEFÍCIOS, QUANDO INDICAR, QUANDO NÃO INDICAR, SERVIÇOS RELACIONADOS, TERMOS RELACIONADOS).
- A tabela-resumo de diferenciação é reconstruída com os serviços do cliente.
- Regras especiais equivalentes à do PDL (serviço "guarda-chuva" sem busca própria) só se aplicam se o cliente tiver um serviço proprietário parecido — verificar com Carlos antes de assumir.

### Documento 04 (Banco de Pautas e Palavras-chave) →
- Parte A (palavras-chave por serviço) é reconstruída usando os TERMOS RELACIONADOS de cada bloco em A.3.
- Parte B (arquitetura de pilares) é reconstruída com base nos nichos prioritários de A.4.
- Parte C (banco de pautas) começa vazio ou com pautas iniciais, se o cliente já tiver algum artigo publicado (perguntar a Carlos).
- Regras de fila e prevenção de canibalização permanecem — é metodologia.

### Documento 05 (Template de Produção) →
- Estrutura da ficha permanece idêntica — é metodologia.
- Nenhuma alteração de conteúdo, apenas os campos são preenchidos artigo a artigo já usando os dados do cliente novo.

### Documento 06 (Checklist de Publicação) →
- Estrutura permanece idêntica.
- Se A.7 tiver alguma restrição específica (ex: aviso legal obrigatório em determinados temas), adicionar um item extra ao checklist.

### Documento 07 (Banco de Resultados e Casos) →
- Reiniciado vazio, exceto se A.6 tiver casos iniciais — nesse caso, pré-preencher com eles.

---

## PARTE C — Regras invariáveis

**[OBRIGATÓRIO] O que NUNCA muda entre clientes** (é metodologia, não conteúdo):
- A lógica de estrutura do artigo (problema → causa → solução → passo a passo → erros comuns → quando buscar ajuda → próximo passo).
- As regras anti-padrão-IA.
- O "teste da cidade trocada" (adaptado: testar se o artigo poderia ser publicado em qualquer outro negócio do mesmo segmento só trocando o nome).
- A lógica técnica de SEO (headings, meta description, schema, links internos, prevenção de canibalização).
- A separação entre blog (aquisição) e página comercial (conversão).
- A regra de nunca citar serviço/caso de forma forçada.

**[OBRIGATÓRIO] O que SEMPRE muda entre clientes** (é conteúdo específico):
- Nome, cidade, tom de voz específico.
- Catálogo de serviços por completo.
- Palavras-chave e pilares temáticos.
- Casos e resultados.
- Qualquer restrição do segmento (ex: setor regulado).

---

## PARTE D — Checklist de validação pós-adaptação

```
[ ] Nenhuma menção residual a "Volta Redonda" fora do cliente atual
[ ] Nenhuma menção residual a "Carlos Eduardo Afonso" fora do cliente atual
[ ] Documento 03 reflete o catálogo real do cliente novo, não o de web design
[ ] Documento 04 tem palavras-chave e pilares coerentes com o segmento do 
    cliente novo
[ ] Prioridade de nicho corresponde a A.4, não à ordem original (clínicas)
[ ] Se o segmento for regulado, restrição extra foi adicionada ao 
    Documento 01 e ao Documento 06
[ ] Domínio e estrutura de URL no Documento 02 correspondem ao cliente novo
[ ] Documento 07 está vazio ou populado apenas com casos reais deste 
    cliente
```

---

## 2. Observação operacional

Este documento é reaproveitável indefinidamente — cada cliente novo gera uma pasta própria com uma Ficha de Briefing (Parte A) preenchida e os Documentos 01–07 adaptados. O Documento 08 em si nunca muda entre clientes: ele é o motor, não o conteúdo.
