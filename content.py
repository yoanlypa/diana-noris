"""Contenido de diananoris.com (EN principal / ES). Edita aquí textos, enlaces e imágenes y ejecuta: python build.py

Los textos salen de la web antigua de Diana (Wix), de su ficha de casting y de su biografía.
Todas las imágenes se sirven desde la propia web: los originales están en media/originals/ y build.py genera
las versiones optimizadas (WebP) en site/assets/img/media/. Ya no se carga nada de Wix.
# TODO Diana: confirmar todos los textos y datos (los de español son una traducción propia).
"""

DOMAIN = "https://www.diananoris.com"
DEMO = False  # True -> la demo no se indexa (noindex). Poner False al publicar la web definitiva.

# --------------------------------------------------------------- redes y enlaces
INSTAGRAM = "https://www.instagram.com/what_dianadid"
YOUTUBE = "https://www.youtube.com/user/diananoris"
FACEBOOK = "https://www.facebook.com/Diananoris"
IMDB = "https://www.imdb.com/name/nm4434619/"
ACTORS_ACCESS = "https://resumes.actorsaccess.com/Diananoris"
SOCIALS = [("Instagram", INSTAGRAM), ("YouTube", YOUTUBE), ("Facebook", FACEBOOK), ("IMDb", IMDB), ("Actors Access", ACTORS_ACCESS)]

# --------------------------------------------------------------- imágenes (archivos propios)
# Cada imagen tiene su original en media/originals/<clave>.<png|jpg> (descargados del Wix antiguo).
# img() devuelve la ruta de la versión WebP de ese ancho y la apunta en MEDIA_USED;
# build.py genera al final las que falten (python build.py lo hace todo).
MEDIA_URL = "/assets/img/media/"
MEDIA_USED = set()


def img(media_id, w, h=None, mode="fit", q=82):
    """Ruta de la imagen local en WebP con w píxeles de ancho (h, mode y q se mantienen por compatibilidad)."""
    key = MEDIA_KEY[media_id]
    MEDIA_USED.add((key, w))
    return f"{MEDIA_URL}{key}-{w}.webp"


def img_png(media_id, w):
    """Igual que img(); el WebP conserva la transparencia (logos)."""
    return img(media_id, w)


# Clave -> identificador que tenía en Wix (se conserva solo como referencia del origen).
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
# Pósters de los proyectos en desarrollo (originales propios, no vienen de Wix).
MEDIA["dev_nemesis"] = "local:dev_nemesis.png"
MEDIA["dev_dad"] = "local:dev_dad.png"
MEDIA["press_malaga"] = "local:press_malaga.jpg"
MEDIA_KEY = {v: k for k, v in MEDIA.items()}

# --------------------------------------------------------------- proyectos en desarrollo (página In development / En desarrollo)
DEV_FILMS = [
    {"key": "dev_nemesis", "title": "My Daughter, My Nemesis", "stage": {"en": "Writing stage", "es": "En escritura"}},
    {"key": "dev_dad", "title": "DAD", "stage": {"en": "Preproduction", "es": "Preproducción"}},
]
# Reportaje de revista que se muestra en Actuación, One Woman Show Films y Prensa.
PRESS_FEATURE = {
    "key": "press_malaga",
    "k": {"en": "Press", "es": "Prensa"},
    "h": {"en": "In the press", "es": "En la prensa"},
    "cap": {"en": "Cine & Cultura · October 2026 — Diana Noris Smith at the 32nd French Film Festival of Málaga",
            "es": "Cine & Cultura · Octubre 2026 — Diana Noris Smith en el 32.º Festival de Cine Francés de Málaga"},
}
# Tráiler de A Latina in DC (YouTube).
LATINA_TRAILER = {"provider": "youtube", "id": "6sAGGMkCcF8", "title": {"en": "A Latina in DC – Official trailer", "es": "A Latina in DC – Tráiler oficial"}}

# --------------------------------------------------------------- representación (copiado de su web actual)
AGENCY = {
    "name": "The Wayne Agency",
    "role": {"en": "Theatrical representation", "es": "Representación teatral"},
    "phones": [("TWA", "804.661.5354"), ("VA", "404.556.9211"), ("ATL", "310.492.5994")],
    # TODO Diana: confirmar representación vigente y qué datos de contacto publicar (email, agencia en España...).
}

