"""
main.py
========
Einstiegspunkt der Anwendung.

Diese Datei:
- startet die GUI
- enthält bewusst KEINE UI- oder Download-Logik
- sorgt für eine saubere Trennung von Start und Implementierung

Wichtig für:
- Übersichtlichkeit
- spätere Erstellung einer .exe mit PyInstaller
"""

from gui.app import DownloaderApp


def main():
    """
    Hauptfunktion der Anwendung.
    Erstellt das GUI-Fenster und startet die Event-Schleife.
    """
    app = DownloaderApp()
    app.run()


# Schutz, damit main() nur ausgeführt wird,
# wenn diese Datei direkt gestartet wird
if __name__ == "__main__":
    main()
