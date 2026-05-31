# Codex Implementation Plan - THE-13

Planning-only artifact for the OptimizeMyLife premium static GitHub Pages rebuild. This document is scoped to Codex 5.5's independent plan and does not modify `index.html`, `styles.css`, or any asset file.

## 1. Assumptions Verified

- The current repository is a static GitHub Pages scaffold at `/mnt/c/Users/MAX/Documents/GitHub/launch-sites-ai-optimise-my-life-`.
- Tracked working files visible in the repo are `README.md`, `index.html`, `styles.css`, `.gitignore`, `.nojekyll`, and `.github/workflows/pages.yml`.
- `README.md` describes an initial setup and says to open `index.html` directly in a browser.
- `index.html` is currently an English starter hero. It references only `styles.css`.
- `styles.css` is a small standalone stylesheet with no framework dependency.
- `.github/workflows/pages.yml` deploys the repository root (`path: "."`) to GitHub Pages on pushes to `main` and manual dispatch.
- `.nojekyll` is present, so GitHub Pages should serve static files without Jekyll processing.
- No `assets/` directory exists in this repo at inspection time.
- No `docs/` directory existed before this THE-13 plan file was created.
- Hidden `.agents/` and `.codex/` directories are present but empty at inspected depth.
- The Empire OS source folder is readable at `/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/`.
- The Linear connector did not fetch a live `THE-13` issue by key in this session. The Empire OS control note does list `THE-13 - Codex 5.5 independent implementation plan - Codex`, so this document treats the user prompt plus that local note as the working source.
- The local control note references `AGENTS.md` and `ENZO_COORDINATION_README.md`, but those files were not present in this repo when inspected.
- The stronger Junior course vault is readable at `/mnt/c/Users/MAX/.openclaw/OpenClaw Memory Vault/OpenClaw Memory Vault/Projects/OptimizeMyLife/`; its `00-INDEX.md` marks the folder as official/up-to-date and lists 8 validated French Tome 1 chapters. File presence was verified for `FR/ch-01.md` through `FR/ch-08.md`.

## 2. Repo Constraints

- Treat this repo as plain static HTML/CSS unless a future issue explicitly changes the stack.
- Do not invent npm, Next.js, build, lint, or package-manager commands for this repo.
- Keep the deployable surface rooted at `/` because the Pages workflow uploads the whole repo.
- Any future public implementation must be careful that `docs/` is also part of the Pages artifact unless the workflow is changed later.
- Avoid third-party runtime dependencies. If a small script is needed later, keep it inline or in a local static JS file.
- Preserve accessibility and performance without relying on a build step.
- Future implementation should change `html lang` to `fr` for the French rebuild.
- Do not activate checkout, paid ads, outreach, or sensitive youth claims without Max approval.

## 3. Source Documents To Use

Use these local sources as inputs, with the noted confidence level:

- `README.md` - repo status and static usage, verified in repo.
- `.github/workflows/pages.yml` - GitHub Pages deployment behavior, verified in repo.
- `/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/PROJECT_CONTROL.md` - current mandate, source pointers, execution order.
- `/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/OPTIMIZEMYLIFE_IMPLEMENTATION_PLAN.md` - trust/demo/challenge/proof priority map.
- `/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/SOURCE_OF_TRUTH_SNAPSHOT.md` - warns against editing wrong OptimizeMyLife copies.
- `/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/assets/oml-multi-agent-rebuild-control-note-2026-05-30.md` - multi-agent ownership, THE-11 through THE-16 track, guardrails.
- `/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/assets/volume-1-felix-first-landing-page-copy-fr.md` - strongest French landing-page copy draft, but not approved for public use until Max gates are cleared.
- `/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/assets/volume-1-landing-page-brief.md` - Volume 1 promise, 7-day structure, parent trust notes.
- `/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/assets/junior-tome-1-conversion-and-release-brief-2026-05-30.md` - release path and current unresolved source/audience/price decisions.
- `/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/assets/parent-trust-center-brief.md` - trust center structure and safety language.
- `/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/assets/felix-direct-seller-voice-system.md` - Felix voice and sales tone guardrails.
- `/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/assets/course-architecture-youth-family-adult.md` - broader youth/family/adult ladder; use only as architecture, not as approved public pricing.
- `/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/assets/true-course-source-map-2026-05-28.md` - source priority and recovery notes.
- `/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/assets/plans-de-cours-produits-vrais-2026-05-28.md` - chapter architecture by product.
- `/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/assets/liste-chapitres-titres-par-produit-2026-05-28.md` - concise chapter title list.
- `/mnt/c/Users/MAX/.openclaw/OpenClaw Memory Vault/OpenClaw Memory Vault/Projects/OptimizeMyLife/00-INDEX.md` - verified local course index for Junior Tome 1.
- `/mnt/c/Users/MAX/.openclaw/OpenClaw Memory Vault/OpenClaw Memory Vault/Projects/OptimizeMyLife/Livre-Tome-1-JUNIOR/FR/ch-01.md` through `ch-08.md` - verified French chapter manuscripts. Do not publish full manuscript content without approval.

