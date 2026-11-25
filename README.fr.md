# AYN Thor — contournement du blocage Wi-Fi

**Expérimental.** Un essai de récupération réussi le 25 novembre 2026 sur le firmware Thor_V1.0.0.377_20260206_165408_user (Android 13). La prévention et la persistance ne sont pas qualifiées.

Le pilote Qualcomm détectait des points d'accès, mais le scanner Android restait bloqué. Le maintien du périphérique PCI 17cb:1107 actif, suivi d'un redémarrage explicite du framework Android, a restauré 17 résultats de scan et l'accès Internet.

Voir [les preuves et limites](docs/TEST_RESULTS.md), [le plan de persistance](docs/PERSISTENCE_PLAN.md) et [le rapport communautaire en préparation](docs/UPSTREAM_REPORT.md).

Le paramètre runtime PM est temporaire. Il peut augmenter la consommation. Le redémarrage du framework ferme les applications : sauvegarder les parties. Aucun flash, aucune modification de partition, aucun changement SELinux. Ne pas utiliser sur un autre appareil sans qualification.

Référence : [JoelMomo/AYN-Thor-WiFi-Recovery](https://github.com/JoelMomo/AYN-Thor-WiFi-Recovery).
