#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Convertisseur Markdown -> DOCX (python-docx), adapte au rendu NIS2.

Gere : titres, paragraphes, gras/italique/code inline, listes a puces et
numerotees, tableaux GFM, blocs de code, citations, filets, sauts de page
(\\pagebreak), page de garde et sommaire automatique Word.
"""
import re
import sys
import pathlib

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# --------------------------------------------------------------------------- #
#  Utilitaires bas niveau
# --------------------------------------------------------------------------- #

BLEU = RGBColor(0x1F, 0x3B, 0x5C)
BLEU_CLAIR = RGBColor(0x2E, 0x6D, 0xA4)
GRIS = RGBColor(0x44, 0x44, 0x44)


def ombrage(cellule, couleur_hex):
    tc_pr = cellule._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), couleur_hex)
    tc_pr.append(shd)


def ombrage_paragraphe(paragraphe, couleur_hex):
    p_pr = paragraphe._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), couleur_hex)
    p_pr.append(shd)


def bordure_gauche(paragraphe, couleur_hex="2E6DA4", taille=18):
    p_pr = paragraphe._p.get_or_add_pPr()
    bordures = OxmlElement("w:pBdr")
    gauche = OxmlElement("w:left")
    gauche.set(qn("w:val"), "single")
    gauche.set(qn("w:sz"), str(taille))
    gauche.set(qn("w:space"), "8")
    gauche.set(qn("w:color"), couleur_hex)
    bordures.append(gauche)
    p_pr.append(bordures)


def champ(paragraphe, instruction):
    """Insere un champ Word (utilise pour le sommaire et la pagination)."""
    run = paragraphe.add_run()
    debut = OxmlElement("w:fldChar")
    debut.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = instruction
    separateur = OxmlElement("w:fldChar")
    separateur.set(qn("w:fldCharType"), "separate")
    texte = OxmlElement("w:t")
    texte.text = "Mettre a jour le champ (F9)"
    fin = OxmlElement("w:fldChar")
    fin.set(qn("w:fldCharType"), "end")
    for element in (debut, instr, separateur, texte, fin):
        run._r.append(element)


# --------------------------------------------------------------------------- #
#  Rendu du texte enrichi
# --------------------------------------------------------------------------- #

MOTIF_INLINE = re.compile(
    r"(\*\*\*.+?\*\*\*|\*\*.+?\*\*|(?<!\*)\*(?!\*).+?(?<!\*)\*(?!\*)|`[^`]+`|\[[^\]]+\]\([^)]+\))"
)


def ajouter_texte(paragraphe, texte, gras_par_defaut=False, taille=None, couleur=None):
    """Ajoute du texte en interpretant le balisage inline."""
    texte = texte.replace("\\|", "|")
    for morceau in MOTIF_INLINE.split(texte):
        if not morceau:
            continue
        gras = gras_par_defaut
        italique = False
        code = False
        contenu = morceau

        if morceau.startswith("***") and morceau.endswith("***") and len(morceau) > 6:
            contenu, gras, italique = morceau[3:-3], True, True
        elif morceau.startswith("**") and morceau.endswith("**") and len(morceau) > 4:
            contenu, gras = morceau[2:-2], True
        elif morceau.startswith("*") and morceau.endswith("*") and len(morceau) > 2:
            contenu, italique = morceau[1:-1], True
        elif morceau.startswith("`") and morceau.endswith("`") and len(morceau) > 2:
            contenu, code = morceau[1:-1], True
        else:
            lien = re.fullmatch(r"\[([^\]]+)\]\(([^)]+)\)", morceau)
            if lien:
                contenu = lien.group(1)

        run = paragraphe.add_run(contenu)
        run.bold = gras
        run.italic = italique
        if code:
            run.font.name = "Consolas"
            run.font.size = Pt(9)
            run.font.color.rgb = RGBColor(0xA3, 0x1D, 0x1D)
        if taille:
            run.font.size = taille
        if couleur:
            run.font.color.rgb = couleur


# --------------------------------------------------------------------------- #
#  Analyse du Markdown
# --------------------------------------------------------------------------- #

def est_ligne_tableau(ligne):
    return ligne.strip().startswith("|") and ligne.strip().endswith("|")


def est_separateur_tableau(ligne):
    return bool(re.fullmatch(r"\|[\s:|-]+\|", ligne.strip()))


def cellules(ligne):
    brut = ligne.strip()
    brut = brut[1:] if brut.startswith("|") else brut
    brut = brut[:-1] if brut.endswith("|") else brut
    return [c.strip() for c in re.split(r"(?<!\\)\|", brut)]


def convertir(chemin_md, chemin_docx, titre, sous_titre, meta):
    lignes = pathlib.Path(chemin_md).read_text(encoding="utf-8").splitlines()
    doc = Document()

    # --- Styles generaux ---------------------------------------------------
    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(10.5)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.12

    for niveau, taille, couleur in (
        (1, 19, BLEU), (2, 15, BLEU), (3, 12.5, BLEU_CLAIR),
        (4, 11, BLEU_CLAIR), (5, 10.5, GRIS), (6, 10.5, GRIS),
    ):
        style = doc.styles[f"Heading {niveau}"]
        style.font.name = "Calibri"
        style.font.size = Pt(taille)
        style.font.bold = True
        style.font.color.rgb = couleur
        style.paragraph_format.space_before = Pt(14 if niveau <= 2 else 10)
        style.paragraph_format.space_after = Pt(5)
        style.paragraph_format.keep_with_next = True

    section = doc.sections[0]
    section.top_margin = Cm(2.2)
    section.bottom_margin = Cm(2.0)
    section.left_margin = Cm(2.2)
    section.right_margin = Cm(2.2)

    # --- Pied de page avec pagination -------------------------------------
    pied = section.footer.paragraphs[0]
    pied.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = pied.add_run("HydroRégie — Mise en conformité NIS2 — page ")
    run.font.size = Pt(8)
    run.font.color.rgb = GRIS
    champ(pied, "PAGE")

    # --- Page de garde -----------------------------------------------------
    for _ in range(4):
        doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(titre)
    r.font.size = Pt(30)
    r.bold = True
    r.font.color.rgb = BLEU

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(sous_titre)
    r.font.size = Pt(15)
    r.font.color.rgb = BLEU_CLAIR

    doc.add_paragraph()
    tableau = doc.add_table(rows=0, cols=2)
    tableau.style = "Light List Accent 1"
    tableau.alignment = WD_TABLE_ALIGNMENT.CENTER
    for cle, valeur in meta:
        ligne = tableau.add_row()
        ligne.cells[0].text = ""
        ligne.cells[1].text = ""
        ajouter_texte(ligne.cells[0].paragraphs[0], cle, gras_par_defaut=True)
        ajouter_texte(ligne.cells[1].paragraphs[0], valeur)

    doc.add_page_break()

    # --- Sommaire automatique ---------------------------------------------
    p = doc.add_paragraph()
    r = p.add_run("Sommaire")
    r.font.size = Pt(19)
    r.bold = True
    r.font.color.rgb = BLEU
    p = doc.add_paragraph()
    r = p.add_run(
        "Sommaire généré par Word. Pour l'afficher : sélectionner le champ ci-dessous "
        "et appuyer sur F9 (ou clic droit → Mettre à jour les champs)."
    )
    r.italic = True
    r.font.size = Pt(9)
    r.font.color.rgb = GRIS
    champ(doc.add_paragraph(), 'TOC \\o "1-3" \\h \\z \\u')
    doc.add_page_break()

    # --- Corps -------------------------------------------------------------
    i = 0
    n = len(lignes)
    saut_en_attente = False

    while i < n:
        ligne = lignes[i]
        nu = ligne.strip()

        # saut de page explicite
        if nu == "<!-- pagebreak -->":
            saut_en_attente = True
            i += 1
            continue

        # bloc de code
        if nu.startswith("```"):
            i += 1
            contenu = []
            while i < n and not lignes[i].strip().startswith("```"):
                contenu.append(lignes[i])
                i += 1
            i += 1
            p = doc.add_paragraph()
            if saut_en_attente:
                p.add_run().add_break(WD_BREAK.PAGE)
                saut_en_attente = False
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(8)
            p.paragraph_format.left_indent = Cm(0.4)
            ombrage_paragraphe(p, "F2F4F7")
            r = p.add_run("\n".join(contenu))
            r.font.name = "Consolas"
            r.font.size = Pt(8)
            continue

        # tableau
        if est_ligne_tableau(ligne) and i + 1 < n and est_separateur_tableau(lignes[i + 1]):
            entete = cellules(ligne)
            i += 2
            corps = []
            while i < n and est_ligne_tableau(lignes[i]):
                corps.append(cellules(lignes[i]))
                i += 1
            largeur = max(len(entete), max((len(l) for l in corps), default=0))
            if saut_en_attente:
                p = doc.add_paragraph()
                p.add_run().add_break(WD_BREAK.PAGE)
                saut_en_attente = False
            tab = doc.add_table(rows=1, cols=largeur)
            tab.style = "Table Grid"
            tab.autofit = True
            for idx in range(largeur):
                cel = tab.rows[0].cells[idx]
                cel.text = ""
                para = cel.paragraphs[0]
                para.paragraph_format.space_after = Pt(2)
                ajouter_texte(para, entete[idx] if idx < len(entete) else "",
                              gras_par_defaut=True, taille=Pt(9), couleur=RGBColor(0xFF, 0xFF, 0xFF))
                ombrage(cel, "1F3B5C")
            for k, contenu_ligne in enumerate(corps):
                r_tab = tab.add_row()
                for idx in range(largeur):
                    cel = r_tab.cells[idx]
                    cel.text = ""
                    para = cel.paragraphs[0]
                    para.paragraph_format.space_after = Pt(2)
                    ajouter_texte(para, contenu_ligne[idx] if idx < len(contenu_ligne) else "",
                                  taille=Pt(9))
                    if k % 2 == 1:
                        ombrage(cel, "F4F6F9")
            doc.add_paragraph().paragraph_format.space_after = Pt(4)
            continue

        # filet horizontal
        if re.fullmatch(r"-{3,}|\*{3,}|_{3,}", nu):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p_pr = p._p.get_or_add_pPr()
            bordures = OxmlElement("w:pBdr")
            bas = OxmlElement("w:bottom")
            bas.set(qn("w:val"), "single")
            bas.set(qn("w:sz"), "6")
            bas.set(qn("w:space"), "1")
            bas.set(qn("w:color"), "C6CDD6")
            bordures.append(bas)
            p_pr.append(bordures)
            i += 1
            continue

        # titre
        titre_md = re.match(r"^(#{1,6})\s+(.*)$", nu)
        if titre_md:
            niveau = len(titre_md.group(1))
            p = doc.add_heading(level=min(niveau, 6))
            if saut_en_attente:
                p.add_run().add_break(WD_BREAK.PAGE)
                saut_en_attente = False
            ajouter_texte(p, titre_md.group(2))
            i += 1
            continue

        # citation
        if nu.startswith(">"):
            contenu = []
            while i < n and lignes[i].strip().startswith(">"):
                contenu.append(re.sub(r"^\s*>\s?", "", lignes[i]))
                i += 1
            texte = " ".join(x.strip() for x in contenu if x.strip())
            if texte:
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Cm(0.5)
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(6)
                bordure_gauche(p)
                ajouter_texte(p, texte)
            continue

        # liste a puces
        puce = re.match(r"^(\s*)[-*+]\s+(.*)$", ligne)
        if puce:
            profondeur = len(puce.group(1)) // 2
            style = "List Bullet" if profondeur == 0 else f"List Bullet {min(profondeur + 1, 3)}"
            try:
                p = doc.add_paragraph(style=style)
            except KeyError:
                p = doc.add_paragraph(style="List Bullet")
            p.paragraph_format.space_after = Pt(2)
            ajouter_texte(p, puce.group(2))
            i += 1
            continue

        # liste numerotee
        num = re.match(r"^(\s*)\d+[.)]\s+(.*)$", ligne)
        if num:
            profondeur = len(num.group(1)) // 2
            style = "List Number" if profondeur == 0 else f"List Number {min(profondeur + 1, 3)}"
            try:
                p = doc.add_paragraph(style=style)
            except KeyError:
                p = doc.add_paragraph(style="List Number")
            p.paragraph_format.space_after = Pt(2)
            ajouter_texte(p, num.group(2))
            i += 1
            continue

        # ligne vide
        if not nu:
            i += 1
            continue

        # paragraphe (regroupe les lignes consecutives)
        contenu = [nu]
        i += 1
        while i < n:
            suivante = lignes[i]
            s = suivante.strip()
            if (not s or s.startswith(("#", ">", "|", "```", "---"))
                    or re.match(r"^\s*([-*+]|\d+[.)])\s+", suivante)):
                break
            contenu.append(s)
            i += 1
        p = doc.add_paragraph()
        if saut_en_attente:
            p.add_run().add_break(WD_BREAK.PAGE)
            saut_en_attente = False
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        ajouter_texte(p, " ".join(contenu))

    doc.save(chemin_docx)
    return chemin_docx


if __name__ == "__main__":
    racine = pathlib.Path(r"C:\Users\Tom\Documents\Github\B3_TempPlein\NIS2")
    sortie = convertir(
        racine / "Documentation.md",
        racine / "Documentation.docx",
        "Mise en conformité NIS2",
        "HydroRégie — réponse complète au cas pratique",
        [
            ("Entité", "HydroRégie — régie des eaux, 450 000 habitants"),
            ("Statut NIS2", "Entité essentielle — art. 3(1)(a)"),
            ("Secteur", "Annexe I, point 6 — Eau potable"),
            ("Objet", "Directive (UE) 2022/2555 — mise en conformité"),
            ("Blocs traités", "1 — Qualification · 2 — Écarts · 3 — Architecture · 4 — Crise"),
            ("Date", "10 septembre 2026"),
            ("Version", "1.0"),
            ("Classification", "Diffusion restreinte"),
        ],
    )
    print("DOCX ecrit :", sortie)
