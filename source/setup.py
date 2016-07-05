"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['Calculadora Paypal.py']
DATA_FILES = ['MainMenu.xib', 'Credits.rtf', 'CPP.icns']
OPTIONS = {'argv_emulation': False, 'iconfile': "CPP.icns"} 

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    name="CPP",
    version="0.1",
)
