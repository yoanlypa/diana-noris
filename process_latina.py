"""Procesa las fotos de «A Latina in DC» (C.LATINA) desde una carpeta con lat-NN.jpg → site/assets/img/latina/.
Uso: python process_latina.py <carpeta>"""
import json, sys
from pathlib import Path
from PIL import Image, ImageOps
sys.path.insert(0, str(Path(__file__).parent))
import content as C

src = Path(sys.argv[1])
out = Path(__file__).parent / "site" / "assets" / "img" / "latina"
out.mkdir(parents=True, exist_ok=True)
sizes = {}
for stem, n, _cap in C.LATINA:
    im = ImageOps.exif_transpose(Image.open(src / f"lat-{n:02d}.jpg")).convert("RGB")
    full = im.copy(); full.thumbnail((1600, 1600), Image.LANCZOS)
    full.save(out / f"{stem}.webp", "WEBP", quality=80, method=6)
    th = im.copy(); th.thumbnail((480, 480), Image.LANCZOS)
    th.save(out / f"{stem}-480.webp", "WEBP", quality=78, method=6)
    sizes[stem] = [*full.size, *th.size]
    print(stem, full.size, (out / f"{stem}.webp").stat().st_size // 1024, "KB")
(out / "sizes.json").write_text(json.dumps(sizes), encoding="utf-8")
