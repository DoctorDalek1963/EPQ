#!/usr/bin/env python

"""This module compiles the Activity Logger in GUI or CLI format. GUI by default.

Functions:
    compile_logger(gui=True) -> None:
        Compile the Activity Logger according to the truthiness of the gui keyword argument. It's true by default.

"""

import os
import shutil
import subprocess

env_text = '''# Any value with spaces should be wrapped in "double quotes"

LEARNER_NAME=
LEARNER_NUMBER=
CENTRE_NAME=
CENTRE_NUMBER=
UNIT_NAME=
UNIT_NUMBER=
TEACHER_ASSESSOR=
PROPOSED_PROJECT_TITLE=

# This is "Activity Log" if not set
FILENAME=

# I'd recommend keeping these both True, but if you
# don't care about the markdown version, you can
# set that to False
# If you set the HTML version to False, then the
# "Open HTML file" button on the GUI won't work
CREATE_HTML=True
CREATE_MARKDOWN=True
'''

readme_text = '''# Activity Logger

This is a Python project to make writing an EPQ Activity Log a bit easier.

To use this yourself, you need to change the values in `.env`. The format should be self-explanatory.

If you're on MacOS or Linux, you need to run the GUI on the command line. First run `pip install -r requirements.txt` and then run `python gui.py`. Alternatively, you could run `python compile.py` to create a binary executable, although this requires pyinstaller, which can be installed with `pip install pyinstaller`.
'''


def compile_logger(gui=True) -> None:
    """Compile the Activity Logger using pyinstaller.

    Keyword arguments:
        gui:
            A boolean which is true if not specified. If true, the function will compile the GUI, if false, it will compile the CLI version.
    """
    # Get filename from gui boolean
    filename = 'gui.py' if gui else 'cli.py'

    if os.path.isfile('Activity_Logger.zip'):
        os.remove('Activity_Logger.zip')

    # Create temporary directory to hold everything
    os.mkdir('compile_temp')

    # Copy files to temporary directory
    shutil.copy('gui.py', 'compile_temp/')
    shutil.copy('cli.py', 'compile_temp/')
    shutil.copy('library.py', 'compile_temp/')
    shutil.copy('requirements.txt', 'compile_temp/')

    # Create other files in temporary directory
    open('compile_temp/.env', 'w').write(env_text)
    open('compile_temp/README.md', 'w').write(readme_text)

    subprocess.call(f'pyinstaller {filename} -wF -n Activity_Logger --distpath ./compile_temp', shell=True)

    os.remove('Activity_Logger.spec')

    # Zip up compiled program with dependencies
    shutil.make_archive('Activity_Logger', 'zip', 'compile_temp')

    # Clear and remove unnecessary directories
    shutil.rmtree('build')
    shutil.rmtree('compile_temp')
    if os.path.isdir('__pycache__'):
        shutil.rmtree('__pycache__')


if __name__ == "__main__":
    compile_logger()
