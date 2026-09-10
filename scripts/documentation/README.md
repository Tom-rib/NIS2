# 📄 Régénérer `Documentation.md` et `Documentation.docx`

Les deux documents de synthèse à la racine du dépôt sont **générés**, pas écrits à la main.
La source de vérité reste les fichiers de [`Documentation/`](../../Documentation/).

> 🔑 **Conséquence pratique** : quand tu corriges une faute ou un chiffre, corrige-le dans
> `Documentation/job-X.md`, **puis régénère**. Sinon les deux versions divergent.

---

## Prérequis

```bash
pip install python-docx
```

Aucun autre outil n'est nécessaire (pas de LaTeX, pas de pandoc).

---

## Régénérer

```bash
# 1. Assembler les livrables en un document unique
python scripts/documentation/build-documentation.py

# 2. Convertir ce document en Word
python scripts/documentation/md2docx.py
```

À exécuter **depuis la racine du dépôt**.

---

## Ce que fait chaque script

| Script | Rôle |
|---|---|
| `build-documentation.py` | Concatène les 4 livrables et les 5 annexes, ajoute une page de garde, un avertissement méthodologique, un résumé d'une page et la liste des sources. Abaisse les titres d'un niveau, retire les liens relatifs (le document doit être autonome) et insère des marqueurs de saut de page invisibles en Markdown |
| `md2docx.py` | Convertit le Markdown en `.docx` avec `python-docx` : titres, tableaux mis en forme, blocs de code, citations encadrées, listes, page de garde et **sommaire Word automatique** |

---

## Après génération du `.docx`

Le sommaire est un **champ Word** : il est vide tant qu'il n'a pas été calculé.

1. Ouvrir `Documentation.docx`
2. Cliquer sur le sommaire
3. Appuyer sur **F9** → « Mettre à jour toute la table »

> 💡 Même manipulation pour les numéros de page du pied de page (`Ctrl+A` puis `F9` met tout à jour).

---

## Adapter à un autre projet

Les deux scripts sont réutilisables tels quels. Il suffit de modifier, dans
`build-documentation.py` :

- la constante `EN_TETE` (page de garde et introduction) ;
- la liste `FICHIERS` (les documents à assembler, dans l'ordre) ;
- la constante `FIN` (sources et annexes finales).

Et, dans `md2docx.py`, le bloc `if __name__ == "__main__":` (titre, sous-titre, métadonnées de
couverture).

⬅️ [Retour au dossier scripts](../README.md)
