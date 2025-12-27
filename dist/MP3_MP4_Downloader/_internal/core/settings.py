"""
core/settings.py
================
Verwaltet das Laden und Speichern von App-Einstellungen.
"""

import json
from pathlib import Path


class SettingsManager:
    def __init__(self):
        # settings.json liegt im Projektordner
        self.settings_file = Path("settings.json")

        # Default-Werte
        self.defaults = {
            "download_path": str(Path.home() / "Downloads"),
            "format": "mp3",
        }

        self.settings = self.defaults.copy()

    # =========================
    # Laden / Speichern
    # =========================

    def load(self):
        """
        Lädt Einstellungen aus settings.json
        """
        if self.settings_file.exists():
            try:
                with open(self.settings_file, "r", encoding="utf-8") as f:
                    self.settings.update(json.load(f))
            except Exception:
                # Bei kaputter Datei → Defaults nutzen
                self.settings = self.defaults.copy()

        return self.settings

    def save(self):
        """
        Speichert Einstellungen in settings.json
        """
        with open(self.settings_file, "w", encoding="utf-8") as f:
            json.dump(self.settings, f, indent=4)

    # =========================
    # Getter / Setter
    # =========================

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key):
        return self.settings.get(key, self.defaults.get(key))
