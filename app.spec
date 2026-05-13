# -*- mode: python ; coding: utf-8 -*-

# WARNING: The .env file below is bundled into the executable. Never run
# PyInstaller with a .env that contains real production secrets — those values
# will be embedded inside the distributed binary.

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[('src/assets', 'src/assets'), ('.env', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
    onefile=True,
)
