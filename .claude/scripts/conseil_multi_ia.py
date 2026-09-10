#!/usr/bin/env python3
"""Conseil multi-IA : pose une même question à plusieurs fournisseurs d'IA et
affiche leurs réponses côte à côte, pour que Claude Code en fasse la synthèse.

Chaque fournisseur n'est interrogé que si sa clé API est présente dans
l'environnement ET que son SDK est installé. Les autres sont ignorés proprement.

Usage :
    python scripts/conseil_multi_ia.py "Ma question ..."
    python scripts/conseil_multi_ia.py            # lit la question sur stdin

Clés d'environnement (voir .env.example) :
    ANTHROPIC_API_KEY  -> Claude  (claude-opus-4-8)
    OPENAI_API_KEY     -> GPT     (gpt-4o)
    GEMINI_API_KEY     -> Gemini  (gemini-2.0-flash)

Installation des SDK (selon les fournisseurs voulus) :
    pip install anthropic openai google-genai
"""
from __future__ import annotations

import os
import sys
from concurrent.futures import ThreadPoolExecutor

MAX_TOKENS = 2048

SYSTEME = (
    "Tu es membre d'un conseil d'IA. Réponds à la question de façon argumentée, "
    "honnête et concise. Si tu as des réserves ou vois un risque, dis-le. "
    "Réponds en français."
)


def demande_claude(question: str) -> str:
    """Interroge Claude via le SDK Anthropic officiel."""
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError("ANTHROPIC_API_KEY absente")
    import anthropic  # import tardif : seulement si la clé existe

    client = anthropic.Anthropic()
    reponse = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=MAX_TOKENS,
        system=SYSTEME,
        messages=[{"role": "user", "content": question}],
    )
    return "".join(bloc.text for bloc in reponse.content if bloc.type == "text")


def demande_gpt(question: str) -> str:
    """Interroge GPT via le SDK OpenAI officiel."""
    if not os.environ.get("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY absente")
    from openai import OpenAI

    client = OpenAI()
    reponse = client.chat.completions.create(
        model="gpt-4o",
        max_tokens=MAX_TOKENS,
        messages=[
            {"role": "system", "content": SYSTEME},
            {"role": "user", "content": question},
        ],
    )
    return reponse.choices[0].message.content or ""


def demande_gemini(question: str) -> str:
    """Interroge Gemini via le SDK google-genai officiel."""
    if not os.environ.get("GEMINI_API_KEY"):
        raise RuntimeError("GEMINI_API_KEY absente")
    from google import genai

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    reponse = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"{SYSTEME}\n\nQuestion : {question}",
    )
    return reponse.text or ""


FOURNISSEURS = {
    "Claude (Anthropic)": demande_claude,
    "GPT (OpenAI)": demande_gpt,
    "Gemini (Google)": demande_gemini,
}


def interroger(nom_et_fn) -> tuple[str, str, bool]:
    nom, fn = nom_et_fn
    try:
        return nom, fn(QUESTION), True
    except Exception as exc:  # clé absente, SDK manquant, erreur réseau…
        return nom, f"(ignoré : {exc})", False


def main() -> int:
    global QUESTION
    if len(sys.argv) > 1:
        QUESTION = " ".join(sys.argv[1:]).strip()
    else:
        print("Entre ta question (Ctrl-D pour finir) :", file=sys.stderr)
        QUESTION = sys.stdin.read().strip()

    if not QUESTION:
        print("Aucune question fournie.", file=sys.stderr)
        return 1

    with ThreadPoolExecutor(max_workers=len(FOURNISSEURS)) as pool:
        resultats = list(pool.map(interroger, FOURNISSEURS.items()))

    repondus = [r for r in resultats if r[2]]

    print("=" * 70)
    print(f"QUESTION : {QUESTION}")
    print("=" * 70)
    for nom, texte, ok in resultats:
        print(f"\n### {nom}\n")
        print(texte.strip())
        print("\n" + "-" * 70)

    if not repondus:
        print(
            "\n⚠️  Aucun fournisseur disponible. Renseigne au moins une clé API "
            "(voir .env.example) et installe le SDK correspondant.",
            file=sys.stderr,
        )
        return 2

    print(
        f"\n✅ {len(repondus)} fournisseur(s) ont répondu. "
        "À Claude Code maintenant de produire la SYNTHÈSE : accords, désaccords, "
        "angles morts, puis recommandation finale.",
    )
    return 0


if __name__ == "__main__":
    QUESTION = ""
    raise SystemExit(main())
