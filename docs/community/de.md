# AYN Thor — Community-Leitfaden zur WLAN-Korrektur

[English](en.md) · [Français](fr.md) · [Español](es.md) · [Deutsch](de.md) · [简体中文](zh-CN.md) · [日本語](ja.md) · [한국어](ko.md) · [Русский](ru.md)

**Vorschau – kein öffentlicher Installer.** Manual Edition RC1 und Permanent Edition V4.3 RC1 wurden privat auf einer einzigen Konsole getestet. Die öffentliche Verteilung ist nicht freigegeben.

## Kompatibilität
Getestet wurde ausschließlich `Thor_V1.0.0.377_20260206_165408_user`, kalama, Android 13 (API 33), Slot a. Andere Firmware, Slots, Hardwarevarianten und OTA-Updates sind nicht qualifiziert. Bei abweichender Version oder Integritätsprüfung abbrechen.

## Edition auswählen
- Manual Edition: privater wiederverwendbarer Launcher, nach jedem vollständigen Start manuell aktivieren. Die Aktivierung startet das Android-Framework neu und schließt Anwendungen. Ein vollständiger Neustart stellt die ursprünglichen WLAN-Komponenten wieder her. Vollständige Deinstallation und gehärtete RC2-Installation sind nicht qualifiziert.
- Permanent Edition: privates Modul V4.3 RC1 für Magisk 31.1 auf dem getesteten Gerät. Aktivierung vor Zygote und zwei Zustandsprüfungen. Drei korrigierte Starts, sechs Prüfungen, wiederholte Aktivierung, Schutz bei simuliertem unbestätigtem Start, Deaktivierung, Deinstallation und Neuinstallation bestanden. Beide Editionen niemals gleichzeitig verwenden.

## Derzeit verfügbar
Auf einer vollständig gestarteten Konsole im Originalzustand Python 3 und die offiziellen [Android Platform-Tools](https://developer.android.com/tools/releases/platform-tools) installieren. USB-Debugging aktivieren, genau ein USB-Gerät verbinden und die Verbindung autorisieren. Im Stammverzeichnis des Repositorys ausführen:
```bash
python3 tools/manual_preflight.py
python3 tools/manual_preflight.py --extract-stock thor-stock-private
```

Unter Windows bei Bedarf `py -3` statt `python3` verwenden. Mit `--adb /path/to/adb` einen abweichenden ADB-Pfad angeben (adb.exe bei Windows-ADB aus WSL). Der zweite Befehl erstellt ein neues privates lokales Verzeichnis. Das Werkzeug liest nur; es rootet, flasht, installiert und startet das Gerät nicht neu. Keine Stock-Prüfung bei aktivem Patch. Extrahierte Dateien privat aufbewahren.

Ein bereits lokal erzeugter Kandidat lässt sich offline prüfen:
```bash
python3 tools/manual_verify_bundle.py path-to-candidate
```

PASS bestätigt nur die exakten Prüfsummen und ist keine Installationsfreigabe. Öffentlicher Builder und vollständiger Installationsablauf sind noch nicht verfügbar.

## Sicherheit und Wiederherstellung
Vor einer späteren Installation Daten sichern. Die permanente Edition erfordert eine unabhängig qualifizierte Root- und Wiederherstellungsumgebung. Keine fremden gepatchten Boot-Images verwenden, nicht anhand dieser Vorschau entsperren oder flashen. Slots und AVB nicht ändern. Bei unbekannter Firmware, unerwarteter Prüfsumme, unbestätigtem Start oder Fehler abbrechen. `pending` nicht manuell löschen. Bei der getesteten privaten Installation das Modul in Magisk deaktivieren oder entfernen und normal neu starten: Nur die WLAN-Komponenten kehren zum Originalzustand zurück, nicht Boot-Partition oder Root-Zustand. Bei Manual ohne Enable neu starten. Wiederherstellung nach echtem Boot-Fehler, Stromausfallbeständigkeit, physische init_boot-Wiederherstellung und Langzeitstabilität sind nicht qualifiziert. Keine weitere Konsole qualifiziert.

## Unterstützung
Edition, Firmware, Fehlerstufe und anonymisierte Diagnosemarker angeben. Seriennummern, Boot-IDs, SSIDs, BSSIDs, Adressen und personenbezogene Daten entfernen. Keine Firmware, JAR/ODEX/VDEX-Dateien oder Boot-Images hochladen. Nach Verfügbarkeit des Supports den Issue-Tracker nutzen. Unabhängiges Projekt, keine offizielle AYN-Veröffentlichung.

[Compatibility matrix](../../compatibility/firmware-matrix.json) · [Release gates](../COMMUNITY_RELEASE.md)
