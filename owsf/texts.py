"""Textos de onewomanshowfilms.com (EN principal en "/", ES en "/es/").

Los textos de la productora salen de la hoja oficial de One Woman Show Films (media/originals/owsf.png),
del reportaje de Cine & Cultura (octubre 2026) y de la web de Diana (content.py). La traducción es propia.
Edita aquí y ejecuta:  python owsf/build.py
"""

DOMAIN = "https://www.onewomanshowfilms.com"
DIANA_SITE = "https://www.diananoris.com"
LETTERBOXD = "https://letterboxd.com/film/a-latina-in-dc/"
PRESS_KIT = "/press-kit/A-Latina-in-DC-Press-Kit.pdf"

# Fotos de la portada (fotogramas de A Latina in DC, en orden de aparición).
HERO_SLIDES = ["lat-04", "lat-03", "lat-07"]
# Fotogramas de la galería «Inside the film».
STILLS = ["lat-02", "lat-06", "lat-05", "lat-15", "lat-16", "lat-14", "lat-09", "lat-20"]

# Frases literales de reseñas de Letterboxd (las completas están en content.REVIEWS).
REVIEW_QUOTES = {
    "en": [
        ("Karlos7484", "A charming story with a beautiful message: Sometimes love isn’t just a swipe away — it might be right next door!"),
        ("KDubMovies", "What a charming and REAL film about dating in DC! The “dates” were wonderfully awful!"),
        ("Univisiontvana", "One word: RELATABLE! Such a super cute, girly, fun film with really good actors!"),
        ("Nerdyforfilms", "I’m not usually into short films, but this is a very well done film."),
        ("leximoran89", "It's funny, relatable, and such an easy watch. I actually wish it had been longer!"),
        ("calypsoeve", "Refreshing, there were parts that made us laugh out loud. The dialogue was so natural, and the characters felt real."),
    ],
}
REVIEW_QUOTES["es"] = REVIEW_QUOTES["en"][:5] + [
    ("lautorresalb", "Excelente y divertidísima! Una mirada divertidísima y muy acertada sobre el desgaste de las citas."),
]

