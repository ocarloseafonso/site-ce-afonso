import os
import re

# Read the 6 blog cards from blog.html
try:
    with open('blog.html', 'r', encoding='utf-8') as f:
        blog_content = f.read()
        
    grid_match = re.search(r'<div class="blog-grid">([\s\S]*?)</div>\s*</div>\s*</section>', blog_content)
    if not grid_match:
        print("Could not find blog grid in blog.html")
        exit(1)
        
    # Extract all individual cards
    cards = re.findall(r'<div class="blog-card">[\s\S]*?</div></div>', grid_match.group(1))
    print(f"Found {len(cards)} blog cards in blog.html.")

    # Process each HTML file
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for file in html_files:
        if file == 'blog.html':
            continue
            
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'class="related-section"' in content:
            file_basename = file.replace('.html', '')
            
            # Select the first 3 cards that do NOT link to the current file
            selected_cards = []
            for card in cards:
                # check if this card links to the current file
                if f'href="{file_basename}"' not in card and f'href="{file_basename}.html"' not in card:
                    selected_cards.append(card)
                if len(selected_cards) == 3:
                    break
                    
            related_html = '\n        '.join(selected_cards)
            
            # Replace the contents of the related-section grid
            related_regex = r'(<section class="related-section">[\s\S]*?<div class="blog-grid">)([\s\S]*?)(</div>\s*</div>\s*</section>)'
            
            new_content = re.sub(related_regex, r'\1\n        ' + related_html + r'\n      \3', content)
            
            if content != new_content:
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated related posts in {file}")

except Exception as e:
    print(f"Error: {e}")
