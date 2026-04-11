import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

total_replacements = 0

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # Remove the whole line containing favicon.svg
        content = re.sub(r'^\s*<link rel="icon" type="image/svg\+xml" href=".*favicon\.svg.*">\n?', '', content, flags=re.MULTILINE)
        
        # We can also clean up the comment just in case
        content = content.replace('(ou .svg)', '')

        if content != original_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            total_replacements += 1
            print(f'Cleaned SVG references in {file}')

    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f'\nFinished! Cleaned SVG references in {total_replacements} files.')
