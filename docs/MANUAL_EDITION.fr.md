# Manual Edition — guide expérimental (préversion documentaire)

**Current status (2026-11-28):** historical evidence below is retained. V4.3 RC1 owner lifecycle is qualified; public installer and independent recovery remain unqualified. See [community release gates](COMMUNITY_RELEASE.md) and [community guides](community/en.md).

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

5. Reconstruire le JAR à partir du stock avec le constructeur autonome, puis compiler localement les composants ART compatibles. La reconstruction autonome a réussi en privé sans archive ni référence binaire ; le constructeur et la compilation ART portable ne sont pas encore distribués.
6. Vérifier les trois empreintes du candidat avec `python tools/manual_preflight.py --bundle chemin-du-candidat`. Cette vérification ne construit ni n'active le candidat.
7. Le futur installateur portable transférera le candidat et le lanceur manuel. L'activation vérifiera le stock, protégera le worker, armera le watchdog, vérifiera les mappings et le scanner après stabilisation, puis maintiendra le correctif jusqu'au redémarrage si les contrôles passent. Le pilote combiné a passé la qualification physique sur une seule console. Le script reste privé en attendant la revue de sécurité et l'intégration de la génération ART.
8. Pour revenir au stock après une activation volatile, effectuer un redémarrage complet. Le retour stock et le rollback autonome ont été démontrés en V3.5-r3 et V3.6 ; ces essais ne qualifient pas la restauration d'une partition de démarrage.

Ne pas utiliser les anciens scripts propres à la session de développement comme installateur public. Ne pas flasher de fichiers partagés, ne pas modifier AVB, ne pas changer de slot. En cas de problème, arrêter et conserver les preuves localement.

## État des preuves

- V3.0 historique : activation manuelle jusqu'au redémarrage démontrée.
- V3.5-r3 : nouveau candidat, scans 8/8, scanner 8/8, joignabilité IP 2/2, mappings ART et retour stock PASS.
- V3.6 : rollback autonome après arrêt brutal du worker PASS.
- Manual Edition pilote : installation, activation, rejet de doublon et réactivation après redémarrage PASS. Portabilité, durcissement, désinstallation et usage prolongé restent à faire.

Voir [la matrice](../compatibility/firmware-matrix.json), [les preuves](TEST_RESULTS.md) et [la récupération](RECOVERY_GATE.md).

### Avancement du constructeur
Le constructeur autonome privé a été assemblé à partir des deux sources historiques vérifiées. Il ne dépend plus de l'archive historique ni du JAR V2. Contrôles locaux de syntaxe, intégrité DEX et empaquetage réussis ; reconstruction intégrale avec les versions de référence réussie en privé. Le script d'activation portable reste à intégrer.


### Reconstruction autonome validée
Un build WSL complet a produit exactement le JAR et le DEX qualifiés, sans archive ni ancien JAR. Le prototype privé de lanceur manuel réutilisable a passé la qualification physique ; il installe des fichiers locaux, sans activation automatique au démarrage. Le constructeur public, la génération ART portable et l'installateur complet restent à publier après revue et essais. Aucun nouveau cycle de huit scans requis pour les artefacts identiques.


## Utilisation après installation du pilote (déjà testé en privé)
Après un redémarrage complet, lancer le même fichier Enable depuis les paramètres AYN, une seule fois. Sauvegarder les parties avant activation : le framework Android redémarre. Attendre la fin du contrôle de disponibilité (environ 70 s observées). Le correctif reste actif jusqu'au prochain redémarrage complet ; aucun PC n'est requis pour cette activation. Pour revenir au stock, redémarrer et ne pas relancer Enable. Cela désactive le correctif mais ne supprime pas les fichiers locaux. La désinstallation complète reste à qualifier. Ne pas lancer sur un firmware différent après OTA.

Les deux activations ont passé les contrôles ART et de scan (9,13 s et 9,14 s) ; le second lancement dans le même boot a été rejeté sans changement du framework. Le redémarrage a conservé l'installation et restauré le stock. Le même lanceur a réactivé le correctif sans transfert. Ce parcours n'est pas encore disponible comme téléchargement public autonome. Aucun firmware complet n'est nécessaire à l'édition manuelle.


## RC2 — préparation de distribution
Le kit privé réunit le constructeur, la compilation ART portable, le pilote durci et la désinstallation réversible. 30 contrôles locaux PASS ; aucune nouvelle exécution Android. Le vérificateur public [manual_verify_bundle.py](../tools/manual_verify_bundle.py) vérifie hors ligne le triplet exact : `python3 tools/manual_verify_bundle.py chemin-du-bundle`. Il ne construit, ne transfère ni n'active le correctif. Le kit complet reste privé en attendant la qualification ART reproductible, le nouvel amorçage, le retrait et la revue de sécurité. Aucun firmware complet requis pour la Manual Edition.

Essai physique RC2 : compilation native et contrôles ART réussis, VDEX identique, ODEX différent. Le contrôle strict a refusé le bundle. Système actif inchangé. Analyse binaire hors ligne requise avant distribution ; aucune nouvelle compilation nécessaire pour cette analyse.

Comparaison finale OAT : équivalence complète des deux ODEX observés hors checksum, taille et métadonnées de chemins autorisées ; tous les autres octets identiques. Le contrôle d'activation par empreinte exacte reste inchangé. Le vérificateur d'équivalence autonome privé est en qualification ; il ne permet pas l'activation d'un nouveau bundle. Prochaine étape : retrait réversible et amorçage durci RC2 lors d'un redémarrage stock planifié.

Vérificateur autonome : PASS sur les deux ODEX réels. Le contrôle strict d'activation reste inchangé. Retrait réversible et nouvel amorçage à tester sur le triplet historique exact qualifié ; le retrait conserve son verrou jusqu'au redémarrage.

### RC2 — qualification suspendue
Le retrait n'a pas été confirmé : les tentatives d'amorçage natif s'arrêtent avant le désinstallateur ou ne produisent pas de journal. Le système stock et l'installation RC1 restent intacts. RC1 demeure la solution personnelle déjà qualifiée ; le durcissement RC2 et la désinstallation restent non qualifiés. Aucun installateur public complet disponible. Ne pas contourner les contrôles d'intégrité.