Missing or unresolved:

- Live Linear issue `THE-13` was not fetched by the connector.
- Final public route, CTA behavior, checkout/waitlist behavior, and price are not verified.
- Audience wording conflicts across notes: `9-14`, `12-14`, `preados/ados`, and broader youth/families all appear. Max must approve the public wording.
- Price conflicts exist: `9.99 CAD`, `79 $`, and family-bundle experiments appear in sources. Do not lock a price in the page until approved.
- Chapters 9 and 10 for Junior Tome 1 are not verified as completed manuscripts.

## 4. Exact Felix Assets To Use

Primary asset source:

`/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/assets/web-image-pack-felix-exact/`

The pack README and manifest state that Felix is not redrawn and that the visuals use the exact Felix/product from Max's provided reference image on white backgrounds. Use this pack for the rebuild, not generated substitutes.

Verified files and dimensions:

- `00-source-felix-crop-exact.png` - 393 x 570, RGBA.
- `00-source-product-cutout-exact-felix.png` - 668 x 996, RGBA.
- `01-hero-landing-felix-exact-white.jpg` - 2200 x 1300.
- `02-product-box-junior-exact-felix-white.jpg` - 1600 x 2000.
- `03-course-card-junior-exact-felix-white.jpg` - 1400 x 1400.
- `04-course-lineup-junior-teen-adult-felix-exact-white.jpg` - 2200 x 1300.
- `04-course-lineup-junior-teen-adult-felix-exact-white-v2.jpg` - 2200 x 1300.
- `05-felix-ai-live-feature-exact-white.jpg` - 2200 x 1300.
- `06-parent-trust-section-felix-exact-white.jpg` - 2200 x 1300.
- `07-project-modules-felix-exact-white.jpg` - 2200 x 1300.
- `07-project-modules-felix-exact-white-v2.jpg` - 2200 x 1300.
- `08-checkout-offer-felix-exact-white.jpg` - 1800 x 1200.
- `09-social-square-junior-felix-exact-white.jpg` - 1600 x 1600.
- `10-footer-cta-banner-felix-exact-white.jpg` - 2400 x 900.
- `00-contact-sheet-all-images.jpg` - reference contact sheet, not a site image.

Secondary asset source:

`/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/assets/felix-expression-pack/`

The expression-pack README says these are newly generated expression variants that should be approved visually before becoming final mascot masters. Do not use them as final public Felix assets unless Max explicitly approves them.

Asset handling rules:

- Preserve Felix exactly: no redraw, no generative replacement, no recolor, no face/body edits, no illustrative reinterpretation.
- Copy selected assets byte-for-byte into the future repo `assets/` folder.
- Use CSS sizing, `object-fit`, and layout containers only. Avoid CSS filters, masks, heavy cropping, artificial shadows over Felix, or transformations that alter the mascot.
- If a crop is needed, use the already provided exact crop PNG rather than making a new crop.
- Keep source filenames traceable or maintain a manifest mapping source path to repo path.

