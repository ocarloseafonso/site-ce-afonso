import os
import re

# Directory containing the site
root_dir = '.'

# Get all webp files in the assets directory for reference
webp_files = {}
for root, dirs, files in os.walk(os.path.join(root_dir, 'assets', 'images')):
    for file in files:
        if file.lower().endswith('.webp'):
            # Store the relative path from the root as the key
            rel_path = os.path.relpath(os.path.join(root, file), root_dir).replace('\\', '/')
            # Also store the basename for "smart" matching if needed
            basename = os.path.splitext(file)[0].lower()
            webp_files[rel_path.lower()] = rel_path
            
            # Key by basename + folder for specific lookups
            folder_name = os.path.basename(root).lower()
            webp_files[f"{folder_name}/{basename}"] = rel_path

print(f"Index built with {len(webp_files)} webp references.")

# Extensions to look for and potentially replace
old_extensions = ['.png', '.jpg', '.jpeg']
html_files = [f for f in os.listdir(root_dir) if f.endswith('.html')]
css_files = []
for root, dirs, files in os.walk(os.path.join(root_dir, 'css')):
    for file in files:
        if file.endswith('.css'):
            css_files.append(os.path.join(root, file))

all_files = html_files + css_files
total_fixes = 0

for file_path in all_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Regex to find image paths in src, href, or url()
        # This handles ?v=... and other query params too
        for ext in old_extensions:
            # Match path + extension + optional query string
            # Example: src="assets/images/blog/photo.png?v=3"
            pattern = re.compile(r'([\"\'])([^\"\']+)' + re.escape(ext) + r'(\?[^\"\']*)?([\"\'])')
            
            def replace_func(match):
                global total_fixes
                quote_start = match.group(1)
                base_path = match.group(2) # e.g. assets/images/blog/photo
                query_string = match.group(3) or "" # e.g. ?v=3
                quote_end = match.group(4)
                
                full_old_path = base_path + ext
                # Clean path for lookup (remove leading slashes, etc)
                lookup_path = full_old_path.lower().lstrip('/')
                
                # Try exact match first
                potential_webp = base_path + ".webp"
                webp_lookup = potential_webp.lower().lstrip('/')
                
                if webp_lookup in webp_files:
                    total_fixes += 1
                    print(f"[{file_path}] Swapping: {full_old_path} -> {potential_webp}")
                    return f"{quote_start}{potential_webp}{query_string}{quote_end}"
                
                return match.group(0)

            content = pattern.sub(replace_func, content)

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print(f"\nOptimization complete! Total image references updated: {total_fixes}")
