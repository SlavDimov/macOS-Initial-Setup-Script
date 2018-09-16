import os
import sys
from util import util
import dependencies

# Description:
# This tweak will make Finder show hidden files and folders.
def FinderShowHiddenFiles(passw):
    print('Showing hidden files in Finder...')
    util.ext_call([['killall', 'Finder']])
    util.ext_call([['defaults', 'write', 'com.apple.finder', 'AppleShowAllFiles', '-bool', 'true']])

# Description:
# This tweak will make Finder hide hidden files and folders.
def FinderHideHiddenFiles(passw):
    print('Hiding hidden files in Finder...')
    util.ext_call([['killall', 'Finder']])
    util.ext_call([['defaults', 'write', 'com.apple.finder', 'AppleShowAllFiles', '-bool', 'false']])

# Description:
# This tweak will make Finder show 'Quit' option in it's menu.
def FinderShowQuitMenu(passw):
    print('Showing \'Quit\' menu in Finder...')
    util.ext_call([['killall', 'Finder']])
    util.ext_call([['defaults', 'write', 'com.apple.finder', 'QuitMenuItem', '-bool', 'true']])

# Description:
# This tweak will make Finder hide the 'Quit' option in it's menu.
def FinderHideQuitMenu(passw):
    print('Hiding \'Quit\' menu in Finder...')
    util.ext_call([['killall', 'Finder']])
    util.ext_call([['defaults', 'write', 'com.apple.finder', 'QuitMenuItem', '-bool', 'false']])

# Description:
# This tweak will make Dock to show only the windows of the currently
# focused application. All other windows are hidden in the background.
def DockShowOnlyActiveApp(passw):
    print('Showing only active app windows with Dock...')
    util.ext_call([['killall', 'Dock']])
    util.ext_call([['defaults', 'write', 'com.apple.dock', 'single-app', '-bool', 'true']])

# Description:
# This tweak will make Dock to show all non-minimised windows
def DockShowAllActiveApp(passw):
    print('Showing all app windows with Dock...')
    util.ext_call([['killall', 'Dock']])
    util.ext_call([['defaults', 'write', 'com.apple.dock', 'single-app', '-bool', 'false']])
    
if __name__ == '__main__':
    sys.exit('Please import this script into "macOS-Initial-Setup-Script.py" and use it from there')