## 5. Recommended Rebuild Shape

Phase 1 should be a premium French single-page static site in `index.html` with anchored sections. This fits the current repo and Pages workflow.

Recommended sections:

1. Top navigation: brand, anchored links, primary CTA.
2. Hero: exact hero asset, French headline from the Volume 1 draft, CTAs for "Voir la demo de Felix" and "Recevoir l'aperçu" or another approved non-checkout action.
3. Problem: random AI use is the risk; structured AI use is the path.
4. Felix mentor block: Felix speaks directly, warm and direct, using approved voice-system tone.
5. Parent Trust Center summary: safety, visibility, boundaries, no therapy/school/professional replacement.
6. Tome 1 / Fondation IA preview: show the 8 verified chapter outcomes, not full manuscript content.
7. Seven-day starter path: Life Map, Focus Reset, Project Plan, Habit Loop, Confidence Script, Parent/Mentor Check-In, 30-Day Plan.
8. Sample lesson CTA: recommend Chapter 4 angle ("Apprendre 3x plus vite avec l'IA") plus a safety bridge from Chapter 3 or 5.
9. Safeguards: no guaranteed grades, no medical/psychological claims, no cheating, no secrecy from parents.
10. Future path: Tomes 2-4 and teen/adult/Home/Work direction only as a light roadmap, clearly not a promise of current availability unless approved.
11. FAQ: adapt from the French landing copy and Parent Trust Center, removing unresolved claims.
12. Final CTA: waitlist/demo/preview until checkout and pricing are approved.

Optional Phase 2 static pages after Max approval:

- `parents.html` - full Parent Trust Center.
- `demo-felix.html` - static Felix demo script or lightweight interactive demo.
- `apercu-tome-1.html` - sample lesson/preview.
- `faq.html` - expanded FAQ and disclaimers.

## 6. Future File Architecture

Current THE-13 change:

```text
docs/
  CODEX_IMPLEMENTATION_PLAN_THE-13.md
```

Recommended future implementation layout:

```text
/
  index.html
  styles.css
  .nojekyll
  README.md
  assets/
    felix-exact/
      00-source-felix-crop-exact.png
      00-source-product-cutout-exact-felix.png
      01-hero-landing-felix-exact-white.jpg
      02-product-box-junior-exact-felix-white.jpg
      03-course-card-junior-exact-felix-white.jpg
      04-course-lineup-junior-teen-adult-felix-exact-white-v2.jpg
      05-felix-ai-live-feature-exact-white.jpg
      06-parent-trust-section-felix-exact-white.jpg
      07-project-modules-felix-exact-white-v2.jpg
      08-checkout-offer-felix-exact-white.jpg
      10-footer-cta-banner-felix-exact-white.jpg
    manifest-felix-source-map.json
  docs/
    CODEX_IMPLEMENTATION_PLAN_THE-13.md
```

Avoid adding generated build outputs, dependency lockfiles, or app-framework scaffolding unless a later issue explicitly changes the repo from static to app-based.

## 7. Task Sequence For Implementation

1. Confirm the branch and working tree before editing: `git status --short --branch`.
2. Create a Codex-owned branch, for example `codex/THE-15-alternate-static-sections` if implementing the later Codex alternate branch.
3. Reconfirm Max-approved decisions before public copy: audience, price, checkout/waitlist behavior, route names, and youth-sensitive wording.
4. Copy only the selected exact Felix assets into `assets/felix-exact/`.
5. Record asset provenance in `assets/manifest-felix-source-map.json`, including original source paths and checksums if practical.
6. Rewrite `index.html` as a French static landing page with semantic sections and anchor navigation.
7. Rewrite `styles.css` for a premium, responsive, white/clean product experience using the exact visual assets.
8. Keep CTAs non-destructive and non-checkout until approval. Use inert anchors, `mailto:`, or approved waitlist/demo links only.
9. Test locally by opening `index.html` and, if needed, serving the repo with `python3 -m http.server`.
10. Verify desktop and mobile screenshots, console errors, image loading, anchors, keyboard navigation, and responsive text wrapping.
11. Confirm Pages workflow still deploys root static files without build changes.
12. Commit only the intended Codex-owned files on the Codex branch.

