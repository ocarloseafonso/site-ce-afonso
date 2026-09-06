"""
Módulo Gerador de Imagem de Capa e Miniatura via Pixazo API (FLUX Schnell)
C.E. Afonso Soluções Digitais
"""

import os
import sys
import json
import urllib.request
import urllib.error
from pathlib import Path
from PIL import Image
import io

ROOT_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT_DIR / ".env"
DEFAULT_OUTPUT_DIR = ROOT_DIR / "assets" / "images" / "blog"

def carregar_env():
    """Carrega variaveis do arquivo .env se existirem."""
    if ENV_PATH.exists():
        with open(ENV_PATH, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))

def obter_api_key():
    carregar_env()
    api_key = os.environ.get("PIXAZO_API_KEY")
    if not api_key:
        raise ValueError("PIXAZO_API_KEY nao encontrada no ambiente nem no arquivo .env!")
    return api_key

def chamar_pixazo_api(prompt, api_key, width=1024, height=576, num_steps=4):
    """Envia o prompt para a API Pixazo FLUX 1 Schnell."""
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
    import ssl
    ctx = ssl._create_unverified_context()
    
    with urllib.request.urlopen(req, context=ctx, timeout=60) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP Error {response.status}: {response.read().decode('utf-8')}")
        result = json.loads(response.read().decode("utf-8"))
        
    image_url = result.get("output")
    if not image_url or not isinstance(image_url, str):
        raise ValueError(f"Resposta da Pixazo nao contem URL valida de imagem: {result}")
    return image_url

def baixar_e_otimizar_webp(image_url, destino_webp, max_width=1280, max_height=720):
    """Baixa a imagem da URL e salva como WebP otimizado."""
    import ssl
    destino_webp.parent.mkdir(parents=True, exist_ok=True)
    
    ctx = ssl._create_unverified_context()
    req = urllib.request.Request(
        image_url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    )
    with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
        img_bytes = resp.read()
        
    with Image.open(io.BytesIO(img_bytes)) as img:
        img = img.convert("RGB")
        # Redimensionamento suave se necessario mantendo proporcao
        img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        img.save(destino_webp, "WEBP", quality=85, method=6)
        print(f"[OK] Imagem salva e otimizada com sucesso em: {destino_webp}")

def gerar_imagem_artigo(slug, prompt, fallback_prompt=None, output_dir=None):
    """
    Gera a imagem para o artigo com base no slug e no prompt.
    Em caso de falha, tenta o fallback_prompt.
    """
    api_key = obter_api_key()
    out_dir = Path(output_dir) if output_dir else DEFAULT_OUTPUT_DIR
    destino = out_dir / f"{slug}.webp"
    
    print(f"\n[PIXAZO] Iniciando geracao de imagem para: {slug}")
    print(f"Prompt: {prompt[:120]}...")
    
    # Tentativa 1
    try:
        img_url = chamar_pixazo_api(prompt, api_key)
        print(f"[PIXAZO] Imagem gerada: {img_url}")
        baixar_e_otimizar_webp(img_url, destino)
        return str(destino)
    except Exception as err1:
        print(f"[AVISO] Primeira tentativa falhou: {err1}")
        
        # Tentativa 2 com fallback ou prompt simplificado
        prompt_tentativa_2 = fallback_prompt if fallback_prompt else f"{prompt[:300]}, natural daylight, editorial photography"
        print(f"[PIXAZO] Tentando novamente com prompt ajustado...")
        try:
            img_url = chamar_pixazo_api(prompt_tentativa_2, api_key)
            print(f"[PIXAZO] Imagem gerada (tentativa 2): {img_url}")
            baixar_e_otimizar_webp(img_url, destino)
            return str(destino)
        except Exception as err2:
            print(f"[ERRO] Falha na segunda tentativa: {err2}")
            print("[AVISO] Prosseguindo sem interromper deploy do artigo.")
            return None

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python gerar_imagem_pixazo.py <slug> <prompt> [fallback_prompt]")
        sys.exit(1)
        
    slug = sys.argv[1]
    prompt = sys.argv[2]
    fallback = sys.argv[3] if len(sys.argv) > 3 else None
    gerar_imagem_artigo(slug, prompt, fallback)
