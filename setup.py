import os
import sys
from PyInstaller.__main__ import run

proj_root = os.path.abspath(os.path.dirname(__file__))

# PyInstaller separator: colon on Linux/macOS, semicolon on Windows
sep = ';' if sys.platform == 'win32' else ':'

# PyInstaller arguments
args = [
    '--name=JavSP',
    '--onefile',  # Single exe file
    '--console',  # Show console window (required for stdout/stderr)
    f'--add-data=config.yml{sep}.',  # Include config
    f'--add-data=data{sep}data',  # Include data folder
    f'--add-data=image{sep}image',  # Include image folder
    '--hidden-import=pendulum',
    '--hidden-import=curl_cffi',
    '--hidden-import=lxml_html_clean',
    '--hidden-import=chardet',
    '--hidden-import=charset_normalizer',
    '--additional-hooks-dir=.',
    '--exclude-module=unittest',
    './javsp/__main__.py',
]

if sys.platform == 'win32':
    args.append('--icon=./image/JavSP.ico')

run(args)
