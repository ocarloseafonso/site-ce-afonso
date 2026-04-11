import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html' and 'modelo' not in f]

# 1. Unify Navigation Menu
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract the nav block from index.html
nav_match = re.search(r'(<nav class="nav" role="navigation" aria-label="Menu principal">.*?</nav>)', index_content, flags=re.DOTALL)
if nav_match:
    nav_index = nav_match.group(1)
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the nav block in the target file
        new_content = re.sub(r'<nav class="nav" role="navigation" aria-label="Menu principal">.*?</nav>', nav_index, content, flags=re.DOTALL)
        
        # Move the active class (basic attempt)
        # First remove active class generically
        new_content = new_content.replace('class="nav-link active"', 'class="nav-link"')
        
        # Add active class based on filename
        base_name = html_file.split('.')[0]
        if base_name == 'sobre':
            new_content = new_content.replace('href="sobre" class="nav-link"', 'href="sobre" class="nav-link active"')
        elif base_name == 'servicos':
            new_content = new_content.replace('href="servicos" class="nav-link nav-dropdown-toggle"', 'href="servicos" class="nav-link nav-dropdown-toggle active"')
        elif base_name == 'blog':
            new_content = new_content.replace('href="blog" class="nav-link"', 'href="blog" class="nav-link active"')
        elif base_name == 'faq':
            new_content = new_content.replace('href="faq" class="nav-link"', 'href="faq" class="nav-link active"')
        elif base_name == 'contato':
            new_content = new_content.replace('href="contato" class="nav-link"', 'href="contato" class="nav-link active"')
            
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated nav in {html_file}")

# 2. Fix CSS
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix Services Grid (4 columns instead of auto-fit 300px)
css = re.sub(
    r'\.services-grid\s*\{[^}]*grid-template-columns:\s*repeat\(auto-fit,\s*minmax\([^,]+,\s*1fr\)\);',
    '.services-grid {\n  display: grid;\n  grid-template-columns: repeat(4, 1fr);',
    css
)

# Convert all white box components to premium dark glass
white_box_classes = [
    r'\.blog-card\s*\{', 
    r'\.feature-item\s*\{', 
    r'\.faq-item\s*\{', 
    r'\.faq-category\s*\{', 
    r'\.contact-card\s*\{', 
    r'\.about-stats\s*\{',
    r'\.sidebar-widget\s*\{',
    r'\.nav-dropdown-menu\s*\{',
    r'\.nav\s*\{'
]

for cls in white_box_classes:
    # We will just replace `background: var(--color-white);` with glass inside these blocks.
    # Actually, it's easier to just globally replace white background if it's inside curly braces,
    # but to be safe we'll use a regex that looks for background: var(--color-white) and border-color: var(--color-border-light)
    pass

# Global replacement for components that had white backgrounds making text unreadable
# Let's replace `background: var(--color-white);` globally to dark color EXCEPT in specific places if needed.
# Since the whole site is a dark theme, `var(--color-white)` background is almost always an error for cards.
# Wait, buttons use `--color-white` for `.btn-white`. They are fine.
# We will target blocks using `background: var(--color-white);` and `border: 1px solid var(--color-border-light);`

css = css.replace(
    'background: var(--color-white);\n  border-radius:',
    'background: rgba(255, 255, 255, 0.03);\n  backdrop-filter: blur(16px);\n  -webkit-backdrop-filter: blur(16px);\n  border-radius:'
)

css = css.replace('background: var(--color-white);', 'background: rgba(255, 255, 255, 0.03);')

# The mobile header menu and dropdown menus shouldn't be transparent glass if they clash
css = css.replace('.nav-dropdown-menu {\n  position: absolute;\n  top: calc(100% + 8px);\n  left: 50%;\n  transform: translateX(-50%) translateY(8px);\n  min-width: 260px;\n  background: rgba(255, 255, 255, 0.03);', 
                  '.nav-dropdown-menu {\n  position: absolute;\n  top: calc(100% + 8px);\n  left: 50%;\n  transform: translateX(-50%) translateY(8px);\n  min-width: 260px;\n  background: rgba(15, 15, 15, 0.98);')

css = css.replace('background: rgba(255, 255, 255, 0.03);\n    flex-direction: column;', 'background: rgba(13, 13, 13, 0.98);\n    flex-direction: column;')

# Increase padding for "respiro"
css = css.replace('padding: 24px;', 'padding: 32px;')
# The testimonial padding
css = css.replace('padding: 30px;', 'padding: 40px;')
# Mobile breakpoint padding for containers might need to stay (padding: 0 20px)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated CSS patterns")