# --------------------------------------------------------------- rutas
PAGES = ["home", "acting", "film", "latina", "filmdev", "press", "artwork", "contact"]
SLUG = {
    "en": {"home": "", "acting": "acting", "film": "film", "latina": "film/a-latina-in-dc", "filmdev": "film/in-development",
           "press": "press", "artwork": "artwork", "contact": "contact"},
    "es": {"home": "", "acting": "actuacion", "film": "cine", "latina": "cine/a-latina-in-dc", "filmdev": "cine/en-desarrollo",
           "press": "prensa", "artwork": "arte", "contact": "contacto"},
}
# Páginas que cuelgan de otra (submenú de One Woman Show Films y migas de pan).
PARENT = {"latina": "film", "filmdev": "film"}
SUBMENU = {"film": ["latina", "filmdev"]}


def path(lang, page):
    s = SLUG[lang][page]
    base = "/" if lang == "en" else "/es/"
    return base + (s + "/" if s else "")


# --------------------------------------------------------------- textos de interfaz
UI = {
    "en": {
        "locale": "en_US", "skip": "Skip to content", "menu": "Menu",
        "nav": {"home": "Home", "acting": "Acting", "film": "One Woman Show Films", "latina": "A Latina in DC", "filmdev": "In development",
                "press": "Press", "artwork": "Artwork", "contact": "Contact"},
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
        "nav": {"home": "Inicio", "acting": "Actuación", "film": "One Woman Show Films", "latina": "A Latina in DC", "filmdev": "En desarrollo",
                "press": "Prensa", "artwork": "Arte", "contact": "Contacto"},
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
        "latina": ("A Latina in DC | Short film by One Woman Show Films – Diana Noris",
                   "A Latina in DC, the short film by Diana Noris and One Woman Show Films: synopsis, audience reviews, photos, posters and press kit."),
        "filmdev": ("In development | One Woman Show Films – Diana Noris",
                    "Projects in development at One Woman Show Films, the independent production company founded by Diana Noris."),
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
        "latina": ("A Latina in DC | Cortometraje de One Woman Show Films – Diana Noris",
                   "A Latina in DC, el cortometraje de Diana Noris y One Woman Show Films: sinopsis, reseñas del público, fotos, carteles y dossier de prensa."),
        "filmdev": ("En desarrollo | One Woman Show Films – Diana Noris",
                    "Proyectos en desarrollo de One Woman Show Films, la productora independiente fundada por Diana Noris."),
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
        "lead": "Fluent in English and Spanish, Diana works seamlessly across both languages, bringing authenticity, emotional range, and cultural fluency to every role. As a dual U.S. and European citizen, she is passport-ready and available to work across both continents, giving productions greater flexibility for international casting.",
        "reel_k": "Reel", "reel_h": "Watch the reel", "reel_note": "Acting reel",
        "cast_k": "Casting profile", "cast_h": "At a glance",
        "cast": [("American measurements", [("Height", "5'7\""), ("Weight", "120 lbs"), ("Bra size", "34C"), ("Waist", "29 in"), ("Hips", "34 in"), ("Eye color", "Green"), ("Hair color", "Auburn")]), ("European measurements", [("Height", "170 cm"), ("Weight", "54.4 kg"), ("Bra size", "75C"), ("Waist", "73.7 cm"), ("Hips", "86.4 cm"), ("Eye color", "Green"), ("Hair color", "Auburn")])],
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
        "lead": "Con dominio del inglés y del español, Diana trabaja con total naturalidad en ambos idiomas y aporta autenticidad, rango emocional y fluidez cultural a cada papel. Como ciudadana estadounidense y europea, tiene el pasaporte listo y está disponible para trabajar en ambos continentes, lo que da a las producciones mayor flexibilidad en castings internacionales.",
        "reel_k": "Reel", "reel_h": "Ver el reel", "reel_note": "Reel de actuación",
        "cast_k": "Ficha de casting", "cast_h": "De un vistazo",
        "cast": [("Medidas americanas", [("Altura", "5'7\""), ("Peso", "120 lbs"), ("Copa", "34C"), ("Cintura", "29 in"), ("Cadera", "34 in"), ("Ojos", "Verdes"), ("Pelo", "Caoba")]), ("Medidas europeas", [("Altura", "170 cm"), ("Peso", "54,4 kg"), ("Copa", "75C"), ("Cintura", "73,7 cm"), ("Cadera", "86,4 cm"), ("Ojos", "Verdes"), ("Pelo", "Caoba")])],
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
        "photos_k": "Photos", "photos_h": "A Latina in DC",
        "kit_k": "Press kit", "kit_h": "Official press kit", "kit_p": "Synopsis, cast, crew and production notes for press and festivals.", "kit_btn": "Download press kit (PDF)", "kit_meta": "PDF · 12 pages · 3 MB",
        "film_k": "Now showing", "film_h1": "A Latina in DC", "film_status": "Coming to festivals worldwide",
        "film_p": "After another disastrous blind date, an exhausted Latina woman in Washington, D.C. begins questioning her relationships and the polished life she has built while navigating modern dating and cultural stereotypes.",
        "gallery_k": "Gallery", "gallery_h": "Posters",
        "dev_k": "In development", "dev_h": "Projects in development",
        "dev_p": "Diana continues to develop new projects. Details will be announced here.",
        "reviews_k": "Reviews", "reviews_h": "What audiences say",
        "reviews_read": "Read on Letterboxd", "reviews_more": "Read more", "reviews_less": "Read less", "reviews_all": "See the film on Letterboxd",
        "trailer_k": "Trailer", "films_k": "Films", "films_h": "Our films", "films_view": "View the film", "films_more": "Learn more",
    },
    "es": {
        "k": "Cine", "h1": "One Woman Show Films", "h2": "Historias valientes, centradas en los personajes",
        "lead": "Una productora independiente fundada por Diana Noris, dedicada a contar historias valientes, centradas en personajes, desde una perspectiva femenina y multicultural.",
        "about": [
            "Su trabajo como cineasta combina el humor con una narrativa emocionalmente honesta, y explora la identidad, las relaciones, la reinvención y las presiones sociales y culturales que enfrentan las mujeres.",
            "Diana se centra especialmente en crear personajes femeninos con capas y en contar historias para mujeres cuyas experiencias y complejidades siguen estando poco representadas en pantalla. A través de One Woman Show Films continúa desarrollando proyectos pensados para conectar con públicos de distintas culturas y generaciones.",
            "Sigue desarrollando y produciendo sus propios proyectos a través de One Woman Show Films.",
        ],
        "photos_k": "Fotos", "photos_h": "A Latina in DC",
        "kit_k": "Dossier de prensa", "kit_h": "Dossier de prensa oficial", "kit_p": "Sinopsis, reparto, equipo y notas de producción para prensa y festivales.", "kit_btn": "Descargar dossier de prensa (PDF)", "kit_meta": "PDF · 12 páginas · 3 MB",
        "film_k": "En cartel", "film_h1": "A Latina in DC", "film_status": "En camino a festivales de todo el mundo",
        "film_p": "Tras otra cita a ciegas desastrosa, una latina agotada en Washington D. C. empieza a cuestionarse sus relaciones y la vida pulida que se ha construido, mientras sortea las citas modernas y los estereotipos culturales.",
        "gallery_k": "Galería", "gallery_h": "Carteles",
        "dev_k": "En desarrollo", "dev_h": "Proyectos en desarrollo",
        "dev_p": "Diana sigue desarrollando nuevos proyectos. Los detalles se anunciarán aquí.",
        "reviews_k": "Reseñas", "reviews_h": "Lo que dice el público",
        "reviews_read": "Leer en Letterboxd", "reviews_more": "Leer más", "reviews_less": "Leer menos", "reviews_all": "Ver la película en Letterboxd",
        "trailer_k": "Tráiler", "films_k": "Películas", "films_h": "Nuestras películas", "films_view": "Ver la película", "films_more": "Más información",
    },
}

