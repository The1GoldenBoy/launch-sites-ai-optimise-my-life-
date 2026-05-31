# Asset Provenance And Felix Manifest

This file documents the approved Felix web image source pack for the OptimizeMyLife static GitHub Pages rebuild.

## Source Location

- Source folder: `/mnt/c/Users/MAX/Documents/Empire OS/01_Projects/OptimizeMyLife/assets/web-image-pack-felix-exact/`
- Source README: `README.md` in that folder
- Source manifest: `manifest.json` in that folder
- Manifest source reference: `/home/max/.hermes/image_cache/img_fdad57f2086f.jpg`
- Source rule: Felix is not redrawn. The web images preserve the exact Felix/product from Max's provided product-box reference and place it on white backgrounds.

Do not move the source-of-truth folder into this repo wholesale. Copy only approved public-safe web assets needed by the static site, and keep provenance documented here.

## Source Inventory

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `00-contact-sheet-all-images.jpg` | 287680 | `86032dca953a412e991838d39bbd2ee4514ab5381d52eab3330ff224054330ee` |
| `00-source-felix-crop-exact.png` | 329348 | `5e5d608b5719fcabf66f32251c6ee00f66385b2dbc62ea659fd5fdf9b22a63af` |
| `00-source-product-cutout-exact-felix.png` | 632772 | `a5ccb692a36223dba804b10c5f59afd2f5f000f234a50fe48d2f60ced5c0953c` |
| `01-hero-landing-felix-exact-white.jpg` | 302473 | `bf3f065018cde6519a36443e84e9e621e4bb1031a8887288946753605e7dedef` |
| `02-product-box-junior-exact-felix-white.jpg` | 385905 | `640b2c2069722952636645f52bd317c22f6567797dbe80ec9e39fc419f113fcd` |
| `03-course-card-junior-exact-felix-white.jpg` | 177538 | `ce4c0e46dbd3f2827e82eb400096c8c82ea0d73f96160f36915ad0357f4b12c2` |
| `04-course-lineup-junior-teen-adult-felix-exact-white-v2.jpg` | 161419 | `a30176d914379c438b63274d8083caf76208ac0eb742d485b028fba6044fa8a8` |
| `04-course-lineup-junior-teen-adult-felix-exact-white.jpg` | 281840 | `c945db0ea0bb2957606bbb5c959b0c4c6adceff2501117b969be9eb52a01d49d` |
| `05-felix-ai-live-feature-exact-white.jpg` | 303225 | `fb28bdb64d9288756f46e053c224dc4d95f3b121b51470e95c9df09de8dd82a1` |
| `06-parent-trust-section-felix-exact-white.jpg` | 165017 | `475cee63de0593f103979d1c3224060bb4a06fb5ffa069f9722bb0d70ad98dc8` |
| `07-project-modules-felix-exact-white-v2.jpg` | 155437 | `28c7455b79efe071682e9c2c30394321a5578e683c8e4673092e6ff1cb06a8ba` |
| `07-project-modules-felix-exact-white.jpg` | 352250 | `d0c53798339b05b30884fb3b7a99f7a58c46a3baa0fe4acbbb3f43454db4a8f5` |
| `08-checkout-offer-felix-exact-white.jpg` | 220843 | `a372e022a0cdf50c407fe858ca6fdf515ef757c81a4ad37d71443461801daf87` |
| `09-social-square-junior-felix-exact-white.jpg` | 204361 | `840c8f26b41da23e21843f0d4391e808b0ab2c7efcead5d6eaf83bf31775efdf` |
| `10-footer-cta-banner-felix-exact-white.jpg` | 177711 | `667e07243d54fc7275cbf78c2e6a4651377fab37a1a3ff7af4cdf7a2e06503ad` |
| `README.md` | 1082 | `54638bc8e5783555f53da2f5e27559f9fd67c51dbd1e01bc76f80944ce373ef3` |
| `manifest.json` | 2014 | `e2fe68a1d3079128d93429e0d856db3377d637f80c3119cb0d86bfda68648cb4` |

## Copy Plan For The Rebuild

When Claude's static rebuild is ready to integrate image assets, copy the following web assets into:

`assets/felix-exact/`

Required web assets:

- `01-hero-landing-felix-exact-white.jpg`
- `02-product-box-junior-exact-felix-white.jpg`
- `03-course-card-junior-exact-felix-white.jpg`
- `04-course-lineup-junior-teen-adult-felix-exact-white.jpg`
- `05-felix-ai-live-feature-exact-white.jpg`
- `06-parent-trust-section-felix-exact-white.jpg`
- `07-project-modules-felix-exact-white.jpg`
- `08-checkout-offer-felix-exact-white.jpg`
- `09-social-square-junior-felix-exact-white.jpg`
- `10-footer-cta-banner-felix-exact-white.jpg`

Optional implementation assets:

- `04-course-lineup-junior-teen-adult-felix-exact-white-v2.jpg` if visually selected over the original lineup file.
- `07-project-modules-felix-exact-white-v2.jpg` if visually selected over the original project-modules file.
- `00-source-felix-crop-exact.png` only if the page needs a standalone Felix crop and the crop passes visual QA.
- `00-source-product-cutout-exact-felix.png` only if the page needs a standalone product cutout.

Do not copy `00-contact-sheet-all-images.jpg`, source `README.md`, or source `manifest.json` into the public site unless a reviewer explicitly needs them in the repo.

## Usage Rules

- Keep Felix on-model. Do not redraw, trace, regenerate, or replace him with a different mascot.
- Preserve the exact asset pixels when copying. Recompression, resizing, and format conversion need explicit visual QA.
- Add descriptive `alt` text for every Felix image in the HTML.
- Avoid cropping off ears, head, paws, or tail in CSS. Use `object-fit: contain` unless the crop is manually verified.
- Keep enough padding around Felix for desktop, mobile, and social-card crops.
- Do not add text directly into Felix image files. Put page copy in HTML.
- Do not publish checkout, pricing, guaranteed youth outcomes, privacy/safety claims, paid ads, or external outreach without Max approval.

## Felix Identity QA

Before the rebuild PR is considered ready, verify:

- Large triangular ears are visible where Felix appears.
- Face geometry, eye color and spacing, muzzle shape, and orange/cream fur balance match the source pack.
- Felix looks like a premium mentor, not a babyish or generic fox character.
- Images load locally from repo paths and produce no browser 404s.
- The final branch passes `python3 tools/static_site_check.py` after assets are copied.
