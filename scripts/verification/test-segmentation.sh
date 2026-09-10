#!/usr/bin/env bash
# =============================================================================
#  HydroRegie - Test de la segmentation IT / OT
#  Projet NIS2 - bloc 3 / fiche 04_tests.md
#  Version 1.0 - 2026-09-10
#
#  OBJET : produire une PREUVE datee que la segmentation fonctionne, c'est-a-dire
#          - que ce qui doit etre bloque l'est reellement,
#          - ET que ce qui doit passer passe toujours.
#
#  Une segmentation qui casse l'exploitation ne survit pas trois jours :
#  les deux moities du test comptent autant l'une que l'autre.
#
#  AVERTISSEMENT OT
#  ----------------
#  Ce script n'envoie que des paquets TCP simples (pas de -A, pas de scripts NSE,
#  debit bride). Il reste a executer :
#    - en FENETRE PLANIFIEE,
#    - avec l'exploitant PRESENT,
#    - jamais de sa propre initiative.
#
#  USAGE : ./test-segmentation.sh [fichier_de_sortie]
# =============================================================================

set -uo pipefail

SORTIE="${1:-resultats-segmentation-$(date +%Y%m%d-%H%M).md}"
HORODATAGE="$(date '+%Y-%m-%d %H:%M:%S %Z')"
DEPUIS="$(hostname) ($(hostname -I 2>/dev/null | awk '{print $1}'))"

# --- Cibles a adapter -------------------------------------------------------
AUTOMATE="10.220.10.15"        # Z7 - automate station de relevage Nord
RESEAU_OT="10.220.0.0/22"      # Z7 - plage de controle
SCADA="10.210.0.10"            # Z6 - superviseur
RELAIS_OPC="10.200.0.20"       # Z5 - relais OPC UA de la DMZ
COLLECTEUR="10.240.0.20"       # Z9 - collecteur de journaux
INTERNET="1.1.1.1"

OK=0
KO=0

# --- Fonctions --------------------------------------------------------------

entete() {
    {
        echo "# Resultats des tests de segmentation IT / OT"
        echo ""
        echo "| Champ | Valeur |"
        echo "|---|---|"
        echo "| Date | $HORODATAGE |"
        echo "| Execute depuis | $DEPUIS |"
        echo "| Operateur | ${USER:-inconnu} |"
        echo ""
        echo "| # | Test | Cible | Attendu | Obtenu | Verdict |"
        echo "|---|---|---|---|---|---|"
    } > "$SORTIE"
}

# verifie_port <id> <libelle> <hote> <port> <attendu: filtered|open>
verifie_port() {
    local id="$1" libelle="$2" hote="$3" port="$4" attendu="$5"
    local etat verdict

    etat=$(nmap -Pn -p "$port" --max-rate 20 --host-timeout 30s "$hote" 2>/dev/null \
           | awk -v p="$port" '$1 ~ "^"p"/tcp" {print $2}')
    etat="${etat:-aucune-reponse}"

    if [[ "$etat" == "$attendu" ]]; then
        verdict="OK"; ((OK++))
    else
        verdict="ECHEC"; ((KO++))
    fi

    printf '| %s | %s | %s:%s | %s | %s | %s |\n' \
        "$id" "$libelle" "$hote" "$port" "$attendu" "$etat" "$verdict" >> "$SORTIE"
    printf '%-6s %-45s attendu=%-9s obtenu=%-9s %s\n' \
        "$id" "$libelle" "$attendu" "$etat" "$verdict"
}

# -----------------------------------------------------------------------------
echo "=============================================================="
echo " Test de segmentation IT / OT - HydroRegie"
echo " $HORODATAGE"
echo "=============================================================="
echo ""

command -v nmap >/dev/null || { echo "ERREUR : nmap est requis."; exit 1; }
entete

