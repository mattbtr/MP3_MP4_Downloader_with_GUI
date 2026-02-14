# 🎵 MP3 / MP4 Downloader (GUI)

 Ein benutzerfreundlicher YouTube MP3/MP4 Downloader mit grafischer Oberfläche, entwickelt in Python mit CustomTkinter und yt-dlp. Das Projekt bietet sowohl eine lokal ausführbare Python-Version als auch eine fertige Windows-EXE, die ohne Python-Installation läuft

## ✨ Features

✅ Download von YouTube-Videos als MP3 oder MP4

✅ Moderne GUI mit CustomTkinter

✅ Rechtsklick-Kontextmenü im URL-Eingabefeld (Kopieren / Einfügen)

✅ Automatische Nutzung von ffmpeg

✅ yt-dlp Update-Mechanismus

✅ Fortschrittsanzeige & Statusmeldungen

✅ Windows-EXE via PyInstaller (onedir)

✅ Automatischer Build über GitHub Actions

## 🚀 Verwendung (Windows – empfohlen (Python u. Ffmpeg in Build vorhanden))

1. Gehe zu Releases oder Actions → Artifacts

2. Lade das ZIP-Archiv herunter

3. Entpacken

4. Starte: MP3_MP4_Downloader.exe im entpacktem Verzeichnis

⚠️ Wichtig:
Bei einem onedir-Build muss der komplette Ordner vorhanden bleiben – nicht nur die .exe.

## 🔄 Updates

yt-dlp und ffmpeg werden über Updaten Button aktuell gehalten. Es empfiehlt sich immer die aktuellste Version vom Repo herunterzuladen und zu nutzen unter /dist/...

## 🛠️ Build (Windows EXE)

🔧 Lokaler Build machen (onedir-Build):

- pyinstaller downloader.spec

## GitHub Actions (CI)

Das Projekt nutzt GitHub Actions, um automatisch eine Windows-EXE zu bauen.

- Workflow-Highlights

- Windows Runner

- Python Setup

- PyInstaller onedir Build

- Upload als Artifact

## ⚠️ Hinweise & Rechtliches

Dieses Tool dient nur zu privaten / Testzwecken

Beachte die Nutzungsbedingungen von YouTube

Der Entwickler übernimmt keine Haftung für Missbrauch

## 🧠 Technologien

Python

yt-dlp

ffmpeg

CustomTkinter

PyInstaller

GitHub Actions


