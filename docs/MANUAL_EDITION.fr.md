# Manual Edition — guide expérimental (préversion documentaire)

**Disponibilité : précontrôle et extraction locale uniquement. Le parcours d'activation complet n'est pas encore publiable comme installateur utilisable.**

## Objectif

Installer les fichiers corrigés en stockage local, puis lancer manuellement le correctif depuis les paramètres AYN après un démarrage. Aucun flash, changement de slot, changement de politique PCI ou modification du démarrage. Un redémarrage complet retire les montages temporaires. Le firmware complet n'est pas requis pour ce parcours. Sauvegarder ses parties avant toute activation future : le redémarrage du framework ferme les applications.

## Compatibilité

Seul le build exact Thor_V1.0.0.377_20260206_165408_user, kalama, API 33, slot a, a été testé. Ne pas extrapoler à d'autres builds, slots ou variantes matérielles. Les trois empreintes stock doivent correspondre. Une OTA, un autre correctif actif ou des empreintes inconnues imposent STOP. La disponibilité du lanceur root natif AYN doit également être vérifiée. Les essais ont été effectués sur une seule console.

## Étapes disponibles

1. Installer Python 3 et les Android SDK Platform-Tools officiels sur le PC, puis cloner ou télécharger ce dépôt.
2. Activer le débogage USB sur la Thor, la connecter au PC et accepter son autorisation USB.
3. Depuis la racine du dépôt, exécuter :

```bash
python tools/manual_preflight.py
```

Sous Windows, utiliser `py -3` si nécessaire ; sous Linux/WSL, `python3`. Si adb n'est pas dans PATH, ajouter `--adb /chemin/vers/adb` (chemin vers adb.exe sur Windows ou WSL). Un seul appareil USB doit être connecté.

4. Si les contrôles passent, extraire les trois fichiers stock de sa propre console dans un nouveau dossier local :

```bash
python tools/manual_preflight.py --extract-stock thor-stock-private
```

Les fichiers sont propriétaires : les garder hors du dépôt et ne pas les partager. Le script ne modifie pas Android, ne lance aucun processus root, ne redémarre pas la console. Le code de ce nouvel outil n'a pas encore été qualifié sur une seconde console. READ_ONLY_PREFLIGHT_PASS ne signifie pas autorisation d'activation.

## Étapes à finaliser

5. Reconstruire le JAR à partir du stock avec le constructeur autonome, puis compiler localement les composants ART compatibles. La reconstruction actuelle dépend encore d'une archive historique privée et d'une référence binaire ; l'outil autonome n'est pas fourni ici.
6. Vérifier les trois empreintes du candidat avec `python tools/manual_preflight.py --bundle chemin-du-candidat`. Cette vérification ne construit ni n'active le candidat.
7. Le futur installateur portable transférera le candidat et le lanceur manuel. L'activation vérifiera le stock, protégera le worker, armera le watchdog, vérifiera les mappings et le scanner après stabilisation, puis maintiendra le correctif jusqu'au redémarrage si les contrôles passent. Ce parcours combiné doit être qualifié physiquement avant publication de son script comme utilisable.
8. Pour revenir au stock après une activation volatile, effectuer un redémarrage complet. Le retour stock et le rollback autonome ont été démontrés en V3.5-r3 et V3.6 ; ces essais ne qualifient pas la restauration d'une partition de démarrage.

Ne pas utiliser les anciens scripts propres à la session de développement comme installateur public. Ne pas flasher de fichiers partagés, ne pas modifier AVB, ne pas changer de slot. En cas de problème, arrêter et conserver les preuves localement.

## État des preuves

- V3.0 historique : activation manuelle jusqu'au redémarrage démontrée.
- V3.5-r3 : nouveau candidat, scans 8/8, scanner 8/8, joignabilité IP 2/2, mappings ART et retour stock PASS.
- V3.6 : rollback autonome après arrêt brutal du worker PASS.
- Nouvelle Manual Edition combinée : à qualifier ; construction indépendante, portabilité, durcissement et usage prolongé restent à faire.

Voir [la matrice](../compatibility/firmware-matrix.json), [les preuves](TEST_RESULTS.md) et [la récupération](RECOVERY_GATE.md).

### Avancement du constructeur
Le constructeur autonome privé a été assemblé à partir des deux sources historiques vérifiées. Il ne dépend plus de l'archive historique ni du JAR V2. Contrôles locaux de syntaxe, intégrité DEX et empaquetage réussis ; reconstruction intégrale avec les outils verrouillés à effectuer avant publication. Le script d'activation portable reste à intégrer.
