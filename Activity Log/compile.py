#!/usr/bin/env python

"""This module compiles the Activity Logger in GUI or CLI format. GUI by default.

Functions:
    compile_logger(gui=True):
        Compile the Activity Logger according to the truthiness of the gui keyword argument. It's true by default.

"""

import os
import shutil
import subprocess


def compile_logger(gui=True):
    """Compile the Activity Logger using pyinstaller.

    Keyword arguments:
        gui:
            A boolean which is true if not specified. If true, the function will compile the GUI, if false, it will compile the CLI version.
    """
    # Get filename from gui boolean
    filename = 'gui.py' if gui else 'cli.py'

    if os.path.isfile('Activity_Logger.exe'):
        os.remove('Activity_Logger.exe')

    subprocess.call(f'pyinstaller {filename} -wF -n Activity_Logger --distpath .', shell=True)

    os.remove('Activity_Logger.spec')

    if os.path.isdir('__pycache__'):
        shutil.rmtree('__pycache__')

    shutil.rmtree('build')


if __name__ == "__main__":
    compile_logger()
