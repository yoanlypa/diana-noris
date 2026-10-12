"""Optimiza los headshots de Diana y los deja en site/assets/img/headshots/ (WebP completo + miniatura de 640 px).

Uso:  python process_headshots.py <carpeta con 13.jpg ... 21.jpg>
El orden y los textos alternativos están en content.py (HEADSHOTS); aquí solo se convierten los archivos.
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageOps

sys.path.insert(0, str(Path(__file__).resolve().parent))
from content import HEADSHOTS  # noqa: E402

SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
OUT = Path(__file__).resolve().parent / "site" / "assets" / "img" / "headshots"
OUT.mkdir(parents=True, exist_ok=True)

sizes = {}
for stem, source, _alt in HEADSHOTS:
    f = SRC / f"{source}.jpg"
    if not f.exists():
        print("falta", f)
        continue
    im = ImageOps.exif_transpose(Image.open(f)).convert("RGB")
    im.thumbnail((1600, 1600), Image.LANCZOS)
    im.save(OUT / f"{stem}.webp", "WEBP", quality=84, method=6)
    thumb = im.copy()
    thumb.thumbnail((640, 1000), Image.LANCZOS)
    thumb.save(OUT / f"{stem}-640.webp", "WEBP", quality=80, method=6)
    sizes[stem] = [im.width, im.height, thumb.width, thumb.height]
    print(stem, im.size, "->", round((OUT / f"{stem}.webp").stat().st_size / 1024), "KB")
(OUT / "sizes.json").write_text(json.dumps(sizes), encoding="utf-8")
