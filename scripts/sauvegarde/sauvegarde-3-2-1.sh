#!/usr/bin/env bash
# =============================================================================
#  HydroRegie - Sauvegarde chiffree avec verification d'integrite
#  Projet NIS2 - ecart E-04 (art. 21(2)(c) : continuite et sauvegardes)
#  Version 1.0 - 2026-09-10
#
#  REGLE APPLIQUEE : 3-2-1-1-0
#    3 copies
#    2 supports de nature differente
#    1 copie hors site
#    1 copie HORS LIGNE ou immuable   <-- la seule qui resiste a un rancongiciel
#    0 erreur au dernier test de restauration
#
#  LE TEST QUI DISQUALIFIE UNE SAUVEGARDE :
#    "Depuis mon compte d'administrateur du domaine, puis-je supprimer les
#     sauvegardes ?"  Si oui, un rancongiciel le peut aussi.
#    -> ce script s'execute avec un compte de service HORS DOMAINE.
#
#  USAGE : ./sauvegarde-3-2-1.sh <source> <destination>
# =============================================================================

set -euo pipefail

SOURCE="${1:?Usage: $0 <source> <destination>}"
DESTINATION="${2:?Usage: $0 <source> <destination>}"
DATE="$(date +%Y-%m-%d)"
NOM="sauvegarde-${DATE}"
ARCHIVE="${DESTINATION}/${NOM}.tar.zst"
CHIFFRE="${ARCHIVE}.gpg"
MANIFESTE="${DESTINATION}/manifests/${DATE}.sha256"
JOURNAL="${DESTINATION}/journal-sauvegarde.log"

# Destinataire GPG - la cle privee N'EST PAS sur ce serveur
GPG_DEST="${GPG_DEST:-sauvegarde@hydroregie.local}"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$JOURNAL"; }

mkdir -p "${DESTINATION}/manifests"

log "=== Debut de sauvegarde : $SOURCE -> $DESTINATION ==="

# --- 1. Archive compressee ---------------------------------------------------
log "1/6 Creation de l'archive"
tar --create --file - --directory "$SOURCE" . \
    | zstd -T0 -3 -o "$ARCHIVE" -q
log "    Archive : $(du -h "$ARCHIVE" | cut -f1)"

# --- 2. Empreinte AVANT chiffrement ------------------------------------------
log "2/6 Calcul de l'empreinte"
sha256sum "$ARCHIVE" > "$MANIFESTE"

# --- 3. Chiffrement (art. 21(2)(h)) ------------------------------------------
log "3/6 Chiffrement GPG"
gpg --batch --yes --trust-model always \
    --recipient "$GPG_DEST" --encrypt --output "$CHIFFRE" "$ARCHIVE"
rm -f "$ARCHIVE"
sha256sum "$CHIFFRE" >> "$MANIFESTE"
log "    Archive chiffree : $(du -h "$CHIFFRE" | cut -f1)"

# --- 4. Verification de lisibilite -------------------------------------------
# Une sauvegarde non verifiee n'est pas une sauvegarde, c'est une intention.
log "4/6 Verification de lisibilite de l'archive chiffree"
if gpg --batch --list-packets "$CHIFFRE" >/dev/null 2>&1; then
    log "    OK - archive lisible"
else
    log "    ECHEC - archive illisible ! ALERTE"
    exit 1
fi

# --- 5. Copie hors site ------------------------------------------------------
log "5/6 Copie hors site"
if [[ -n "${SITE_DISTANT:-}" ]]; then
    rsync -a --partial "$CHIFFRE" "$MANIFESTE" "${SITE_DISTANT}/" \
        && log "    OK - copie envoyee vers $SITE_DISTANT" \
        || log "    ECHEC de la copie hors site - ALERTE"
else
    log "    IGNORE - variable SITE_DISTANT non definie"
fi

# --- 6. Copie hors ligne (rappel humain hebdomadaire) ------------------------
log "6/6 Copie hors ligne"
if [[ "$(date +%u)" -eq 5 ]]; then
    log "    >>> VENDREDI : sortir la bande du robot et la stocker hors site <<<"
    log "    >>> Cette copie est la SEULE qui resiste a un rancongiciel     <<<"
    # Notification a l'equipe (a adapter au canal reel)
    # printf 'Sortie de bande hebdomadaire a effectuer\n' | mail -s "[NIS2] Sauvegarde hors ligne" exploitation@...
fi

# --- Bilan -------------------------------------------------------------------
log "=== Sauvegarde terminee : $CHIFFRE ==="

cat <<INFO

--------------------------------------------------------------------
 RAPPELS - ce que le script NE FAIT PAS a votre place
--------------------------------------------------------------------
 [ ] TEST DE RESTAURATION mensuel dans un bac a sable ISOLE
       -> chronometrer : c'est le RTO reel, pas celui du contrat
       -> cible HydroRegie : SCADA restaure en moins de 4 h

 [ ] Verifier que ce compte de service N'EST PAS membre du domaine

 [ ] Verifier que les PROGRAMMES AUTOMATES sont bien dans le perimetre
       -> piege classique : on sauvegarde l'ERP et on oublie les
          programmes automates, qui vivent sur le poste d'ingenierie...
          lui aussi chiffre par le rancongiciel

 [ ] Verifier que la CONFIGURATION DU SCADA (synoptiques, alarmes,
     variables) est sauvegardee

 [ ] Verifier que les CONFIGURATIONS RESEAU (commutateurs, pare-feu,
     VPN) sont versionnees

 Verification d'integrite d'un point de restauration :
   sha256sum -c $MANIFESTE
--------------------------------------------------------------------
INFO
