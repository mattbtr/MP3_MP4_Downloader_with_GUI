"""
gui/app.py
==========
Beinhaltet die Haupt-GUI der Anwendung.

Diese Datei:
- erstellt das Hauptfenster
- konfiguriert das Erscheinungsbild (Theme, Größe)
- enthält (vorerst) nur einfache UI-Elemente
"""

import customtkinter as ctk
from gui.widgets import UrlInput, FormatSelector, ActionButtons, StatusLabel
import threading
from core.downloader import Downloader
from core.updater import Updater
from gui.widgets import DownloadProgress
from gui.widgets import DownloadPathSelector
from pathlib import Path
from core.settings import SettingsManager
from core.version_info import get_versions
from gui.widgets import VersionLabel
from gui.widgets.process_popup import ProcessResultPopup



class DownloaderApp:
    """
    Hauptklasse für die GUI-Anwendung.
    """

    def __init__(self):
        """
        Konstruktor der GUI.

        Wird aufgerufen, sobald DownloaderApp() erstellt wird.
        """
        # Erscheinungsbild festlegen (Dark / Light / System)
        ctk.set_appearance_mode("System")

        # Farbthema (z. B. "blue", "green", "dark-blue")
        ctk.set_default_color_theme("blue")

        # Hauptfenster erstellen
        self.app = ctk.CTk()
        

        # Fenstereigenschaften
        self.app.title("MP3 / MP4 Downloader")
        self.app.geometry("600x600")
        self.app.resizable(False, True)

        # Settings initialisieren
        self.settings = SettingsManager()
        self.loaded_settings = self.settings.load() or {}

        # UI-Elemente erstellen
        self._create_widgets()

        # Downloader initialisieren
        self.downloader = Downloader(
            status_callback=self._thread_safe_status,
            progress_callback=self._thread_safe_progress,
            done_callback=self._on_download_finished
        )

        # Updater initialisieren
        self.updater = Updater(
            status_callback=self._thread_safe_status
        )


    def _create_widgets(self):
        """
        Erstellt alle UI-Elemente im Hauptfenster.

        Das '_' am Anfang signalisiert:
        → interne Hilfsmethode
        → wird nur innerhalb der Klasse genutzt
        """

        # Titel-Label
        self.title_label = ctk.CTkLabel(
            self.app,
            text="YouTube MP3 / MP4 Downloader",
            font=ctk.CTkFont(size=22, weight="bold")
        )
        self.title_label.pack(pady=(20, 10))

        # Downlaod-Path von Settings holen
        self.path_selector = DownloadPathSelector(
            self.app,
            default_path=self.loaded_settings.get("download_path", "")
        )
        self.path_selector.pack(fill="x", padx=20, pady=5)


         # URL-Eingabe
        self.url_input = UrlInput(self.app)
        self.url_input.pack(fill="x", padx=20, pady=5)

        # Format-Auswahl
        self.format_selector = FormatSelector(self.app)
        self.format_selector.pack(fill="x", padx=20, pady=5)

        # Aktions-Buttons
        self.action_buttons = ActionButtons(
            self.app,
            on_download=self.on_download_clicked,
            on_update=self.on_update_clicked
        )
        self.action_buttons.pack(fill="x", padx=20, pady=10)

        self.progress = DownloadProgress(self.app)
        self.progress.pack(fill="x", padx=20, pady=5)


         # Statusanzeige
        self.status_label = StatusLabel(self.app)
        self.status_label.pack(fill="x", padx=20, pady=(10, 20))

        # Versionsanzeige
        versions = get_versions()
        self.version_label = VersionLabel(self.app, versions)
        self.version_label.pack(fill="x", padx=20, pady=(0, 10))


    # =========================
    # Button-Callbacks
    # =========================
    def on_download_clicked(self):
        """
        Wird aufgerufen, wenn der Download-Button gedrückt wird.
        """
        url = self.url_input.get_url()
        format_ = self.format_selector.get_format()

        self.settings.set("download_path", self.path_selector.get_path())
        self.settings.set("format", format_)
        self.settings.save()

        if not url:
            self.status_label.set_status("❌ Bitte eine YouTube-URL eingeben.")
            return
        
        # UI vorbereiten
        self.action_buttons.disable()
        self.progress.reset()

        # Platzhalter – echte Logik kommt später
        self.status_label.set_status(f"⬇ Download gestartet\nURL: {url}\nFormat: {format_.upper()}")

        self.downloader.set_download_path(
            self.path_selector.get_path()
        )

        # Download in separatem Thread starten
        thread = threading.Thread(
            target=self.downloader.download,
            args=(url, format_),
            daemon=True
        )
        thread.start()

        

    def on_update_clicked(self):
        """
        Wird aufgerufen, wenn der Update-Button gedrückt wird.
        """
        self.action_buttons.disable()
        self.progress.reset()
        self.status_label.set_status("🔄 Update wird gestartet...")
        

        thread = threading.Thread(
            target=self._run_update,
            daemon=True
        )
        thread.start()


    def _on_download_finished(self):
        """
        Wird nach dem Download im GUI-Thread aufgerufen.
        """
        self.action_buttons.enable()
        self.status_label.set_status("✅ Download abgeschlossen")

        ProcessResultPopup(
            parent=self.app,
            title="Download abgeschlossen",
            success=True,
            summary="Der Download wurde erfolgreich durchgeführt.",
            details=[
                "Komponente: yt-dlp",
                "Audio extrahiert mit ffmpeg",
                f"Zielordner:\n{self.path_selector.get_path()}",
            ],
        )


    def _thread_safe_status(self, text: str):
        self.app.after(0, self.status_label.set_status, text)

    def _thread_safe_progress(self, percent: float, downloaded_mb, total_mb):
        self.app.after(0, self.progress.update_progress, percent, downloaded_mb, total_mb)


    
    def _run_update(self):
        """
        Führt den Update-Prozess im Hintergrund aus.
        """
        self.updater.update_all()
        self.app.after(0, self._on_update_finished)


    def _on_update_finished(self):
        """
        Wird nach Abschluss des Updates im GUI-Thread aufgerufen.
        """
        self.action_buttons.enable()
        self.status_label.set_status("✅ Update abgeschlossen")

        ProcessResultPopup(
            parent=self.app,
            title="Update abgeschlossen",
            success=True,
            summary="Alle Komponenten wurden aktualisiert.",
            details=[
                "yt-dlp aktualisiert",
                "ffmpeg aktualisiert",
            ],
        )


    def run(self):
        """
        Startet die GUI-Event-Schleife.

        Diese Methode blockiert den Thread,
        bis das Fenster geschlossen wird.
        """
        self.app.mainloop()

