"""Contenido de diananoris.com (EN principal / ES). Edita aquí textos, enlaces e imágenes y ejecuta: python build.py

Los textos salen de la web actual de Diana (https://www.diananoris.com), de su ficha de casting y de su biografía.
Las imágenes se enlazan de momento desde su Wix actual (demo). Para producción hay que sustituirlas por archivos propios en alta resolución.
# TODO Diana: confirmar todos los textos y datos (los de español son una traducción propia).
"""

DOMAIN = "https://www.diananoris.com"
DEMO = True  # True -> la demo no se indexa (noindex). Poner False al publicar la web definitiva.

# --------------------------------------------------------------- redes y enlaces
INSTAGRAM = "https://www.instagram.com/what_dianadid"
YOUTUBE = "https://www.youtube.com/user/diananoris"
FACEBOOK = "https://www.facebook.com/Diananoris"
IMDB = "https://www.imdb.com/name/nm4434619/"
ACTORS_ACCESS = "https://resumes.actorsaccess.com/Diananoris"
SOCIALS = [("Instagram", INSTAGRAM), ("YouTube", YOUTUBE), ("Facebook", FACEBOOK), ("IMDb", IMDB), ("Actors Access", ACTORS_ACCESS)]

# --------------------------------------------------------------- imágenes (Wix, prefijo 761d7f_)
WIX = "https://static.wixstatic.com/media/761d7f_"


def img_png(media_id, w):
    """Igual que img() pero conserva la transparencia (para logos)."""
    return f"{WIX}{media_id}/v1/fit/w_{w},h_{w},al_c,q_90,enc_auto/logo.png"


def img(media_id, w, h=None, mode="fit", q=82):
    """URL optimizada del servidor de imágenes de Wix (sirve webp/avif según el navegador)."""
    h = h or w
    return f"{WIX}{media_id}/v1/{mode}/w_{w},h_{h},al_c,q_{q},enc_auto/diana-noris.jpg"


MEDIA = {
    "banner": "e3ddfbd003c7409092f88d5a5706c077~mv2.png",      # banner panorámico (lleva el logo manuscrito)
    "portrait": "db657863393d44b791746e5f69bff1b9~mv2.png",    # retrato de la portada
    "hs1": "26dbe0ba672648afa5e4bf8531262e92~mv2.png",
    "hs2": "ad98e52584c0473da0e1ed69a8e13f4c~mv2.png",
    "hs4": "7cb787dfd9a3433c86d7c739c0b083e4~mv2.png",
    "hs5": "0ca631e2c984486b8e7ca5976470821e~mv2.png",
    "reelcover": "2fd7d8d6f3da430e905e577629385d24~mv2.png",    # collage de headshots con el logo
    "still1": "a99d5efad9cb4eaca64838cbf5d8212a~mv2.jpg",
    "still2": "82faa72f3a3545fcb72029cddd737d78~mv2.jpg",
    "still3": "6bcf5c908b1d40abada372de439376fb~mv2.jpg",
    "poster": "e4368dbc90f2482bbbe32c4d626e396e~mv2.jpg",       # póster de A Latina in DC
    "poster2": "f420b79bc6f94de79f0c689847e1b068~mv2.png",      # cartel de texto de A Latina in DC
    "shoe1": "2de2b078fcab4d86b036bf43deb039e3~mv2.jpg",
    "shoe2": "afb2bfb8d9c94333b6807653f8d6f478~mv2.jpg",
    "showbiz1": "14919abba77540d98bd66a5368b3a624~mv2.png",
    "showbiz2": "b302587656644e28ba8a9ee785a7ede0~mv2.png",
    "mags": "a1249fbba62f4d8ca08b9976cef40cbc~mv2.png",
    "seenon": "6f28c3729b2e47128cefef2315e9bfc3~mv2.jpg",
    "owsf": "f3bfc64ee5ec4246be75e8de65f106a2~mv2.png",
    "imdbcard": "0010880ca42741d096159aade930170d~mv2.png",     # tarjeta de IMDb Pro
    "logo_imdb": "e29a2896a6c84f5a95ab6398655bd858~mv2.png",
    "logo_aa": "1fbca671225a4599bf58f1a1957766f2~mv2.png",      # Actors Access
}
# Vídeo del reel (Wix Video, sin sonido de portada). Se prueba la calidad más alta primero.
REEL_SOURCES = [
    "https://video.wixstatic.com/video/11062b_62f0356712544a87b392417662c4658d/720p/mp4/file.mp4",
    "https://video.wixstatic.com/video/11062b_62f0356712544a87b392417662c4658d/480p/mp4/file.mp4",
]

