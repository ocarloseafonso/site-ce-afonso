import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
css_files = [os.path.join('css', f) for f in os.listdir('css') if f.endswith('.css')] if os.path.isdir('css') else []

all_files = html_files + css_files

old_exts = ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG']
total_replacements = 0

for file in all_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        
        # Replace extensions unconditionally
        for ext in old_exts:
            # Match src="....png", href="....png", url('....png')
            # Look for ext followed by either end quotes/parens or query strings
            pattern = re.compile(r'([\"\'\(])([^\"\'\(\)]+)' + re.escape(ext) + r'((?:\?[^\"\'\)]*)?)([\"\'\)])')
            
            def replacer(match):
                global total_replacements
                total_replacements += 1
                base_path = match.group(2)
                # Ensure cache busted
                return f"{match.group(1)}{base_path}.webp?v=4{match.group(4)}"
                
            new_content = pattern.sub(replacer, new_content)
            
        # Also let's update any existing ?v=\d tags on existing .webp
        new_content = re.sub(r'\.webp\?(v=\d+)', r'.webp?v=4', new_content)
        # And if there are webps that don't have a cache buster, conditionally add one inside quotes
        new_content = re.sub(r'(\.webp)([\"\'])', r'\1?v=4\2', new_content)
        # Clean up double query params if accidentally added
        new_content = new_content.replace('?v=4?v=4', '?v=4')
        new_content = new_content.replace('.webp?v=4?v=', '.webp?v=')

        if content != new_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated WebP refs in {file}')

    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f'\nFinished! Total .png/.jpg references changed to .webp: {total_replacements}')
