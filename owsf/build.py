"""Genera onewomanshowfilms.com en owsf/site/ (EN en "/", ES en "/es/").   Uso:  python owsf/build.py

Reutiliza datos e imágenes de la web de Diana (content.py, media/originals/, site/assets/img/).
Textos propios de la productora: owsf/texts.py. Diseño: owsf/site/assets/css/owsf.css y js/owsf.js.
"""
import html
import json
import shutil
import sys
from pathlib import Path

from PIL import Image, ImageOps

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))
import content as C  # noqa: E402  (web de Diana: tráiler, pósters, sinopsis, bio)
import texts as X  # noqa: E402

SITE = HERE / "site"
IMG = SITE / "assets" / "img"
V = "20261027b"

STARRING = "Diana Noris Smith, Jonathan Turpin, Nick Blanchet, Francesco Pultro, Rick Jermain"
DIRECTOR, FILMMAKER = "Diana Noris", "Nick Blanchet"


def esc(s):
    return html.escape(s, quote=True)


def home(lang):
    return "/" if lang == "en" else "/es/"


# ---------------------------------------------------------------- imágenes
def webp(src, name, widths, q=82):
    """Crea name-<w>.webp (sin ampliar) a partir de src; devuelve {w: (ruta, ancho, alto)}."""
    out = {}
    im0 = ImageOps.exif_transpose(Image.open(src))
    im0 = im0.convert("RGBA" if im0.mode in ("RGBA", "LA", "P") else "RGB")
    for w in widths:
        dst = IMG / f"{name}-{w}.webp"
        im = im0
        if im.width > w:
            im = im0.resize((w, round(im0.height * w / im0.width)), Image.LANCZOS)
        if not dst.exists():
            im.save(dst, "WEBP", quality=q, method=6)
        out[w] = (f"/assets/img/{dst.name}", im.width, im.height)
    return out


def srcset(v):
    return ", ".join(f"{p} {w}w" for p, w, _h in v.values())


