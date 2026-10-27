/* One Woman Show Films — cabecera, menú, portada, aparición, tráiler y visor de imágenes */
(function () {
  "use strict";
  var doc = document, root = doc.documentElement;
  root.classList.remove("no-js");
  function $(s, c) { return (c || doc).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || doc).querySelectorAll(s)); }
  function safe(fn) { try { fn(); } catch (e) { /* una parte no rompe las demás */ } }

  /* cabecera sólida al bajar */
  safe(function () {
    var h = $(".hdr");
    function on() { h.classList.toggle("solid", window.scrollY > 60); }
    on(); window.addEventListener("scroll", on, { passive: true });
  });

  /* menú a pantalla completa */
  safe(function () {
    var b = $(".burger"), m = $("#menu");
    function set(o) { root.classList.toggle("menu-open", o); b.setAttribute("aria-expanded", o ? "true" : "false"); m.setAttribute("aria-hidden", o ? "false" : "true"); }
    b.addEventListener("click", function () { set(!root.classList.contains("menu-open")); });
    $$("a", m).forEach(function (a) { a.addEventListener("click", function () { set(false); }); });
    doc.addEventListener("keydown", function (e) { if (e.key === "Escape") set(false); });
  });

  /* portada: fotogramas que se van fundiendo */
  safe(function () {
    var s = $$(".slide"), i = 0;
    if (s.length < 2 || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    setInterval(function () { s[i].classList.remove("on"); i = (i + 1) % s.length; s[i].classList.add("on"); }, 6500);
  });

  /* aparición al hacer scroll */
  safe(function () {
    var els = $$(".reveal");
    if (!("IntersectionObserver" in window)) { els.forEach(function (e) { e.classList.add("in"); }); return; }
    var io = new IntersectionObserver(function (en) { en.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add("in"); io.unobserve(x.target); } }); }, { threshold: 0.08, rootMargin: "0px 0px -40px 0px" });
    els.forEach(function (e) { io.observe(e); });
    setTimeout(function () { els.forEach(function (e) { e.classList.add("in"); }); }, 4000);
  });

  /* tráiler: el reproductor de YouTube (sin cookies) se carga al pulsar */
  safe(function () {
    $$(".yt").forEach(function (a) {
      a.addEventListener("click", function (e) {
        if (e.metaKey || e.ctrlKey || e.shiftKey) return;
        e.preventDefault();
        var f = doc.createElement("iframe");
        f.src = "https://www.youtube-nocookie.com/embed/" + a.getAttribute("data-yt") + "?autoplay=1&rel=0&modestbranding=1";
        f.title = a.getAttribute("aria-label") || "Trailer";
        f.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture; web-share";
        f.setAttribute("allowfullscreen", "");
        a.replaceWith(f);
      });
    });
  });

  /* visor de imágenes (agrupa por [data-gallery]) */
  safe(function () {
    var lb = $(".lightbox"), img = $("img", lb), cap = $(".lb-cap", lb), group = [], idx = 0;
    function show(i) { idx = (i + group.length) % group.length; var t = group[idx]; img.src = t.getAttribute("data-full"); img.alt = t.getAttribute("aria-label") || ""; cap.textContent = t.getAttribute("data-cap") || ""; }
    function open(t) { group = $$(".tile", t.closest("[data-gallery]") || doc); show(group.indexOf(t)); lb.classList.add("open"); lb.setAttribute("aria-hidden", "false"); doc.body.style.overflow = "hidden"; $(".lb-close", lb).focus(); }
    function close() { lb.classList.remove("open"); lb.setAttribute("aria-hidden", "true"); doc.body.style.overflow = ""; }
    $$(".tile").forEach(function (t) { t.addEventListener("click", function () { open(t); }); });
    var po = $(".js-open-press"); if (po) po.addEventListener("click", function () { open($(".press .tile")); });
    $(".lb-close", lb).addEventListener("click", close);
    $(".lb-prev", lb).addEventListener("click", function () { show(idx - 1); });
    $(".lb-next", lb).addEventListener("click", function () { show(idx + 1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) close(); });
    doc.addEventListener("keydown", function (e) {
      if (!lb.classList.contains("open")) return;
      if (e.key === "Escape") close(); else if (e.key === "ArrowLeft") show(idx - 1); else if (e.key === "ArrowRight") show(idx + 1);
    });
  });
})();