# --------------------------------------------------------------- reseñas de «A Latina in DC» (Letterboxd)
# El texto es una frase literal de cada reseña, en su idioma original (no se traduce). stars: 0-5 (0 = sin nota).
LETTERBOXD_FILM = "https://letterboxd.com/film/a-latina-in-dc/"
REVIEWS = [
    # Texto completo de cada reseña de Letterboxd: un párrafo por elemento; "\n" = salto de línea dentro del párrafo.
    {"author": "Karlos7484", "stars": 5, "url": "https://letterboxd.com/karlos7484/film/a-latina-in-dc/1/",
     "text": ["⭐⭐⭐⭐⭐ 5/5 Stars",
              "A Charming and Heartwarming Romantic Story!",
              "“Latina in DC is a delightful and relatable short film that beautifully captures the challenges of modern dating, the humor of unexpected encounters, and the magic of finding love when you least expect it.",
              "Through a series of disappointing dating app experiences, the story reminds us that people aren’t always who they appear to be online and that sometimes the connection we’ve been searching for is closer than we realize.",
              "What makes this film special is its combination of humor, romance, and a heartfelt message about love, authenticity, and unexpected possibilities.",
              "A charming story with a beautiful message: Sometimes love isn’t just a swipe away — it might be right next door!",
              "Congratulations to the cast for bringing such a sweet and entertaining story to life. Wishing her continued success in her filmmaking journey!”"]},
    {"author": "calypsoeve", "stars": 5, "url": "https://letterboxd.com/calypsoeve/film/a-latina-in-dc/",
     "text": ["Refreshing, there were parts that made us laugh out loud. The dialogue was so natural, and the characters felt real. Love the animal actors!!!"]},
    {"author": "Budger", "stars": 0, "url": "https://letterboxd.com/budger/film/a-latina-in-dc/",
     "text": ["I was very impressed with all the performances. This film was funny and I’m sure, relatable too.\nI recommend it for a fun short film."]},
    {"author": "Nerdyforfilms", "stars": 5, "url": "https://letterboxd.com/nerdyforfilms/film/a-latina-in-dc/",
     "text": ["Wow, I am pretty impressed. I’m not usually into short films, but this is a very well done film. I really loved how natural everyone’s acting felt, especially the two main actresses who play Eva and her friend. They have really great chemistry together.\nAlso, can I please have the phone number of that neighbor? Wow! <3 😂\nAs a kid from the ’80s, hearing the OMD music brought back so much nostalgia and gave me such a warm and fuzzy feeling.",
              "And for all the cat lovers out there, you’re definitely going to have a good laugh. The cats in the film are so funny and cute, and they honestly have some great moments of their own.\nThank you for inviting me to the private screening. I truly hope you get all the awards you guys deserve on the festival circuit!"]},
    {"author": "leximoran89", "stars": 5, "url": "https://letterboxd.com/leximoran89/film/a-latina-in-dc/",
     "text": ["Watched this hilarious short film yesterday, and I gotta tell you, I laughed so hard! 😂 I can totally understand why she hates men. I've had my own share of bad dating experiences in Washington, DC, because honestly, men out there are unhinged! LOL!",
              "The acting was really good, which is something that's hard to find in short films these days. Loved the kitty cats, and the banter between the main actress and her friend was freaking hilarious! And those face masks she kept using throughout the film had me dying! 😂",
              "It's funny, relatable, and such an easy watch. I actually wish it had been longer! The ending leaves you with so many questions, though. Maybe a sequel is in order?",
              "Great job to everyone involved! Definitely worth watching!"]},
    {"author": "Madridfilmfest", "stars": 5, "url": "https://letterboxd.com/madridfilmfest/film/a-latina-in-dc/",
     "text": ["Really cool and refreshing short film! First of all, the actor who plays Maurizio is a hottie! LOL! And I really liked the other guy too, I think his name was Josh? Both hotties and really good acting all around!",
              "I was actually expecting a more intense ending, but it definitely leaves you wondering about a few things. Also, why on earth did she keep letting her friend set her up on dates? After that many horrible experiences, I would've been like HELL NO! 😂",
              "And can we talk about that man who gave her that gift?! I would LOVE to know the name of that douchebag! What a horrible man! Apparently, this film is based on real experiences from the lead actress's life, which makes it even crazier. Like, WHAT THE HELL?! That's insane!",
              "Really entertaining film, and I enjoyed watching it!"]},
    {"author": "lautorresalb", "stars": 5, "url": "https://letterboxd.com/lautorresalb/film/a-latina-in-dc/", "lang": "es",
     "text": ["Excelente y divertidísima!\nUna mirada divertidísima y muy acertada sobre el desgaste de las citas. Desmonta con bastante ironía el cliché de la latina en el que caen tantos tipos, pero lo que realmente sostiene la historia es la voz de ella: cercana, transparente y sin adornos. Te ríes con cada desastre porque sientes que te lo está contando una amiga en confianza. Fresca, necesaria y muy bien llevada."]},
    {"author": "KDubMovies", "stars": 5, "url": "https://letterboxd.com/kdubmovies/film/a-latina-in-dc/",
     "text": ["What a charming and REAL film about dating in DC! The \"dates\" were wonderfully awful! What an accomplishment! I loved the cast, down to the sweet heroes of the film (meow). So happy for you Diana!"]},
    {"author": "Univisiontvana", "stars": 5, "url": "https://letterboxd.com/univisiontvana/film/a-latina-in-dc/",
     "text": ["One word: RELATABLE! Such a super cute, girly, fun film with really good actors!",
              "I really liked the ladies at the beginning, and that first scene with the cat was hilarious! And can we talk about that horrible guy who told her she wasn't American because she's Puerto Rican?! What a disgusting human being! I can't believe people like that actually exist, but then again, we're living in a crazy world where racism and misogyny seem to be everywhere.",
              "I love that this film touches on so many things women deal with today, especially dating, misogyny, racism, and men who are just good for nothing. Well, most of them anyway! LOL!",
              "The whole neighbor situation was SO relatable! How many of us have run into a cute neighbor in the hallway at the absolute worst moment, looking like a complete disaster and praying nobody sees us? Those scenes had me laughing because we've all been there!",
              "And OMG, the music! Orchestral Manoeuvres in the Dark! What an amazing soundtrack! The music brought so much to the film, and honestly, that soundtrack is priceless.",
              "This should've been a feature film because there's so much more to explore, and it covers so many things women are experiencing in today's world. I would've happily watched another hour of it!",
              "Really enjoyed this one, especially the music! Five stars in my book! ⭐⭐⭐⭐⭐"]},
]

