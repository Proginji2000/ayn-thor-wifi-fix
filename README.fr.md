# AYN Thor — Correctif Wi-Fi

[English](docs/community/en.md) · [Français](docs/community/fr.md) · [Español](docs/community/es.md) · [Deutsch](docs/community/de.md) · [简体中文](docs/community/zh-CN.md) · [日本語](docs/community/ja.md) · [한국어](docs/community/ko.md) · [Русский](docs/community/ru.md)

**Qualification privée sur console : PASS — aucun installateur public disponible.**

Projet indépendant visant un correctif reproductible et réversible. Une seule AYN Thor, `Thor_V1.0.0.377_20260206_165408_user` (kalama, Android 13 / API 33, slot a), est qualifiée.

| Édition | Preuves privées | Disponibilité communautaire |
|---|---|---|
| Manual RC1 | Activation réutilisable après démarrage, fonctionnement et retour stock après redémarrage validés | Précontrôle en lecture seule et vérificateur hors ligne uniquement |
| Permanent V4.3 RC1 | Magisk 31.1 ; 3 démarrages corrigés, 6 contrôles de santé, récurrence, protection simulée, désactivation, désinstallation et réinstallation validés | Module privé, aucun installateur public |

Commence par le [guide communautaire](docs/community/fr.md). Les guides en huit langues sont des aperçus documentaires, pas des autorisations d'installation.

## Outils disponibles
- [Précontrôle et extraction stock en lecture seule](tools/manual_preflight.py)
- [Vérification hors ligne du bundle exact](tools/manual_verify_bundle.py)

## Documentation technique
- [Critères de distribution communautaire](docs/COMMUNITY_RELEASE.md)
- [Passation](docs/HANDOFF.md)
- [Preuves](docs/TEST_RESULTS.md)
- [Matrice de compatibilité](compatibility/firmware-matrix.json)
- [Historique Manual Edition](docs/MANUAL_EDITION.fr.md)
- [Historique Permanent Edition](docs/PERMANENT_EDITION.md)
- [Récupération](docs/RECOVERY_GATE.md)
- [Rapport upstream en préparation](docs/UPSTREAM_REPORT.md)

## Sécurité
Ne combine pas les éditions. Firmware inconnu ou OTA non qualifiée : arrêt. L'essai Magisk privé a nécessité une écriture de partition de démarrage strictement autorisée sur la console du propriétaire ; V4.3 n'écrit pas dans les partitions de démarrage. Le retour stock Wi-Fi ne restaure ni le root ni les partitions de démarrage. Récupération après panne réelle, restauration physique d'init_boot, résistance aux coupures, stabilité prolongée et autres consoles non qualifiées. Ne flashe pas d'image partagée et ne redistribue pas d'artefacts propriétaires. Aucune distribution publique autorisée.

Référence : [JoelMomo/AYN-Thor-WiFi-Recovery](https://github.com/JoelMomo/AYN-Thor-WiFi-Recovery). Aucun lien officiel avec ce projet.
