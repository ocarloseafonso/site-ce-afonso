import os
import re

ROOT_DIR = os.path.join(os.path.dirname(__file__), '..')
BLOG_DIR = os.path.join(ROOT_DIR, 'blog')

def fix_file(filepath, is_blog):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Remove Serviços Column
    if is_blog:
        services_re = r'\s*<div><h4>Serviços</h4><ul class="footer-links"><li><a href="\.\./posicionamento\.html">Posicionamento no Google</a></li><li><a href="\.\./atendimento\.html">Atendimento \(Zap que Vende\)</a></li><li><a href="\.\./relacionamento\.html">Relacionamento com Leads</a></li><li><a href="\.\./trafego\.html">Tráfego Pago Estratégico</a></li><li><a href="\.\./servicos\.html" style="color:var\(--color-primary\);font-weight:600;">Ver todos os serviços →</a></li></ul></div>'
    else:
        services_re = r'\s*<div><h4>Serviços</h4><ul class="footer-links"><li><a href="posicionamento">Posicionamento no Google</a></li><li><a href="atendimento">Atendimento \(Zap que Vende\)</a></li><li><a href="relacionamento">Relacionamento com Leads</a></li><li><a href="trafego">Tráfego Pago Estratégico</a></li><li><a href="servicos" style="color:var\(--color-primary\);font-weight:600;">Ver todos os serviços →</a></li></ul></div>'

    content = re.sub(services_re, '', content, flags=re.DOTALL)

    # 2. Add Protocolo PDL to Navegação
    if is_blog:
        nav_old = '<div><h4>Navegação</h4><ul class="footer-links"><li><a href="../index.html">Início</a></li><li><a href="../sobre.html">Sobre</a></li><li><a href="../blog.html">Blog</a></li><li><a href="../faq.html">FAQ</a></li><li><a href="../contato.html">Contato</a></li><li><a href="../privacy.html">Política de Privacidade</a></li></ul></div>'
        nav_new = '<div><h4>Navegação</h4><ul class="footer-links"><li><a href="../index.html">Início</a></li><li><a href="../sobre.html">Sobre</a></li><li><a href="../pdl.html">Protocolo PDL</a></li><li><a href="../blog.html">Blog</a></li><li><a href="../faq.html">FAQ</a></li><li><a href="../contato.html">Contato</a></li><li><a href="../privacy.html">Política de Privacidade</a></li></ul></div>'
    else:
        nav_old = '<div><h4>Navegação</h4><ul class="footer-links"><li><a href="/">Início</a></li><li><a href="sobre">Sobre</a></li><li><a href="blog">Blog</a></li><li><a href="faq">FAQ</a></li><li><a href="contato">Contato</a></li><li><a href="privacy">Política de Privacidade</a></li></ul></div>'
        nav_new = '<div><h4>Navegação</h4><ul class="footer-links"><li><a href="/">Início</a></li><li><a href="sobre">Sobre</a></li><li><a href="pdl">Protocolo PDL</a></li><li><a href="blog">Blog</a></li><li><a href="faq">FAQ</a></li><li><a href="contato">Contato</a></li><li><a href="privacy">Política de Privacidade</a></li></ul></div>'

    
    if nav_old in content:
        content = content.replace(nav_old, nav_new)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {os.path.basename(filepath)}")

def main():
    skip_pages = {'servicos.html', 'trafego.html', 'relacionamento.html', 'atendimento.html'}
    
    for filename in os.listdir(ROOT_DIR):
        if filename.endswith('.html') and filename not in skip_pages:
            fix_file(os.path.join(ROOT_DIR, filename), is_blog=False)
            
    for filename in os.listdir(BLOG_DIR):
        if filename.endswith('.html'):
            fix_file(os.path.join(BLOG_DIR, filename), is_blog=True)
            
if __name__ == '__main__':
    main()
