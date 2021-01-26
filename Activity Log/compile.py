import os
import shutil

os.system('cmd /c "pyinstaller acca_gui.py -wF -n Activity_Logger --distpath ."')

os.remove('Activity_Logger.spec')

if os.path.isdir('__pycache__'):
    shutil.rmtree('__pycache__')

shutil.rmtree('build')
