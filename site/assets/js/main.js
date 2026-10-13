/* diananoris.com — comportamiento (clásico, sin dependencias) */
(function () {
  "use strict";
  var doc = document, root = doc.documentElement;
  root.classList.remove("no-js");
  function safe(fn, name) { try { fn(); } catch (e) { if (window.console) console.warn("[dn] " + name, e); } }
  function $(s, c) { return (c || doc).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || doc).querySelectorAll(s)); }

  /* idioma: recuerda la elección de las banderas; solo redirige desde la portada en inglés */
  safe(function () {
    var lang = root.getAttribute("lang") === "es" ? "es" : "en";
    $$(".lang a").forEach(function (a) { a.addEventListener("click", function () { try { localStorage.setItem("dn-lang", a.getAttribute("hreflang")); } catch (e) {} }); });
    var saved = null; try { saved = localStorage.getItem("dn-lang"); } catch (e) {}
    var own = doc.referrer.indexOf(location.host) !== -1;
    if (lang === "en" && saved === "es" && !own && location.pathname === "/") {
      var t = $('.lang a[hreflang="es"]'); if (t) location.replace(t.getAttribute("href") + (location.hash || ""));
    }
  }, "lang");

  /* cabecera sólida al hacer scroll + menú móvil */
  safe(function () {
    var h = $(".header");
    function on() { h.classList.toggle("solid", window.scrollY > 40 || h.hasAttribute("data-solid")); }
    on(); window.addEventListener("scroll", on, { passive: true });
    var b = $(".burger");
    b.addEventListener("click", function () { var o = root.classList.toggle("menu-open"); b.setAttribute("aria-expanded", o ? "true" : "false"); });
    $$(".nav a").forEach(function (a) { a.addEventListener("click", function () { root.classList.remove("menu-open"); b.setAttribute("aria-expanded", "false"); }); });
  }, "header");

  /* aparición al hacer scroll (umbral bajo + red de seguridad) */
  safe(function () {
    var els = $$(".reveal");
    if (!("IntersectionObserver" in window)) { els.forEach(function (e) { e.classList.add("in"); }); return; }
    var io = new IntersectionObserver(function (en) { en.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add("in"); io.unobserve(x.target); } }); }, { threshold: 0.04, rootMargin: "0px 0px -4% 0px" });
    els.forEach(function (e) { io.observe(e); });
    setTimeout(function () { els.forEach(function (e) { e.classList.add("in"); }); }, 6000);
  }, "reveal");

  /* slider horizontal con botones */
  safe(function () {
    $$(".slider-wrap").forEach(function (w) {
      var s = $(".slider", w), prev = $(".prev", w), next = $(".next", w); if (!s) return;
      function step() { var f = s.firstElementChild; return f ? f.getBoundingClientRect().width + 18 : 300; }
      if (prev) prev.addEventListener("click", function () { s.scrollBy({ left: -step(), behavior: "smooth" }); });
      if (next) next.addEventListener("click", function () { s.scrollBy({ left: step(), behavior: "smooth" }); });
    });
  }, "slider");

  /* vídeos de YouTube: el reproductor (sin cookies) se carga solo al pulsar */
  safe(function () {
    $$(".yt").forEach(function (a) {
      a.addEventListener("click", function (e) {
        if (e.metaKey || e.ctrlKey || e.shiftKey) return; // permite abrir en pestaña nueva
        e.preventDefault();
        var f = doc.createElement("iframe");
        f.src = "https://www.youtube-nocookie.com/embed/" + a.getAttribute("data-yt") + "?autoplay=1&rel=0&modestbranding=1";
        f.title = a.getAttribute("data-title") || "Video";
        f.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share";
        f.setAttribute("allowfullscreen", "");
        a.replaceWith(f);
      });
    });
  }, "youtube");

  /* visor de fotos (agrupa por [data-gallery]) */
  safe(function () {
    var lb = $(".lightbox"); if (!lb) return;
    var img = $("img", lb), cap = $(".lb-cap", lb), group = [], idx = 0;
    function show(i) { idx = (i + group.length) % group.length; var t = group[idx], im = $("img", t); img.src = t.getAttribute("data-full") || im.currentSrc || im.src; img.alt = im.alt; cap.textContent = t.getAttribute("data-cap") || ""; }
    function open(t) { group = $$(".tile", t.closest("[data-gallery]") || doc); show(group.indexOf(t)); lb.classList.add("open"); lb.setAttribute("aria-hidden", "false"); doc.body.style.overflow = "hidden"; }
    function close() { lb.classList.remove("open"); lb.setAttribute("aria-hidden", "true"); doc.body.style.overflow = ""; }
    $$(".tile").forEach(function (t) { t.addEventListener("click", function () { open(t); }); });
    $(".lb-close", lb).addEventListener("click", close);
    $(".lb-prev", lb).addEventListener("click", function () { show(idx - 1); });
    $(".lb-next", lb).addEventListener("click", function () { show(idx + 1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) close(); });
    doc.addEventListener("keydown", function (e) { if (!lb.classList.contains("open")) return; if (e.key === "Escape") close(); else if (e.key === "ArrowLeft") show(idx - 1); else if (e.key === "ArrowRight") show(idx + 1); });
  }, "lightbox");
})();
