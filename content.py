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
IMDB = "https://www.imdb.com/find/?q=Diana%20Noris%20Smith"  # TODO Diana: enlace directo a su perfil de IMDb
SOCIALS = [("Instagram", INSTAGRAM), ("YouTube", YOUTUBE), ("Facebook", FACEBOOK), ("IMDb", IMDB)]

# --------------------------------------------------------------- imágenes (Wix, prefijo 761d7f_)
WIX = "https://static.wixstatic.com/media/761d7f_"


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
        "nav": {"acting": "Acting", "film": "Film", "press": "Press", "artwork": "Artwork", "contact": "Contact"},
        "watch": "Watch reel", "contact_btn": "Contact", "home": "Home",
        "roles": "Actress · Writer · Producer · Director · Visual artist",
        "pills": ["Bilingual EN / ES", "Puerto Rican", "Málaga · Madrid · London"],
        "read_more": "Learn more", "view": "View",
        "footer_cta": "Let's work together", "footer_sub": "Acting · Film · Collaborations",
        "rights": "All rights reserved.", "follow": "Follow", "explore": "Explore", "reach": "Contact",
        "legal_demo": "Preview version, not published.",
        "lang_name": "English",
    },
    "es": {
        "locale": "es_ES", "skip": "Saltar al contenido", "menu": "Menú",
        "nav": {"acting": "Actuación", "film": "Cine", "press": "Prensa", "artwork": "Arte", "contact": "Contacto"},
        "watch": "Ver reel", "contact_btn": "Contacto", "home": "Inicio",
        "roles": "Actriz · Guionista · Productora · Directora · Artista visual",
        "pills": ["Bilingüe ES / EN", "Puertorriqueña", "Málaga · Madrid · Londres"],
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
        "home": ("Diana Noris | Actress, Filmmaker & Visual Artist in Málaga",
                 "Diana Noris is a bilingual Puerto Rican actress, writer, producer and filmmaker based in Málaga, Spain, and founder of One Woman Show Films."),
        "acting": ("Acting | Diana Noris – Bilingual Actress (English / Spanish)",
                   "Reel, headshots and casting profile of Diana Noris, a bilingual (English/Spanish) actress working on Spanish and European productions."),
        "film": ("Film | One Woman Show Films & A Latina in DC – Diana Noris",
                 "One Woman Show Films, the independent production company founded by Diana Noris, and the film A Latina in DC, coming to festivals worldwide."),
        "press": ("Press | Diana Noris", "Press and magazine covers featuring actress and filmmaker Diana Noris."),
        "artwork": ("Artwork | Diana Noris – Mixed-media & Whimsical Art", "Mixed-media and whimsical art by Diana Noris, former owner of an art gallery in Miami."),
        "contact": ("Contact | Diana Noris", "Representation and contact details for actress and filmmaker Diana Noris."),
    },
    "es": {
        "home": ("Diana Noris | Actriz, cineasta y artista visual en Málaga",
                 "Diana Noris es una actriz, guionista, productora y cineasta puertorriqueña y bilingüe afincada en Málaga, y fundadora de One Woman Show Films."),
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
        "about_k": "About Diana",
        "about_h1": "A bilingual actress, writer and filmmaker",
        "about_h2": "telling bold stories from Málaga to Madrid and London",
        "bio": [
            "Diana Noris is a bilingual Puerto Rican actress, writer, producer and filmmaker based in Málaga, Spain. She is the founder of One Woman Show Films, an independent production company dedicated to telling bold, character-driven stories through a female and multicultural perspective.",
            "Her work blends humor with emotionally honest storytelling, exploring identity, relationships, reinvention and the social and cultural pressures women face. She is particularly interested in creating stories that connect with audiences across cultures and generations.",
            "As an actress and filmmaker, she is currently working on Spanish and European productions, with projects taking her between Málaga, Madrid and London. She is also developing and filming several of her own projects while collaborating on other international productions.",
        ],
        "facts": [("Languages", "English · Spanish"), ("Based in", "Málaga, Spain"), ("Production company", "One Woman Show Films")],
        "about_cta": "Acting profile",
        "disc_k": "What I do", "disc_h1": "Four disciplines,", "disc_h2": "one point of view",
        "disc": [
            ("acting", "Acting", "Bilingual actress (English / Spanish) working on Spanish and European productions.", "acting"),
            ("film", "Filmmaking", "Founder of One Woman Show Films, developing and filming her own projects between Málaga and Madrid.", "film"),
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
        "cta_k": "Collaborate", "cta_h1": "Looking for a bilingual actress", "cta_h2": "or a co-producer?",
        "cta_p": "For acting, projects, collaborations or press, get in touch through representation or social media.",
    },
    "es": {
        "about_k": "Sobre Diana",
        "about_h1": "Una actriz, guionista y cineasta bilingüe",
        "about_h2": "que cuenta historias valientes de Málaga a Madrid y Londres",
        "bio": [
            "Diana Noris es una actriz, guionista, productora y cineasta puertorriqueña y bilingüe afincada en Málaga, España. Es la fundadora de One Woman Show Films, una productora independiente dedicada a contar historias valientes, centradas en personajes, desde una perspectiva femenina y multicultural.",
            "Su trabajo combina el humor con una narrativa emocionalmente honesta, y explora la identidad, las relaciones, la reinvención y las presiones sociales y culturales que enfrentan las mujeres. Le interesa especialmente crear historias que conecten con públicos de distintas culturas y generaciones.",
            "Como actriz y cineasta, trabaja actualmente en producciones españolas y europeas, con proyectos que la llevan entre Málaga, Madrid y Londres. También desarrolla y rueda varios proyectos propios mientras colabora en otras producciones internacionales.",
        ],
        "facts": [("Idiomas", "Español · Inglés"), ("Residencia", "Málaga, España"), ("Productora", "One Woman Show Films")],
        "about_cta": "Perfil de actriz",
        "disc_k": "Lo que hago", "disc_h1": "Cuatro disciplinas,", "disc_h2": "una sola mirada",
        "disc": [
            ("acting", "Actuación", "Actriz bilingüe (español / inglés) que trabaja en producciones españolas y europeas.", "acting"),
            ("film", "Dirección y cine", "Fundadora de One Woman Show Films, desarrolla y rueda sus propios proyectos entre Málaga y Madrid.", "film"),
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
        "cta_k": "Colabora", "cta_h1": "¿Buscas una actriz bilingüe", "cta_h2": "o una coproductora?",
        "cta_p": "Para actuación, proyectos, colaboraciones o prensa, contacta a través de su representación o de las redes sociales.",
    },
}

ACTING = {
    "en": {
        "k": "Acting", "h1": "Bilingual actress", "h2": "English · Spanish",
        "lead": "Working in both English and Spanish, Diana brings a cross-cultural perspective to every role, with a focus on character-driven storytelling that feels both intimate and universal.",
        "reel_k": "Reel", "reel_h": "Watch the reel", "reel_note": "Acting reel",
        "cast_k": "Casting profile", "cast_h": "At a glance",
        "cast": [("Height", "5'7\" / 170 cm"), ("Eye color", "Green"), ("Hair", "Auburn, long"), ("Languages", "English, Spanish (bilingual)"), ("Based in", "Málaga · Madrid · London")],
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
        "cast": [("Altura", "1,70 m (5'7\")"), ("Ojos", "Verdes"), ("Pelo", "Caoba, largo"), ("Idiomas", "Español, inglés (bilingüe)"), ("Residencia", "Málaga · Madrid · Londres")],
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
            "She is currently developing and filming several of her own projects between Málaga and Madrid.",
        ],
        "film_k": "Now showing", "film_h1": "A Latina in DC", "film_status": "Coming to festivals worldwide",
        "film_p": "A One Woman Show Films production.",
        "gallery_k": "Gallery", "gallery_h": "Posters",
        "dev_k": "In development", "dev_h": "Projects in development",
        "dev_p": "Diana is developing new projects between Málaga and Madrid. Details will be announced here.",
    },
    "es": {
        "k": "Cine", "h1": "One Woman Show Films", "h2": "Historias valientes, centradas en los personajes",
        "lead": "Una productora independiente fundada por Diana Noris, dedicada a contar historias valientes, centradas en personajes, desde una perspectiva femenina y multicultural.",
        "about": [
            "Su trabajo como cineasta combina el humor con una narrativa emocionalmente honesta, y explora la identidad, las relaciones, la reinvención y las presiones sociales y culturales que enfrentan las mujeres.",
            "Diana se centra especialmente en crear personajes femeninos con capas y en contar historias para mujeres cuyas experiencias y complejidades siguen estando poco representadas en pantalla. A través de One Woman Show Films continúa desarrollando proyectos pensados para conectar con públicos de distintas culturas y generaciones.",
            "Actualmente desarrolla y rueda varios proyectos propios entre Málaga y Madrid.",
        ],
        "film_k": "En cartel", "film_h1": "A Latina in DC", "film_status": "En camino a festivales de todo el mundo",
        "film_p": "Una producción de One Woman Show Films.",
        "gallery_k": "Galería", "gallery_h": "Carteles",
        "dev_k": "En desarrollo", "dev_h": "Proyectos en desarrollo",
        "dev_p": "Diana desarrolla nuevos proyectos entre Málaga y Madrid. Los detalles se anunciarán aquí.",
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
           "rep_h": "Representation", "social_h": "Social media", "base_h": "Based in",
           "base": "Málaga, Spain. Working between Málaga, Madrid and London.",
           "note": "Great to meet you. Gracias!"},
    "es": {"k": "Contacto", "h1": "Hablemos", "h2": "",
           "lead": "Para actuación, colaboraciones y prensa, contacta a través de su representación o de las redes sociales.",
           "rep_h": "Representación", "social_h": "Redes sociales", "base_h": "Residencia",
           "base": "Málaga, España. Trabaja entre Málaga, Madrid y Londres.",
           "note": "Encantada de conocerte. ¡Gracias!"},
}