T = {
    "en": {
        "lang_name": "English", "skip": "Skip to content", "menu": "Menu", "close": "Close",
        "nav": [("about", "About"), ("founder", "Founder"), ("latest", "Latest"), ("upcoming", "Upcoming"), ("press", "Press"), ("contact", "Contact")],
        "title": "One Woman Show Films | Women-centered stories with a point of view",
        "desc": "One Woman Show Films is the independent production company founded by Diana Noris: bold, character-driven stories through a female and multicultural lens. New York · Málaga.",
        "hero_h1": "Women-centered stories", "hero_h2": "with a point of view.",
        "hero_tags": ["Female stories", "Multicultural perspectives", "Honest cinema"],
        "scroll": "Scroll",
        "about_k": "About us",
        "about_p": "Founded by Diana Noris, One Woman Show Films develops bold, character-driven stories through a female and multicultural lens, creating emotionally honest work about identity, relationships, reinvention, and the voices women are not always allowed to say out loud.",
        "about_cities": "New York · Málaga",
        "founder_k": "The founder", "founder_h1": "Behind the", "founder_h2": "camera",
        "founder_role": "Founder · Writer · Director · Producer",
        "founder_more": "Visit diananoris.com",
        "latest_k": "Projects", "latest_h1": "Latest:", "latest_h2": "A Latina in DC",
        "trailer_cap": "A Latina in DC — Official trailer",
        "acc_about": "About A Latina in DC", "acc_festival": "Festival journey", "acc_kit": "Press kit",
        "f_title": "Title", "f_genre": "Genre", "f_logline": "Logline", "f_director": "Director", "f_filmmaker": "Filmmaker",
        "f_starring": "Starring", "f_runtime": "Runtime", "f_filmed": "Filmed in",
        "genre": "Dark comedy inspired by a true story", "runtime": "30 minutes", "filmed": "Washington, D.C., Virginia and Madrid",
        "festival_p": "A Latina in DC is beginning its festival journey across Europe, the United States and South America.",
        "kit_p": "Synopsis, cast, crew and production notes for press and festivals.", "kit_btn": "Download the press kit (PDF)",
        "reviews_k": "Audience reviews", "reviews_h1": "What audiences", "reviews_h2": "are saying",
        "reviews_all": "Read all reviews on Letterboxd", "stars": "5 out of 5 stars",
        "stills_k": "Inside the film",
        "upcoming_k": "Upcoming projects", "upcoming_h1": "In", "upcoming_h2": "development",
        "upcoming_note": "Both projects will be filmed between Málaga and Madrid, Spain.",
        "press_k": "Press", "press_h1": "In the", "press_h2": "press",
        "press_title": "Diana Noris Smith: a new chapter on the international scene",
        "press_meta": "Cine & Cultura · October 2026 · 32nd French Film Festival of Málaga",
        "press_p": "The actress, director and founder of One Woman Show Films took part in a professional day for filmmakers and producers at the Alliance Française de Málaga.",
        "press_open": "Read the article", "press_all": "More press on diananoris.com",
        "contact_k": "Contact", "contact_h1": "Let’s", "contact_h2": "talk",
        "contact_p": "For festivals, press, co-productions and collaborations, get in touch through Diana Noris.",
        "contact_btn": "Contact", "rights": "All rights reserved.", "credit": "Web design",
        "lb_prev": "Previous", "lb_next": "Next",
        "statuses": {"dev_nemesis": "Writing stage", "dev_dad": "Preproduction"},
        "dev_lines": {"dev_nemesis": "Based on a true story. Love. Betrayal. Power. Legacy.",
                      "dev_dad": "Memory. Family. Absence. What remains."},
    },
    "es": {
        "lang_name": "Español", "skip": "Saltar al contenido", "menu": "Menú", "close": "Cerrar",
        "nav": [("about", "Nosotras"), ("founder", "Fundadora"), ("latest", "Película"), ("upcoming", "Próximos"), ("press", "Prensa"), ("contact", "Contacto")],
        "title": "One Woman Show Films | Historias de mujeres con una mirada propia",
        "desc": "One Woman Show Films es la productora independiente fundada por Diana Noris: historias valientes, centradas en personajes, desde una mirada femenina y multicultural. Nueva York · Málaga.",
        "hero_h1": "Historias de mujeres", "hero_h2": "con una mirada propia.",
        "hero_tags": ["Historias femeninas", "Perspectivas multiculturales", "Cine honesto"],
        "scroll": "Bajar",
        "about_k": "Quiénes somos",
        "about_p": "Fundada por Diana Noris, One Woman Show Films desarrolla historias valientes, centradas en personajes, desde una mirada femenina y multicultural: un cine emocionalmente honesto sobre la identidad, las relaciones, la reinvención y las voces que a las mujeres no siempre se les permite decir en voz alta.",
        "about_cities": "Nueva York · Málaga",
        "founder_k": "La fundadora", "founder_h1": "Detrás de la", "founder_h2": "cámara",
        "founder_role": "Fundadora · Guionista · Directora · Productora",
        "founder_more": "Visita diananoris.com",
        "latest_k": "Proyectos", "latest_h1": "Última película:", "latest_h2": "A Latina in DC",
        "trailer_cap": "A Latina in DC — Tráiler oficial",
        "acc_about": "Sobre A Latina in DC", "acc_festival": "Recorrido por festivales", "acc_kit": "Dossier de prensa",
        "f_title": "Título", "f_genre": "Género", "f_logline": "Sinopsis", "f_director": "Dirección", "f_filmmaker": "Filmmaker",
        "f_starring": "Reparto", "f_runtime": "Duración", "f_filmed": "Rodada en",
        "genre": "Comedia negra inspirada en una historia real", "runtime": "30 minutos", "filmed": "Washington D. C., Virginia y Madrid",
        "festival_p": "A Latina in DC comienza su recorrido por festivales de Europa, Estados Unidos y Sudamérica.",
        "kit_p": "Sinopsis, reparto, equipo y notas de producción para prensa y festivales.", "kit_btn": "Descargar el dossier (PDF)",
        "reviews_k": "Reseñas del público", "reviews_h1": "Lo que dice", "reviews_h2": "el público",
        "reviews_all": "Leer todas las reseñas en Letterboxd", "stars": "5 de 5 estrellas",
        "stills_k": "Dentro de la película",
        "upcoming_k": "Próximos proyectos", "upcoming_h1": "En", "upcoming_h2": "desarrollo",
        "upcoming_note": "Los dos proyectos se rodarán entre Málaga y Madrid.",
        "press_k": "Prensa", "press_h1": "En la", "press_h2": "prensa",
        "press_title": "Diana Noris Smith: un nuevo capítulo en la escena internacional",
        "press_meta": "Cine & Cultura · Octubre 2026 · 32.º Festival de Cine Francés de Málaga",
        "press_p": "La actriz, directora y fundadora de One Woman Show Films participó en una jornada profesional para cineastas y productores en la Alianza Francesa de Málaga.",
        "press_open": "Leer el reportaje", "press_all": "Más prensa en diananoris.com",
        "contact_k": "Contacto", "contact_h1": "Hablemos", "contact_h2": "",
        "contact_p": "Para festivales, prensa, coproducciones y colaboraciones, contacta a través de Diana Noris.",
        "contact_btn": "Contactar", "rights": "Todos los derechos reservados.", "credit": "Diseño web",
        "lb_prev": "Anterior", "lb_next": "Siguiente",
        "statuses": {"dev_nemesis": "En escritura", "dev_dad": "Preproducción"},
        "dev_lines": {"dev_nemesis": "Basada en una historia real. Amor. Traición. Poder. Legado.",
                      "dev_dad": "Memoria. Familia. Ausencia. Lo que queda."},
    },
}