# --------------------------------------------------------------- representación (copiado de su web actual)
AGENCY = {
    "name": "The Wayne Agency",
    "role": {"en": "Theatrical representation", "es": "Representación teatral"},
    "phones": [("TWA", "804.661.5354"), ("VA", "404.556.9211"), ("ATL", "310.492.5994")],
    # TODO Diana: confirmar representación vigente y qué datos de contacto publicar (email, agencia en España...).
}

# --------------------------------------------------------------- rutas
PAGES = ["home", "acting", "film", "press", "artwork", "contact"]
SLUG = {
    "en": {"home": "", "acting": "acting", "film": "film", "press": "press", "artwork": "artwork", "contact": "contact"},
    "es": {"home": "", "acting": "actuacion", "film": "cine", "press": "prensa", "artwork": "arte", "contact": "contacto"},
}


def path(lang, page):
    s = SLUG[lang][page]
    base = "/" if lang == "en" else "/es/"
    return base + (s + "/" if s else "")


# --------------------------------------------------------------- textos de interfaz
UI = {
    "en": {
        "locale": "en_US", "skip": "Skip to content", "menu": "Menu",
        "nav": {"acting": "Acting", "film": "One Woman Show Films", "press": "Press", "artwork": "Artwork", "contact": "Contact"},
        "watch": "Watch reel", "contact_btn": "Contact", "home": "Home",
        "roles": "Actress · Filmmaker · Artist",
        "pills": ["Bilingual EN / ES", "Spain · New York"],
        "read_more": "Learn more", "view": "View",
        "footer_cta": "Let's work together", "footer_sub": "Acting · Film · Collaborations",
        "rights": "All rights reserved.", "follow": "Follow", "explore": "Explore", "reach": "Contact",
        "legal_demo": "Preview version, not published.",
        "lang_name": "English",
    },
    "es": {
        "locale": "es_ES", "skip": "Saltar al contenido", "menu": "Menú",
        "nav": {"acting": "Actuación", "film": "One Woman Show Films", "press": "Prensa", "artwork": "Arte", "contact": "Contacto"},
        "watch": "Ver reel", "contact_btn": "Contacto", "home": "Inicio",
        "roles": "Actriz · Filmmaker · Artista",
        "pills": ["Bilingüe ES / EN", "España · Nueva York"],
        "read_more": "Saber más", "view": "Ver",
        "footer_cta": "Trabajemos juntos", "footer_sub": "Actuación · Cine · Colaboraciones",
        "rights": "Todos los derechos reservados.", "follow": "Sígueme", "explore": "Explorar", "reach": "Contacto",
        "legal_demo": "Versión de vista previa, no publicada.",
        "lang_name": "Español",
    },
}

# --------------------------------------------------------------- páginas
SEO = {
    "en": {
        "home": ("Diana Noris | Bilingual Actress, Writer & Filmmaker – Spain & New York",
                 "Diana Noris is a bilingual actress, writer and filmmaker working between Spain and New York, and founder of One Woman Show Films."),
        "acting": ("Acting | Diana Noris – Bilingual Actress (English / Spanish)",
                   "Reel, headshots and casting profile of Diana Noris, a bilingual (English/Spanish) actress working on Spanish and European productions."),
        "film": ("Film | One Woman Show Films & A Latina in DC – Diana Noris",
                 "One Woman Show Films, the independent production company founded by Diana Noris, and the film A Latina in DC, coming to festivals worldwide."),
        "press": ("Press | Diana Noris", "Press and magazine covers featuring actress and filmmaker Diana Noris."),
        "artwork": ("Artwork | Diana Noris – Mixed-media & Whimsical Art", "Mixed-media and whimsical art by Diana Noris, former owner of an art gallery in Miami."),
        "contact": ("Contact | Diana Noris", "Representation and contact details for actress and filmmaker Diana Noris."),
    },
    "es": {
        "home": ("Diana Noris | Actriz bilingüe, guionista y filmmaker – España y Nueva York",
                 "Diana Noris es una actriz bilingüe, guionista y filmmaker que trabaja entre España y Nueva York, y fundadora de One Woman Show Films."),
        "acting": ("Actuación | Diana Noris – Actriz bilingüe (español / inglés)",
                   "Reel, fotos de actriz y ficha de casting de Diana Noris, actriz bilingüe (español/inglés) que trabaja en producciones españolas y europeas."),
        "film": ("Cine | One Woman Show Films y A Latina in DC – Diana Noris",
                 "One Woman Show Films, la productora independiente fundada por Diana Noris, y la película A Latina in DC, en camino a festivales de todo el mundo."),
        "press": ("Prensa | Diana Noris", "Prensa y portadas de revistas con la actriz y cineasta Diana Noris."),
        "artwork": ("Arte | Diana Noris – Técnica mixta y arte fantasioso", "Arte de técnica mixta y estilo fantasioso de Diana Noris, antigua propietaria de una galería de arte en Miami."),
        "contact": ("Contacto | Diana Noris", "Representación y datos de contacto de la actriz y cineasta Diana Noris."),
    },
}

