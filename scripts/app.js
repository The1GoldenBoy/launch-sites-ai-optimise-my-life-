/* OptimizeMyLife — interactions partagées
   Aucune dépendance externe. Progressive enhancement. */
(function () {
  "use strict";

  /* ---- Menu mobile ---- */
  function initNav() {
    var header = document.querySelector(".site-header");
    var toggle = document.querySelector(".nav__toggle");
    if (toggle && header) {
      toggle.addEventListener("click", function () {
        header.classList.toggle("is-open");
        var open = header.classList.contains("is-open");
        toggle.setAttribute("aria-expanded", String(open));
      });
    }

    /* Dropdowns "Produits" : clic + survol */
    document.querySelectorAll(".nav__group").forEach(function (group) {
      var btn = group.querySelector("button");
      if (!btn) return;
      btn.addEventListener("click", function (e) {
        e.stopPropagation();
        var open = group.getAttribute("data-open") === "true";
        document.querySelectorAll(".nav__group").forEach(function (g) {
          g.setAttribute("data-open", "false");
        });
        group.setAttribute("data-open", open ? "false" : "true");
      });
    });
    document.addEventListener("click", function () {
      document.querySelectorAll(".nav__group").forEach(function (g) {
        g.setAttribute("data-open", "false");
      });
    });
  }

  /* ---- Détection des assets Félix ----
     On ne dessine pas Félix : si l'image est absente, on affiche un
     emplacement clairement marqué pour que l'asset réel soit déposé. */
  function initFelix() {
    document.querySelectorAll(".felix img").forEach(function (img) {
      function fail() {
        var box = img.closest(".felix");
        if (box) box.classList.add("is-missing");
      }
      img.addEventListener("error", fail);
      if (img.complete && img.naturalWidth === 0) fail();
    });
  }

  /* ---- Modale vidéo (Félix mentor) ---- */
  function initVideo() {
    var modal = document.querySelector("[data-modal]");
    if (!modal) return;
    var box = modal.querySelector(".modal__box");
    var defaultHTML = box ? box.innerHTML : "";

    function open(src) {
      if (src && box) {
        box.innerHTML =
          '<iframe src="' + src + '" allow="autoplay; encrypted-media" allowfullscreen></iframe>';
      } else if (box) {
        box.innerHTML = defaultHTML;
      }
      modal.setAttribute("data-open", "true");
      document.body.style.overflow = "hidden";
    }
    function close() {
      modal.setAttribute("data-open", "false");
      if (box) box.innerHTML = defaultHTML;
      document.body.style.overflow = "";
    }

    document.querySelectorAll("[data-video]").forEach(function (trigger) {
      trigger.addEventListener("click", function () {
        open(trigger.getAttribute("data-video"));
      });
    });
    modal.addEventListener("click", function (e) {
      if (e.target === modal || e.target.closest(".modal__close")) close();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") close();
    });
  }

  /* ---- Carousel de screenshots ---- */
  function initCarousels() {
    document.querySelectorAll("[data-carousel]").forEach(function (car) {
      var track = car.querySelector(".carousel__track");
      var prev = car.querySelector("[data-prev]");
      var next = car.querySelector("[data-next]");
      if (!track) return;
      function step() {
        var first = track.querySelector(".shot");
        return first ? first.getBoundingClientRect().width + 22 : 400;
      }
      if (prev) prev.addEventListener("click", function () { track.scrollBy({ left: -step(), behavior: "smooth" }); });
      if (next) next.addEventListener("click", function () { track.scrollBy({ left: step(), behavior: "smooth" }); });
    });
  }

  /* ---- Tabs ---- */
  function initTabs() {
    document.querySelectorAll("[data-tabs]").forEach(function (tabs) {
      var buttons = tabs.querySelectorAll(".tabs__head button");
      var panels = tabs.querySelectorAll(".tabs__panel");
      buttons.forEach(function (btn) {
        btn.addEventListener("click", function () {
          var target = btn.getAttribute("data-tab");
          buttons.forEach(function (b) { b.setAttribute("aria-selected", String(b === btn)); });
          panels.forEach(function (p) {
            p.setAttribute("data-active", String(p.getAttribute("data-panel") === target));
          });
        });
      });
    });
  }

  /* ---- Thème clair / foncé (rapport parent, cockpit) ---- */
  function initTheme() {
    document.querySelectorAll("[data-theme-toggle]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var root = document.documentElement;
        var dark = root.getAttribute("data-theme") === "dark";
        root.setAttribute("data-theme", dark ? "light" : "dark");
        var label = btn.querySelector("[data-theme-label]");
        if (label) label.textContent = dark ? "Mode foncé" : "Mode clair";
      });
    });
  }

  /* ---- Reveal on scroll ---- */
  function initReveal() {
    var els = document.querySelectorAll(".reveal");
    if (!("IntersectionObserver" in window) || !els.length) {
      els.forEach(function (el) { el.classList.add("is-in"); });
      return;
    }
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    els.forEach(function (el) { obs.observe(el); });
  }

  /* ---- Année courante dans le footer ---- */
  function initYear() {
    document.querySelectorAll("[data-year]").forEach(function (el) {
      el.textContent = String(new Date().getFullYear());
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    initNav();
    initFelix();
    initVideo();
    initCarousels();
    initTabs();
    initTheme();
    initReveal();
    initYear();
  });
})();
