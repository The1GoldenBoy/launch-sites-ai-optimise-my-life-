# 00 — MASTER PLAN CONSOLIDÉ — OptimizeMyLife (app mobile)

> **Version :** 2026-06-16, finalisée après la 3e compétition (tournoi de styles, voir
> `PLANS NUIT 2026-06-16/01-STYLES-TOURNOI.md`).
> **C'est LE plan qu'on suit.**
>
> ⚠️ **Limite d'honnêteté de cette version :** elle a été compilée dans une session GitHub remote qui n'a
> PAS accès aux fichiers locaux des compétitions 1, 3 et 4 (`Mobile Concept\MASTER PLAN MOBILE 2026-06-15\`,
> `02-FEATURE-PLAN-par-page.md`, `03-MARKETING-PLAN-lancement.md`). J'ai intégré la **3e compétition en
> entier** (rejouée ici) + tout l'état verrouillé de la passation. Pour les sections marquées
> **[RÉCONCILIER]**, croise avec tes plans locaux détaillés avant de coder — je ne veux pas réécrire par
> mémoire ce qui existe déjà en mieux en local.

---

## 1. THÈSE & MOAT

**Promesse :** *Become provably good at AI in 15 min/day.*
**ICP (verrouillé, panel marketing) :** « The Exposed Professional » — adulte 28-45, peur que l'IA le
remplace, paie seul. Il n'achète pas du *contenu* (Brilliant/Coursera le font moins cher) ; il achète de
**l'anxiété convertie en preuve mesurable**.

**Moat (3 couches, du plus copiable au moins copiable) :**
1. **La preuve.** Mesurer la *readiness IA* et la faire monter — pas « apprendre », « prouver qu'on n'est plus
   remplaçable ». (Insight clé du tournoi : c'est le territoire « instrument de mesure », non occupé en edtech IA.)
2. **Félix, humain réel.** Coach identité-lockée, founder-led. Dans le bon style, il devient l'*expert qui lit
   ton dossier*, pas un avatar de chatbot.
3. **Le high-ticket on-site.** Service founder-led à 10k$+ (Max prend l'avion). Inimitable par un concurrent
   logiciel. C'est l'escalade logique de la mesure, façon bilan santé → consultation.

---

## 2. SYSTÈME DE LOOK PAR AUDIENCE

**État verrouillé :** 2 styles retenus à l'origine (Warm Minimal + Command Center), Editorial SORTI.
**Apport du tournoi :** un 3e style sérieux a émergé — **« Le Dossier » (Clinical Confidence)** — recommandé
par 3 critiques sur 4 pour l'adulte.

| Audience | Style recommandé | Pourquoi |
|---|---|---|
| Kids 9-14 | **Warm Minimal v2** | chaleur, accueil, ludique-mais-propre |
| Ados 15-20 | **Command Center v2** (nettoyé) | esthétique OS/gaming, edgy/dark |
| Adultes (ICP) | ⚠️ **DÉCISION OUVERTE** | 3 options codables — voir ci-dessous |

### 🔴 LA décision ouverte : look adulte
Trois candidats, tous prototypables via le toggle sur `/dashboard` :
- **(a) Warm Minimal v2** — directive Max d'origine (clean/friendly-premium).
- **(b) Command Center v2** — reco panel marketing (~70/30), MAIS doit être nettoyé (voir tournoi : tuer le
  boot terminal, sortir la mono de la lecture, fixer Félix sur sombre).
- **(c) ⭐ Le Dossier** — reco du tournoi de styles. Incarne « provably », honnêteté native, Félix expert-lecteur,
  high-ticket = escalade logique.

**Action :** Max flippe le toggle, compare les 3 sur `/dashboard`, tranche → on verrouille `lib/audience.ts`.
**Reco synthèse :** (c) Le Dossier pour l'adulte. Argument complet dans `01-STYLES-TOURNOI.md`.

### Corrections de style non négociables (toutes audiences, issues du panel UX)
1. **CTA principal du jour en sticky bottom** (zone pouce), jamais en héros à scroller.
2. **Contraste AA réel** : texte ≥ 4.5:1, lignes structurantes ≥ 20 % d'opacité (jamais 8-12 %), cibles
   tactiles ≥ 48px.
3. **Toute animation skippable ≤ 300ms**, désactivée après le 1er run, `prefers-reduced-motion` respecté.

### Contraintes visuelles verrouillées
- Vraie app, **jamais un poster**. UI flat/clean. **ZÉRO golden-hour.**
- Palette : blanc #ffffff + orange #f4731f + ink #0a0a0a. Zéro beige/gris décoratif (gris *fonctionnel* OK —
  correction du tournoi sur Warm Minimal).
- Félix identité-lockée : réf `Felix Identity\S09-T01.png` + « match exact identity + flat app lighting » à
  CHAQUE génération. Jamais golden-hour comme réf mobile.

---

## 3. SPEC PAR PAGE (les 13 écrans)

Format : but · features CORE (existe ou prioritaire) · features ADVANCED [RÉCONCILIER avec
`02-FEATURE-PLAN-par-page.md`] · note de look.

1. **/welcome + /meet (Meet Félix)** — *But :* premier contact, établir Félix comme humain crédible (pas un bot).
   CORE : portrait flat, promesse « provably good… 15 min/jour », CTA commencer. ADVANCED : micro-séquence
   d'entrée *honnête* (PAS de boot terminal faux). Look : Félix héros, cadrage buste, regard caméra.
2. **/menu (Command Menu)** — *But :* navigation code-style. CORE : accès rapide aux écrans. Look : la signature
   « OS » de Command Center peut vivre ici même si l'adulte choisit un autre style ailleurs.
3. **/dashboard** — *But :* l'écran de retour quotidien. CORE : Next-Best-Action (sticky bottom) + ring de
   readiness + stats honnêtes + modules + AI Pulse (honnête/état vide) + coach Félix + carte high-ticket (bas).
   C'est l'écran-toggle où Max tranche le look adulte.
4. **/learn** — *But :* parcours 12 chapitres → leçon → exam. CORE : liste chapitres, états (fait/en cours/
   verrouillé), leçon lisible (Inter, ~60ch), exam = la *preuve*. ADVANCED [RÉCONCILIER].
5. **/products-mobile** — *But :* vitrine des boîtes/cours. CORE : packshots `box-*.png`, prix honnêtes.
6. **/product/[slug]** — *But :* page de vente. CORE : titre, promesse, prix honnête (jamais faux barré),
   CTA sticky, « ce que tu obtiens », curriculum, mot de Félix founder-led. ADVANCED [RÉCONCILIER].
7. **/progress** — *But :* matérialiser la readiness dans le temps. CORE : données réelles ou état vide honnête.
8. **/profile** — *But :* compte + modules réels câblés. CORE : déjà câblé aux modules réels.
9. **/parents** — *But :* showcase parent (`// sample`). CORE : marquer clairement « échantillon ».
10. **/den** — [RÉCONCILIER] *À re-skin au thème audience.*
11. **/certification** — [RÉCONCILIER] *À re-skin au thème audience.* Renforce le claim « provably ».
12. **exam** — *But :* la preuve mesurable. CORE : feedback honnête (jamais score gonflé), résultat = ring +
    « ce qu'il te reste à revoir ». À re-skin au thème.
13. **High-ticket (composant partagé `HighTicketCard`)** — *But :* vendre le service on-site. CORE : « Programme
    d'Optimisation Personnalisée », « à partir de 10 000 $ » (affiché, jamais caché), CTA *secondaire* « réserver
    une consultation gratuite » (conversation, pas achat impulsif), ligne « aucune pression ».

---

## 4. FUNNEL & HIGH-TICKET

- **Acquisition :** short-form vidéo (Félix) + email (verrouillé, panel marketing). [RÉCONCILIER avec
  `03-MARKETING-PLAN-lancement.md`.]
- **Échelle de valeur :** cours/boîtes (entrée) → progression mesurée → **escalade vers le high-ticket on-site
  10k$+** présentée comme la lecture logique des métriques (« tes mesures justifient une intervention »).
- **Honnêteté :** zéro faux prix/témoignage/IA/donnée. Consultations *gratuites* réelles. Le high-ticket se vend
  par conversation, pas par tap.
- **NE PAS toucher :** Lemon Squeezy / prix / `checkout.ts` (décision Max). `activation.ts` = seulement le champ
  additif `purchaserType`.

---

## 5. ARCHITECTURE CODE — fait vs à-faire

**FAIT (branche `mobile-phase-0`, build prod vert, 13 commits `e451b75`→`43d6857`, repo privé
`github.com/The1GoldenBoy/oml-mobile-app`) :**
- App mobile complète role-adaptive, navigable. Base partagée `components/mobile/ui.tsx`
  (useAudienceUI, AudienceToggle, MobileTabBar, Ring, ScreenFrame, Body, HighTicketCard) + `lib/audience.ts`
  (3 thèmes) + toggle de preview par écran. Les 13 écrans existent. High-ticket intégré. `/profile` câblé aux
  modules réels.

**À FAIRE (recommandation d'architecture issue du tournoi — ingénieur buildabilité) :**
1. **Refondre `lib/audience.ts` en résolveur de tokens.** Deux axes *orthogonaux* (STYLE × AUDIENCE), PAS 6 forks.
   Sortie = un dictionnaire de variables CSS, pas des couleurs en dur.
2. **`@theme` Tailwind v4** : déclarer toutes les variables `--oml-*` (bg, surface, ink, accent, radius, shadow,
   border, font-sans/mono, density/gap/pad/tap, scale, photo-overlay). Pilotées par `data-style` + `data-audience`
   sur `ScreenFrame`. Les composants lisent des *tokens*, jamais `style`/`audience` directement.
3. **`ScreenFrame`** = point d'entrée mince qui injecte `data-*` + variables. Dériver le thème par CSS, pas par
   `setState` (évite le piège react-hooks).
4. **Token-driven :** `Body`, `Ring`, `MobileTabBar`, `HighTicketCard`, `AudienceToggle`.
5. **Seule vraie variante structurelle :** le layout de cartes — `<CardGrid variant>` (pile arrondie Warm /
   bento Command / lignes-instrument Le Dossier). C'est le seul endroit où le DOM change.
6. **`<FelixImage screen audience>`** : `next/image` WebP, `priority` sur le seul hero, `loading="lazy"` ailleurs,
   placeholder blur, **état vide honnête** si image manquante (jamais un carré cassé, jamais le fallback d'une
   autre audience). Nommage `/public/felix/{screen}-{audience}.webp`.
7. **Coût relatif :** Command Center ≈ 1.6-2× Warm Minimal (bento + lisibilité photo sombre + tabular).
   Le Dossier ≈ Warm Minimal (white-base, token-driven) une fois les hairlines réglées.

---

## 6. ORDRE DE BUILD

1. `lib/audience.ts` → résolveur de tokens (source de vérité). Rien ne bouge avant.
2. `@theme` Tailwind v4 : variables `--oml-*` + utilities. **Débloque 11 des 13 écrans sans les toucher.**
3. `ScreenFrame` : injection `data-style`/`data-audience` + variables.
4. **Warm Minimal d'abord, full token-driven** → baseline verte de référence.
5. `<CardGrid>` (bento + lignes-instrument) : la seule variante structurelle par-écran.
6. `<FelixImage>` + états vides honnêtes.
7. `AudienceToggle` étendu pour basculer AUSSI le style en preview → **c'est là que Max tranche le look adulte.**
8. Étape locale : générer le pack d'images GPT (voir `00-GPT-IMAGE-PROMPTS-CONSOLIDÉS.md` + `01-STYLES-TOURNOI.md`),
   les brancher via `<FelixImage>`.
9. Câbler les vraies données (sample → `lib/progress` / `lib/volumes`), re-skin `/den` + `/certification` + exam.

**Pièges à coder autour :** `rm -rf .next` avant rebuild après déplacement de routes ; `queueMicrotask` pour tout
`setState` dans `useEffect` ; texte `//` dans JSX → `{"// ..."}` ; `npx eslint <fichiers>` (pas `next lint --file`) ;
commits SCOPÉS (`git add <fichiers>`, jamais `-A`), toujours sur `mobile-phase-0`, jamais merger master sans OK Max.

---

## 7. TROIS FAÇONS D'ÉCHOUER

1. **Trancher le look adulte par goût au lieu du toggle.** Les 3 styles existent justement pour décider sur
   pièce. Choisir Command Center sans le nettoyer = violer l'honnêteté (boot terminal) + Félix cireux + ICP
   aliéné.
2. **Coder 6 thèmes au lieu de 2 axes de tokens.** Duplication ingérable. STYLE × AUDIENCE = tokens orthogonaux,
   une seule variante structurelle (`CardGrid`).
3. **Trahir l'honnêteté pour « remplir » l'UI.** Faux ring, fausse AI Pulse, fausses specs, faux badge live. La
   marque entière repose sur la preuve réelle ou l'état vide assumé. C'est aussi le critère qui a disqualifié
   Command Center dans le tournoi.

---

## 8. CE QUI RESTE STRICTEMENT LOCAL (pas faisable en session remote)

- **Étape 3 — génération d'images GPT** (app ChatGPT desktop, computer-use, réf Félix, ~4 min/image).
- **Étape 4 — coder dans `oml-mobile-app`** (repo privé, branche `mobile-phase-0`) : non accessible depuis
  cette session, verrouillée sur un autre repo. Les recommandations d'architecture ci-dessus sont prêtes à
  appliquer en local.