HOME = {
    "en": {
        "hero_h1": ("Bilingual storyteller", "across cultures"),
        "hero_lead": "Actress, filmmaker and artist working between Spain and New York, creating stories that connect across cultures.",
        "about_k": "About Diana",
        "about_h1": "A bilingual actress, writer and filmmaker",
        "about_h2": "working between Spain and New York",
        "bio": [
            "Diana Noris is a bilingual Puerto Rican actress, writer, producer, filmmaker, director, and visual artist currently based in Málaga, Spain. She is the founder of One Woman Show Films, an independent production company dedicated to developing bold, character-driven stories through a female and multicultural perspective.",
            "As a filmmaker, Diana is drawn to stories that blend humor with emotional honesty while exploring identity, relationships, reinvention, and the social and cultural pressures women face. Her work is particularly focused on creating layered female characters and telling stories for women whose experiences and complexities are still too often underrepresented on screen. Through One Woman Show Films, she continues to develop projects designed to connect with audiences across cultures and generations.",
            "In addition to her work in film and acting, Diana is an accomplished visual artist specializing in mixed-media and whimsical art. She previously owned and operated an art gallery in Miami, Florida, and her artwork has been collected and sold to buyers around the world. Her background as an artist continues to influence her filmmaking, particularly her approach to visual storytelling, composition, color, and character.",
            "Now living in Spain, Diana continues to expand her work internationally across acting, filmmaking, producing, writing, directing, and visual art, bringing together the different creative disciplines that have shaped her career.",
        ],
        "bio_credit": "IMDb mini biography by: Leo Samuel",
        "facts": [("Languages", "English · Spanish"), ("Working in", "Spain · New York"), ("Production company", "One Woman Show Films")],
        "about_cta": "Acting profile",
        "disc_k": "What I do", "disc_h1": "Four disciplines,", "disc_h2": "one point of view",
        "disc": [
            ("acting", "Acting", "Bilingual actress (English / Spanish) working on Spanish, European and U.S. productions.", "acting"),
            ("film", "Filmmaking", "Founder of One Woman Show Films, developing and producing her own projects.", "film"),
            ("pen", "Writing & producing", "Layered female characters and stories for women whose experiences are still underrepresented on screen.", "film"),
            ("art", "Visual art", "Mixed-media and whimsical art, collected by buyers around the world. Former gallery owner in Miami.", "artwork"),
        ],
        "feat_k": "Featured film", "feat_h1": "A Latina in DC", "feat_h2": "by One Woman Show Films",
        "feat_p": "An independent production by One Woman Show Films, the company founded by Diana Noris to tell bold, character-driven stories through a female and multicultural perspective.",
        "feat_status": "Coming to festivals worldwide",
        "feat_cta": "Discover the film",
        "port_k": "Portfolio", "port_h1": "Headshots", "port_h2": "and looks",
        "reel_cta": "Watch the reel",
        "press_k": "Press", "press_h1": "In the", "press_h2": "spotlight",
        "press_p": "Magazine covers and press appearances.",
        "press_cta": "See the press",
        "cta_k": "Collaborate", "cta_h1": "Have a project", "cta_h2": "in mind?",
        "cta_p": "Currently working between Spain and New York. For acting, collaborations and press inquiries, please contact representation or reach out on social media.",
    },
    "es": {
        "hero_h1": ("Narradora bilingüe", "entre culturas"),
        "hero_lead": "Actriz, filmmaker y artista que trabaja entre España y Nueva York, creando historias que conectan culturas.",
        "about_k": "Sobre Diana",
        "about_h1": "Una actriz, guionista y filmmaker bilingüe",
        "about_h2": "que trabaja entre España y Nueva York",
        "bio": [
            "Diana Noris es una actriz, guionista, productora, cineasta, directora y artista visual puertorriqueña y bilingüe, actualmente afincada en Málaga, España. Es la fundadora de One Woman Show Films, una productora independiente dedicada a desarrollar historias valientes, centradas en personajes, desde una perspectiva femenina y multicultural.",
            "Como cineasta, a Diana le atraen las historias que combinan humor y honestidad emocional mientras exploran la identidad, las relaciones, la reinvención y las presiones sociales y culturales que enfrentan las mujeres. Su trabajo se centra especialmente en crear personajes femeninos con capas y en contar historias para mujeres cuyas experiencias y complejidades siguen estando, con demasiada frecuencia, poco representadas en pantalla. A través de One Woman Show Films, continúa desarrollando proyectos pensados para conectar con públicos de distintas culturas y generaciones.",
            "Además de su trabajo en cine y actuación, Diana es una artista visual consumada, especializada en técnica mixta y en un estilo de arte fantasioso. Fue propietaria y gestora de una galería de arte en Miami, Florida, y su obra ha sido adquirida por compradores de todo el mundo. Su formación como artista sigue influyendo en su cine, especialmente en su manera de entender la narración visual, la composición, el color y los personajes.",
            "Ahora que vive en España, Diana sigue ampliando su trabajo a nivel internacional en actuación, cine, producción, guion, dirección y arte visual, uniendo las distintas disciplinas creativas que han marcado su carrera.",
        ],
        "bio_credit": "Minibiografía de IMDb por: Leo Samuel",
        "facts": [("Idiomas", "Español · Inglés"), ("Trabaja en", "España · Nueva York"), ("Productora", "One Woman Show Films")],
        "about_cta": "Perfil de actriz",
        "disc_k": "Lo que hago", "disc_h1": "Cuatro disciplinas,", "disc_h2": "una sola mirada",
        "disc": [
            ("acting", "Actuación", "Actriz bilingüe (español / inglés) que trabaja en producciones españolas y europeas.", "acting"),
            ("film", "Dirección y cine", "Fundadora de One Woman Show Films, desarrolla y produce sus propios proyectos.", "film"),
            ("pen", "Guion y producción", "Personajes femeninos con capas e historias para mujeres cuyas experiencias siguen poco representadas en pantalla.", "film"),
            ("art", "Arte visual", "Arte de técnica mixta y estilo fantasioso, adquirido por compradores de todo el mundo. Antigua propietaria de una galería en Miami.", "artwork"),
        ],
        "feat_k": "Película destacada", "feat_h1": "A Latina in DC", "feat_h2": "de One Woman Show Films",
        "feat_p": "Una producción independiente de One Woman Show Films, la compañía fundada por Diana Noris para contar historias valientes, centradas en personajes, desde una perspectiva femenina y multicultural.",
        "feat_status": "En camino a festivales de todo el mundo",
        "feat_cta": "Descubre la película",
        "port_k": "Portfolio", "port_h1": "Fotos de actriz", "port_h2": "y looks",
        "reel_cta": "Ver el reel",
        "press_k": "Prensa", "press_h1": "En", "press_h2": "portada",
        "press_p": "Portadas de revistas y apariciones en prensa.",
        "press_cta": "Ver la prensa",
        "cta_k": "Colabora", "cta_h1": "¿Tienes un proyecto", "cta_h2": "en mente?",
        "cta_p": "Actualmente trabaja entre España y Nueva York. Para actuación, colaboraciones y consultas de prensa, contacta con su representación o escribe por las redes sociales.",
    },
}

