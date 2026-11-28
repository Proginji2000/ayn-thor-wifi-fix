# AYN Thor — Guía comunitaria del corrector Wi-Fi

[English](en.md) · [Français](fr.md) · [Español](es.md) · [Deutsch](de.md) · [简体中文](zh-CN.md) · [日本語](ja.md) · [한국어](ko.md) · [Русский](ru.md)

**Vista previa: no hay instalador público.** Manual Edition RC1 y Permanent Edition V4.3 RC1 se han probado de forma privada en una sola consola. La distribución pública no está autorizada.

## Compatibilidad
Solo se ha probado `Thor_V1.0.0.377_20260206_165408_user`, kalama, Android 13 (API 33), ranura a. Otros firmwares, ranuras, variantes de hardware y actualizaciones OTA no están cualificados. Detente si la versión o la integridad no coinciden.

## Elige una edición
- Manual Edition: iniciador privado reutilizable; actívalo después de cada arranque completo. Reinicia el framework de Android y cierra las aplicaciones. Un reinicio completo restaura los componentes Wi-Fi originales. La desinstalación completa y la instalación RC2 reforzada no están cualificadas.
- Permanent Edition: módulo privado V4.3 RC1 para Magisk 31.1 en el dispositivo probado. Se activa antes de Zygote y ejecuta dos comprobaciones de salud. Se validaron tres arranques corregidos, seis comprobaciones, recurrencia, protección ante un estado de fallo simulado, desactivación, desinstalación y reinstalación. Nunca combines ambas ediciones.

## Disponible actualmente
En una consola original completamente iniciada, instala Python 3 y las [Android Platform-Tools oficiales](https://developer.android.com/tools/releases/platform-tools). Activa la depuración USB, conecta un solo dispositivo y autoriza la conexión. Desde la raíz del repositorio, ejecuta:
```bash
python3 tools/manual_preflight.py
python3 tools/manual_preflight.py --extract-stock thor-stock-private
```

En Windows usa `py -3` en lugar de `python3` si es necesario. Usa `--adb /path/to/adb` si ADB no está en la ruta habitual (adb.exe para ADB de Windows desde WSL). El segundo comando crea un directorio local privado nuevo. La herramienta solo lee el dispositivo; no obtiene root, flashea, instala ni reinicia. No compruebes el estado original con el parche activo. Conserva los archivos extraídos en privado.

Si ya tienes un candidato generado localmente, puedes verificarlo sin conexión:
```bash
python3 tools/manual_verify_bundle.py path-to-candidate
```

PASS solo confirma las huellas exactas; no autoriza la instalación. El generador público y el procedimiento de instalación completo todavía no están disponibles.

## Seguridad y recuperación
Haz una copia de seguridad antes de cualquier instalación futura. La edición permanente requiere root y una recuperación cualificados de forma independiente; no uses imágenes de arranque modificadas compartidas ni desbloquees o flashees siguiendo esta vista previa. No cambies ranuras ni AVB. Detente ante firmware desconocido, huellas inesperadas, arranque no confirmado o cualquier error. No borres `pending` manualmente. En la instalación privada probada, desactiva o elimina el módulo en Magisk y reinicia normalmente: se restauran los componentes Wi-Fi originales, no la partición de arranque ni el estado root. Para Manual, reinicia sin ejecutar Enable. La recuperación tras un fallo real, la resistencia a cortes de energía, la restauración física de init_boot y la estabilidad a largo plazo no están cualificadas. No se ha cualificado otra consola.

## Soporte
Indica edición, firmware, etapa del error y marcadores de diagnóstico anonimizados. Elimina números de serie, identificadores de arranque, SSID, BSSID, direcciones y datos personales. No publiques firmware, archivos JAR/ODEX/VDEX ni imágenes de arranque. Usa las incidencias del repositorio cuando haya soporte. Proyecto independiente, no oficial de AYN.

[Compatibility matrix](../../compatibility/firmware-matrix.json) · [Release gates](../COMMUNITY_RELEASE.md)
