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

# Description:
# This tweak will make the Dock and Menu bar switch to a dark theme
def SystemDarkMenuAndDock(passw):
    print('Switching Dock and Menu bar to a dark theme...')
    util.ext_call([['defaults', 'write', 'NSGlobalDomain', 'AppleInterfaceStyle', 'Dark']])

# Description:
# This tweak will make the Dock and Menu bar switch to a light theme
def SystemLightMenuAndDock(passw):
    print('Switching Dock and Menu bar to a light theme...')
    util.ext_call([['defaults', 'write', 'NSGlobalDomain', 'AppleInterfaceStyle', 'Light']])

# Description:
# This tweak will start automatically hiding the menu bar
def SystemAutoHideMenuBar(passw):
    print('Switching Menu bar to auto hiding...')
    util.ext_call([['defaults', 'write', 'NSGlobalDomain', '_HIHideMenuBar', '-int', '1']])

# Description:
# This tweak will stop automatically hiding the menu bar
def SystemNoHideMenuBar(passw):
    print('Switching Menu bar to static position...')
    util.ext_call([['defaults', 'write', 'NSGlobalDomain', '_HIHideMenuBar', '-int', '0']])

# Description:
# This tweak will change the color variant of buttons, menus and windows to Blue
def SystemAppearanceBlue(passw):
    print('Changing Appearance to blue...')
    util.ext_call([['defaults', 'write', 'NSGlobalDomain', 'AppleAquaColorVariant', '-int', '1']])

# Description:
# This tweak will change the color variant of buttons, menus and windows to Graphite
def SystemAppearanceGraphite(passw):
    print('Changing Appearance to graphite...')
    util.ext_call([['defaults', 'write', 'NSGlobalDomain', 'AppleAquaColorVariant', '-int', '6']])

# Description:
# This tweak will change the size of the Sidebar Icons to small
def SystemSidebarIconsSmall(passw):
    print('Changing Sidebar Icons Size to small...')
    util.ext_call([['defaults', 'write', 'NSGlobalDomain', 'NSTableViewDefaultSizeMode', '-int', '1']])

# Description:
# This tweak will change the size of the Sidebar Icons to medium
def SystemSidebarIconsMedium(passw):
    print('Changing Sidebar Icons Size to medium...')
    util.ext_call([['defaults', 'write', 'NSGlobalDomain', 'NSTableViewDefaultSizeMode', '-int', '2']])

# Description:
# This tweak will change the size of the Sidebar Icons to large
def SystemSidebarIconsLarge(passw):
    print('Changing Sidebar Icons Size to large...')
    util.ext_call([['defaults', 'write', 'NSGlobalDomain', 'NSTableViewDefaultSizeMode', '-int', '3']])

# Description:
# This tweak will change the behavioiur of the scroll bars to
# show/hide automatically based on mouse or trackpad
def SystemShowScrollbarAutomatic(passw):
    print('Changing Scroll Bar behaviour to automatic...')
    util.ext_call([['defaults', 'write', 'NSGlobalDomain', 'AppleShowScrollBars', 'Automatic']])

# Description:
# This tweak will change the behavioiur of the scroll bars to
# show/hide when scrolling
def SystemShowScrollbarWhenScrolling(passw):
    print('Changing Scroll Bar behaviour to show/hide when scrolling...')
    util.ext_call([['defaults', 'write', 'NSGlobalDomain', 'AppleShowScrollBars', 'WhenScrolling']])

# Description:
# This tweak will change the behavioiur of the scroll bars to
# always show
def SystemShowScrollbarAlways(passw):
    print('Changing Scroll Bar behaviour to always show...')
    util.ext_call([['defaults', 'write', 'NSGlobalDomain', 'AppleShowScrollBars', 'Always']])

# Description:
# This tweak will change the behavioiur of the scroll bars to
# jump to the next page when clicked
def SystemClickScrollbarNextPage(passw):
    print('Changing Scroll Bar behaviour to jump to next page when clicked...')
    util.ext_call([['defaults', 'write', 'NSGlobalDomain', 'AppleScrollerPagingBehavior', '-int', '0']])

# Description:
# This tweak will change the behavioiur of the scroll bars to
# jump to to the desired spot when clicked
def SystemClickScrollbarClickedSpot(passw):
    print('Changing Scroll Bar behaviour to jump to the spot that\'s clicked...')
    util.ext_call([['defaults', 'write', 'NSGlobalDomain', 'AppleScrollerPagingBehavior', '-int', '1']])

# Description:
# This tweak will change the behavioiur of the scroll bars to
# jump to to the desired spot when clicked
def SystemClickScrollbarClickedSpot(passw):
    print('Changing Scroll Bar behaviour to jump to the spot that\'s clicked...')
    util.ext_call([['defaults', 'write', 'NSGlobalDomain', 'AppleScrollerPagingBehavior', '-int', '1']])

# Description:
# This tweak will make macOS ask to keep changes
# in a document when closing it.
def SystemAskToKeepChanges(passw):
    print('Setting \'Ask to keep changes when closing documents\'...')
    util.ext_call([['defaults', 'write', 'NSGlobalDomain', 'NSCloseAlwaysConfirmsChanges', '-int', '1']])

# Description:
# This tweak will make macOS stop asking to keep changes
# in a document when closing it.
def SystemDontAskToKeepChanges(passw):
    print('Unsetting \'Ask to keep changes when closing documents\'...')
    util.ext_call([['defaults', 'write', 'NSGlobalDomain', 'NSCloseAlwaysConfirmsChanges', '-int', '0']])

# Description:
# This tweak will make macOS close app's windows when
# quitting it. When activated, open documents
# and windows won't be restored when you reopen an app.
def SystemCloseWindowsOnAppQuit(passw):
    print('Setting \'Close windows when quitting an app\'...')
    util.ext_call([['defaults', 'write', 'NSGlobalDomain', 'NSQuitAlwaysKeepsWindows', '-int', '0']])

# Description:
# This tweak will make macOS not close app's windows when
# quitting it.
def SystemDontCloseWindowsOnAppQuit(passw):
    print('Unsetting \'Close windows when quitting an app\'...')
    util.ext_call([['defaults', 'write', 'NSGlobalDomain', 'NSQuitAlwaysKeepsWindows', '-int', '1']])

    
if __name__ == '__main__':
    sys.exit('Please import this script into "macOS-Initial-Setup-Script.py" and use it from there')