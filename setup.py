import os
import sys
from PyInstaller.__main__ import run

proj_root = os.path.abspath(os.path.dirname(__file__))

# PyInstaller arguments
args = [
    '--name=JavSP',
    '--onefile',  # Single exe file
    '--windowed',  # No console window
    '--add-data=config.yml;.',  # Include config
    '--add-data=data;data',  # Include data folder
    '--add-data=image;image',  # Include image folder
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
