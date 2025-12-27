"""
core/version_info.py
====================
Ermittelt Versionsinformationen von App & externen Tools.
"""

import subprocess
import shutil
from core.version import APP_VERSION


def get_versions():
    versions = {
        "app": APP_VERSION,
        "yt_dlp": "nicht gefunden",
        "ffmpeg": "nicht gefunden",
    }

    # yt-dlp
    try:
        result = subprocess.run(
            ["yt-dlp", "--version"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            versions["yt_dlp"] = result.stdout.strip()
    except FileNotFoundError:
        pass

    # ffmpeg
    if shutil.which("ffmpeg"):
        versions["ffmpeg"] = "vorhanden"

    return versions
