#!/usr/bin/env python3
"""Static GitHub Pages sanity checks for OptimizeMyLife."""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    Path("README.md"),
    Path("index.html"),
    Path("styles.css"),
    Path("app.js"),
    Path("AGENTS.md"),
    Path("CLAUDE.md"),
    Path("docs/ASSET_PROVENANCE_AND_FELIX_MANIFEST.md"),
    Path("docs/STATIC_QA_CHECKLIST.md"),
    Path("assets/felix-exact/manifest.json"),
]

EXPECTED_FELIX_ASSETS = [
    "01-hero-landing-felix-exact-white.jpg",
    "02-product-box-junior-exact-felix-white.jpg",
    "03-course-card-junior-exact-felix-white.jpg",
    "04-course-lineup-junior-teen-adult-felix-exact-white.jpg",
    "05-felix-ai-live-feature-exact-white.jpg",
    "06-parent-trust-section-felix-exact-white.jpg",
    "07-project-modules-felix-exact-white.jpg",
    "08-checkout-offer-felix-exact-white.jpg",
    "09-social-square-junior-felix-exact-white.jpg",
    "10-footer-cta-banner-felix-exact-white.jpg",
]

ASSET_DIR = Path("assets/felix-exact")
LOCAL_ATTRS = {
    "a": ("href",),
    "img": ("src",),
    "link": ("href",),
    "script": ("src",),
    "source": ("src", "srcset"),
    "video": ("src", "poster"),
}
CSS_URL_RE = re.compile(r"url\((?P<value>[^)]+)\)")


class SiteHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.anchors: list[tuple[str, str]] = []
        self.refs: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {name: value for name, value in attrs if value is not None}
        if "id" in attr_map:
            self.ids.add(attr_map["id"])
        if "name" in attr_map:
            self.ids.add(attr_map["name"])
        for attr in LOCAL_ATTRS.get(tag, ()):
            value = attr_map.get(attr)
            if not value:
                continue
            if attr == "srcset":
                for candidate in split_srcset(value):
                    self.refs.append((f"{tag}[{attr}]", candidate))
            elif tag == "a" and value.startswith("#"):
                self.anchors.append((tag, value[1:]))
            else:
                self.refs.append((f"{tag}[{attr}]", value))


def split_srcset(value: str) -> list[str]:
    urls: list[str] = []
    for part in value.split(","):
        candidate = part.strip().split()
        if candidate:
            urls.append(candidate[0])
    return urls


def is_external(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https", "mailto", "tel", "data"} or value.startswith("//")


def local_path_for(value: str, base: Path) -> Path | None:
    if not value or is_external(value) or value.startswith("#"):
        return None
    parsed = urlparse(value)
    raw_path = unquote(parsed.path)
    if not raw_path:
        return None
    if raw_path.startswith("/"):
        return ROOT / raw_path.lstrip("/")
    return (base.parent / raw_path).resolve()


def display_path(path: Path) -> Path:
    try:
        return path.relative_to(ROOT)
    except ValueError:
        return path


def check_required_files(results: list[tuple[str, str]]) -> None:
    for rel_path in REQUIRED_FILES:
        path = ROOT / rel_path
        if path.exists():
            results.append(("OK", f"required file exists: {rel_path}"))
        else:
            results.append(("ERROR", f"required file missing: {rel_path}"))


def check_no_stack_drift(results: list[tuple[str, str]]) -> None:
    stack_files = [
        "package.json",
        "package-lock.json",
        "pnpm-lock.yaml",
        "yarn.lock",
        "next.config.js",
        "next.config.mjs",
        "vite.config.js",
        "vite.config.ts",
    ]
    found = [name for name in stack_files if (ROOT / name).exists()]
    if found:
        results.append(("WARN", f"stack approval needed for: {', '.join(found)}"))
    else:
        results.append(("OK", "no package manager or framework config detected"))


def check_html(results: list[tuple[str, str]]) -> None:
    index = ROOT / "index.html"
    if not index.exists():
        return

    parser = SiteHTMLParser()
    parser.feed(index.read_text(encoding="utf-8"))

    for tag, anchor in parser.anchors:
        if not anchor:
            continue
        if anchor in parser.ids:
            results.append(("OK", f"anchor target exists: #{anchor}"))
        else:
            results.append(("ERROR", f"missing anchor target for {tag} href='#{anchor}'"))

    for label, value in parser.refs:
        path = local_path_for(value, index)
        if path is None:
            continue
        rel = display_path(path)
        if path.exists():
            results.append(("OK", f"local reference exists: {label} -> {rel}"))
        else:
            results.append(("ERROR", f"missing local reference: {label} -> {rel}"))


def check_css(results: list[tuple[str, str]]) -> None:
    css = ROOT / "styles.css"
    if not css.exists():
        return

    text = css.read_text(encoding="utf-8")
    for match in CSS_URL_RE.finditer(text):
        value = match.group("value").strip().strip("\"'")
        path = local_path_for(value, css)
        if path is None:
            continue
        rel = display_path(path)
        if path.exists():
            results.append(("OK", f"CSS url exists: {rel}"))
        else:
            results.append(("ERROR", f"missing CSS url: {rel}"))


def check_felix_assets(results: list[tuple[str, str]], skip: bool) -> None:
    if skip:
        results.append(("WARN", "Felix asset presence check skipped"))
        return
    for filename in EXPECTED_FELIX_ASSETS:
        rel_path = ASSET_DIR / filename
        if (ROOT / rel_path).exists():
            results.append(("OK", f"Felix asset exists: {rel_path}"))
        else:
            results.append(("TODO", f"copy Felix asset after rebuild selection: {rel_path}"))


def print_results(results: list[tuple[str, str]]) -> int:
    order = {"ERROR": 0, "TODO": 1, "WARN": 2, "OK": 3}
    for level, message in sorted(results, key=lambda item: (order[item[0]], item[1])):
        print(f"{level}: {message}")
    if any(level in {"ERROR", "TODO"} for level, _ in results):
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skip-felix-assets",
        action="store_true",
        help="Skip expected assets/felix-exact presence checks.",
    )
    args = parser.parse_args()

    results: list[tuple[str, str]] = []
    check_required_files(results)
    check_no_stack_drift(results)
    check_html(results)
    check_css(results)
    check_felix_assets(results, skip=args.skip_felix_assets)
    return print_results(results)


if __name__ == "__main__":
    sys.exit(main())
