#!/usr/bin/env python

import os
import shutil
import subprocess


def compile_acca(gui=True):
    """Compile the Activity Logger using pyinsyaller.

This function takes one argument, gui, which is true by default. If it's true, this function will compile the GUI version of the logger, if false, it will compile the command line version."""
    # Get filename from gui boolean
    filename = 'acca_gui.py' if gui else 'acca_cli.py'

    if os.path.isfile('Activity_Logger.exe'):
        os.remove('Activity_Logger.exe')

    subprocess.call('pyinstaller acca_gui.py -wF -n Activity_Logger --distpath .', shell=True)

    os.remove('Activity_Logger.spec')

    if os.path.isdir('__pycache__'):
        shutil.rmtree('__pycache__')

    shutil.rmtree('build')


if __name__ == "__main__":
    compile_acca()
