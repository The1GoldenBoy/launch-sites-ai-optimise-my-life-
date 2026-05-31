# OptimizeMyLife Agent Operating Rules

This repo is the dedicated **OptimizeMyLife static GitHub Pages implementation repo**.

## Absolute Separation

- Empire OS is the command center/source of truth, not the implementation repo.
- Read strategy/specs/assets from:
  `/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/`
- Implement public static-site artifacts only in this repo.
- Do not mix MyCompanion, Goose, OpenClaw workspace experiments, or unrelated project assets into this repo.

## Current Stack

This repo is static GitHub Pages:

- `index.html`
- `styles.css`
- `.github/workflows/pages.yml`

Do not invent npm, Next.js, package.json, or build steps unless Max explicitly approves a stack migration.

## Agent Lanes

- **Claude Code Opus 4.8:** premium French homepage/site rebuild, emotional UX, visual polish, exact Félix placement.
- **Codex 5.5:** support lane: asset manifest/provenance, QA checklist/scripts, risk/readiness reports, alternate section suggestions if assigned.
- **Enzo/Hermes:** orchestration, source discipline, PR review, verification, merge strategy.

One issue = one agent = one branch = one scope. Stop on collisions.

## Félix Identity Lock

Use only approved exact Félix assets from:

`/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/assets/web-image-pack-felix-exact/`

Do not redraw, regenerate, recolor, re-face, or reinterpret Félix. If assets are unavailable, stop and report the blocker; do not invent placeholders except clearly labeled empty slots.

## Copy and Claims

- French public copy.
- Parent/admin copy uses vouvoiement.
- Youth lesson text may use tutoiement only in lesson context.
- No unapproved pricing, checkout, income guarantees, grade guarantees, therapy/medical/legal claims, or school/parent replacement claims.
- CTA stays safe: preview, demo, waitlist, contact — unless Max approves checkout/pricing.

## Verification

Before reporting done:

```bash
git status --short --branch
python3 -m http.server 4173
```

Verify:

- `/` returns 200;
- images load;
- anchors work;
- mobile layout is usable;
- no console errors;
- git diff includes only intended files.