## 8. Risks

- Exact Felix integrity can be broken by regenerating, redrawing, recoloring, over-cropping, or using the unapproved expression pack.
- Source conflicts can leak into public copy, especially age range and pricing.
- The current repo has no asset folder, so implementation must add assets deliberately and traceably.
- GitHub Pages deploys the full repo root; docs and internal planning files may be publicly visible unless workflow scope changes later.
- The existing starter page is English and generic; a French premium rebuild must replace content comprehensively in a future implementation, not just patch text.
- Checkout or paid claims could go live too early if CTA behavior is not gated.
- Course manuscript excerpts could be over-published before Max approves release status.
- Claude Opus and Codex branches can overwrite each other if both edit root static files without a later integration owner.

## 9. Acceptance Criteria

For this THE-13 task:

- Only `docs/CODEX_IMPLEMENTATION_PLAN_THE-13.md` is added.
- `index.html`, `styles.css`, and assets remain untouched.
- The plan lists verified assumptions, repo constraints, source docs/assets, sections/pages, file architecture, task sequence, risks, acceptance criteria, visual QA, and multi-agent separation rules.
- Missing or unresolved information is stated instead of guessed.
- Felix preservation is explicit and strict.

For a later implementation task:

- The site is a French premium static GitHub Pages experience.
- The page works without npm, framework build output, or external runtime dependencies.
- Exact Felix assets are used from the approved local image pack and remain visually unchanged.
- No generated placeholder or unapproved expression variant appears as final Felix.
- All visible claims are approved, careful, and free of guaranteed educational, medical, psychological, financial, or legal outcomes.
- CTAs match the approved behavior and do not activate checkout prematurely.
- The page is responsive, accessible, fast, and free of broken images/anchors.
- The GitHub Pages workflow remains valid.

## 10. Visual QA Checklist

- Confirm every visible Felix image comes from `web-image-pack-felix-exact` or an explicitly approved replacement.
- Compare copied asset checksums against the local source pack after copying.
- Inspect desktop around 1440 px, laptop around 1280 px, tablet around 768 px, and mobile around 390 px.
- Verify no text overlaps images, cards, buttons, navigation, or the next section.
- Verify headline and button text wraps cleanly in French.
- Check that the hero shows the real product/Felix signal in the first viewport.
- Confirm section rhythm feels premium and product-specific, not generic SaaS.
- Confirm the page is not dominated by one color family and does not rely on decorative gradient/orb backgrounds.
- Check image aspect ratios and avoid distorted Felix/product boxes.
- Verify links, anchor offsets, focus states, hover states, and keyboard tab order.
- Check contrast for body copy, CTA text, captions, and trust/disclaimer text.
- Confirm no browser console errors and no missing asset requests.
- Confirm the Pages deployment artifact would include every referenced image path.

## 11. Keeping Codex Output Separate From Claude Opus

- This file is the Codex THE-13 planning artifact. Claude Opus should not edit it unless the integration owner explicitly asks for a merged plan.
- Codex future implementation work should happen on a Codex-named branch and be committed with `THE-13`, `THE-15`, or the relevant Linear key in the commit message.
- Claude Opus prototype work should remain on its own Claude-named branch for THE-14.
- Do not copy Claude-generated sections into Codex output without marking them as imported during the THE-16 merge/review step.
- Do not overwrite root `index.html`/`styles.css` on a shared branch while Claude is also producing a prototype. Compare branches first, then merge intentionally.
- Use repo truth for implementation files, Linear truth for issue ownership/status, and Empire OS truth for product/source decisions.
- The THE-16 best-of merge should be the first place where Claude Opus and Codex visual/copy variants are intentionally combined.
