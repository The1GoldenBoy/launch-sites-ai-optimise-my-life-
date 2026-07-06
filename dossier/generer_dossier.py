#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Intégration des photos réelles au dossier d'incident Nunes / Langlois (Beneva).

Principe : on NE reconstruit PAS le dossier. On repart du PDF original
(Dossier_incident_Nunes_Langlois_ORIGINAL.pdf), on garde toutes ses pages
intactes, et on INSÈRE juste après la section « Photographies réelles des
dommages » (page 7) des pages supplémentaires présentant chaque vraie photo
déposée dans ./photos-reelles/, dans le même gabarit graphique, avec le badge
« PHOTO RÉELLE » (vert).

Les images de reconstitution IA du dossier restent intactes et gardent leur
étiquette « Reconstitution — non photographique ». Le dossier reste honnête
envers l'assureur.

Usage : python3 generer_dossier.py
Sortie : ./Dossier_incident_Nunes_Langlois.pdf
"""

import os
import io
import glob

import fitz  # PyMuPDF
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth

HERE = os.path.dirname(os.path.abspath(__file__))
PHOTOS_DIR = os.path.join(HERE, "photos-reelles")
ORIGINAL = os.path.join(HERE, "Dossier_incident_Nunes_Langlois_ORIGINAL.pdf")
OUTPUT = os.path.join(HERE, "Dossier_incident_Nunes_Langlois.pdf")

# La section « Photographies réelles des dommages » est la page 7 (index 6).
INSERT_AFTER_PAGE_INDEX = 6

# ----------------------------------------------------------------------------
# Polices (calquées sur le document original : corps en DejaVu Sans, étiquettes
# en mono, titres en serif).
# ----------------------------------------------------------------------------
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("Body", f"{FONT_DIR}/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("Body-Bold", f"{FONT_DIR}/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Mono", f"{FONT_DIR}/DejaVuSansMono.ttf"))
pdfmetrics.registerFont(TTFont("Mono-Bold", f"{FONT_DIR}/DejaVuSansMono-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Serif", f"{FONT_DIR}/DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("Serif-Bold", f"{FONT_DIR}/DejaVuSerif-Bold.ttf"))

# Palette échantillonnée sur le PDF original
OR = colors.HexColor("#A8895E")        # accent or / tan
OR_CLAIR = colors.HexColor("#C7A778")
NAVY = colors.HexColor("#12293F")      # titres / éléments sombres
SLATE = colors.HexColor("#5C6472")     # corps de texte gris ardoise
SLATE_CLAIR = colors.HexColor("#8A909B")
VERT = colors.HexColor("#1E7A46")      # badge « Photo réelle »
VERT_CLAIR = colors.HexColor("#EAF5EE")
AMBRE = colors.HexColor("#B26A00")     # statut « à venir »
BLANC = colors.white

PAGE_W, PAGE_H = A4
MARGE = 22 * mm

# ----------------------------------------------------------------------------
# Utilitaires
# ----------------------------------------------------------------------------

def spaced(text, gap=" "):
    """Renvoie le texte avec espacement entre les lettres (style petites capitales)."""
    return gap.join(list(text))


def draw_tracked(c, text, x, y, font, size, color, tracking=1.4):
    """Dessine du texte avec crénage/tracking manuel (letter-spacing)."""
    c.setFont(font, size)
    c.setFillColor(color)
    cur = x
    for ch in text:
        c.drawString(cur, y, ch)
        cur += stringWidth(ch, font, size) + tracking
    return cur


def wrap_text(text, font, size, max_width):
    lignes = []
    for para in text.split("\n"):
        if para == "":
            lignes.append("")
            continue
        courant = ""
        for mot in para.split(" "):
            essai = mot if courant == "" else courant + " " + mot
            if stringWidth(essai, font, size) <= max_width:
                courant = essai
            else:
                if courant:
                    lignes.append(courant)
                courant = mot
        lignes.append(courant)
    return lignes


def header(c, right_top, right_bottom):
    y = PAGE_H - MARGE
    draw_tracked(c, "DOSSIER D'INCIDENT  ·  NUNES–LANGLOIS", MARGE, y - 3,
                 "Mono", 7.5, OR, tracking=1.2)
    c.setFont("Mono", 7.5)
    c.setFillColor(SLATE)
    c.drawRightString(PAGE_W - MARGE, y - 3, right_top)
    c.drawRightString(PAGE_W - MARGE, y - 3 - 4.2 * mm, right_bottom)
    # Filet or : segment épais à gauche + trait fin sur toute la largeur
    ry = y - 8 * mm
    c.setStrokeColor(colors.HexColor("#E7E1D6"))
    c.setLineWidth(0.6)
    c.line(MARGE, ry, PAGE_W - MARGE, ry)
    c.setStrokeColor(OR)
    c.setLineWidth(2)
    c.line(MARGE, ry, MARGE + 28 * mm, ry)
    return ry - 10 * mm


def footer(c, label="PHOTOGRAPHIES"):
    y = 14 * mm
    c.setStrokeColor(colors.HexColor("#E7E1D6"))
    c.setLineWidth(0.6)
    c.line(MARGE, y + 4 * mm, PAGE_W - MARGE, y + 4 * mm)
    draw_tracked(c, "NUNES–LANGLOIS  ·  21 FÉV. 2026", MARGE, y,
                 "Mono", 7, SLATE_CLAIR, tracking=1.0)
    c.setFont("Mono", 7)
    c.setFillColor(SLATE_CLAIR)
    c.drawRightString(PAGE_W - MARGE, y, label)


def section_title(c, numeral, titre, y):
    c.setFont("Serif-Bold", 13)
    c.setFillColor(OR)
    c.drawString(MARGE, y, numeral)
    nw = stringWidth(numeral, "Serif-Bold", 13)
    c.setFont("Serif-Bold", 21)
    c.setFillColor(NAVY)
    c.drawString(MARGE + nw + 5 * mm, y, titre)
    return y - 9 * mm


def badge_photo_reelle(c, x, y):
    """Badge « PHOTO RÉELLE » (vert), style boîte encadrée du document original."""
    w, h = 26 * mm, 9 * mm
    c.setFillColor(VERT_CLAIR)
    c.setStrokeColor(VERT)
    c.setLineWidth(1.1)
    c.roundRect(x, y, w, h, 1.2 * mm, fill=1, stroke=1)
    c.setFillColor(VERT)
    draw_tracked(c, "PHOTO", x + 4.5 * mm, y + h - 3.6 * mm, "Mono-Bold", 7, VERT, 0.8)
    draw_tracked(c, "RÉELLE", x + 4.5 * mm, y + 1.6 * mm, "Mono-Bold", 7, VERT, 0.8)
    return w, h


def fit(path, box_w, box_h):
    img = ImageReader(path)
    iw, ih = img.getSize()
    r = min(box_w / iw, box_h / ih)
    return iw * r, ih * r, img


LEGENDES = {
    "feu-arriere": "FEU ARRIÈRE — LENTILLE FENDUE ET BRISÉE",
    "aile-arriere": "AILE ARRIÈRE — ENFONCEMENT ET ÉRAFLURES",
    "aile-enfoncee": "AILE ARRIÈRE — ENFONCEMENT AU POINT DE CONTACT",
    "wrap-dechire": "HABILLAGE (WRAP) DÉCHIRÉ ET SOULEVÉ",
    "wrap": "HABILLAGE (WRAP) DÉCHIRÉ ET SOULEVÉ",
    "pare-chocs": "COIN DE PARE-CHOCS ENFONCÉ",
    "coin-pare-chocs": "COIN DE PARE-CHOCS ENFONCÉ",
    "raccord": "RACCORD AILE / PARE-CHOCS DÉSALIGNÉ",
    "raccord-desaligne": "RACCORD AILE / PARE-CHOCS DÉSALIGNÉ",
    "bas-de-caisse": "BAS DE CAISSE — TRACES DE CONTACT",
    "bas-caisse": "BAS DE CAISSE — TRACES DE CONTACT",
}


def legende(path):
    base = os.path.splitext(os.path.basename(path))[0].lower()
    # retire préfixe "photo-reelle-NN-"
    key = base
    for pre in ("photo-reelle-", "photo-reele-"):
        if key.startswith(pre):
            key = key[len(pre):]
    # enlève le numéro de tête
    parts = key.split("-")
    if parts and parts[0].isdigit():
        parts = parts[1:]
    key = "-".join(parts)
    if key in LEGENDES:
        return LEGENDES[key]
    # correspondance partielle
    for k, v in LEGENDES.items():
        if k in key:
            return v
    return spaced(key.replace("-", " ").upper(), " ") if key else "PHOTOGRAPHIE DU VÉHICULE A"


def list_photos():
    exts = ("*.jpg", "*.jpeg", "*.JPG", "*.JPEG", "*.png", "*.PNG")
    found = []
    for e in exts:
        found += glob.glob(os.path.join(PHOTOS_DIR, e))
    return sorted(set(found))


# ----------------------------------------------------------------------------
# Construction des pages supplémentaires (photos réelles)
# ----------------------------------------------------------------------------

def build_photo_pages_pdf(photos):
    """Retourne un PDF (bytes) contenant les pages de photos réelles."""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)

    per_page = 2
    total = len(photos)
    idx = 0
    while idx < total:
        y = header(c, "Photographies", "des dommages (suite)")
        y = section_title(c, "VI", "Photographies réelles — compléments", y)
        # sous-titre
        c.setFont("Body", 9.5)
        c.setFillColor(SLATE)
        sub = ("Clichés authentiques supplémentaires du véhicule A (Jaguar F-Type R), "
               "pris après l'événement — aucune retouche.")
        for ln in wrap_text(sub, "Body", 9.5, PAGE_W - 2 * MARGE):
            c.drawString(MARGE, y, ln)
            y -= 4.6 * mm
        y -= 4 * mm

        zone_top = y
        zone_bottom = 22 * mm
        slot_h = (zone_top - zone_bottom) / per_page

        for _ in range(per_page):
            if idx >= total:
                break
            path = photos[idx]
            cap_h = 11 * mm
            box_w = PAGE_W - 2 * MARGE
            box_h = slot_h - cap_h - 6 * mm
            try:
                w, h, img = fit(path, box_w, box_h)
            except Exception:
                idx += 1
                continue
            slot_top = zone_top - (_ ) * slot_h
            x = MARGE + (box_w - w) / 2
            img_top = slot_top
            c.drawImage(img, x, img_top - h, width=w, height=h,
                        preserveAspectRatio=True, mask='auto')
            c.setStrokeColor(colors.HexColor("#D8D8D8"))
            c.setLineWidth(0.8)
            c.rect(x, img_top - h, w, h, fill=0, stroke=1)

            # barre de légende sous la photo
            cap_y = img_top - h - cap_h
            c.setFillColor(colors.HexColor("#F5F3EE"))
            c.rect(MARGE, cap_y, box_w, cap_h, fill=1, stroke=0)
            c.setFillColor(OR)
            c.rect(MARGE, cap_y, 2.5 * mm, cap_h, fill=1, stroke=0)
            # texte légende (mono, tracké) — possiblement sur 2 lignes
            lg = legende(path)
            c.setFillColor(NAVY)
            lg_lines = wrap_text(lg, "Mono-Bold", 7.5, box_w - 40 * mm)
            ty = cap_y + cap_h - 4 * mm if len(lg_lines) > 1 else cap_y + cap_h / 2 - 1 * mm
            for ln in lg_lines:
                draw_tracked(c, ln, MARGE + 7 * mm, ty, "Mono-Bold", 7.5, NAVY, 0.8)
                ty -= 4 * mm
            # badge
            badge_photo_reelle(c, PAGE_W - MARGE - 26 * mm - 3 * mm, cap_y + (cap_h - 9 * mm) / 2)

            idx += 1

        footer(c)
        c.showPage()

    c.save()
    buf.seek(0)
    return buf.read()


# ----------------------------------------------------------------------------
# Assemblage : original[0..6] + pages photos + original[7..]
# ----------------------------------------------------------------------------

# Signatures des témoins à déposer sur la page « Témoins » (prénom -> fichier).
SIGN_DIR = os.path.join(HERE, "signatures")
SIGNATURES_TEMOINS = {
    "Lucie": "signature_lucie.jpg",
    "Rosalie": "signature_rosalie.jpg",
    "Michael": "signature_michael.jpg",
}


def place_signatures_temoins(doc):
    """Dépose les signatures manuscrites dans la colonne Signature de la page Témoins."""
    for page in doc:
        txt = page.get_text()
        if "Témoins" not in txt:
            continue
        words = page.get_text("words")  # x0,y0,x1,y1,mot,...
        # bornes de la colonne « Signature »
        sig_hdr = [w for w in words if w[4].upper() == "SIGNATURE"]
        if not sig_hdr:
            continue
        col_x0 = sig_hdr[0][0] - 4
        page_right = page.rect.width - 57.9  # marge symétrique
        for prenom, fname in SIGNATURES_TEMOINS.items():
            path = os.path.join(SIGN_DIR, fname)
            if not os.path.exists(path):
                continue
            # trouve la ligne du témoin par son prénom
            row = [w for w in words if w[4] == prenom]
            if not row:
                continue
            yc = (row[0][1] + row[0][3]) / 2
            rect = fitz.Rect(col_x0 + 6, yc - 26, min(col_x0 + 6 + 120, page_right), yc + 26)
            page.insert_image(rect, filename=path, keep_proportion=True, overlay=True)
        break


# Coordonnées des témoins (prénom -> lignes à écrire dans la colonne Coordonnées).
COORDS_TEMOINS = {
    "Lucie": ["450 531-3185", "luciejodoin@hotmail.com"],
    "Michael": ["450 522-0430"],
    "Rosalie": ["450 994-3480"],
}


def place_coordinates_temoins(doc):
    """Écrit les coordonnées des témoins dans la colonne « Coordonnées »."""
    for page in doc:
        if "Témoins" not in page.get_text():
            continue
        words = page.get_text("words")
        hdr = [w for w in words if w[4].upper().startswith("COORDONN")]
        if not hdr:
            continue
        cx = hdr[0][0]
        for prenom, lines in COORDS_TEMOINS.items():
            row = [w for w in words if w[4] == prenom]
            if not row:
                continue
            ybase = row[0][3]
            for k, ln in enumerate(lines):
                size = 8.5 if k == 0 else 7.3
                page.insert_text((cx, ybase + k * 9), ln, fontname="helv",
                                 fontsize=size, color=(0.36, 0.39, 0.45))
        break


# Déclarations signées des témoins (recueillies via le formulaire en ligne).
DECLARATIONS = [
    {
        "nom": "Michael Ménard", "role": "COPROPRIÉTAIRE DES LIEUX",
        "coord": "450 522-0430",
        "texte": ("Timothé, avec la van de sa conjointe, a reculé dans le côté droit "
                  "arrière du véhicule stationné de Sara Nunes en voulant sortir de la "
                  "cour pour s'en aller. On a entendu l'impact de l'intérieur. Il y avait "
                  "des débris de lumière arrière sur le sol."),
        "signee": True,
    },
    {
        "nom": "Rosalie Jodoin", "role": "COPROPRIÉTAIRE DES LIEUX",
        "coord": "450 994-3480",
        "texte": ("Timothé, avec la van de sa conjointe, a reculé dans le côté droit "
                  "arrière du véhicule stationné de Sara Nunes en voulant sortir de la "
                  "cour pour s'en aller. On a entendu l'impact de l'intérieur. Il y avait "
                  "des débris de lumière arrière sur le sol."),
        "signee": False,
    },
    {
        "nom": "Lucie Jodoin", "role": "INVITÉE",
        "coord": "450 531-3185 · luciejodoin@hotmail.com",
        "texte": ("À son départ, mon neveu Timothé a reculé sur la voiture de Sara."),
        "signee": True,
    },
]


def build_declarations_pdf():
    """Page « Déclarations signées des témoins » (bytes PDF)."""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    y = header(c, "Attestations", "des témoins")
    y = section_title(c, "VIII", "Déclarations signées des témoins", y)
    c.setFont("Body", 9.5)
    c.setFillColor(SLATE)
    intro = ("Déclarations recueillies auprès des personnes présentes, via le formulaire "
             "en ligne. Chaque témoin confirme les faits constatés le 21 février 2026.")
    for ln in wrap_text(intro, "Body", 9.5, PAGE_W - 2 * MARGE):
        c.drawString(MARGE, y, ln)
        y -= 4.6 * mm
    y -= 5 * mm

    for d in DECLARATIONS:
        lines = wrap_text(d["texte"], "Body", 10, PAGE_W - 2 * MARGE - 12 * mm)
        h = 20 * mm + len(lines) * 4.8 * mm
        c.setFillColor(colors.HexColor("#FBFCFD"))
        c.setStrokeColor(colors.HexColor("#E1E6EC"))
        c.setLineWidth(0.8)
        c.roundRect(MARGE, y - h, PAGE_W - 2 * MARGE, h, 2 * mm, fill=1, stroke=1)
        c.setFillColor(OR)
        c.roundRect(MARGE, y - h, 2.5 * mm, h, 1 * mm, fill=1, stroke=0)
        # nom + rôle
        c.setFillColor(NAVY)
        c.setFont("Serif-Bold", 12.5)
        c.drawString(MARGE + 7 * mm, y - 8 * mm, d["nom"])
        draw_tracked(c, d["role"], MARGE + 7 * mm, y - 12.5 * mm, "Mono", 7, SLATE_CLAIR, 0.6)
        # coordonnées (à droite)
        c.setFont("Mono", 8)
        c.setFillColor(SLATE)
        c.drawRightString(PAGE_W - MARGE - 6 * mm, y - 8 * mm, d["coord"])
        # statut attestation / signature (à droite, 2e ligne)
        if d["signee"]:
            statut, col = "ATTESTATION : OUI  ·  SIGNÉ", VERT
        else:
            statut, col = "ATTESTATION : OUI  ·  SIGNATURE À VENIR", AMBRE
        c.setFont("Mono-Bold", 7)
        c.setFillColor(col)
        c.drawRightString(PAGE_W - MARGE - 6 * mm, y - 12.5 * mm, statut)
        # déclaration
        c.setFont("Body", 10)
        c.setFillColor(SLATE)
        ty = y - 18 * mm
        for ln in lines:
            c.drawString(MARGE + 7 * mm, ty, ln)
            ty -= 4.8 * mm
        y -= h + 6 * mm

    footer(c, label="ATTESTATIONS")
    c.showPage()
    c.save()
    buf.seek(0)
    return buf.read()


# Identification du conducteur du véhicule B (permis de conduire).
PIECES_DIR = os.path.join(HERE, "pieces")
PERMIS_VEH_B = {
    "Nom": "Timothée Langlois",
    "N° de permis": "L5248-120995-18",
    "Date de naissance": "12 septembre 1995",
    "Adresse": "441, rue Tardif, Val-des-Sources (QC) J1T 3G5",
    "Classe(s)": "5",
    "Conditions": "Aucune",
    "Mentions": "Aucune",
    "N° de référence": "R4MUN9F36",
    "Sexe / Taille / Yeux": "M · 175 cm · Bruns",
    "Validité": "Valide le 2024-12-10 · Expire le 2027-09-12",
    "Émis par": "Société de l'assurance automobile du Québec (SAAQ)",
}


def _find_permis_image():
    if not os.path.isdir(PIECES_DIR):
        return None
    for ext in ("*.jpg", "*.jpeg", "*.png", "*.JPG", "*.JPEG", "*.PNG"):
        found = glob.glob(os.path.join(PIECES_DIR, "permis*" + ext[1:]))
        if found:
            return sorted(found)[0]
    return None


def build_identification_pdf():
    """Page « Conducteur du véhicule B — identification » (bytes PDF)."""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    y = header(c, "Conducteur", "véhicule B")
    y = section_title(c, "IX", "Conducteur du véhicule B — identification", y)

    # Encadré : absence de signature
    note = ("M. Timothée Langlois, conducteur du véhicule B au moment de l'incident, "
            "n'a pas signé le constat à l'amiable. Son identité est établie ci-dessous "
            "d'après son permis de conduire du Québec.")
    nlines = wrap_text(note, "Body", 9.5, PAGE_W - 2 * MARGE - 12 * mm)
    nh = 8 * mm + len(nlines) * 4.4 * mm
    c.setFillColor(AMBRE_CLAIR if 'AMBRE_CLAIR' in globals() else colors.HexColor("#FBF0DD"))
    c.setStrokeColor(AMBRE)
    c.setLineWidth(0.9)
    c.roundRect(MARGE, y - nh, PAGE_W - 2 * MARGE, nh, 2 * mm, fill=1, stroke=1)
    draw_tracked(c, "CONSTAT NON SIGNÉ PAR LE CONDUCTEUR B", MARGE + 6 * mm, y - 6.5 * mm,
                 "Mono-Bold", 7.5, AMBRE, 0.7)
    c.setFillColor(GRIS if 'GRIS' in globals() else SLATE)
    c.setFont("Body", 9.5)
    ty = y - 11.5 * mm
    for ln in nlines:
        c.drawString(MARGE + 6 * mm, ty, ln)
        ty -= 4.4 * mm
    y = y - nh - 8 * mm

    # Carte : données du permis
    keys = list(PERMIS_VEH_B.items())
    ch = 12 * mm + len(keys) * 7 * mm
    c.setFillColor(colors.HexColor("#FBFCFD"))
    c.setStrokeColor(colors.HexColor("#E1E6EC"))
    c.setLineWidth(0.8)
    c.roundRect(MARGE, y - ch, PAGE_W - 2 * MARGE, ch, 2 * mm, fill=1, stroke=1)
    c.setFillColor(BLEU if 'BLEU' in globals() else NAVY)
    c.roundRect(MARGE, y - ch, 2.5 * mm, ch, 1 * mm, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.setFont("Serif-Bold", 12)
    c.drawString(MARGE + 8 * mm, y - 8 * mm, "Permis de conduire — Québec (SAAQ)")
    yy = y - 16 * mm
    for k, v in keys:
        c.setFillColor(SLATE_CLAIR)
        c.setFont("Mono", 7.5)
        c.drawString(MARGE + 8 * mm, yy, k.upper())
        c.setFillColor(NAVY)
        c.setFont("Body", 10)
        c.drawString(MARGE + 62 * mm, yy, v)
        yy -= 7 * mm
    y = y - ch - 8 * mm

    # Image du permis si fournie
    img = _find_permis_image()
    if img:
        box_w = PAGE_W - 2 * MARGE
        box_h = y - 24 * mm
        try:
            ir = ImageReader(img); iw, ih = ir.getSize()
            r = min(box_w / iw, box_h / ih)
            w, h = iw * r, ih * r
            x = MARGE + (box_w - w) / 2
            c.drawImage(ir, x, y - h, width=w, height=h, preserveAspectRatio=True, mask='auto')
            c.setStrokeColor(colors.HexColor("#D8D8D8")); c.setLineWidth(0.8)
            c.rect(x, y - h, w, h, fill=0, stroke=1)
            c.setFillColor(SLATE); c.setFont("Body-Bold", 9.5)
            c.drawString(MARGE, y - h - 6 * mm, "Permis de conduire du conducteur du véhicule B (copie fournie).")
        except Exception:
            pass
    else:
        c.setFillColor(SLATE_CLAIR)
        c.setFont("Body-Italic" if 'Body-Italic' in [f for f in pdfmetrics.getRegisteredFontNames()] else "Body", 9)
        c.drawString(MARGE, y - 2 * mm,
                     "Copie du permis de conduire jointe séparément au dossier.")

    footer(c, label="IDENTIFICATION")
    c.showPage()
    c.save()
    buf.seek(0)
    return buf.read()


def build():
    photos = list_photos()
    if not os.path.exists(ORIGINAL):
        raise SystemExit(f"PDF original introuvable : {ORIGINAL}")

    base = fitz.open(ORIGINAL)
    if not photos:
        base.save(OUTPUT)
        return OUTPUT, 0, base.page_count

    extra_bytes = build_photo_pages_pdf(photos)
    extra = fitz.open("pdf", extra_bytes)

    out = fitz.open()
    # pages 1..7 (index 0..6)
    out.insert_pdf(base, from_page=0, to_page=INSERT_AFTER_PAGE_INDEX)
    # pages photos réelles
    out.insert_pdf(extra)
    # reste du dossier (index 7..fin)
    if INSERT_AFTER_PAGE_INDEX + 1 <= base.page_count - 1:
        out.insert_pdf(base, from_page=INSERT_AFTER_PAGE_INDEX + 1, to_page=base.page_count - 1)

    # Dépose les signatures manuscrites + coordonnées des témoins
    place_signatures_temoins(out)
    place_coordinates_temoins(out)

    # Ajoute la page « Déclarations signées des témoins » à la fin
    decl = fitz.open("pdf", build_declarations_pdf())
    out.insert_pdf(decl)

    # Ajoute la page d'identification du conducteur du véhicule B (permis)
    ident = fitz.open("pdf", build_identification_pdf())
    out.insert_pdf(ident)

    out.set_metadata({
        "title": "Dossier d'incident — Nunes / Langlois",
        "author": "Dossier de réclamation Beneva",
        "subject": "Constat à l'amiable — 21 février 2026",
    })
    out.save(OUTPUT, deflate=True, garbage=3)
    return OUTPUT, len(photos), out.page_count


if __name__ == "__main__":
    out, nb, pages = build()
    print(f"OK -> {out}")
    print(f"Photos réelles ajoutées : {nb}")
    print(f"Total pages du dossier final : {pages}")
