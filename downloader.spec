# downloader.spec
# =================

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[
        ('tools/ffmpeg.exe', 'tools'),
        ('tools/node/node.exe', 'tools/node'),
    ],
    datas=[
        ('runtime/yt-dlp.exe', 'runtime'),
        ('gui', 'gui'),
        ('core', 'core'),
    ],
    hiddenimports=[
        'yt_dlp',
        'customtkinter',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MP3_MP4_Downloader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='MP3_MP4_Downloader'
)