def img_tag(v, sizes, alt, cls="", lazy=True, w_default=None):
    keys = sorted(v)
    p, w, h = v[w_default or keys[len(keys) // 2]]
    ld = ' loading="lazy"' if lazy else ' fetchpriority="high"'
    c = f' class="{cls}"' if cls else ""
    return f'<img src="{p}" srcset="{srcset(v)}" sizes="{sizes}" alt="{esc(alt)}" width="{w}" height="{h}"{ld} decoding="async"{c}>'


def prepare_images():
    IMG.mkdir(parents=True, exist_ok=True)
    orig, lat, hs = ROOT / "media" / "originals", ROOT / "site" / "assets" / "img" / "latina", ROOT / "site" / "assets" / "img" / "headshots"
    I = {}
    for k in set(X.HERO_SLIDES + X.STILLS):
        I[k] = webp(lat / f"{k}.webp", k, [480, 960, 1600])
    I["founder"] = webp(hs / "hs-01.webp", "diana-noris", [480, 800, 1100])
    I["poster"] = webp(orig / "poster.jpg", "a-latina-in-dc-poster", [400, 700, 1000])
    for d in C.DEV_FILMS:
        I[d["key"]] = webp(orig / f'{d["key"]}.png', d["key"].replace("_", "-"), [400, 700])
    I["press"] = webp(orig / "press_malaga.jpg", "cine-cultura-octubre-2026", [600, 1000, 1600])
    kit = SITE / "press-kit"
    kit.mkdir(exist_ok=True)
    shutil.copy2(ROOT / "site" / "press-kit" / "A-Latina-in-DC-Press-Kit.pdf", kit / "A-Latina-in-DC-Press-Kit.pdf")
    shutil.copy2(ROOT / "site" / "assets" / "img" / "press-kit-cover.webp", IMG / "press-kit-cover.webp")
    (IMG / "favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#0d0b0b"/>'
        '<text x="32" y="44" font-family="Georgia,serif" font-weight="700" font-size="30" fill="#c8102e" text-anchor="middle">W</text></svg>', encoding="utf-8")
    return I


# ---------------------------------------------------------------- piezas
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>'
PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>'
DL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4v11m0 0 4.5-4.5M12 15l-4.5-4.5M5 20h14"/></svg>'


def logo(tag="span", cls="logo"):
    return f'<{tag} class="{cls}">One <em>Woman</em> Show Films</{tag}>'


def label(text):
    return f'<span class="eyebrow">{text}</span>'


def heading(a, b, level="h2"):
    b = f" <em>{b}</em>" if b else ""
    return f"<{level} class=\"title\">{a}{b}</{level}>"


def header(lang):
    t = T = X.T[lang]
    other = "es" if lang == "en" else "en"
    links = "".join(f'<li><a href="#{k}">{v}</a></li>' for k, v in T["nav"])
    return f'''<a class="skip" href="#main">{t["skip"]}</a>
<header class="hdr">
  <a class="hdr-logo" href="{home(lang)}" aria-label="One Woman Show Films">{logo()}</a>
  <div class="hdr-right">
    <a class="lang-sw" href="{home(other)}" hreflang="{other}" lang="{other}">{other.upper()}</a>
    <button class="burger" type="button" aria-controls="menu" aria-expanded="false" aria-label="{t["menu"]}"><span></span></button>
  </div>
</header>
<nav class="menu" id="menu" aria-label="{t["menu"]}" aria-hidden="true">
  <ul>{links}</ul>
  <p class="menu-tag">Women-centered stories <em>with a point of view.</em></p>
</nav>
'''


def video(vid, title):
    return (f'<div class="video"><a class="yt" href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener" data-yt="{vid}" aria-label="{esc(title)}">'
            f'<img src="https://i.ytimg.com/vi/{vid}/maxresdefault.jpg" alt="{esc(title)}" loading="lazy" decoding="async" '
            f'onerror="this.onerror=null;this.src=\'https://i.ytimg.com/vi/{vid}/hqdefault.jpg\'">'
            f'<span class="yt-play" aria-hidden="true">{PLAY}</span></a></div>')


def tile(v, alt, cap, sizes, cls="tile"):
    full = v[max(v)][0]
    return (f'<button class="{cls}" type="button" data-full="{full}" data-cap="{esc(cap)}" aria-label="{esc(alt)}">'
            f'{img_tag(v, sizes, alt)}</button>')


# ---------------------------------------------------------------- página
def page(lang, I):
    t = X.T[lang]
    F = C.FILM[lang]
    bio = C.HOME[lang]["bio"]
    founder_bio = "".join(f"<p>{p}</p>" for p in (bio[0], bio[1], bio[3]))
    slides = "".join(
        f'<div class="slide{" on" if i == 0 else ""}" style="--fx:{X.HERO_FOCUS.get(k, "50%")}">{img_tag(I[k], "(max-width: 900px) 1600px, 100vw", "A Latina in DC", lazy=i > 0, w_default=1600)}</div>'
        for i, k in enumerate(X.HERO_SLIDES))
    tags = "".join(f"<li>{x}</li>" for x in t["hero_tags"])
    facts = [(t["f_title"], "A Latina in DC"), (t["f_genre"], t["genre"]), (t["f_logline"], F["film_p"]),
             (t["f_director"], DIRECTOR), (t["f_filmmaker"], FILMMAKER), (t["f_starring"], STARRING),
             (t["f_runtime"], t["runtime"]), (t["f_filmed"], t["filmed"])]
    facts_html = "".join(f"<p><b>{k}:</b> {esc(v)}</p>" for k, v in facts)
    quotes = "".join(
        f'<figure class="q"><span class="q-stars" role="img" aria-label="{t["stars"]}">★★★★★</span>'
        f'<blockquote lang="{"es" if a == "lautorresalb" else "en"}">“{esc(q)}”</blockquote><figcaption>— {esc(a)}, Letterboxd</figcaption></figure>'
        for a, q in X.REVIEW_QUOTES[lang])
    stills = "".join(f'<div class="still">{tile(I[k], cap, cap, "(max-width:700px) 50vw, 25vw")}</div>'
                     for k in X.STILLS for cap in [next(c[lang] for s, _n, c in C.LATINA if s == k)])
    upcoming = "".join(
        f'''<article class="proj">
      <div class="proj-media">{tile(I[d["key"]], d["title"] + " – poster", d["title"] + " · " + t["statuses"][d["key"]], "(max-width:700px) 100vw, 45vw")}</div>
      <div class="proj-body"><h3>{d["title"]} <span>({t["statuses"][d["key"]]})</span></h3><p>{t["dev_lines"][d["key"]]}</p></div>
    </article>''' for d in C.DEV_FILMS)
    press_v = I["press"]
    ig, imdb = C.INSTAGRAM, C.IMDB
    contact_url = X.DIANA_SITE + C.path(lang, "contact")
    press_url = X.DIANA_SITE + C.path(lang, "press")
    other = "es" if lang == "en" else "en"
    ld = [{"@context": "https://schema.org", "@type": "Organization", "@id": X.DOMAIN + "/#org", "name": "One Woman Show Films",
           "url": X.DOMAIN + home(lang), "slogan": "Women-centered stories with a point of view.", "description": t["about_p"],
           "founder": {"@type": "Person", "name": "Diana Noris Smith", "url": X.DIANA_SITE, "sameAs": [imdb]},
           "location": ["New York", "Málaga"], "sameAs": [X.INSTAGRAM]},
          {"@context": "https://schema.org", "@type": "Movie", "name": "A Latina in DC", "genre": t["genre"], "description": F["film_p"],
           "director": {"@type": "Person", "name": DIRECTOR}, "productionCompany": {"@id": X.DOMAIN + "/#org"},
           "image": X.DOMAIN + I["poster"][1000][0], "trailer": {"@type": "VideoObject", "name": t["trailer_cap"],
           "embedUrl": f'https://www.youtube.com/embed/{C.LATINA_TRAILER["id"]}', "thumbnailUrl": f'https://i.ytimg.com/vi/{C.LATINA_TRAILER["id"]}/hqdefault.jpg',
           "description": t["trailer_cap"], "uploadDate": "2026-10-20"}}]
    ld_html = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    og = X.DOMAIN + I["poster"][1000][0]
    return f'''<!doctype html>
<html lang="{lang}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t["title"])}</title>
<meta name="description" content="{esc(t["desc"])}">
<meta name="theme-color" content="#0d0b0b">
<link rel="canonical" href="{X.DOMAIN}{home(lang)}">
<link rel="alternate" hreflang="en" href="{X.DOMAIN}/">
<link rel="alternate" hreflang="es" href="{X.DOMAIN}/es/">
<link rel="alternate" hreflang="x-default" href="{X.DOMAIN}/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="One Woman Show Films">
<meta property="og:title" content="{esc(t["title"])}">
<meta property="og:description" content="{esc(t["desc"])}">
<meta property="og:url" content="{X.DOMAIN}{home(lang)}">
<meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="/assets/img/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Oswald:wght@300;400&family=Lora:ital,wght@0,400;0,500;1,400&family=Pinyon+Script&display=swap">
<link rel="stylesheet" href="/assets/css/owsf.css?v={V}">
{ld_html}
</head>
<body>
{header(lang)}
<main id="main">

<section class="hero" aria-label="One Woman Show Films">
  <div class="slides" aria-hidden="true">{slides}</div>
  <div class="hero-shade"></div>
  <div class="hero-text">
    <h1 class="hero-h1">{t["hero_h1"]}<br><em>{t["hero_h2"]}</em></h1>
    <ul class="hero-tags">{tags}</ul>
  </div>
  <a class="scroll" href="#about" aria-label="{t["scroll"]}"><span></span></a>
</section>

<section class="sec center" id="about">
  {label(t["about_k"])}
  <div class="about-logo reveal">{logo("p", "logo-xl")}<p class="script">Women-centered stories with a point of view.</p></div>
  <p class="lede reveal">{t["about_p"]}</p>
  <p class="cities reveal">{t["about_cities"]}</p>
</section>

<section class="sec textured" id="founder">
  <div class="center">{label(t["founder_k"])}{heading(t["founder_h1"], t["founder_h2"])}</div>
  <div class="wrap founder">
    <div class="founder-photo reveal">
      {img_tag(I["founder"], "(max-width:900px) 90vw, 440px", "Diana Noris Smith, founder of One Woman Show Films")}
      <ul class="socials"><li><a href="{ig}" target="_blank" rel="noopener me">Instagram</a></li><li><a href="{imdb}" target="_blank" rel="noopener me">IMDb</a></li><li><a href="{X.DIANA_SITE}{C.path(lang, "home")}" target="_blank" rel="noopener">diananoris.com</a></li></ul>
    </div>
    <div class="founder-text reveal">
      <h3 class="name">Diana <em>Noris Smith</em></h3>
      <span class="role">{t["founder_role"]}</span>
      {founder_bio}
      <a class="more" href="#press">{t["press_k"]} {ARROW}</a>
    </div>
  </div>
</section>

<section class="sec" id="latest">
  <div class="center">{label(t["latest_k"])}<h2 class="title"><em>{t["latest_h1"]}</em> {t["latest_h2"]}</h2></div>
  <div class="wrap latest">
    <div class="latest-media reveal">
      {video(C.LATINA_TRAILER["id"], t["trailer_cap"])}
      <p class="cap">{t["trailer_cap"]}</p>
    </div>
    <div class="acc reveal">
      <details open><summary>{t["acc_about"]}</summary><div class="acc-body">{facts_html}</div></details>
      <details><summary>{t["acc_festival"]}</summary><div class="acc-body"><p>{t["festival_p"]}</p></div></details>
      <details><summary>{t["acc_kit"]}</summary><div class="acc-body kit">
        <a class="kit-cover" href="{X.PRESS_KIT}" target="_blank" rel="noopener"><img src="/assets/img/press-kit-cover.webp" alt="A Latina in DC – press kit" width="900" height="636" loading="lazy" decoding="async"></a>
        <p>{t["kit_p"]}</p><a class="btn" href="{X.PRESS_KIT}" download>{DL} {t["kit_btn"]}</a></div></details>
    </div>
  </div>

  <div class="wrap reviews">
    <div class="center">{heading(t["reviews_h1"], t["reviews_h2"], "h3")}</div>
    <div class="q-grid reveal">{quotes}</div>
    <div class="center"><a class="btn" href="{X.LETTERBOXD}" target="_blank" rel="noopener">{t["reviews_all"]}</a></div>
  </div>

  <div class="wrap stills-wrap">
    <div class="center">{label(t["stills_k"])}</div>
    <div class="stills reveal" data-gallery>{stills}</div>
  </div>
</section>

<section class="sec alt" id="upcoming">
  <div class="center">{label(t["upcoming_k"])}{heading(t["upcoming_h1"], t["upcoming_h2"])}</div>
  <div class="wrap projs" data-gallery>{upcoming}</div>
  <p class="center note">{t["upcoming_note"]}</p>
</section>

<section class="sec" id="press">
  <div class="center">{label(t["press_k"])}{heading(t["press_h1"], t["press_h2"])}</div>
  <div class="wrap press" data-gallery>
    <div class="press-media reveal">{tile(press_v, t["press_title"], t["press_meta"], "(max-width:900px) 100vw, 640px")}</div>
    <div class="press-text reveal">
      <span class="meta">{t["press_meta"]}</span>
      <h3>{t["press_title"]}</h3>
      <p>{t["press_p"]}</p>
      <div class="btn-row"><button class="btn js-open-press" type="button">{t["press_open"]}</button><a class="link" href="{press_url}" target="_blank" rel="noopener">{t["press_all"]} {ARROW}</a></div>
    </div>
  </div>
</section>

<section class="sec alt center" id="contact">
  {label(t["contact_k"])}{heading(t["contact_h1"], t["contact_h2"])}
  <p class="lede reveal">{t["contact_p"]}</p>
  <div class="btn-row center-row"><a class="btn" href="{contact_url}" target="_blank" rel="noopener">{t["contact_btn"]} {ARROW}</a><a class="btn ghost" href="{X.INSTAGRAM}" target="_blank" rel="noopener me">Instagram {X.INSTAGRAM_HANDLE}</a></div>
  <p class="cities">{t["about_cities"]}</p>
</section>

</main>

<footer class="ftr">
  <div class="wrap ftr-grid">
    <a href="{home(lang)}" aria-label="One Woman Show Films">{logo()}</a>
    <ul class="ftr-nav">{"".join(f'<li><a href="#{k}">{v}</a></li>' for k, v in t["nav"])}<li><a href="{home(other)}" hreflang="{other}">{X.T[other]["lang_name"]}</a></li><li><a href="{X.INSTAGRAM}" target="_blank" rel="noopener me">Instagram {X.INSTAGRAM_HANDLE}</a></li></ul>
  </div>
  <div class="wrap ftr-bottom"><span>© 2026 One Woman Show Films · {t["rights"]}</span><span class="credit">{t["credit"]}: <a href="https://yoapro.site" target="_blank" rel="noopener">YOA PRO</a></span></div>
</footer>

<div class="lightbox" role="dialog" aria-modal="true" aria-hidden="true">
  <button class="lb-close" type="button" aria-label="{t["close"]}">×</button>
  <button class="lb-prev" type="button" aria-label="{t["lb_prev"]}">‹</button>
  <img src="" alt="">
  <button class="lb-next" type="button" aria-label="{t["lb_next"]}">›</button>
  <div class="lb-cap"></div>
</div>
<script src="/assets/js/owsf.js?v={V}" defer></script>
</body>
</html>
'''


def main():
    I = prepare_images()
    for lang in ("en", "es"):
        out = SITE / ("index.html" if lang == "en" else "es/index.html")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(lang, I), encoding="utf-8")
    (SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {X.DOMAIN}/sitemap.xml\n", encoding="utf-8")
    urls = "".join(f'  <url><loc>{X.DOMAIN}{p}</loc><xhtml:link rel="alternate" hreflang="en" href="{X.DOMAIN}/"/>'
                   f'<xhtml:link rel="alternate" hreflang="es" href="{X.DOMAIN}/es/"/></url>\n' for p in ("/", "/es/"))
    (SITE / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                                      'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + urls + "</urlset>\n", encoding="utf-8")
    print("built: onewomanshowfilms (en, es)")


if __name__ == "__main__":
    main()
