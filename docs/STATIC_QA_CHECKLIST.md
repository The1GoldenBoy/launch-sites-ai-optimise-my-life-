# Static QA Checklist

Use this checklist for the OptimizeMyLife GitHub Pages static site. This repo should remain plain HTML, CSS, and public static assets unless Max explicitly approves a stack change.

## Local Setup

1. Confirm branch and worktree:
   ```bash
   git status --short --branch
   ```
2. Confirm the site is still static:
   ```bash
   find . -maxdepth 2 -name package.json -o -name next.config.\* -o -name vite.config.\*
   ```
   Expected result unless approved: no output.
3. Run the static checker:
   ```bash
   python3 tools/static_site_check.py
   ```
4. Start a local static server:
   ```bash
   python3 -m http.server 4173
   ```
5. Open:
   `http://127.0.0.1:4173/`

## Required File Checks

- `index.html` exists at repo root.
- `styles.css` exists at repo root and is linked from `index.html`.
- Felix assets used by the page are copied under `assets/felix-exact/`.
- Every local image, stylesheet, script, video, poster, and CSS `url(...)` path resolves.
- No `node_modules/`, generated build output, or package-manager files are introduced without approval.

## Browser Checks

- Hard refresh the local preview.
- Check the browser console for 404s, CSP errors, or JavaScript errors.
- Click every nav item, CTA, skip link, carousel control, FAQ toggle, and form-like control.
- Verify every `href="#section"` target exists on the page.
- Verify external links open intentionally and do not block review.
- Confirm the page works with JavaScript disabled if no JavaScript is required.

## Responsive Checks

Check at least these widths:

- 375px mobile
- 768px tablet
- 1024px laptop
- 1440px desktop

For each width:

- No horizontal scroll.
- Text does not overflow buttons, cards, badges, or nav.
- Felix images keep ears, head, paws, and tail visible where intended.
- CTAs remain usable with at least 44px touch targets.
- Hero content leaves a visible hint of the next section on common desktop and mobile viewports.

## Content And Claim Checks

- Premium rebuild user-facing copy is French.
- No fake checkout or live pricing is introduced without Max approval.
- Youth outcomes are framed responsibly and not guaranteed.
- Privacy, safety, legal, school, institutional, or medical-adjacent claims stay conservative unless approved.
- Felix is presented as the OptimizeMyLife guide/mentor, not a generic AI mascot.

## Asset Checks

- Compare copied assets against `docs/ASSET_PROVENANCE_AND_FELIX_MANIFEST.md`.
- Confirm copied file names and SHA-256 hashes match the manifest unless an intentional optimized derivative is documented.
- If an optimized derivative is created, keep the original manifest asset in the repo or document the exact derivative process.
- Prefer `object-fit: contain` for Felix unless the crop is visually verified.
- Every image has useful `alt` text or an intentional empty `alt=""` for purely decorative usage.

## PR Readiness

- `git status --short --branch` shows only intended changes before commit.
- `python3 tools/static_site_check.py` passes or any remaining failures are listed as Claude/Max approval TODOs.
- Include screenshots or a review link for desktop and mobile when the page implementation changes.
- Do not merge to `main` or publish GitHub Pages without Max approval.