ACTING = {
    "en": {
        "k": "Acting", "h1": "Bilingual actress", "h2": "English · Spanish",
        "lead": "Working in both English and Spanish, Diana brings a cross-cultural perspective to every role, with a focus on character-driven storytelling that feels both intimate and universal.",
        "reel_k": "Reel", "reel_h": "Watch the reel", "reel_note": "Acting reel",
        "cast_k": "Casting profile", "cast_h": "At a glance",
        "cast": [("Height", "5'7\" / 170 cm"), ("Eye color", "Green"), ("Hair", "Auburn, long"), ("Languages", "English, Spanish (bilingual)"), ("Working between", "Spain · New York")],
        "credits_k": "Credits", "credits_h": "Selected projects",
        "credits_p": "Titles listed on her IMDb profile. Full credits and roles on IMDb.",
        "credits": ["A Latina in DC", "Douglas Is Cancelled", "Jekka Trilogy", "Casa Caracol"],
        "imdb": "View on IMDb",
        "hs_k": "Portfolio", "hs_h": "Headshots",
        "stills_k": "On set", "stills_h": "Stills and behind the scenes",
        "comm_k": "Commercial", "comm_h": "Commercial work",
        "comm_p": "Fashion and advertising campaigns, including a shoe campaign.",
    },
    "es": {
        "k": "Actuación", "h1": "Actriz bilingüe", "h2": "Español · Inglés",
        "lead": "Trabajando en español e inglés, Diana aporta una mirada intercultural a cada papel, con foco en una narrativa centrada en los personajes, íntima y universal a la vez.",
        "reel_k": "Reel", "reel_h": "Ver el reel", "reel_note": "Reel de actuación",
        "cast_k": "Ficha de casting", "cast_h": "De un vistazo",
        "cast": [("Altura", "1,70 m (5'7\")"), ("Ojos", "Verdes"), ("Pelo", "Caoba, largo"), ("Idiomas", "Español, inglés (bilingüe)"), ("Trabaja entre", "España · Nueva York")],
        "credits_k": "Créditos", "credits_h": "Proyectos destacados",
        "credits_p": "Títulos de su perfil de IMDb. Créditos completos y papeles en IMDb.",
        "credits": ["A Latina in DC", "Douglas Is Cancelled", "Jekka Trilogy", "Casa Caracol"],
        "imdb": "Ver en IMDb",
        "hs_k": "Portfolio", "hs_h": "Fotos de actriz",
        "stills_k": "En el set", "stills_h": "Fotogramas y detrás de cámaras",
        "comm_k": "Publicidad", "comm_h": "Trabajo comercial",
        "comm_p": "Campañas de moda y publicidad, incluida una campaña de zapatos.",
    },
}

