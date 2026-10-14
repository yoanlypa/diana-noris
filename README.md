# diananoris.com — web nueva (demo para que Diana decida)

Web estática, bilingüe (EN en `/`, ES en `/es/`), estética cinematográfica oscura inspirada en Filmoo (ver `docs/filmoo-style-brief.json`).
Plan y análisis de la web actual: `docs/diananoris-plan.json`.

## Ver la demo en tu PC
```bash
cd site
python -m http.server 8780
```
y abre http://localhost:8780/

## Editar y regenerar
Todo el contenido está en `content.py` (textos EN/ES, enlaces, imágenes, datos de la agencia). Después:
```bash
python build.py
```
Genera las 12 páginas en `site/`. El diseño está en `site/assets/css/styles.css` y `site/assets/js/main.js`.

## Estado de la demo
- **Imágenes**: ya no dependen de Wix. Los originales descargados del Wix antiguo están en `media/originals/` (con `wix-manifest.json` como referencia) y `python build.py` genera las versiones WebP que usa cada página en `site/assets/img/media/` (solo crea las que falten). Para cambiar una imagen, sustituye su original y borra sus WebP de `site/assets/img/media/`.
- **Vídeos de prensa**: lista `PRESS_VIDEOS` en `content.py` (YouTube o Vimeo). Se muestran en Press / Prensa con el mismo reproductor que los reels (el vídeo se carga al pulsar).
- **No se indexa**: `DEMO = True` en `content.py` añade `noindex` y un `robots.txt` que bloquea todo. Poner `False` el día de publicar.
- **Textos**: salen de su web actual, su ficha de casting y su biografía. La traducción al español es propia: debe revisarla Diana.
- **Datos que hay que confirmar** (marcados con `# TODO Diana` en `content.py`): representación vigente (The Wayne Agency es de EE. UU.), créditos (ahora solo los 4 títulos de su tarjeta de IMDb, sin papeles), si se publican medidas de casting (solo altura, ojos y pelo), y que no haya datos de contacto que ya no valgan.
- **Páginas con poco material**: Artwork (sin fotos, muestra "Galería próximamente") y la sección de proyectos en desarrollo de Film.

## Publicar
- La raíz del repositorio ya trae el `Staticfile` (`root: site`). En Railway: *New project* → *Deploy from GitHub repo* → `yoanlypa/diana-noris`. Railway sirve la carpeta `site/` sin más configuración (después, *Settings → Networking → Generate Domain*).
- Cuando Diana apruebe: apuntar el dominio `diananoris.com` al nuevo servicio, poner `DEMO = False`, regenerar y enviar `sitemap.xml` a Google Search Console.
- **Redirecciones 301 desde las direcciones antiguas del Wix** (para no perder lo posicionado):

| Wix actual | Nueva |
|---|---|
| `/reel-1` | `/acting/` |
| `/portfolio` | `/acting/` |
| `/commercial` | `/acting/` |
| `/press` | `/press/` |
| `/one-woman-show-films-1` | `/film/` |
| `/one-woman-show-films` (A Latina in DC) | `/film/` |
| `/development` | `/film/` |
| `/artwork` | `/artwork/` |
| `/contact` | `/contact/` |

## Qué se necesita de Diana para la versión definitiva
Fotos en alta resolución (headshots y retratos), el reel en el archivo original (hay un 1080p en Wix, pero conviene el original), créditos con papeles o su perfil de IMDb, enlaces de prensa y los clips de la gira, material de A Latina in DC (póster, sinopsis, tráiler), fotos de su arte, redes sociales correctas y la representación vigente. Permiso y derechos de todas las imágenes y vídeos.
