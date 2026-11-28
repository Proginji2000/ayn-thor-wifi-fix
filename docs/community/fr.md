# AYN Thor — Guide communautaire

[English](en.md) · [Français](fr.md) · [Español](es.md) · [Deutsch](de.md) · [简体中文](zh-CN.md) · [日本語](ja.md) · [한국어](ko.md) · [Русский](ru.md)

**Prépublication — aucun installateur public.** Manual Edition RC1 et Permanent Edition V4.3 RC1 ont été testées en privé sur une seule console. La distribution publique n'est pas autorisée.

## Compatibilité
Seul `Thor_V1.0.0.377_20260206_165408_user`, kalama, Android 13 (API 33), slot a, a été testé. Autres firmwares, slots, variantes matérielles et mises à jour OTA non qualifiés. Arrête si la version ou les contrôles d'intégrité diffèrent.

## Choisir une édition
- Manual Edition : lanceur privé réutilisable, activation après chaque démarrage complet. L'activation redémarre le framework Android et ferme les applications. Un redémarrage complet restaure les composants Wi-Fi stock. Désinstallation complète et installation RC2 durcie non qualifiées.
- Permanent Edition : module privé V4.3 RC1 pour Magisk 31.1 sur la console testée. Activation avant Zygote et deux contrôles de santé. Trois démarrages corrigés, six contrôles, récurrence, protection sur état d'échec simulé, désactivation, désinstallation et réinstallation réussis. Ne combine jamais les deux éditions.

## Disponible actuellement
Sur une console stock complètement démarrée, installe Python 3 et les [Android Platform-Tools officiels](https://developer.android.com/tools/releases/platform-tools). Active le débogage USB, connecte une seule console et autorise la connexion. À la racine du dépôt, exécute :
```bash
python3 tools/manual_preflight.py
python3 tools/manual_preflight.py --extract-stock thor-stock-private
```

Sous Windows, utilise `py -3` si nécessaire à la place de `python3`. Indique `--adb /path/to/adb` pour un exécutable ADB non standard (adb.exe avec ADB Windows depuis WSL). La deuxième commande crée un nouveau dossier local privé. L'outil lit uniquement la console ; il ne root pas, ne flashe pas, n'installe rien et ne redémarre pas. Ne lance pas le contrôle stock sur un correctif actif. Garde les fichiers extraits privés.

Si tu disposes déjà d'un candidat construit localement, le vérificateur hors ligne est disponible :
```bash
python3 tools/manual_verify_bundle.py path-to-candidate
```

Un PASS confirme uniquement les empreintes exactes. Il n'autorise pas l'installation. Le constructeur public et la procédure d'installation complète ne sont pas encore disponibles.

## Sécurité et récupération
Sauvegarde tes données avant toute future installation. L'édition permanente nécessite un environnement root et une récupération déjà qualifiés indépendamment ; n'utilise pas d'image de démarrage patchée partagée, ne déverrouille ni ne flashe à partir de cet aperçu. Ne change pas de slot ni d'AVB. Arrête sur un firmware inconnu, une empreinte inattendue, un démarrage non confirmé ou une erreur. Ne supprime pas manuellement `pending`. Sur l'installation privée testée, désactive ou supprime le module dans Magisk, puis redémarre normalement : les composants Wi-Fi reviennent au stock, pas la partition de démarrage ni l'état root. Pour Manual, redémarre sans exécuter Enable. Récupération après panne réelle, résistance aux coupures, restauration physique d'init_boot et stabilité prolongée non qualifiées. Aucune autre console qualifiée.

## Assistance
Indique l'édition, le firmware, l'étape en échec et les marqueurs de diagnostic anonymisés. Retire numéros de série, identifiants de démarrage, SSID, BSSID, adresses et données personnelles. Ne publie pas les firmwares, fichiers JAR/ODEX/VDEX ou images de démarrage. Utilise les issues du dépôt lorsque l'assistance sera disponible. Projet indépendant, non officiel AYN.

[Compatibility matrix](../../compatibility/firmware-matrix.json) · [Release gates](../COMMUNITY_RELEASE.md)
