const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');
const IMAGES_DIR = path.join(ROOT_DIR, 'assets', 'images');
const GALERIA_DIR = path.join(IMAGES_DIR, 'galeria');

/**
 * Normaliza uma string para comparação
 */
function normalize(str) {
    if (!str) return '';
    return str.toLowerCase()
        .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
        .replace(/[^a-z0-9]/g, '-')
        .replace(/-+/g, '-')
        .replace(/^-|-$/g, '');
}

function syncImages() {
    console.log('====================================================');
    console.log('   Sincronização C.E. Afonso - V4 (Animação e Blog)   ');
    console.log('====================================================\n');

    // 1. Mapear blog para o Smart Match
    const blogImagesDir = path.join(IMAGES_DIR, 'blog');
    const blogImageMap = new Map();
    if (fs.existsSync(blogImagesDir)) {
        fs.readdirSync(blogImagesDir).filter(f => /\.(png|jpg|jpeg|webp|svg)$/i.test(f)).forEach(file => {
            blogImageMap.set(normalize(path.parse(file).name), file);
        });
    }

    // 2. Extrair Posts REIAS do blog.html para a Related Section
    let relatedPostsHtml = '';
    const blogHtmlPath = path.join(ROOT_DIR, 'blog.html');
    if (fs.existsSync(blogHtmlPath)) {
        const blogContent = fs.readFileSync(blogHtmlPath, 'utf8');
        const gridRegex = /<div class="blog-grid">([\s\S]*?)<\/div>\s*<\/div>\s*<\/section>/;
        const gridMatch = blogContent.match(gridRegex);
        if (gridMatch) {
            // Pegar os primeiros 3 cards
            const cards = [];
            const cardRegex = /<div class="blog-card">[\s\S]*?<\/div><\/div>/g;
            let match;
            while ((match = cardRegex.exec(gridMatch[1])) !== null && cards.length < 3) {
                cards.push(match[0]);
            }
            relatedPostsHtml = cards.join('\n        ');
        }
    }

    // 3. Processar arquivos HTML
    const rootFiles = fs.readdirSync(ROOT_DIR).filter(f => f.endsWith('.html'));
    const blogHtmlDir = path.join(ROOT_DIR, 'blog');
    const blogFiles = fs.existsSync(blogHtmlDir) ? fs.readdirSync(blogHtmlDir).filter(f => f.endsWith('.html')).map(f => path.join('blog', f)) : [];
    const htmlFiles = [...rootFiles, ...blogFiles];

    htmlFiles.forEach(file => {
        const filePath = path.join(ROOT_DIR, file);
        let content = fs.readFileSync(filePath, 'utf8');
        let modified = false;

        const h1Match = content.match(/<h1[^>]*>(.*?)<\/h1>/i);
        const normalizedPageTitle = normalize(h1Match ? h1Match[1] : '');
        const slug = normalize(path.parse(file).name);

        // --- Cache Buster CSS ---
        const cssRegex = /href="css\/style\.css(\?v=\d+)?"/g;
        if (content.match(cssRegex)) {
            content = content.replace(cssRegex, 'href="css/style.css?v=6"');
            modified = true;
        }

        // --- LÓGICA 1: CORREÇÃO UNIVERSAL DE EXTENSÕES ---
        const imgRegex = /<img[^>]+src="([^">]+)"[^>]*>/g;
        content = content.replace(imgRegex, (match, src) => {
            const parts = src.split('/');
            const currentFile = parts[parts.length - 1];
            const relativePathToFolder = src.substring(0, src.lastIndexOf('/') + 1);
            const absoluteFolderPath = path.join(ROOT_DIR, relativePathToFolder);

            // Sincronização de extensões (.png -> .webp etc)
            if (src.includes('assets/images/')) {
                const basename = path.basename(currentFile, path.extname(currentFile));
                const dir = path.dirname(currentFile);
                const candidates = ['.webp', '.png', '.jpg', '.jpeg', '.svg'];
                
                for (const ext of candidates) {
                    const candidate = path.join(dir, basename + ext).replace(/\\/g, '/');
                    const absoluteCandidate = path.join(process.cwd(), candidate);
                    if (fs.existsSync(absoluteCandidate)) {
                        if (candidate !== currentFile) {
                            modified = true;
                            // Assegura que se o original tinha / no início, o novo também terá
                            const finalPath = src.startsWith('/') ? '/' + candidate : candidate;
                            return match.replace(currentFile, finalPath);
                        }
                    }
                }
            }

            // Smart Blog
            if (src.includes('assets/images/blog/')) {
                const altMatch = match.match(/alt="([^"]+)"/i);
                const altText = altMatch ? normalize(altMatch[1]) : '';
                let target = blogImageMap.get(slug) || blogImageMap.get(altText) || blogImageMap.get(normalizedPageTitle);
                if (target && target !== currentFile) {
                    // console.log(`[${file}] Blog Match: ${currentFile} -> ${target}`);
                    modified = true;
                    // Assegura que se o original tinha / no início, o novo também terá
                    const finalPath = src.startsWith('/') ? '/' + target : target;
                    return match.replace(currentFile, finalPath);
                }
            }

            return match;
        });

        // --- LÓGICA 2: GALERIA AUTOMÁTICA (Slide Infinito / Manual) ---
        const serviceSlug = slug;
        const galleryPath = path.join(GALERIA_DIR, serviceSlug);

        if (content.includes('service-gallery') && fs.existsSync(galleryPath)) {
            const files = fs.readdirSync(galleryPath);
            const supportedImages = files.filter(f => /\.(png|jpg|jpeg|webp|svg)$/i.test(f)).sort((a, b) => {
                const numA = parseInt(a); const numB = parseInt(b);
                if (!isNaN(numA) && !isNaN(numB)) return numA - numB;
                return a.localeCompare(b);
            });
            const heicFiles = files.filter(f => /\.heic$/i.test(f));
            if (heicFiles.length > 0) {
                console.log(`[AVISO] ${file}: ${heicFiles.length} arquivo(s) .HEIC não aparecem no site. Converta para .JPG.`);
            }

            if (supportedImages.length > 0) {
                // Build the slide HTML
                const slide = (img) => `                <div class="gallery-slide lightbox-trigger" style="flex:0 0 280px;width:280px;min-width:280px;max-width:280px;border-radius:8px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.15);"><img src="assets/images/galeria/${serviceSlug}/${img}" alt="${serviceSlug} ${path.parse(img).name}" style="width:100%;height:210px;object-fit:cover;"></div>`;
                const allSlides = supportedImages.map(slide).join('\n');
                
                const newGalleryBlock = `<h3 style="margin-bottom: 24px;">Galeria de Inspirações</h3>
            <div class="gallery-slider-infinite" style="display:flex; overflow:visible; width:100%;">
              <div class="gallery-slider-wrapper" style="position:relative; width:100%;">
                <button class="gallery-arrow prev" aria-label="Anterior">&#10094;</button>
                <div class="gallery-slider-track">\n${allSlides}\n                </div>
                <button class="gallery-arrow next" aria-label="Próximo">&#10095;</button>
              </div>
            </div>`;

                // Wipe out everything between <div class="service-gallery" ...> and <div class="post-cta-banner">
                // Note: The regex needs to be extremely careful to not swallow other parts of the page.
                const repairRegex = /(<div class="service-gallery"[^>]*>)[\s\S]*?(<\/div>\s*<div class="post-cta-banner">)/;
                if (repairRegex.test(content)) {
                    const matchOld = content.match(repairRegex)[0];
                    if (!matchOld.includes(newGalleryBlock)) {
                        content = content.replace(repairRegex, `$1\n            ${newGalleryBlock}\n          $2`);
                        console.log(`[${file}] Galeria Atualizada/Padronizada: ${supportedImages.length} fotos.`);
                        modified = true;
                    }
                }
            }
        }

        // --- LÓGICA 3: INSERIR IMAGEM DE DESTAQUE NO BLOG ---
        const targetImage = blogImageMap.get(slug) || blogImageMap.get(normalizedPageTitle);
        if (content.includes('data-page="blog"') && content.includes('<div class="post-content">') && file !== 'blog.html') {
            // Se já tem a imagem, ignora ou atualiza
            if (!content.includes('class="post-featured-image"')) {
const isInsideBlog = file.startsWith('blog\\') || file.startsWith('blog/');
                const imgPrefix = isInsideBlog ? '../assets/images/blog/' : 'assets/images/blog/';
                
                if (targetImage) {
                    const imgHtml = `\n        <div class="post-featured-image" style="margin-bottom: 32px; border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-sm);"><img src="${imgPrefix}${targetImage}" alt="${normalizedPageTitle}" style="width: 100%; height: auto; aspect-ratio: 16/9; object-fit: cover;"></div>`;
                    
                    // Inserir APÓS a post-meta-bar
                    content = content.replace(/(<div class="post-meta-bar">[\s\S]*?<\/div>)/, `$1${imgHtml}`);
                    console.log(`[${file}] Imagem de Cabeçalho ('${targetImage}') adicionada.`);
                    modified = true;
                }
            } else if (targetImage) {
                // Atualiza a imagem se ela já existir no cabeçalho
                const featuredRegex = /(<div class="post-featured-image"[^>]*><img src=")([^"]+)(")/;
                content = content.replace(featuredRegex, (match, prefix, currentSrc, suffix) => {
                    const currentFile = path.basename(currentSrc);
                    if (currentFile !== targetImage) {
                        modified = true;
                        const isInsideBlog = file.startsWith('blog\\') || file.startsWith('blog/');
                        const imgPrefix = isInsideBlog ? '../assets/images/blog/' : 'assets/images/blog/';
                        return `${prefix}${imgPrefix}${targetImage}${suffix}`;
                    }
                    return match;
                });
            }
        }

        // --- LÓGICA 4: ATUALIZAR SEÇÃO "POSTS RELACIONADOS" REAL ---
        if (relatedPostsHtml && content.includes('class="related-section"')) {
            const relatedRegex = /(<section class="related-section">[\s\S]*?<div class="blog-grid">)([\s\S]*?)(<\/div>\s*<\/div>\s*<\/section>)/;
            const match = content.match(relatedRegex);
            if (match && match[2].trim() !== relatedPostsHtml.trim() && file !== 'blog.html') {
                content = content.replace(relatedRegex, `$1\n        ${relatedPostsHtml}\n      $3`);
                console.log(`[${file}] 'Posts Relacionados' atualizado com posts reais.`);
                modified = true;
            }
        }

        if (modified) fs.writeFileSync(filePath, content, 'utf8');
    });

    console.log('\n--- Sincronização Concluída ---');
}

syncImages();