# --- A. Ce qui DOIT etre bloque ---------------------------------------------
echo "--- A. Flux qui doivent etre BLOQUES -------------------------"
verifie_port "A1" "Modbus depuis la bureautique vers un automate"   "$AUTOMATE" 502   "filtered"
verifie_port "A2" "IEC-104 depuis la bureautique vers un automate"  "$AUTOMATE" 2404  "filtered"
verifie_port "A3" "EtherNet/IP depuis la bureautique"               "$AUTOMATE" 44818 "filtered"
verifie_port "A4" "S7comm depuis la bureautique"                    "$AUTOMATE" 102   "filtered"
verifie_port "A5" "RDP vers le superviseur SCADA"                   "$SCADA"    3389  "filtered"

echo ""
echo "--- A6. Balayage du sous-reseau OT (aucun hote ne doit repondre)"
HOTES=$(nmap -sn --max-rate 20 "$RESEAU_OT" 2>/dev/null | grep -c "Nmap scan report" || true)
if [[ "$HOTES" -eq 0 ]]; then
    echo "| A6 | Balayage du reseau OT | $RESEAU_OT | 0 hote | $HOTES hote(s) | OK |" >> "$SORTIE"
    echo "A6     Balayage du reseau OT                        attendu=0 hote  obtenu=$HOTES     OK"; ((OK++))
else
    echo "| A6 | Balayage du reseau OT | $RESEAU_OT | 0 hote | $HOTES hote(s) | ECHEC |" >> "$SORTIE"
    echo "A6     Balayage du reseau OT                        attendu=0 hote  obtenu=$HOTES     ECHEC"; ((KO++))
fi

# --- B. Ce qui DOIT fonctionner ---------------------------------------------
echo ""
echo "--- B. Flux qui doivent PASSER -------------------------------"
echo "  (a executer depuis les zones legitimes : Z3 pour B1, Z6 pour B2)"
verifie_port "B1" "OPC UA depuis l'IT metier vers le relais DMZ"    "$RELAIS_OPC" 4840 "open"
verifie_port "B2" "Syslog TLS vers le collecteur"                   "$COLLECTEUR" 6514 "open"

# --- C. La DMZ n'est pas un tremplin ----------------------------------------
echo ""
echo "--- C. La DMZ ne doit pas atteindre les automates ------------"
echo "  (a executer DEPUIS le serveur relais de la DMZ)"
verifie_port "C1" "DMZ vers automate (Modbus)"                      "$AUTOMATE" 502 "filtered"

# --- D. Sortie Internet depuis l'OT -----------------------------------------
echo ""
echo "--- D. Un automate ne doit pas joindre Internet --------------"
echo "  (a executer DEPUIS le VLAN OT)"
verifie_port "D1" "OT vers Internet (HTTPS)"                        "$INTERNET" 443 "filtered"

# --- Bilan ------------------------------------------------------------------
{
    echo ""
    echo "## Bilan"
    echo ""
    echo "- Tests conformes : **$OK**"
    echo "- Tests en echec  : **$KO**"
    echo ""
    if [[ "$KO" -eq 0 ]]; then
        echo "> RESULTAT : conforme a la matrice de flux."
    else
        echo "> RESULTAT : **NON CONFORME** - $KO ecart(s). Analyser les journaux du pare-feu"
        echo "> avant toute modification de regle."
    fi
    echo ""
    echo "## Preuves a joindre"
    echo ""
    echo "- [ ] Capture d'ecran horodatee de cette sortie"
    echo "- [ ] Extrait des journaux du pare-feu montrant les blocages (prefixes D01 a D10)"
    echo "- [ ] Capture Wireshark des SYN sans reponse (tests A1 a A5)"
    echo ""
    echo "*Rappel : 'filtered' = le paquet a ete jete (bon resultat)."
    echo "'closed' = le paquet a atteint la cible, qui a repondu RST (moins bon :"
    echo "le pare-feu rejette au lieu de jeter).*"
} >> "$SORTIE"

echo ""
echo "=============================================================="
echo " Conformes : $OK   |   Echecs : $KO"
echo " Rapport ecrit dans : $SORTIE"
echo "=============================================================="

[[ "$KO" -eq 0 ]] && exit 0 || exit 1
