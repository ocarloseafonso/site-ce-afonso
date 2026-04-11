import os
import re
import glob

# Get all actual files in the servicos image folder
servicos_dir = os.path.join('assets', 'images', 'servicos')
actual_files = [f for f in os.listdir(servicos_dir) if os.path.isfile(os.path.join(servicos_dir, f))]

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
total_replacements = 0

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        
        # We look for references like "assets/images/servicos/ANYTHING.ext"
        # We will replace them with the actual file that matches "ANYTHING" or close to it
        
        def replacer(match):
            global total_replacements
            prefix = match.group(1)
            filename = match.group(2)
            ext = match.group(3)
            # Find the best match
            # Priority: exact name (regardless of ext), then exact name with 's' or without 's'
            best_match = None
            
            # Exact match
            for f in actual_files:
                if f.startswith(filename + '.') and f != 'COLOQUE-AQUI.txt':
                    best_match = f
                    break
            
            # If dreads -> dreads-removiveis
            if not best_match and filename == 'dreads':
                best_match = 'dreads-removiveis.webp'
                
            # If fulani-braid -> fulani-braids
            if not best_match and filename == 'fulani-braid':
                for f in actual_files:
                    if f.startswith('fulani-braids.'):
                        best_match = f
                        break

            if best_match:
                # keep cache breaker if needed, but since we are doing this, let's bump it to ?v=5 for safety
                new_src = f'assets/images/servicos/{best_match}?v=5'
                if new_src != f'assets/images/servicos/{filename}{ext}':
                    total_replacements += 1
                    return f'{prefix}{new_src}'
            
            # Fallback string untouched
            return match.group(0)
            
        pattern = re.compile(r'([\"\']assets/images/servicos/)([^\"\.\?]+)(\.[a-z]+)(?:\?v=\d+)?', re.IGNORECASE)
        content = pattern.sub(replacer, content)

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated references in {file_path}')

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print(f'\nTotal fixes applied for servicos images: {total_replacements}')
