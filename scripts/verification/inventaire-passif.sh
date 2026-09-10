#!/usr/bin/env bash
# =============================================================================
#  HydroRegie - Inventaire PASSIF du reseau industriel
#  Projet NIS2 - ecart E-08 (art. 21(2)(i) : gestion des actifs)
#  Version 1.0 - 2026-09-10
#
#  POURQUOI PASSIF ?
#  Un scan actif agressif peut faire tomber un automate ancien, et donc
#  interrompre la distribution d'eau. En OT, la SURETE prime sur tout le reste.
#  Ce script N'EMET AUCUN PAQUET : il ecoute une copie du trafic sur un port
#  miroir (SPAN) ou via un TAP reseau.
#
#  PREREQUIS : interface raccordee a un port miroir, en RECEPTION SEULE.
#  USAGE     : sudo ./inventaire-passif.sh <interface> [duree_en_secondes]
#  EXEMPLE   : sudo ./inventaire-passif.sh eth1 3600
# =============================================================================

set -uo pipefail

IFACE="${1:-eth1}"
DUREE="${2:-3600}"
HORODATAGE="$(date +%Y%m%d-%H%M)"
CAPTURE="capture-ot-${HORODATAGE}.pcap"
RAPPORT="inventaire-ot-${HORODATAGE}.md"

command -v tcpdump >/dev/null || { echo "ERREUR : tcpdump est requis."; exit 1; }
[[ $EUID -eq 0 ]] || { echo "ERREUR : executer avec sudo."; exit 1; }

echo "=============================================================="
echo " Inventaire PASSIF du reseau OT"
echo " Interface : $IFACE    Duree : ${DUREE}s ($((DUREE/60)) min)"
echo " AUCUN paquet ne sera emis."
echo "=============================================================="
echo ""

# --- 1. Neutraliser l'interface en emission ---------------------------------
# On retire toute adresse IP : l'interface ne peut plus rien envoyer.
ip addr flush dev "$IFACE" 2>/dev/null || true
ip link set "$IFACE" up promisc on
echo "[*] Interface $IFACE en mode promiscuite, sans adresse IP."

# --- 2. Capture --------------------------------------------------------------
echo "[*] Capture en cours vers $CAPTURE ..."
timeout "$DUREE" tcpdump -i "$IFACE" -nn -s 128 -w "$CAPTURE" 2>/dev/null || true
echo "[*] Capture terminee : $(du -h "$CAPTURE" | cut -f1)"

# --- 3. Analyse --------------------------------------------------------------
echo "[*] Analyse ..."

{
    echo "# Inventaire passif du reseau OT"
    echo ""
    echo "| Champ | Valeur |"
    echo "|---|---|"
    echo "| Date | $(date '+%Y-%m-%d %H:%M:%S %Z') |"
    echo "| Interface | $IFACE (port miroir, reception seule) |"
    echo "| Duree de capture | $((DUREE/60)) minutes |"
    echo "| Fichier de capture | \`$CAPTURE\` |"
    echo ""
    echo "> Methode **passive** : aucun paquet emis vers le reseau industriel."
    echo ""

    echo "## 1. Equipements detectes (adresses IP)"
    echo ""
    echo "| Adresse IP | Paquets observes |"
    echo "|---|---|"
    tcpdump -nn -r "$CAPTURE" 2>/dev/null \
        | grep -oE 'IP [0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' \
        | awk '{print $2}' | sort | uniq -c | sort -rn \
        | awk '{printf "| %s | %s |\n", $2, $1}'

    echo ""
    echo "## 2. Protocoles industriels observes"
    echo ""
    echo "| Port | Protocole | Paquets |"
    echo "|---|---|---|"
    for entree in "502:Modbus/TCP" "2404:IEC 60870-5-104" "20000:DNP3" \
                  "44818:EtherNet/IP" "102:S7comm" "4840:OPC UA" "47808:BACnet"; do
        port="${entree%%:*}"; nom="${entree#*:}"
        n=$(tcpdump -nn -r "$CAPTURE" "tcp port $port or udp port $port" 2>/dev/null | wc -l)
        [[ "$n" -gt 0 ]] && printf '| %s | %s | %s |\n' "$port" "$nom" "$n"
    done

    echo ""
    echo "## 3. Couples source -> destination les plus frequents"
    echo ""
    echo "| Flux | Paquets |"
    echo "|---|---|"
    tcpdump -nn -r "$CAPTURE" 2>/dev/null \
        | awk '/IP/ {print $3" -> "$5}' | sed 's/://' \
        | sort | uniq -c | sort -rn | head -30 \
        | awk '{c=$1; $1=""; printf "| %s | %s |\n", substr($0,2), c}'

    echo ""
    echo "## 4. Points de vigilance a verifier manuellement"
    echo ""
    echo "- [ ] Chaque adresse IP de la section 1 figure-t-elle dans l'inventaire officiel ?"
    echo "      *Toute adresse inconnue est un ecart a traiter (E-08).*"
    echo "- [ ] Les ecritures Modbus (codes fonction 05, 06, 16) proviennent-elles"
    echo "      **uniquement** du superviseur SCADA ?"
    echo "- [ ] Observe-t-on des protocoles bureautiques (SMB, HTTP, DNS) dans le VLAN OT ?"
    echo "      *Leur presence est anormale et doit etre expliquee.*"
    echo "- [ ] Observe-t-on du trafic sortant vers Internet depuis l'OT ?"
    echo "- [ ] Les flux observes correspondent-ils tous a une ligne de la matrice de flux ?"
    echo ""
    echo "## 5. Suite"
    echo ""
    echo "1. Rapprocher cette liste de l'inventaire GMAO."
    echo "2. Documenter chaque equipement : marque, modele, version de firmware,"
    echo "   localisation, criticite, responsable, fournisseur."
    echo "3. Alimenter la **matrice de flux** avec les flux legitimes observes."
    echo "4. Renouveler la capture sur un week-end et pendant une astreinte :"
    echo "   certains flux n'existent qu'a ces moments-la."
} > "$RAPPORT"

# --- 4. Restauration --------------------------------------------------------
ip link set "$IFACE" promisc off

echo ""
echo "=============================================================="
echo " Rapport : $RAPPORT"
echo " Capture : $CAPTURE  (a conserver comme preuve, art. 32)"
echo "=============================================================="
