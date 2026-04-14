import os
import re

ROOT_DIR = os.path.join(os.path.dirname(__file__), '..')
BLOG_DIR = os.path.join(ROOT_DIR, 'blog')

social_col_root = '<div><h4>Conecte-se</h4><ul class="footer-links"><li><a href="https://www.instagram.com/ocarloseafonso" target="_blank" rel="noopener noreferrer">Instagram</a></li><li><a href="https://www.facebook.com/ocarloseafonso" target="_blank" rel="noopener noreferrer">Facebook</a></li><li><a href="https://www.youtube.com/@ocarloseafonso" target="_blank" rel="noopener noreferrer">YouTube</a></li><li><a href="https://www.tiktok.com/@ocarlosEafonso" target="_blank" rel="noopener noreferrer">TikTok</a></li><li><a href="https://substack.com/@ocarloseafonso" target="_blank" rel="noopener noreferrer">Substack</a></li><li><a href="https://chat.whatsapp.com/BSHBsM71FJJ2amvvn8ocjy" target="_blank" rel="noopener noreferrer">Grupo VIP (WhatsApp)</a></li></ul></div>'

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Remove <div class="footer-social">...</div>
    content = re.sub(r'\s*<div class="footer-social">.*?</div>', '', content, flags=re.DOTALL)

    # 2. Add social column before Navegação
    nav_h4 = '<div><h4>Navegação</h4>'
    if nav_h4 in content:
        # only insert if not already there
        if '<h4>Conecte-se</h4>' not in content:
            new_block = social_col_root + nav_h4
            content = content.replace(nav_h4, new_block)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {os.path.basename(filepath)}")

def main():
    skip_pages = {'servicos.html', 'trafego.html', 'relacionamento.html', 'atendimento.html'}
    
    for filename in os.listdir(ROOT_DIR):
        if filename.endswith('.html') and filename not in skip_pages:
            fix_file(os.path.join(ROOT_DIR, filename))
            
    if os.path.exists(BLOG_DIR):
        for filename in os.listdir(BLOG_DIR):
            if filename.endswith('.html'):
                fix_file(os.path.join(BLOG_DIR, filename))
            
if __name__ == '__main__':
    main()
