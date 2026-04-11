# Guia de Imagens - Ateliê DK

## Como Substituir as Imagens

Para trocar qualquer imagem, basta **substituir o arquivo** mantendo o **mesmo nome e formato**. Não é preciso mexer no código.

### Exemplo:
1. Tire uma foto real do serviço Box Braid
2. Salve como `box-braid.jpg` (ou `.png`)
3. Substitua o arquivo `assets/images/servicos/box-braid.svg` pelo novo arquivo
4. Pronto! A imagem será exibida automaticamente

---

## Estrutura de Pastas

```
assets/images/
├── logo/              # Logo e favicon
│   ├── logo.svg       → Substitua por logo.png ou logo.svg
│   └── favicon.svg    → Substitua por favicon.png ou favicon.ico
├── hero/              # Imagem principal do site
│   └── hero-principal.svg → Substitua por hero-principal.jpg (1400x800px)
├── sobre/             # Imagens da página Sobre
│   └── sobre-equipe.svg   → Substitua por sobre-equipe.jpg (700x500px)
├── servicos/          # Imagens dos serviços
│   ├── box-braid.svg      → Substitua por box-braid.jpg (600x400px)
│   ├── nago.svg           → Substitua por nago.jpg (600x400px)
│   ├── twist.svg          → Substitua por twist.jpg (600x400px)
│   ├── dreads.svg         → Substitua por dreads.jpg (600x400px)
│   ├── fulani-braid.svg   → Substitua por fulani-braid.jpg (600x400px)
│   ├── trancas-cachos.svg → Substitua por trancas-cachos.jpg (600x400px)
│   ├── penteados-infantis.svg → Substitua por penteados-infantis.jpg (600x400px)
│   ├── cabelos-naturais.svg   → Substitua por cabelos-naturais.jpg (600x400px)
│   └── aplicacoes.svg       → Substitua por aplicacoes.jpg (600x400px)
├── blog/              # Imagens dos artigos do blog
│   ├── post-1.svg     → Substitua por post-1.jpg (700x400px)
│   ├── post-2.svg     → Substitua por post-2.jpg (700x400px)
│   └── post-3.svg     → Substitua por post-3.jpg (700x400px)
└── ui/                # Elementos de interface (ícones, etc.)
```

---

## Tamanhos Recomendados

| Local | Tamanho | Formato |
|-------|---------|---------|
| Logo | 200x60px | PNG ou SVG |
| Favicon | 32x32px | PNG ou ICO |
| Hero | 1400x800px | JPG (otimizado) |
| Serviços | 600x400px | JPG (otimizado) |
| Blog | 700x400px | JPG (otimizado) |
| Sobre | 700x500px | JPG (otimizado) |
| Portfólio | 400x400px | JPG (otimizado) |

---

## Dicas de Otimização

- Use JPG para fotos (menor tamanho)
- Use PNG para logos com transparência
- Use SVG para logos e ícones (qualidade infinita)
- Comprima imagens antes de subir (tinypng.com ou squoosh.app)
- Mantenha o tamanho recomendado para carregamento rápido

---

## Notas

- Os arquivos `.svg` atuais são placeholders temporários
- Ao substituir, pode usar `.jpg`, `.png` ou `.svg`
- O código já está configurado para aceitar qualquer formato
- Todas as imagens possuem `alt` text para acessibilidade e SEO
