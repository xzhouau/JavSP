import os
import sys
from pathlib import Path
from PyInstaller.building.build_main import Analysis, PYZ, EXE

# Get project root from spec file location (spec is in project root)
spec_dir = Path(sys.argv[0] if '__file__' not in dir() else __file__).parent.resolve()
proj_root = spec_dir

sys.path.insert(0, str(proj_root))

version = "5.2.5"

block_cipher = None

# All web crawler modules
web_modules = [
    'airav', 'arzon', 'arzon_iv', 'avsox', 'avwiki', 'dl_getchu',
    'fanza', 'fc2', 'fc2fan', 'fc2ppvdb', 'gyutto', 'jav321',
    'javbus', 'javdb', 'javlib', 'javmenu', 'mgstage', 'njav',
    'prestige', 'proxyfree', 'translate',
]

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
] + [f'javsp.web.{m}' for m in web_modules]

a = Analysis(
    [str(proj_root / 'javsp' / '__main__.py')],
    pathex=[str(proj_root)],
    binaries=[],
    datas=[
        (str(proj_root / 'config.yml'), '.'),
        (str(proj_root / 'data'), 'data'),
        (str(proj_root / 'image'), 'image'),
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
    icon=str(proj_root / 'image' / 'JavSP.ico') if sys.platform == 'win32' else None,
)
