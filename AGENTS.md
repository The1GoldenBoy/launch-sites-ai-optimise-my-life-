# Agent Instructions

This repository is the static GitHub Pages implementation repo for OptimizeMyLife. Empire OS is the command center and source-of-truth, not the implementation repo.

## Current Lane

- Keep work on `codex/THE-15-support-manifest-qa` unless Max or Enzo assigns another branch.
- Codex support work owns manifests, provenance, QA checklists, static-readiness scripts, and repo-local agent instructions.
- Claude Opus owns the premium homepage rebuild on a separate branch.
- Do not overwrite `index.html` or `styles.css` for the main rebuild unless explicitly assigned to that implementation lane.

## Stack Rules

- This is a static GitHub Pages repo.
- Use plain HTML, CSS, and public static assets.
- Do not add Next.js, npm, package managers, bundlers, or framework config unless explicitly approved.
- Keep implementation files public-safe. Do not copy private Empire OS notes into deployed site content.

## Source Rules

- Read relevant command-center docs from:
  `/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/`
- Approved Felix web asset source pack:
  `/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/assets/web-image-pack-felix-exact/`
- Copy approved public-safe assets into this repo only when implementation needs them, and document provenance.
- Do not redraw Felix, invent a replacement mascot, or use off-model generated Felix imagery.

## Verification

- Run `git status --short --branch` before and after changes.
- For static checks, use `python3 tools/static_site_check.py` when present.
- Preview with a local static server such as `python3 -m http.server 4173`.
- Max approval is required before publishing to production/main, pricing, checkout, youth outcome claims, privacy/safety claims, paid ads, or external outreach.
