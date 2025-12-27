# core/updater.py
import subprocess
import sys
from pathlib import Path
import urllib.request
import zipfile
import shutil
import tempfile


class Updater:
    """
    Kümmert sich um:
    - Update der yt-dlp Standalone-EXE
    - Automatisches Update von ffmpeg
    """

    YTDLP_URL = "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe"
    FFMPEG_ZIP_URL = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"

    def __init__(self, status_callback):
        self.status_callback = status_callback
        self.base_path = self._get_base_path()

        self.ytdlp_path = self.base_path / "runtime" / "yt-dlp.exe"
        self.ffmpeg_path = self.base_path / "tools" / "ffmpeg.exe"

    # =========================
    # Public API
    # =========================

    def update_all(self):
        self.status_callback("🔄 Starte Update-Prozess...")
        print("[Updater] Starte Update-Prozess")

        self._update_yt_dlp()
        self._update_ffmpeg()

        print("[Updater] Update-Prozess abgeschlossen")

    # =========================
    # yt-dlp Update (Standalone)
    # =========================

    def _update_yt_dlp(self):
        self.status_callback("⬆ Aktualisiere yt-dlp...")
        print("[Updater] Aktualisiere yt-dlp")

        try:
            self.ytdlp_path.parent.mkdir(parents=True, exist_ok=True)

            tmp_file = self.ytdlp_path.with_suffix(".tmp")

            urllib.request.urlretrieve(self.YTDLP_URL, tmp_file)

            if self.ytdlp_path.exists():
                self.ytdlp_path.unlink()

            tmp_file.rename(self.ytdlp_path)

            self.status_callback("✔ yt-dlp erfolgreich aktualisiert")
            print("[Updater] yt-dlp erfolgreich aktualisiert")

        except Exception as e:
            self.status_callback(f"❌ yt-dlp Update fehlgeschlagen:\n{e}")
            print(f"[Updater] yt-dlp Update fehlgeschlagen: {e}")

    # =========================
    # ffmpeg Update (Auto)
    # =========================

    def _update_ffmpeg(self):
        self.status_callback("⬆ Aktualisiere ffmpeg...")
        print("[Updater] Aktualisiere ffmpeg")

        try:
            self.ffmpeg_path.parent.mkdir(parents=True, exist_ok=True)

            with tempfile.TemporaryDirectory() as tmp_dir:
                zip_path = Path(tmp_dir) / "ffmpeg.zip"

                urllib.request.urlretrieve(self.FFMPEG_ZIP_URL, zip_path)

                with zipfile.ZipFile(zip_path, "r") as zip_ref:
                    zip_ref.extractall(tmp_dir)

                extracted_root = next(Path(tmp_dir).glob("ffmpeg-*"))
                ffmpeg_exe = extracted_root / "bin" / "ffmpeg.exe"

                if not ffmpeg_exe.exists():
                    raise FileNotFoundError("ffmpeg.exe nicht im Archiv gefunden")

                if self.ffmpeg_path.exists():
                    self.ffmpeg_path.unlink()

                shutil.copy(ffmpeg_exe, self.ffmpeg_path)

            self.status_callback("✔ ffmpeg erfolgreich aktualisiert")
            print("[Updater] ffmpeg erfolgreich aktualisiert")

        except Exception as e:
            self.status_callback(f"❌ ffmpeg Update fehlgeschlagen:\n{e}")
            print(f"[Updater] ffmpeg Update fehlgeschlagen: {e}")

    # =========================
    # Helpers
    # =========================

    def _get_base_path(self) -> Path:
        """
        Liefert den korrekten Basispfad:
        - PyInstaller: Ordner der EXE
        - Dev-Modus: Projekt-Root
        """
        if getattr(sys, "frozen", False):
            return Path(sys.executable).parent
        return Path(__file__).resolve().parent.parent
