# AYN Thor — Correctif Wi-Fi

[English](README.md)

**Expérimental — récupération en fonctionnement testée ; installation permanente non qualifiée.**

Sur une AYN Thor équipée du firmware Android 13 `Thor_V1.0.0.377_20260206_165408_user`, les diagnostics répétés du système original montrent un blocage du scanner Wi-Fi Android pendant le traitement des résultats. Le correctif Java historique V2 a été testé sur la console avec ses artefacts ART associés et la politique d'alimentation PCI d'origine (auto). V3.0 permet une activation manuelle volatile ; un redémarrage complet restaure le système original. Le maintien du PCI actif seul n'est pas une solution permanente démontrée.

V3.3-r3 produit deux JAR strictement identiques lors de deux constructions locales complètes. Les 3 138 classes désassemblées correspondent au candidat historique. Le binaire diffère de V2 : sa compilation ART native et sa qualification fonctionnelle temporaire ont réussi (V3.5-r3, 8/8 scans). Le rollback autonome après arrêt brutal du worker a réussi (V3.6). Aucune installation permanente ni distribution stable autorisée.

## Manual Edition — préparation communautaire
- [Tutoriel expérimental et état de disponibilité](docs/MANUAL_EDITION.fr.md)
- [Script de précontrôle et extraction stock](tools/manual_preflight.py)

Le script est en lecture seule sur la console. La reconstruction indépendante a réussi en privé sur le WSL d'origine ; le pilote manuel a réussi l'installation, le rejet de doublon et la réactivation après redémarrage. Le constructeur et le lanceur restent privés ; l'installateur portable public complet n'est pas encore disponible.

## Documentation
- [Passation et prochaine étape](docs/HANDOFF.md)
- [Preuves et limites](docs/TEST_RESULTS.md)
- [Matrice de compatibilité](compatibility/firmware-matrix.json)
- [Plan de persistance et maintenance](docs/PERSISTENCE_PLAN.md)
- [Rapport upstream en préparation, non transmis](docs/UPSTREAM_REPORT.md)
- [Consignes pour les agents IA](AGENTS.md)

## Sécurité
Seul le firmware exact testé est dans le périmètre. Refuser toute activation sur une version inconnue ou après une OTA non qualifiée. Aucune installation permanente, restauration de partition ou activation automatique au démarrage n'est qualifiée. Aucun flash de partition n'a été effectué. L'objectif est un correctif maintenable, réversible et idéalement intégré par le constructeur, sans redistribution de binaires propriétaires. Aucune version stable n'est disponible. Les expériences historiques ne constituent pas un guide d'installation.

Référence : [JoelMomo/AYN-Thor-WiFi-Recovery](https://github.com/JoelMomo/AYN-Thor-WiFi-Recovery).
