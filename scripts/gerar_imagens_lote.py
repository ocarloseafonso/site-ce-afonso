import os
import sys
import time
from pathlib import Path
from PIL import Image
import io
import urllib.request
import json
import ssl

ROOT_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT_DIR / ".env"
BLOG_DIR = ROOT_DIR / "assets" / "images" / "blog"
HERO_DIR = ROOT_DIR / "assets" / "images" / "hero"

def carregar_env():
    if ENV_PATH.exists():
        with open(ENV_PATH, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))

def obter_api_key():
    carregar_env()
    key = os.environ.get("PIXAZO_API_KEY")
    if not key:
        raise ValueError("PIXAZO_API_KEY não encontrada no .env!")
    return key

def chamar_pixazo_api(prompt, api_key, width=1024, height=576, num_steps=4):
    url = "https://gateway.pixazo.ai/flux-1-schnell/v1/getData"
    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "Ocp-Apim-Subscription-Key": api_key
    }
    payload = {
        "prompt": prompt,
        "num_steps": num_steps,
        "width": width,
        "height": height
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    ctx = ssl._create_unverified_context()
    
    with urllib.request.urlopen(req, context=ctx, timeout=90) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP Error {response.status}: {response.read().decode('utf-8')}")
        result = json.loads(response.read().decode("utf-8"))
        
    image_url = result.get("output")
    if not image_url or not isinstance(image_url, str):
        raise ValueError(f"Resposta inválida da Pixazo: {result}")
    return image_url

def salvar_imagem(image_url, destino_path, format="WEBP", quality=85):
    destino_path.parent.mkdir(parents=True, exist_ok=True)
    ctx = ssl._create_unverified_context()
    req = urllib.request.Request(
        image_url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    )
    with urllib.request.urlopen(req, context=ctx, timeout=90) as resp:
        img_bytes = resp.read()
        
    with Image.open(io.BytesIO(img_bytes)) as img:
        img = img.convert("RGB")
        img.save(destino_path, format=format, quality=quality)
        print(f"[OK] Imagem salva: {destino_path} ({format})")

TAREFAS = [
    {
        "slug": "anuncios-vs-organico",
        "dir": BLOG_DIR,
        "filename": "anuncios-vs-organico.webp",
        "format": "WEBP",
        "prompt": "Natural documentary photograph of a Black Brazilian local business owner, a man in his late 30s with short hair, thoughtfully analyzing search traffic and sales performance on a tablet at a clean wooden desk in his office in Brazil, sunny morning light, genuine contemplative expression, realistic skin texture, authentic Brazilian commercial office environment, 50mm lens photography, restrained colors, no text, no logos, no watermark"
    },
    {
        "slug": "erros-mapa-google",
        "dir": BLOG_DIR,
        "filename": "erros-mapa-google.webp",
        "format": "WEBP",
        "prompt": "Candid realistic photograph of a Black Brazilian small business owner in his 40s standing outside his local retail store in a Brazilian city commercial avenue, holding his smartphone to check map directions, bright natural daylight, authentic street background with Brazilian storefronts, natural posture, realistic skin tones and details, no text, no letters, no logos, no watermark"
    },
    {
        "slug": "guia-google-meu-negocio",
        "dir": BLOG_DIR,
        "filename": "guia-google-meu-negocio.webp",
        "format": "WEBP",
        "prompt": "Warm editorial photograph of a confident Black Brazilian female entrepreneur in her 30s, smiling naturally while standing inside her welcoming local business clinic or boutique in Brazil, customer in soft focus background, soft natural interior lighting, authentic everyday Brazilian business setting, sharp 50mm documentary style, no text, no watermark"
    },
    {
        "slug": "importancia-seo-local",
        "dir": BLOG_DIR,
        "filename": "importancia-seo-local.webp",
        "format": "WEBP",
        "prompt": "Documentary photograph of two Black Brazilian professionals, a man in his 40s and a young woman in her 20s, collaborating at a wooden conference table in a modern modest Brazilian office, discussing local growth strategy, focused work atmosphere, natural daylight through window, realistic skin texture, no text, no logo, no watermark"
    },
    {
        "slug": "poder-das-avaliacoes",
        "dir": BLOG_DIR,
        "filename": "poder-das-avaliacoes.webp",
        "format": "WEBP",
        "prompt": "Authentic photograph of a Black Brazilian service technician or clinic professional in a modern neat Brazilian workspace, checking customer feedback on a smartphone with a satisfied and proud expression, soft natural side lighting, realistic skin details, candid moment, no text, no typography, no watermark"
    },
    {
        "slug": "por-que-sistema-posicionamento",
        "dir": BLOG_DIR,
        "filename": "por-que-sistema-posicionamento.webp",
        "format": "WEBP",
        "prompt": "Editorial photograph of a Black Brazilian business strategist in his 30s holding a notepad standing next to a large window in a clean modern Brazilian office building, looking outward thoughtfully, soft natural reflections, restrained color grading, realistic professional ambiance, 85mm lens look, no text, no watermark"
    },
    {
        "slug": "site-para-negocio-local",
        "dir": BLOG_DIR,
        "filename": "site-para-negocio-local.webp",
        "format": "WEBP",
        "prompt": "Natural editorial photograph of a Black Brazilian woman in her 30s, small business manager, sitting at a desk with a computer monitor, reviewing a modern website layout for her local company, well-lit contemporary office in Brazil, candid realistic capture, documentary style, no text, no watermark"
    },
    {
        "slug": "topo-google-volta-redonda",
        "dir": BLOG_DIR,
        "filename": "topo-google-volta-redonda.webp",
        "format": "WEBP",
        "prompt": "Authentic street level documentary photograph of a lively Brazilian commercial district in Volta Redonda Rio de Janeiro, with a Black Brazilian shopkeeper smiling warmly at the entrance of his storefront welcoming a client, warm afternoon sunlight, real Brazilian city atmosphere, no text, no watermark"
    },
    {
        "slug": "whatsapp-para-negocios",
        "dir": BLOG_DIR,
        "filename": "whatsapp-para-negocios.webp",
        "format": "WEBP",
        "prompt": "Warm candid photograph of a Black Brazilian receptionist or sales coordinator in her late 20s, holding a smartphone responding to customer inquiries with a friendly professional smile at a clean reception desk in Brazil, natural soft daylight, authentic indoor setting, no text, no watermark"
    },
    {
        "slug": "hero-principal",
        "dir": HERO_DIR,
        "filename": "hero-principal.png",
        "format": "PNG",
        "prompt": "Professional authentic editorial photograph of a sharp Black Brazilian digital marketing strategist man in his late 20s or 30s consulting with a local business client in a stylish well-lit modern office in Brazil, analyzing strategic growth on a laptop, confident collaborative atmosphere, soft natural window light, 50mm portrait lens, shallow depth of field, restrained color grading, realistic skin textures, no text, no logos, no watermark"
    }
]

def main():
    api_key = obter_api_key()
    print(f"Iniciando geracao de {len(TAREFAS)} imagens...")
    
    for idx, item in enumerate(TAREFAS, 1):
        slug = item["slug"]
        destino = item["dir"] / item["filename"]
        print(f"\n[{idx}/{len(TAREFAS)}] Gerando: {item['filename']}...")
        try:
            img_url = chamar_pixazo_api(item["prompt"], api_key)
            salvar_imagem(img_url, destino, format=item["format"])
            # Se for hero-principal.png, salvar também como hero-principal.webp para performance
            if slug == "hero-principal":
                webp_destino = item["dir"] / "hero-principal.webp"
                salvar_imagem(img_url, webp_destino, format="WEBP")
            time.sleep(1)
        except Exception as e:
            print(f"[ERRO] Falha ao gerar {item['filename']}: {e}")

if __name__ == "__main__":
    main()
