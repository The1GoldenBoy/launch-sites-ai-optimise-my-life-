# Claude Code Context

OptimizeMyLife is being rebuilt as a premium static GitHub Pages launch site. This repo is implementation only; Empire OS remains the strategic source-of-truth.

## Assignment

- Claude Opus owns the premium homepage/static page rebuild on its own branch.
- Codex owns this support lane: manifest, provenance, QA, and readiness docs.
- Do not treat Codex support docs as a substitute for the premium rebuild; use them to verify assets and reduce merge risk.

## Hard Constraints

- Static site only: edit HTML, CSS, and public assets.
- No Next.js, npm, build step, or package manager unless Max explicitly approves.
- User-facing site copy should be French for the premium rebuild.
- Do not overwrite support docs unless updating them intentionally with new provenance or QA findings.

## Felix Rules

- Use the exact Felix source pack from:
  `/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/assets/web-image-pack-felix-exact/`
- Copy web-ready assets into `assets/felix-exact/` when the rebuild needs them.
- Preserve Felix identity: same face geometry, ears, muzzle, eye color/spacing, orange/cream fur balance, and premium mentor feel.
- Reject cropped ears/head/tail, babyish proportions, distorted muzzle/eyes, fake redraws, and cheap image-warp animation.

## Expected Support Files

- `docs/ASSET_PROVENANCE_AND_FELIX_MANIFEST.md`
- `docs/STATIC_QA_CHECKLIST.md`
- `tools/static_site_check.py`

Run `python3 tools/static_site_check.py` after copying assets and before opening the rebuild PR.
