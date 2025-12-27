import yt_dlp
from pathlib import Path
import sys


class Downloader:
    """
    Downloader-Klasse für MP3 / MP4 Downloads mit yt-dlp.
    """

    def __init__(self, status_callback=None, progress_callback=None, done_callback=None):
        self.status_callback = status_callback
        self.progress_callback = progress_callback
        self.done_callback = done_callback

        # Standard-Download-Ordner
        self.download_path = Path.home() / "Downloads"

        # ffmpeg-Pfad sauber ermitteln (funktioniert auch in .exe)
        self.ffmpeg_path = self._resolve_ffmpeg_path()

    # =========================
    # Öffentliche API
    # =========================

    def download(self, url: str, format_: str):
        try:
            self._set_status("⬇ Download wird vorbereitet...")

            options = (
                self._mp3_options() if format_ == "mp3"
                else self._mp4_options()
            )

            with yt_dlp.YoutubeDL(options) as ydl:
                self._set_status("⬇ Download läuft...")
                ydl.download([url])

            self._set_progress(1.0)

        except Exception as e:
            self._set_status(f"❌ Fehler beim Download:\n{e}")

        finally:
            if self.done_callback:
                self.done_callback()

    # =========================
    # yt-dlp Optionen
    # =========================

    def _base_options(self) -> dict:
        """
        Gemeinsame Optionen für alle Downloads
        """
        options = {
            "outtmpl": str(self.download_path / "%(title)s.%(ext)s"),
            "progress_hooks": [self._progress_hook],
            "quiet": True,
            "now_warnings": True,
            "ffmpeg_location": str(self.ffmpeg_path),
            "noplaylist": True,
        }
        #options.update(self._resolve_js_runtime())
        return options

    def _mp3_options(self) -> dict:
        options = self._base_options()
        options.update({
            "format": "bestaudio/best",
            # Zusatzdateien
            "writethumbnail": True,
            "writeinfojson": False,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                },
                {
                    "key": "EmbedThumbnail",
                },
                {
                    "key": "FFmpegMetadata",
                },
            ],
        })
        return options

    def _mp4_options(self) -> dict:
        options = self._base_options()
        options.update({
            "format": "bestvideo+bestaudio/best",
            # Zusatzdateien
            "writethumbnail": True,
            "writeinfojson": False,
            "merge_output_format": "mp4",

            "postprocessors": [
                {
                    "key": "FFmpegMetadata",
                },
                {
                    "key": "EmbedThumbnail",
                },
            ],
        })
        return options

    # =========================
    # Callbacks
    # =========================

    def _set_status(self, message: str):
        if self.status_callback:
            self.status_callback(message)

    def _set_progress(self, percent: float):
        if self.progress_callback:
            self.progress_callback(percent)

    def _progress_hook(self, d):
        if d["status"] == "downloading":
            downloaded = d.get("downloaded_bytes", 0)
            total = d.get("total_bytes") or d.get("total_bytes_estimate")

            if total:
                percent = downloaded / total
                downloaded_mb = downloaded / (1024 * 1024)
                total_mb = total / (1024 * 1024)

                if self.progress_callback:
                    self.progress_callback(percent, downloaded_mb, total_mb)

        elif d["status"] == "finished":
            if self.progress_callback:
                self.progress_callback(1.0, 0, 0)

    # =========================
    # tools
    # =========================

    def set_download_path(self, path: str):
        self.download_path = Path(path)


    def _resolve_ffmpeg_path(self) -> Path:
        """
        Findet ffmpeg zuverlässig – auch in PyInstaller-EXE
        """
        if getattr(sys, "frozen", False):
            base_path = Path(sys._MEIPASS)
        else:
            base_path = Path(__file__).resolve().parent.parent

        ffmpeg = base_path / "tools" / "ffmpeg.exe"

        if not ffmpeg.exists():
            raise FileNotFoundError(f"ffmpeg nicht gefunden: {ffmpeg}")

        return ffmpeg
    
    def _resolve_js_runtime(self) -> dict:
        """
        Fügt JS-Runtime hinzu, wenn vorhanden
        """
        js_runtime = self._resolve_node_path()

        if js_runtime:
            return {
                "js_runtimes": {
                    "node": str(js_runtime)
                }
            }
        return {}
    
    def _resolve_node_path(self):
        if getattr(sys, "frozen", False):
            base_path = Path(sys._MEIPASS)
        else:
            base_path = Path(__file__).resolve().parent.parent

        node = base_path / "tools" / "node" / "node.exe"
        return node if node.exists() else None



    