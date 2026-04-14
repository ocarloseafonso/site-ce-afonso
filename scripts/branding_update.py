import os

files_to_update = [
    'posicionamento.html',
    'atendimento.html',
    'relacionamento.html',
    'trafego.html',
    'faq.html',
    'js/main.js'
]

replacements = {
    'Método PART': 'Protocolo de Destaque Local (PDL)',
    'Carlos E. Afonso': 'Carlos Eduardo Afonso'
}

base_path = r'c:\Users\cadu_\OneDrive\Área de Trabalho\C.E. Afonso Soluções Digitais\Clientes\C.E. Afonso Soluções Digitais\Site - CE Afonso Soluções Digitais'

for filename in files_to_update:
    filepath = os.path.join(base_path, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        for old, new in replacements.items():
            new_content = new_content.replace(old, new)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"No changes for {filename}")
    else:
        print(f"File not found: {filename}")
