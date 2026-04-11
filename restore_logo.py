import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
total_restored = 0

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = content
        
        # Split gently around the footer-brand class
        if '<div class="footer-brand">' in new_content:
            parts = new_content.split('<div class="footer-brand">')
            # The second part is after the footer-brand declaration
            footer_part = parts[1]
            end_div_pos = footer_part.find('</div>')
            
            if end_div_pos != -1:
                inner_footer = footer_part[:end_div_pos]
                if 'logo-original.webp' in inner_footer:
                    new_inner_footer = inner_footer.replace('logo-original.webp', 'logo-alternativa.webp')
                    
                    # Reconstruct
                    new_footer_part = new_inner_footer + footer_part[end_div_pos:]
                    new_content = parts[0] + '<div class="footer-brand">' + new_footer_part
                    total_restored += 1

        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Restored logo-alternativa in {file_path}')

    except Exception as e:
        print(f'Error processing {file_path}: {e}')

print(f'\nTotal files restored: {total_restored}')