PRESS = {
    "en": {"k": "Press", "h1": "In the", "h2": "spotlight", "lead": "Magazine covers and press appearances featuring Diana Noris.",
           "covers_h": "Covers", "seen_h": "As seen on", "videos_h": "Interviews & TV"},
    "es": {"k": "Prensa", "h1": "En", "h2": "portada", "lead": "Portadas de revistas y apariciones en prensa de Diana Noris.",
           "covers_h": "Portadas", "seen_h": "Visto en", "videos_h": "Entrevistas y televisión"},
}

ARTWORK = {
    "en": {"k": "Artwork", "h1": "Artist", "h2": "",
           "lead": "",
           "p": ["Diana Noris is an artist known for whimsical, imaginative paintings that combine traditional techniques with unexpected materials and texture. Her work often blends oil and acrylic paint with fabric, textiles, rhinestones, and other mixed-media elements, creating pieces that are playful, dimensional, and highly individual.",
                 "She previously owned an art gallery in Miami, where she exhibited and sold her work, and she continues to create commissioned pieces for private clients. Her collectors have included personalities from the entertainment industry and other high-profile clients.",
                 "Her work has been featured by CNN en Español, CNN, Forbes, and Latina Magazine, among other media outlets.",
                 "Now based in Málaga, Diana is working on a new collection that she is preparing to exhibit in Málaga. The collection is currently in development, and she is excited to complete the work and present it in an upcoming exhibition.",
                 "Painting remains an important part of her creative life, giving her a space to experiment with color, texture, humor, and imagination."],
           "soon": "Gallery coming soon"},
    "es": {"k": "Arte", "h1": "Artista", "h2": "",
           "lead": "",
           "p": ["Diana Noris es una artista conocida por sus pinturas fantasiosas e imaginativas, que combinan técnicas tradicionales con materiales y texturas inesperados. Su obra mezcla a menudo óleo y acrílico con tela, textiles, strass y otros elementos de técnica mixta, y da lugar a piezas lúdicas, con volumen y muy personales.",
                 "Fue propietaria de una galería de arte en Miami, donde exhibió y vendió su obra, y sigue creando piezas por encargo para clientes privados. Entre sus coleccionistas se cuentan personalidades del mundo del espectáculo y otros clientes de alto perfil.",
                 "Su trabajo ha sido destacado por CNN en Español, CNN, Forbes y Latina Magazine, entre otros medios.",
                 "Ahora afincada en Málaga, Diana trabaja en una nueva colección que prepara para exponer en Málaga. La colección está en desarrollo y está ilusionada con terminarla y presentarla en una próxima exposición.",
                 "La pintura sigue siendo una parte importante de su vida creativa y le ofrece un espacio para experimentar con el color, la textura, el humor y la imaginación."],
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
LATINA = [  # fotos de «A Latina in DC»: (stem, nº de archivo origen, pie de foto)
    ("lat-01", 1, {"en": "Diana Noris Smith in “A Latina in DC”", "es": "Diana Noris Smith en «A Latina in DC»"}),
    ("lat-02", 2, {"en": "Diana Noris Smith in “A Latina in DC”", "es": "Diana Noris Smith en «A Latina in DC»"}),
    ("lat-03", 3, {"en": "Diana Noris Smith in “A Latina in DC”", "es": "Diana Noris Smith en «A Latina in DC»"}),
    ("lat-04", 4, {"en": "Diana Noris Smith in “A Latina in DC”", "es": "Diana Noris Smith en «A Latina in DC»"}),
    ("lat-05", 5, {"en": "“A Latina in DC”", "es": "«A Latina in DC»"}),
    ("lat-06", 6, {"en": "Diana Noris Smith in “A Latina in DC”", "es": "Diana Noris Smith en «A Latina in DC»"}),
    ("lat-07", 7, {"en": "Diana Noris Smith in “A Latina in DC”", "es": "Diana Noris Smith en «A Latina in DC»"}),
    ("lat-08", 8, {"en": "Jonathan Turpin in “A Latina in DC”", "es": "Jonathan Turpin en «A Latina in DC»"}),
    ("lat-09", 9, {"en": "Diana Noris Smith and Nick Blanchet in “A Latina in DC”", "es": "Diana Noris Smith y Nick Blanchet en «A Latina in DC»"}),
    ("lat-10", 10, {"en": "“A Latina in DC”", "es": "«A Latina in DC»"}),
    ("lat-11", 11, {"en": "“A Latina in DC”", "es": "«A Latina in DC»"}),
    ("lat-12", 12, {"en": "“A Latina in DC”", "es": "«A Latina in DC»"}),
    ("lat-13", 13, {"en": "Francesco Pultro and Diana Noris Smith in “A Latina in DC”", "es": "Francesco Pultro y Diana Noris Smith en «A Latina in DC»"}),
    ("lat-14", 14, {"en": "Jonathan Turpin and Diana Noris Smith in “A Latina in DC”", "es": "Jonathan Turpin y Diana Noris Smith en «A Latina in DC»"}),
    ("lat-15", 16, {"en": "Jonathan Turpin and Diana Noris Smith in “A Latina in DC”", "es": "Jonathan Turpin y Diana Noris Smith en «A Latina in DC»"}),
    ("lat-16", 17, {"en": "Diana Noris Smith and Rick Jermain in “A Latina in DC”", "es": "Diana Noris Smith y Rick Jermain en «A Latina in DC»"}),
    ("lat-17", 18, {"en": "Diana Noris Smith in “A Latina in DC”", "es": "Diana Noris Smith en «A Latina in DC»"}),
    ("lat-18", 19, {"en": "Diana Noris Smith in “A Latina in DC”", "es": "Diana Noris Smith en «A Latina in DC»"}),
    ("lat-19", 20, {"en": "Diana Noris Smith in “A Latina in DC”", "es": "Diana Noris Smith en «A Latina in DC»"}),
    ("lat-20", 21, {"en": "Behind the scenes of “A Latina in DC”", "es": "Detrás de cámaras de «A Latina in DC»"}),
    ("lat-21", 22, {"en": "Behind the scenes of “A Latina in DC”", "es": "Detrás de cámaras de «A Latina in DC»"}),
    ("lat-22", 23, {"en": "Behind the scenes of “A Latina in DC”", "es": "Detrás de cámaras de «A Latina in DC»"}),
    ("lat-23", 24, {"en": "Behind the scenes of “A Latina in DC”", "es": "Detrás de cámaras de «A Latina in DC»"}),
    ("lat-24", 25, {"en": "Behind the scenes of “A Latina in DC”", "es": "Detrás de cámaras de «A Latina in DC»"}),
    ("lat-25", 26, {"en": "Behind the scenes of “A Latina in DC”", "es": "Detrás de cámaras de «A Latina in DC»"}),
    ("lat-26", 27, {"en": "Behind the scenes of “A Latina in DC”", "es": "Detrás de cámaras de «A Latina in DC»"}),
    ("lat-27", 28, {"en": "Behind the scenes of “A Latina in DC”", "es": "Detrás de cámaras de «A Latina in DC»"}),
]

BTS = [  # (stem, nº de archivo origen, pie de foto)
    ("bts-01", 1, {"en": "On set of “A Latina in DC”", "es": "En el set de «A Latina in DC»"}),
    ("bts-02", 2, {"en": "On set of “A Latina in DC”", "es": "En el set de «A Latina in DC»"}),
    ("bts-03", 3, {"en": "On set of “A Latina in DC”", "es": "En el set de «A Latina in DC»"}),
    ("bts-04", 4, {"en": "At the trailer while filming in Madrid", "es": "En la caravana durante el rodaje en Madrid"}),
    ("bts-05", 5, {"en": "Behind the scenes of “Bullet”", "es": "Detrás de cámaras de «Bullet»"}),
    ("bts-06", 6, {"en": "Behind the scenes of “The Asylum”", "es": "Detrás de cámaras de «The Asylum»"}),
    ("bts-07", 7, {"en": "Behind the scenes of “The Asylum”", "es": "Detrás de cámaras de «The Asylum»"}),
    ("bts-08", 8, {"en": "Behind the scenes of “The Asylum”", "es": "Detrás de cámaras de «The Asylum»"}),
    ("bts-09", 9, {"en": "Behind the scenes of “The Asylum”", "es": "Detrás de cámaras de «The Asylum»"}),
    ("bts-10", 10, {"en": "Behind the scenes of “The Asylum”", "es": "Detrás de cámaras de «The Asylum»"}),
    ("bts-11", 11, {"en": "Behind the scenes of “The Asylum”", "es": "Detrás de cámaras de «The Asylum»"}),
    ("bts-12", 12, {"en": "Behind the scenes of “The Asylum”", "es": "Detrás de cámaras de «The Asylum»"}),
    ("bts-13", 13, {"en": "Behind the scenes of “The Asylum”", "es": "Detrás de cámaras de «The Asylum»"}),
    ("bts-14", 15, {"en": "Behind the scenes, stunts in Málaga", "es": "Detrás de cámaras, escena de acción en Málaga"}),
    ("bts-15", 16, {"en": "Behind the scenes, stunt work", "es": "Detrás de cámaras, trabajo de especialista"}),
]

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

# --------------------------------------------------------------- vídeos de prensa (página Press / Prensa)
# provider: "youtube" o "vimeo". Para añadir otro, copia una línea y cambia id y títulos.
# "seconds" y "thumb" son opcionales (thumb solo hace falta en Vimeo).
PRESS_VIDEOS = [
    {"provider": "youtube", "id": "KLtiS08MJDU", "title": {"en": "Alexis Valdés · Interview, 2012", "es": "Alexis Valdés · Entrevista, 2012"}},
    {"provider": "youtube", "id": "pAdNu5XUI3Y", "title": {"en": "Interviews · Clips", "es": "Entrevistas · Fragmentos"}},
    {"provider": "youtube", "id": "wOBUv72GP60", "title": {"en": "VIP TV · Women in the Arts", "es": "VIP TV · Women in the Arts"}},
    {"provider": "youtube", "id": "jIfbCNfSy6A", "title": {"en": "Arte Mujer", "es": "Arte Mujer"}},
    {"provider": "vimeo", "id": "320407154", "title": {"en": "89.3 FM NYC · Radio interview", "es": "89.3 FM NYC · Entrevista en radio"},
     "seconds": 102, "thumb": "https://i.vimeocdn.com/video/762825587-cd6f70aa85e26365397a7aece5fade1c8c7caf76fc92438774c0df992d813e30-d_1280"},
    {"provider": "youtube", "id": "H7yVnMvBzq8", "title": {"en": "Infórmate con GiGi · Interview", "es": "Infórmate con GiGi · Entrevista"}},
    {"provider": "youtube", "id": "z2mEJIvpMXU", "title": {"en": "NBC · In the Mix", "es": "NBC · In the Mix"}},
]