FILM = {
    "en": {
        "k": "Film", "h1": "One Woman Show Films", "h2": "Bold, character-driven stories",
        "lead": "An independent production company founded by Diana Noris, dedicated to telling bold, character-driven stories through a female and multicultural perspective.",
        "about": [
            "Her work as a filmmaker blends humor with emotionally honest storytelling, exploring identity, relationships, reinvention and the social and cultural pressures women face.",
            "Diana is particularly focused on creating layered female characters and telling stories for women whose experiences and complexities are still too often underrepresented on screen. Through One Woman Show Films she continues to develop projects designed to connect with audiences across cultures and generations.",
            "She continues to develop and produce her own projects through One Woman Show Films.",
        ],
        "film_k": "Now showing", "film_h1": "A Latina in DC", "film_status": "Coming to festivals worldwide",
        "film_p": "A One Woman Show Films production.",
        "gallery_k": "Gallery", "gallery_h": "Posters",
        "dev_k": "In development", "dev_h": "Projects in development",
        "dev_p": "Diana continues to develop new projects. Details will be announced here.",
    },
    "es": {
        "k": "Cine", "h1": "One Woman Show Films", "h2": "Historias valientes, centradas en los personajes",
        "lead": "Una productora independiente fundada por Diana Noris, dedicada a contar historias valientes, centradas en personajes, desde una perspectiva femenina y multicultural.",
        "about": [
            "Su trabajo como cineasta combina el humor con una narrativa emocionalmente honesta, y explora la identidad, las relaciones, la reinvención y las presiones sociales y culturales que enfrentan las mujeres.",
            "Diana se centra especialmente en crear personajes femeninos con capas y en contar historias para mujeres cuyas experiencias y complejidades siguen estando poco representadas en pantalla. A través de One Woman Show Films continúa desarrollando proyectos pensados para conectar con públicos de distintas culturas y generaciones.",
            "Sigue desarrollando y produciendo sus propios proyectos a través de One Woman Show Films.",
        ],
        "film_k": "En cartel", "film_h1": "A Latina in DC", "film_status": "En camino a festivales de todo el mundo",
        "film_p": "Una producción de One Woman Show Films.",
        "gallery_k": "Galería", "gallery_h": "Carteles",
        "dev_k": "En desarrollo", "dev_h": "Proyectos en desarrollo",
        "dev_p": "Diana sigue desarrollando nuevos proyectos. Los detalles se anunciarán aquí.",
    },
}

PRESS = {
    "en": {"k": "Press", "h1": "In the", "h2": "spotlight", "lead": "Magazine covers and press appearances featuring Diana Noris.",
           "covers_h": "Covers", "seen_h": "As seen on"},
    "es": {"k": "Prensa", "h1": "En", "h2": "portada", "lead": "Portadas de revistas y apariciones en prensa de Diana Noris.",
           "covers_h": "Portadas", "seen_h": "Visto en"},
}

