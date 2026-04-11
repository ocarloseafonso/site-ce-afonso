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

        # Remove .html from internal links for clean URLs on HostGator
        for page in internal_pages:
            content = re.sub(r'href=\"' + page + r'\.html\"', f'href=\"{page}\"', content)
            
        content = content.replace('href="index.html"', 'href="/"')
        content = content.replace('href="/index.html"', 'href="/"')
        content = content.replace('href="./index.html"', 'href="/"')

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f'Processed urls in {file}')
    except Exception as e:
        print(f'Error processing {file}: {e}')
