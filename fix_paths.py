import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

internal_pages = ['sobre', 'servicos', 'blog', 'faq', 'contato', 'privacy',
                 'nago-masculina', 'nago-feminina', 'twist-braid', 'penteados-infantis',
                 'cabelos-naturais', 'fulani-braid', 'trancas-com-cachos', 'dreads-removiveis',
                 'box-braid', 'aplicacoes', 'tratamentos-capilares',
                 'como-escolher-trancista-volta-redonda', 'quanto-tempo-dura-box-braid',
                 'como-cuidar-das-trancas-no-dia-a-dia', 'melhor-trancista-em-volta-redonda',
                 'cuidados-com-trancas-infantis', 'diferencas-entre-tipos-de-tranca']

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Make paths relative so it works locally via file:///
        content = content.replace('href="/css/', 'href="css/')
        content = content.replace('src="/js/', 'src="js/')
        content = content.replace('href="/assets/', 'href="assets/')
        content = content.replace('src="/assets/', 'src="assets/')
        content = content.replace('href="/favicon', 'href="favicon')
        
        # 2. Add .html to internal clean links so they work locally without a server
        for page in internal_pages:
            content = re.sub(r'href="/?' + page + r'"', f'href="{page}.html"', content)
            
        # Also fix index.html link to /
        content = content.replace('href="/"', 'href="index.html"')
        
        # 3. Fix the specific image on index.html
        if file == 'index.html':
            content = content.replace('escolher-trancista.png', 'como-escolher-trancista-volta-redonda.png')
            content = content.replace('escolher-trancista.webp', 'como-escolher-trancista-volta-redonda.webp')

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f'Processed {file}')
    except Exception as e:
        print(f'Error processing {file}: {e}')
