import os
import re

servicos_dir = os.path.join('assets', 'images', 'servicos')
actual_files = [f for f in os.listdir(servicos_dir) if os.path.isfile(os.path.join(servicos_dir, f))]

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
total_replacements = 0

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        
        def replacer(match):
            global total_replacements
            prefix = match.group(1)
            filename = match.group(2)
            ext = match.group(3)
            best_match = None
            
            # Exact match without extension
            for f in actual_files:
                if f.startswith(filename + '.') and f != 'COLOQUE-AQUI.txt':
                    best_match = f
                    break
            
            # Singular/Plural fallback
            if not best_match:
                for f in actual_files:
                    if filename.startswith(f.split('.')[0]) or f.split('.')[0].startswith(filename):
                        best_match = f
                        break
                        
            # Specific manual overrides just in case
            if not best_match and filename == 'dreads':
                best_match = 'dreads-removiveis.webp'
            if not best_match and filename == 'fulani-braid':
                best_match = 'fulani-braids.webp'

            if best_match:
                # use v=6
                new_src = f'assets/images/servicos/{best_match}?v=6'
                if new_src not in match.group(0) or ext != f'.{best_match.split(".")[-1]}':
                    total_replacements += 1
                    return f'{prefix}{new_src}'
            
            return match.group(0)
            
        pattern = re.compile(r'([\"\']assets/images/servicos/)([^\"\.\?]+)(\.[a-zA-Z0-9]+)(?:\?v=\d+)?', re.IGNORECASE)
        content = pattern.sub(replacer, content)

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated references in {file_path}')

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print(f'\nTotal fixes applied for servicos images: {total_replacements}')