ARTWORK = {
    "en": {"k": "Artwork", "h1": "Mixed-media", "h2": "and whimsical art",
           "lead": "In addition to her work in film and acting, Diana is an accomplished visual artist specializing in mixed-media and whimsical art.",
           "p": ["She previously owned and operated an art gallery in Miami, Florida, and her artwork has been collected and sold to buyers around the world.",
                 "Her background as an artist continues to influence her filmmaking, particularly her approach to visual storytelling, composition, color and character."],
           "soon": "Gallery coming soon"},
    "es": {"k": "Arte", "h1": "Técnica mixta", "h2": "y arte fantasioso",
           "lead": "Además de su trabajo en cine y actuación, Diana es una artista visual consumada, especializada en técnica mixta y arte de estilo fantasioso.",
           "p": ["Fue propietaria y gestora de una galería de arte en Miami, Florida, y su obra ha sido adquirida por compradores de todo el mundo.",
                 "Su formación como artista sigue influyendo en su cine, especialmente en su manera de entender la narración visual, la composición, el color y los personajes."],
           "soon": "Galería próximamente"},
}

CONTACT = {
    "en": {"k": "Contact", "h1": "Let's", "h2": "connect",
           "lead": "For acting, collaborations and press, please reach out through representation or social media.",
           "rep_h": "Representation", "social_h": "Social media", "base_h": "Working between",
           "base": "Working between Spain and New York.",
           "note": "Great to meet you. Gracias!"},
    "es": {"k": "Contacto", "h1": "Hablemos", "h2": "",
           "lead": "Para actuación, colaboraciones y prensa, contacta a través de su representación o de las redes sociales.",
           "rep_h": "Representación", "social_h": "Redes sociales", "base_h": "Trabaja entre",
           "base": "Trabaja entre España y Nueva York.",
           "note": "Encantada de conocerte. ¡Gracias!"},
}


# --------------------------------------------------------------- headshots propios (alojados en site/assets/img/headshots/)
# (nombre del archivo, número del archivo original, textos alternativos). Se generan con process_headshots.py
HEADSHOTS = [
    ("hs-01", 16, {"en": "Diana Noris headshot in a burgundy leather jacket", "es": "Diana Noris, foto de actriz con chaqueta de cuero burdeos"}),
    ("hs-02", 14, {"en": "Diana Noris headshot in a black leather jacket and mustard turtleneck", "es": "Diana Noris, foto de actriz con chaqueta de cuero negra y cuello alto mostaza"}),
    ("hs-03", 15, {"en": "Diana Noris headshot in a black blazer and white top", "es": "Diana Noris, foto de actriz con blazer negro y top blanco"}),
    ("hs-04", 17, {"en": "Diana Noris headshot in a grey tank top on a dark blue background", "es": "Diana Noris, foto de actriz con camiseta gris sobre fondo azul oscuro"}),
    ("hs-05", 19, {"en": "Diana Noris headshot in a white shirt", "es": "Diana Noris, foto de actriz con camisa blanca"}),
    ("hs-06", 18, {"en": "Diana Noris headshot with her hand on her chin", "es": "Diana Noris, foto de actriz con la mano en la barbilla"}),
    ("hs-07", 20, {"en": "Diana Noris headshot in a black blazer, three-quarter view", "es": "Diana Noris, foto de actriz con blazer negro, de tres cuartos"}),
]


# --------------------------------------------------------------- vídeos de YouTube (canal de Diana Noris Smith)
VIDEOS = {
    "reel_es": {"id": "jsaj-kCF05c", "title": {"en": "Spanish reel", "es": "Reel en español"}, "seconds": 242, "date": "2026-10-09"},
    "reel_en": {"id": "69_9jvr76iQ", "title": {"en": "English reel", "es": "Reel en inglés"}, "seconds": 202, "date": "2026-10-11"},
    "theatre": {"id": "ikacfvPiPQc", "title": {"en": "Spanish theatre", "es": "Teatro en español"}, "seconds": 198, "date": "2023-10-30"},
}
# El reel grande de cada idioma es el de ese idioma; debajo van los demás vídeos.
FEATURED = {"en": "reel_en", "es": "reel_es"}
MORE = {"en": ["reel_es", "theatre"], "es": ["reel_en", "theatre"]}
MORE_LABEL = {"en": "More videos", "es": "Más vídeos"}
