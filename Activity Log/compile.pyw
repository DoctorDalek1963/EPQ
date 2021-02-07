#!/usr/bin/env python

import os
import shutil
import subprocess

if os.path.isfile('Activity_Logger.exe'):
    os.remove('Activity_Logger.exe')

subprocess.call('pyinstaller acca_gui.py -wF -n Activity_Logger --distpath .', shell=True)

os.remove('Activity_Logger.spec')

if os.path.isdir('__pycache__'):
    shutil.rmtree('__pycache__')

shutil.rmtree('build')
