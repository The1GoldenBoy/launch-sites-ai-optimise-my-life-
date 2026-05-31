/* OptimizeMyLife prototype — light interaction layer.
 * No backend. No auth. No data persistence.
 * Drives: mobile menu, login role tabs, demo login → post-login preview, app screen tabs, report theme toggle.
 */
(function () {
  "use strict";

  // -------- Mobile nav toggle --------
  var burger = document.getElementById("navBurger");
  var mobile = document.getElementById("navMobile");
  var nav = document.querySelector(".nav");
  function setNavOpen(open) {
    if (!mobile || !burger) return;
    mobile.hidden = !open;
    burger.setAttribute("aria-expanded", String(open));
    if (nav) nav.setAttribute("data-mobile-open", String(open));
  }
  if (burger && mobile) {
    burger.addEventListener("click", function () {
      setNavOpen(mobile.hidden);
    });
    mobile.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        setNavOpen(false);
      });
    });
  }

  // -------- Login role tabs --------
  var loginTabs = document.querySelectorAll(".login-tab");
  var loginGreeting = document.getElementById("loginGreeting");
  var greetings = {
    jeune: "Bonjour, prêt·e à choisir une priorité ?",
    parent: "Bienvenue. Voici comment vous suivez le parcours.",
    mentor: "Bonjour mentor. Voici l'aperçu de vos jeunes."
  };
  var currentRole = "jeune";
  loginTabs.forEach(function (btn) {
    btn.addEventListener("click", function () {
      loginTabs.forEach(function (b) {
        b.classList.remove("login-tab--active");
        b.setAttribute("aria-selected", "false");
      });
      btn.classList.add("login-tab--active");
      btn.setAttribute("aria-selected", "true");
      currentRole = btn.dataset.role || "jeune";
      if (loginGreeting) loginGreeting.textContent = greetings[currentRole] || greetings.jeune;
    });
  });

  // -------- Demo login → reveal post-login preview --------
  var loginForm = document.getElementById("loginForm");
  var demoBtn = document.getElementById("demoLogin");
  var postLogin = document.getElementById("postLogin");
  var postLoginTitle = document.getElementById("postLoginTitle");
  var loginNote = document.getElementById("loginNote");

  function revealPreview() {
    if (!postLogin) return;
    postLogin.hidden = false;
    var roleLabel = currentRole === "parent" ? "Parent" : currentRole === "mentor" ? "Mentor" : "Jeune";
    if (postLoginTitle) postLoginTitle.textContent = "Voici ce que vous verriez en mode " + roleLabel + ".";
    if (loginNote) loginNote.textContent = "Aperçu activé. Prototype visuel — aucune authentification réelle.";
    // If parent or mentor, default to the parent report screen.
    if (currentRole !== "jeune") activateScreen("parent");
    // Smooth scroll into post-login preview without changing the URL.
    postLogin.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  if (demoBtn) {
    demoBtn.addEventListener("click", revealPreview);
  }
  if (loginForm) {
    loginForm.addEventListener("submit", function (e) {
      e.preventDefault();
      revealPreview();
    });
  }

  // -------- App screen tabs (post-login) --------
  var screenButtons = document.querySelectorAll(".app-tabs__btn");
  function activateScreen(name) {
    screenButtons.forEach(function (btn) {
      var active = btn.dataset.screen === name;
      btn.classList.toggle("app-tabs__btn--active", active);
      btn.setAttribute("aria-selected", active ? "true" : "false");
    });
    document.querySelectorAll(".screen").forEach(function (el) {
      el.hidden = el.id !== "screen-" + name;
    });
  }
  screenButtons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      activateScreen(btn.dataset.screen);
    });
  });

  // -------- Parent report light/dark toggle --------
  var reportTabs = document.querySelectorAll(".report__tab");
  var reportLight = document.getElementById("report-light");
  var reportDark = document.getElementById("report-dark");
  reportTabs.forEach(function (btn) {
    btn.addEventListener("click", function () {
      reportTabs.forEach(function (b) {
        b.classList.remove("report__tab--active");
        b.setAttribute("aria-selected", "false");
      });
      btn.classList.add("report__tab--active");
      btn.setAttribute("aria-selected", "true");
      var theme = btn.dataset.theme;
      if (reportLight) reportLight.hidden = theme !== "light";
      if (reportDark) reportDark.hidden = theme !== "dark";
    });
  });
})();
