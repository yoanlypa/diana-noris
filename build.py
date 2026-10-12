"""Genera diananoris/site/ (EN en "/" y ES en "/es/").   Uso:  python build.py"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import content as C  # noqa: E402
from content import UI, MEDIA, img, path, DOMAIN  # noqa: E402

SITE = Path(__file__).resolve().parent / "site"
V = "20261012"
OTHER = {"en": "es", "es": "en"}

# ---------------------------------------------------------------- iconos
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>'
PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 4.5v15l13-7.5z"/></svg>'
CHEV_L = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 5-7 7 7 7"/></svg>'
CHEV_R = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>'
ICONS = {
    "acting": '<path d="M12 10h40v22c0 12-9 22-20 22S12 44 12 32z"/><path d="M22 26h6M36 26h6"/><path d="M24 38c3 4 13 4 16 0"/>',
    "film": '<rect x="8" y="24" width="48" height="30" rx="2"/><path d="M8 24 14 10l10 14 10-14 10 14 10-14 2 4"/>',
    "pen": '<path d="M10 54l6-18L44 8l12 12-28 28z"/><path d="M38 14l12 12M10 54l10-4"/>',
    "art": '<path d="M32 8C18 8 8 18 8 30c0 12 10 22 22 22 4 0 6-3 4-6-2-3 0-6 4-6h8c6 0 10-4 10-10C56 18 46 8 32 8z"/><circle cx="20" cy="30" r="3"/><circle cx="28" cy="20" r="3"/><circle cx="40" cy="20" r="3"/>',
}


def icon(name):
    return f'<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'


FLAG_ES = '<svg viewBox="0 0 60 60" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="60" height="60" fill="#c60b1e"/><rect y="15" width="60" height="30" fill="#ffc400"/></svg>'
FLAG_EN = '<svg viewBox="0 0 60 60" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="60" height="60" fill="#012169"/><path d="M0 0 60 60M60 0 0 60" stroke="#fff" stroke-width="11"/><path d="M0 0 60 60M60 0 0 60" stroke="#c8102e" stroke-width="4"/><path d="M30 0v60M0 30h60" stroke="#fff" stroke-width="18"/><path d="M30 0v60M0 30h60" stroke="#c8102e" stroke-width="10"/></svg>'


# ---------------------------------------------------------------- utilidades
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def write(rel, html):
    out = SITE / rel.strip("/") / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


def pic(key, widths, sizes, alt, cls="", loading="lazy", w=None, h=None, priority=False):
    mid = MEDIA[key]
    srcset = ", ".join(f"{img(mid, x)} {x}w" for x in widths)
    dims = f' width="{w}" height="{h}"' if w and h else ""
    pr = ' fetchpriority="high"' if priority else ""
    ld = "" if priority else f' loading="{loading}"'
    return f'<img src="{img(mid, widths[len(widths) // 2])}" srcset="{srcset}" sizes="{sizes}" alt="{esc(alt)}"{dims}{pr}{ld} decoding="async" class="{cls}">'


def tile(key, widths, sizes, alt, cap="", ratio=None):
    full = img(MEDIA[key], 1600)
    style = f' style="aspect-ratio:{ratio}"' if ratio else ""
    return (f'<button class="tile" type="button" data-cap="{esc(cap or alt)}" data-full="{full}" aria-label="{esc(alt)}"{style}>'
            f'{pic(key, widths, sizes, alt)}</button>')


def two_tone(a, b):
    return f"<b>{a}</b> <span>{b}</span>" if b else f"<b>{a}</b>"


def crumbs(lang, label):
    return f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{path(lang, "home")}">{UI[lang]["home"]}</a><span>/</span>{label}</nav>'


# ---------------------------------------------------------------- piezas comunes
def head(lang, page, ld, og_key="banner", solid_title=None):
    title, desc = C.SEO[lang][page]
    p = path(lang, page)
    es_p, en_p = path("es", page), path("en", page)
    robots = '<meta name="robots" content="noindex, nofollow">\n' if C.DEMO else ""
    ld_html = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    return f'''<!doctype html>
<html lang="{lang}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{robots}<meta name="theme-color" content="#0a0a0a">
<link rel="canonical" href="{DOMAIN}{p}">
<link rel="alternate" hreflang="en" href="{DOMAIN}{en_p}">
<link rel="alternate" hreflang="es" href="{DOMAIN}{es_p}">
<link rel="alternate" hreflang="x-default" href="{DOMAIN}{en_p}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Diana Noris">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{DOMAIN}{p}">
<meta property="og:locale" content="{UI[lang]["locale"]}">
<meta property="og:image" content="{img(MEDIA[og_key], 1200)}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="/assets/img/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://static.wixstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alumni+Sans:wght@400;600&family=DM+Sans:wght@400;500;700&family=Inter:wght@300;400;500&family=Pinyon+Script&display=swap">
<link rel="stylesheet" href="/assets/css/styles.css?v={V}">
{ld_html}
</head>
'''


def header(lang, page, solid):
    u = UI[lang]
    links = "".join(
        f'<a href="{path(lang, k)}"{" aria-current=\"page\"" if k == page else ""}>{u["nav"][k]}</a>'
        for k in ("acting", "film", "press", "artwork", "contact"))
    cur = lambda l: ' aria-current="true"' if l == lang else ""  # noqa: E731
    flags = (f'<a href="{path("en", page)}" hreflang="en" lang="en" title="English" aria-label="English"{cur("en")}>{FLAG_EN}</a>'
             f'<a href="{path("es", page)}" hreflang="es" lang="es" title="Español" aria-label="Español"{cur("es")}>{FLAG_ES}</a>')
    reel = path(lang, "acting") + "#reel"
    return f'''<body{' class="home"' if page == 'home' else ''}>
<a class="skip" href="#main">{u["skip"]}</a>
<header class="header{" solid" if solid else ""}"{" data-solid" if solid else ""}>
  <div class="wrap">
    <a class="logo" href="{path(lang, "home")}" aria-label="Diana Noris">Diana <i>N</i>oris</a>
    <div class="header-right">
      <nav class="nav" id="nav" aria-label="{u["menu"]}">{links}<a class="btn sm nav-cta" href="{reel}">{u["watch"]}</a></nav>
      <a class="btn sm hdr-btn" href="{reel}">{u["watch"]} {ARROW}</a>
      <div class="lang" role="group" aria-label="Language / Idioma">{flags}</div>
      <button class="burger" type="button" aria-label="{u["menu"]}" aria-controls="nav" aria-expanded="false"><span></span></button>
    </div>
  </div>
</header>
'''


def footer(lang):
    u = UI[lang]
    explore = "".join(f'<li><a href="{path(lang, k)}">{ARROW}{u["nav"][k]}</a></li>' for k in ("acting", "film", "press", "artwork", "contact"))
    soc = "".join(f'<li><a href="{url}" target="_blank" rel="noopener me">{ARROW}{name}</a></li>' for name, url in C.SOCIALS)
    demo = f" · {u['legal_demo']}" if C.DEMO else ""
    return f'''<footer class="footer">
  <div class="wrap">
    <div class="f-grid">
      <div><a class="logo" href="{path(lang, "home")}" aria-label="Diana Noris">Diana <i>N</i>oris</a><p>{u["roles"]}</p></div>
      <div><h4>{u["explore"]}</h4><ul>{explore}</ul></div>
      <div><h4>{u["follow"]}</h4><ul>{soc}</ul></div>
    </div>
    <div class="f-bottom"><span>© 2026 Diana Noris · {u["rights"]}{demo}</span><span>Málaga · Madrid · London</span></div>
  </div>
</footer>

<div class="lightbox" role="dialog" aria-modal="true" aria-hidden="true">
  <button class="lb-close" type="button" aria-label="Close">×</button>
  <button class="lb-prev" type="button" aria-label="Previous">‹</button>
  <img src="" alt="">
  <button class="lb-next" type="button" aria-label="Next">›</button>
  <div class="lb-cap"></div>
</div>
<script src="/assets/js/main.js?v={V}" defer></script>
</body>
</html>
'''


def bigcta(lang, h1, h2, p_text):
    u = UI[lang]
    return f'''<section class="bigcta"><div class="wrap">
  <span class="label reveal">{C.HOME[lang]["cta_k"]}</span>
  <a class="display d-xl reveal" href="{path(lang, "contact")}">{two_tone(h1, h2)}{ARROW}</a>
  <p class="lead reveal">{p_text}</p>
  <div class="btn-row reveal" style="justify-content:center"><a class="btn" href="{path(lang, "contact")}">{u["contact_btn"]} {ARROW}</a><a class="btn outline" href="{C.INSTAGRAM}" target="_blank" rel="noopener me">Instagram {ARROW}</a></div>
</div></section>'''


def p_hero(lang, page, k, h1, h2, lead):
    u = UI[lang]
    return f'''<section class="p-hero"><div class="wrap">
  {crumbs(lang, k)}
  <span class="label">{k}</span>
  <h1 class="display d-xl">{two_tone(h1, h2)}</h1>
  <p class="lead">{lead}</p>
</div></section>
'''


# ---------------------------------------------------------------- JSON-LD
def person_ld():
    return {
        "@context": "https://schema.org", "@type": "Person", "@id": DOMAIN + "/#person",
        "name": "Diana Noris", "alternateName": "Diana Noris Smith",
        "jobTitle": ["Actress", "Filmmaker", "Producer", "Screenwriter", "Visual artist"],
        "description": C.SEO["en"]["home"][1], "url": DOMAIN + "/", "image": img(MEDIA["portrait"], 1200),
        "knowsLanguage": ["en", "es"], "homeLocation": {"@type": "Place", "name": "Málaga, Spain"},
        "sameAs": [u for _, u in C.SOCIALS], "founder": {"@id": DOMAIN + "/#owsf"},
    }


def org_ld():
    return {"@context": "https://schema.org", "@type": "Organization", "@id": DOMAIN + "/#owsf", "name": "One Woman Show Films",
            "description": C.FILM["en"]["lead"], "founder": {"@id": DOMAIN + "/#person"}, "url": DOMAIN + path("en", "film")}


def breadcrumb_ld(lang, page, name):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": UI[lang]["home"], "item": DOMAIN + path(lang, "home")},
        {"@type": "ListItem", "position": 2, "name": name, "item": DOMAIN + path(lang, page)}]}


# ---------------------------------------------------------------- páginas
def build_home(lang):
    u, h = UI[lang], C.HOME[lang]
    banner_m = MEDIA["banner"]
    hero_img = (f'<picture><source media="(max-width:900px)" srcset="{img(MEDIA["hs4"], 900)}">'
                f'<img src="{img(banner_m, 1942)}" srcset="{img(banner_m, 1200)} 1200w, {img(banner_m, 1942)} 1942w" sizes="100vw" '
                f'alt="Diana Noris, actress, filmmaker and artist" width="1942" height="805" fetchpriority="high" decoding="async"></picture>')
    facts = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in h["facts"])
    bio = "".join(f"<p>{p}</p>" for p in h["bio"])
    disc = "".join(
        f'<a class="disc frame reveal" href="{path(lang, pg)}" style="--d:{i * .08:.2f}s">{icon(ic)}<h3 class="display d-sm">{t}</h3><p>{d}</p>'
        f'<span class="link-arrow">{u["read_more"]} {ARROW}</span></a>'
        for i, (ic, t, d, pg) in enumerate(h["disc"]))
    slides = "".join(
        f'<div class="slide frame">{tile(k, [400, 600, 900], "300px", f"Diana Noris headshot {n}", f"Diana Noris – {h["port_k"]} {n}")}</div>'
        for n, k in enumerate(["hs1", "hs2", "hs4", "hs5", "portrait"], 1))
    ring = "WATCH THE REEL • WATCH THE REEL • WATCH THE REEL • " if lang == "en" else "VER EL REEL • VER EL REEL • VER EL REEL • VER EL REEL • "
    reel = path(lang, "acting") + "#reel"
    press = "".join(
        f'<figure class="reveal" style="--d:{i * .08:.2f}s"><div class="frame">{tile(k, [400, 600, 900], "(max-width:900px) 100vw, 380px", cap, cap)}</div></figure>'
        for i, (k, cap) in enumerate([("showbiz1", "ShowBiz Magazine"), ("showbiz2", "ShowBiz Magazine"), ("mags", "Magazine covers" if lang == "en" else "Portadas de revistas")]))

    html = head(lang, "home", [person_ld(), org_ld()]) + header(lang, "home", False) + f'''
<main id="main">
<section class="hero">
  <div class="hero-media">{hero_img}</div>
  <div class="wrap hero-body">
    <span class="label">{u["roles"]}</span>
    <h1 class="display d-xl"><span class="sr-only">Diana Noris – </span>{two_tone("Bold, character-driven", "stories") if lang == "en" else two_tone("Historias valientes", "centradas en personajes")}</h1>
    <p class="lead">{C.SEO[lang]["home"][1]}</p>
    <div class="btn-row"><a class="btn" href="{reel}">{u["watch"]} {ARROW}</a><a class="btn outline" href="{path(lang, "contact")}">{u["contact_btn"]}</a></div>
    <div class="pills">{"".join(f"<span>{x}</span>" for x in u["pills"])}</div>
  </div>
</section>

<section class="sec" id="about"><div class="wrap about-grid">
  <div class="portrait frame reveal">{pic("portrait", [500, 800, 1100], "(max-width:900px) 100vw, 480px", "Diana Noris portrait", w=869, h=1086)}</div>
  <div class="about-text reveal" style="--d:.1s">
    <span class="label">{h["about_k"]}</span>
    <h2 class="display d-lg">{two_tone(h["about_h1"], h["about_h2"])}</h2>
    <div style="height:30px"></div>
    {bio}
    <dl class="facts">{facts}</dl>
    <a class="btn" href="{path(lang, "acting")}">{h["about_cta"]} {ARROW}</a>
  </div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sec-head reveal"><span class="label">{h["disc_k"]}</span><h2 class="display d-lg">{two_tone(h["disc_h1"], h["disc_h2"])}</h2></div>
  <div class="disc-grid">{disc}</div>
</div></section>

<section class="sec"><div class="wrap feat-grid">
  <div class="poster frame reveal">{pic("poster", [400, 600, 900], "(max-width:900px) 80vw, 460px", "A Latina in DC – poster")}</div>
  <div class="reveal" style="--d:.1s">
    <span class="label">{h["feat_k"]}</span>
    <h2 class="display d-xl">{two_tone(h["feat_h1"], "")}</h2>
    <div style="height:14px"></div>
    <span class="status">{h["feat_status"]}</span>
    <p class="lead" style="margin-bottom:32px">{h["feat_p"]}</p>
    <a class="btn" href="{path(lang, "film")}">{h["feat_cta"]} {ARROW}</a>
  </div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sec-head reveal"><span class="label">{h["port_k"]}</span><h2 class="display d-lg">{two_tone(h["port_h1"], h["port_h2"])}</h2></div>
  <div class="slider-wrap reveal" data-gallery>
    <div class="slider-nav"><button class="prev" type="button" aria-label="Previous">{CHEV_L}</button><button class="next" type="button" aria-label="Next">{CHEV_R}</button></div>
    <div class="slider">{slides}</div>
  </div>
</div></section>

<section class="sec reel-band" id="reel-band"><div class="wrap">
  <a class="spin reveal" href="{reel}" aria-label="{u["watch"]}"><svg class="ring" viewBox="0 0 200 200" aria-hidden="true"><defs><path id="ringp" d="M100,100 m-82,0 a82,82 0 1,1 164,0 a82,82 0 1,1 -164,0"/></defs><text font-family="Alumni Sans,sans-serif" font-size="21" font-weight="600" fill="currentColor"><textPath href="#ringp" textLength="505" lengthAdjust="spacing">{ring}</textPath></text></svg><span class="play">{PLAY}</span></a>
  <span class="label reveal">Reel</span>
  <h2 class="display d-lg reveal">{two_tone(h["reel_cta"], "")}</h2>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head reveal"><span class="label">{h["press_k"]}</span><h2 class="display d-lg">{two_tone(h["press_h1"], h["press_h2"])}</h2><p class="lead" style="margin-top:20px">{h["press_p"]}</p></div>
  <div class="press-grid" data-gallery>{press}</div>
  <div style="margin-top:44px"><a class="link-arrow" href="{path(lang, "press")}">{h["press_cta"]} {ARROW}</a></div>
</div></section>

{bigcta(lang, h["cta_h1"], h["cta_h2"], h["cta_p"])}
</main>

''' + footer(lang)
    write(path(lang, "home"), html)


def build_acting(lang):
    u, a = UI[lang], C.ACTING[lang]
    cast = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in a["cast"])
    credits = "".join(f"<li><span>{t}</span></li>" for t in a["credits"])
    srcs = "".join(f'<source src="{s}" type="video/mp4">' for s in C.REEL_SOURCES)
    hs = "".join(f'<div class="frame">{tile(k, [400, 600, 900], "(max-width:640px) 45vw, 220px", f"Diana Noris headshot {n}", f"Diana Noris – headshot {n}")}</div>'
                 for n, k in enumerate(["hs1", "hs2", "hs4", "hs5", "portrait"], 1))
    stills = "".join(f'<div class="frame">{tile(k, [500, 800, 960], "(max-width:640px) 100vw, 380px", f"Diana Noris still {n}", f"Diana Noris – still {n}", ratio="16/10")}</div>'
                     for n, k in enumerate(["still1", "still2", "still3"], 1))
    comm = "".join(f'<div class="frame">{tile(k, [500, 800, 960], "(max-width:640px) 100vw, 500px", "Shoe campaign", "Shoe campaign")}</div>' for k in ("shoe1", "shoe2"))
    html = head(lang, "acting", [person_ld(), breadcrumb_ld(lang, "acting", u["nav"]["acting"])], og_key="reelcover") + header(lang, "acting", True) + f'''
<main id="main">
{p_hero(lang, "acting", a["k"], a["h1"], a["h2"], a["lead"])}

<section class="sec" id="reel"><div class="wrap">
  <div class="sec-head reveal"><span class="label">{a["reel_k"]}</span><h2 class="display d-lg">{two_tone(a["reel_h"], "")}</h2></div>
  <div class="frame reveal"><div class="video"><video controls playsinline preload="none" poster="{img(MEDIA["reelcover"], 1200)}" aria-label="{esc(a["reel_note"])}">{srcs}</video></div></div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sec-head reveal"><span class="label">{a["cast_k"]}</span><h2 class="display d-lg">{two_tone(a["cast_h"], "")}</h2></div>
  <dl class="cast reveal">{cast}</dl>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head reveal"><span class="label">{a["credits_k"]}</span><h2 class="display d-lg">{two_tone(a["credits_h"], "")}</h2><p class="lead" style="margin-top:20px">{a["credits_p"]}</p></div>
  <ol class="credits reveal">{credits}</ol>
  <a class="btn outline reveal" href="{C.IMDB}" target="_blank" rel="noopener me">{a["imdb"]} {ARROW}</a>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sec-head reveal"><span class="label">{a["hs_k"]}</span><h2 class="display d-lg">{two_tone(a["hs_h"], "")}</h2></div>
  <div class="grid-5 reveal" data-gallery>{hs}</div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head reveal"><span class="label">{a["stills_k"]}</span><h2 class="display d-lg">{two_tone(a["stills_h"], "")}</h2></div>
  <div class="grid-3 reveal" data-gallery>{stills}</div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sec-head reveal"><span class="label">{a["comm_k"]}</span><h2 class="display d-lg">{two_tone(a["comm_h"], "")}</h2><p class="lead" style="margin-top:20px">{a["comm_p"]}</p></div>
  <div class="grid-2 reveal" data-gallery>{comm}</div>
</div></section>

{bigcta(lang, C.HOME[lang]["cta_h1"], C.HOME[lang]["cta_h2"], C.HOME[lang]["cta_p"])}
</main>

''' + footer(lang)
    write(path(lang, "acting"), html)


def build_film(lang):
    u, f = UI[lang], C.FILM[lang]
    about = "".join(f"<p>{p}</p>" for p in f["about"])
    posters = "".join(f'<div class="frame">{tile(k, [500, 800, 960], "(max-width:640px) 100vw, 380px", f"A Latina in DC – poster {n}", f"A Latina in DC {n}", ratio=r)}</div>'
                      for n, (k, r) in enumerate([("poster", "296/442"), ("poster2", "320/449"), ("owsf", "561/701")], 1))
    html = head(lang, "film", [org_ld(), breadcrumb_ld(lang, "film", u["nav"]["film"])], og_key="poster") + header(lang, "film", True) + f'''
<main id="main">
{p_hero(lang, "film", f["k"], f["h1"], "", f["lead"])}

<section class="sec"><div class="wrap"><div class="text-col reveal">{about}</div></div></section>

<section class="sec alt"><div class="wrap feat-grid">
  <div class="poster frame reveal">{pic("poster", [400, 600, 900], "(max-width:900px) 80vw, 460px", "A Latina in DC – poster")}</div>
  <div class="reveal" style="--d:.1s">
    <span class="label">{f["film_k"]}</span>
    <h2 class="display d-xl">{two_tone(f["film_h1"], "")}</h2>
    <div style="height:14px"></div>
    <span class="status">{f["film_status"]}</span>
    <p class="lead">{f["film_p"]}</p>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head reveal"><span class="label">{f["gallery_k"]}</span><h2 class="display d-lg">{two_tone(f["gallery_h"], "")}</h2></div>
  <div class="grid-3 reveal" data-gallery>{posters}</div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sec-head reveal"><span class="label">{f["dev_k"]}</span><h2 class="display d-lg">{two_tone(f["dev_h"], "")}</h2></div>
  <div class="soon reveal">{icon("film")}<p>{f["dev_p"]}</p></div>
</div></section>

{bigcta(lang, C.HOME[lang]["cta_h1"], C.HOME[lang]["cta_h2"], C.HOME[lang]["cta_p"])}
</main>

''' + footer(lang)
    write(path(lang, "film"), html)


def build_press(lang):
    u, p = UI[lang], C.PRESS[lang]
    covers = "".join(f'<figure><div class="frame">{tile(k, [400, 700, 1000], "(max-width:900px) 100vw, 380px", cap, cap)}</div><figcaption>{cap}</figcaption></figure>'
                     for k, cap in [("showbiz1", "ShowBiz Magazine"), ("showbiz2", "ShowBiz Magazine"), ("mags", "Magazine covers" if lang == "en" else "Portadas de revistas")])
    seen = f'<div class="frame" style="max-width:520px">{tile("seenon", [400, 700, 1000], "(max-width:640px) 100vw, 520px", p["seen_h"], p["seen_h"], ratio="1/1")}</div>'
    html = head(lang, "press", [breadcrumb_ld(lang, "press", u["nav"]["press"])], og_key="showbiz1") + header(lang, "press", True) + f'''
<main id="main">
{p_hero(lang, "press", p["k"], p["h1"], p["h2"], p["lead"])}
<section class="sec"><div class="wrap">
  <div class="sec-head reveal"><span class="label">{p["covers_h"]}</span></div>
  <div class="press-grid reveal" data-gallery>{covers}</div>
</div></section>
<section class="sec alt"><div class="wrap">
  <div class="sec-head reveal"><span class="label">{p["seen_h"]}</span></div>
  <div class="reveal" data-gallery>{seen}</div>
</div></section>
{bigcta(lang, C.HOME[lang]["cta_h1"], C.HOME[lang]["cta_h2"], C.HOME[lang]["cta_p"])}
</main>

''' + footer(lang)
    write(path(lang, "press"), html)


def build_artwork(lang):
    u, a = UI[lang], C.ARTWORK[lang]
    ps = "".join(f"<p>{x}</p>" for x in a["p"])
    html = head(lang, "artwork", [breadcrumb_ld(lang, "artwork", u["nav"]["artwork"])]) + header(lang, "artwork", True) + f'''
<main id="main">
{p_hero(lang, "artwork", a["k"], a["h1"], a["h2"], a["lead"])}
<section class="sec"><div class="wrap"><div class="text-col reveal">{ps}</div>
  <div class="soon reveal">{icon("art")}<p>{a["soon"]}</p></div>
</div></section>
{bigcta(lang, C.HOME[lang]["cta_h1"], C.HOME[lang]["cta_h2"], C.HOME[lang]["cta_p"])}
</main>

''' + footer(lang)
    write(path(lang, "artwork"), html)


def build_contact(lang):
    u, c = UI[lang], C.CONTACT[lang]
    ag = C.AGENCY
    phones = "".join(f'<li><span>{loc}</span><a href="tel:+1{num.replace(".", "")}">{num}</a></li>' for loc, num in ag["phones"])
    soc = "".join(f'<li><span>{name}</span><a href="{url}" target="_blank" rel="noopener me">{url.replace("https://www.", "").replace("https://", "")}</a></li>' for name, url in C.SOCIALS)
    html = head(lang, "contact", [breadcrumb_ld(lang, "contact", u["nav"]["contact"])]) + header(lang, "contact", True) + f'''
<main id="main">
{p_hero(lang, "contact", c["k"], c["h1"], c["h2"], c["lead"])}
<section class="sec"><div class="wrap">
  <div class="contact-grid">
    <div class="c-card frame reveal"><h3>{ag["name"]}</h3><span class="role">{ag["role"][lang]}</span><ul>{phones}</ul></div>
    <div class="c-card frame reveal" style="--d:.1s"><h3>{c["social_h"]}</h3><span class="role">Diana Noris</span><ul>{soc}</ul></div>
  </div>
  <div class="text-col reveal" style="margin-top:50px"><span class="label">{c["base_h"]}</span><p class="lead">{c["base"]}</p></div>
  <p class="script-note reveal">{c["note"]}</p>
</div></section>
</main>

''' + footer(lang)
    write(path(lang, "contact"), html)


def write_support():
    (SITE / "assets" / "img").mkdir(parents=True, exist_ok=True)
    (SITE / "assets" / "img" / "favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#0a0a0a"/><text x="32" y="46" font-family="Georgia,serif" font-style="italic" font-size="40" fill="#e5546f" text-anchor="middle">D</text></svg>', encoding="utf-8")
    if C.DEMO:
        (SITE / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
    else:
        (SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n", encoding="utf-8")
    body = ""
    for page in C.PAGES:
        for lang in ("en", "es"):
            body += (f"  <url><loc>{DOMAIN}{path(lang, page)}</loc>\n"
                     f'    <xhtml:link rel="alternate" hreflang="en" href="{DOMAIN}{path("en", page)}"/>\n'
                     f'    <xhtml:link rel="alternate" hreflang="es" href="{DOMAIN}{path("es", page)}"/>\n'
                     f'    <xhtml:link rel="alternate" hreflang="x-default" href="{DOMAIN}{path("en", page)}"/></url>\n')
    (SITE / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + body + "</urlset>\n", encoding="utf-8")
    (Path(__file__).resolve().parent / "Staticfile").write_text("root: site\n", encoding="utf-8")


if __name__ == "__main__":
    for lang in ("en", "es"):
        build_home(lang)
        build_acting(lang)
        build_film(lang)
        build_press(lang)
        build_artwork(lang)
        build_contact(lang)
    write_support()
    print("built: 12 pages")
