import os
import sys
from pathlib import Path
from PyInstaller.building.build_main import Analysis, PYZ, EXE

proj_root = Path(__file__).parent.resolve()
sys.path.insert(0, str(proj_root))

version = "5.2.5"

block_cipher = None

hiddenimports = [
    'pendulum',
    'curl_cffi',
    'lxml_html_clean',
    'chardet',
    'charset_normalizer',
    'lxml',
    'lxml.html',
    'lxml.etree',
    'lxml_html_clean',
]

a = Analysis(
    ['javsp/__main__.py'],
    pathex=[str(proj_root)],
    binaries=[],
    datas=[
        ('config.yml', '.'),
        ('data', 'data'),
        ('image', 'image'),
    ],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    key=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='JavSP',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    console=True,
    icon='image/JavSP.ico' if sys.platform == 'win32' else None,
)
