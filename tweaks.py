import os
import sys
from util import util
import dependencies


# Description:
# This tweak will make Finder show hidden files and folders.
def FinderShowHiddenFiles(passw):
    print('Showing hidden files in Finder...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'AppleShowAllFiles', '-bool', 'true'])

# Description:
# This tweak will make Finder hide hidden files and folders.
def FinderHideHiddenFiles(passw):
    print('Hiding hidden files in Finder...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'AppleShowAllFiles', '-bool', 'false'])

# Description:
# This tweak will make Finder show 'Quit' option in it's menu.
def FinderShowQuitMenu(passw):
    print('Showing \'Quit\' menu in Finder...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'QuitMenuItem', '-bool', 'true'])

# Description:
# This tweak will make Finder hide the 'Quit' option in it's menu.
def FinderHideQuitMenu(passw):
    print('Hiding \'Quit\' menu in Finder...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'QuitMenuItem', '-bool', 'false'])

# Description:
# This tweak will show all available hard disks on the desktop
def FinderShowHardDisksOnDesktop(passw):
    print('Showing available hard disks on desktop...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'ShowHardDrivesOnDesktop', '-int', '1'])

# Description:
# This tweak will hide all available hard disks from the desktop
def FinderHideHardDisksFromDesktop(passw):
    print('Hiding available hard disks from desktop...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'ShowHardDrivesOnDesktop', '-int', '0'])

# Description:
# This tweak will show all external disks on the desktop
def FinderShowExtDisksOnDesktop(passw):
    print('Showing available external disks on desktop...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'ShowExternalHardDrivesOnDesktop', '-int', '1'])

# Description:
# This tweak will hide all external disks from the desktop
def FinderHideExtDisksFromDesktop(passw):
    print('Hiding available external disks from desktop...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'ShowExternalHardDrivesOnDesktop', '-int', '0'])

# Description:
# This tweak will show all removable media (CDs, DVDs, iPods etc.) on the desktop
def FinderShowRemovableMediaOnDesktop(passw):
    print('Showing removable media on desktop...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'ShowRemovableMediaOnDesktop', '-int', '1'])

# Description:
# This tweak will hide all removable media (CDs, DVDs, iPods etc.) from the desktop
def FinderHideRemovableMediaFromDesktop(passw):
    print('Hiding removable media from desktop...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'ShowRemovableMediaOnDesktop', '-int', '0'])

# Description:
# This tweak will show all connected servers on the desktop
def FinderShowConnectedServersOnDesktop(passw):
    print('Showing connected servers on desktop...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'ShowMountedServersOnDesktop', '-int', '1'])

# Description:
# This tweak will hide all connected servers from the desktop
def FinderHideConnectedServersFromDesktop(passw):
    print('Hiding connected servers from desktop...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'ShowMountedServersOnDesktop', '-int', '0'])

# Description:
# This tweak set the 'Recents' category as Finders's startup window
def FinderStartupWindowRecents(passw):
    print('Setting \'Recents\' as Finder\'s startup window...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'NewWindowTarget', 'PfAF'])
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'NewWindowTargetPath', 
    'file:///System/Library/CoreServices/Finder.app/Contents/Resources/MyLibraries/myDocuments.cannedSearch'])

# Description:
# This tweak set the /home/<user> directory as Finders's startup window
def FinderStartupWindowHome(passw):
    home = util.get_home_dir()
    print('Setting \'%s\' dir as Finder\'s startup window...' % home)
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'NewWindowTarget', 'PfHm'])
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'NewWindowTargetPath', 'file://%s' % home])

# Description:
# This tweak set the / directory as Finders's startup window
def FinderStartupWindowRoot(passw):
    print('Setting \'/\' (root) dir as Finder\'s startup window...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'NewWindowTarget', 'PfVo'])
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'NewWindowTargetPath', 'file:///'])

# Description:
# This tweak set Finder to open folders in new window
def FinderOpenFoldersInNewWindow(passw):
    print('Setting Finder to open folders in new window...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'FinderSpawnTab', '-int', '0'])

# Description:
# This tweak set Finder to open folders in new tab
def FinderOpenFoldersInNewTab(passw):
    print('Setting Finder to open folders in new tab...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'FinderSpawnTab', '-int', '1'])

# Description:
# This tweak set Finder to show all filename extensions
def FinderShowAllFilenameExtensionsOn(passw):
    print('Showing all filename extensions...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleShowAllExtensions', '-int', '1'])

# Description:
# This tweak set Finder not to show all filename extensions
def FinderShowAllFilenameExtensionsOff(passw):
    print('Hiding known filename extensions...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleShowAllExtensions', '-int', '0'])

# Description:
# This tweak set Finder to show a warning before changing an extension
def FinderShowWarningOnExtensionChangeOn(passw):
    print('Setting Finder to show warnings on extension change...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'FXEnableExtensionChangeWarning', '-int', '1'])

# Description:
# This tweak set Finder not to show a warning before changing an extension
def FinderShowWarningOnExtensionChangeOff(passw):
    print('Setting Finder not to show warnings on extension change...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'FXEnableExtensionChangeWarning', '-int', '0'])

# Description:
# This tweak set Finder to show a warning before removing from iCloud Drive
def FinderShowWarningBeforeRmFromICDriveOn(passw):
    print('Setting Finder to show warnings before removing from iCloud Drive...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'FXEnableRemoveFromICloudDriveWarning', '-int', '1'])

# Description:
# This tweak set Finder not to show a warning before removing from iCloud Drive
def FinderShowWarningBeforeRmFromICDriveOff(passw):
    print('Setting Finder not to show warnings before removing from iCloud Drive...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'FXEnableRemoveFromICloudDriveWarning', '-int', '0'])

# Description:
# This tweak set Finder to show a warning before emptying the trash
def FinderShowWarningBeforeTrashEmptyOn(passw):
    print('Setting Finder to show warning before emptying the trash...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'WarnOnEmptyTrash', '-int', '1'])

# Description:
# This tweak set Finder not to show a warning before emptying the trash
def FinderShowWarningBeforeTrashEmptyOff(passw):
    print('Setting Finder not to show warning before emptying the trash...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'WarnOnEmptyTrash', '-int', '0'])

# Description:
# This tweak automatically remove items from the Trash after 30 days
def FinderAutoEmptyTrashOn(passw):
    print('Setting Trash to auto remove items after 30 days...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'FXRemoveOldTrashItems', '-int', '1'])

# Description:
# This tweak stop removing items automatically from the Trash after 30 days
def FinderAutoEmptyTrashOff(passw):
    print('Setting Trash to not auto remove items after 30 days...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'FXRemoveOldTrashItems', '-int', '0'])

# Description:
# This tweak set Finder to show a POSIX style path in it's title
def FinderPosixPathInTitleOn(passw):
    print('Setting Finder to show a POSIX style path in it\'s title...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', '_FXShowPosixPathInTitle', '-int', '1'])

# Description:
# This tweak set Finder to show the default path style in it's title
def FinderPosixPathInTitleOff(passw):
    print('Setting Finder to show the default path style in it\'s title...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', '_FXShowPosixPathInTitle', '-int', '0'])

# Description:
# This tweak set Finder to show folders before files
def FinderShowFoldersBeforeFilesOn(passw):
    print('Setting Finder to show folders before files...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', '_FXSortFoldersFirst', '-int', '1'])

# Description:
# This tweak set Finder not to show folders before files
def FinderShowFoldersBeforeFilesOff(passw):
    print('Setting Finder not to show folders before files...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', '_FXSortFoldersFirst', '-int', '0'])

# Description:
# This tweak set Finder's search scope to 'This Mac'
def FinderSearchScopeThisMac(passw):
    print('Setting Finder\'s search scope to \'This Mac\'...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'FXDefaultSearchScope', 'SCev'])

# Description:
# This tweak set Finder's search scope to current directory
def FinderSearchScopeCurrentDir(passw):
    print('Setting Finder\'s search scope to current directory...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'FXDefaultSearchScope', 'SCcf'])

# Description:
# This tweak set Finder's search scope to 'Previous search scope'
def FinderSearchScopePrevSeachScope(passw):
    print('Setting Finder\'s search scope to \'Previous search scope\'...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'FXDefaultSearchScope', 'SCsp'])

# Description:
# This tweak will show Finder's tab view
def FinderShowTabView(passw):
    print('Showing Finder\'s tab view...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'ShowTabView', '-int', '1'])

# Description:
# This tweak will hide Finder's tab view
def FinderHideTabView(passw):
    print('Hiding Finder\'s tab view...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'ShowTabView', '-int', '0'])

# Description:
# This tweak will show Finder's sidebar
def FinderShowSidebar(passw):
    print('Showing Finder\'s sidebar...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'ShowSidebar', '-int', '1'])

# Description:
# This tweak will hide Finder's sidebar
def FinderHideSidebar(passw):
    print('Hiding Finder\'s sidebar...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'ShowSidebar', '-int', '0'])

# Description:
# This tweak will show Finder's status bar
def FinderShowStatusBar(passw):
    print('Showing Finder\'s status bar...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'ShowStatusBar', '-int', '1'])

# Description:
# This tweak will hide Finder's status bar
def FinderHideStatusBar(passw):
    print('Hiding Finder\'s status bar...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'ShowStatusBar', '-int', '0'])

# Description:
# This tweak will show Finder's preview pane
def FinderShowPreviewPane(passw):
    print('Showing Finder\'s preview pane...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'ShowPreviewPane', '-int', '1'])

# Description:
# This tweak will hide Finder's preview pane
def FinderHidePreviewPane(passw):
    print('Hiding Finder\'s preview pane...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'ShowPreviewPane', '-int', '0'])

# Description:
# This tweak will show Finder's pathbar
def FinderShowPathbar(passw):
    print('Showing Finder\'s pathbar...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'ShowPathbar', '-int', '1'])

# Description:
# This tweak will hide Finder's pathbar
def FinderHidePathbar(passw):
    print('Hiding Finder\'s pathbar...')
    util.ext_call(['defaults', 'write', 'com.apple.finder', 'ShowPathbar', '-int', '0'])

# Description:
# Restarts Finder (this allows settings to be applied)
def FinderRestart(passw):
    print('Restarting Finder...')
    util.ext_call(['killall', 'Finder'])

# Description:
# This tweak will make Dock to show only the windows of the currently
# focused application. All other windows are hidden in the background.
def DockShowOnlyActiveApp(passw):
    print('Showing only active app windows with Dock...')  
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'single-app', '-bool', 'true'])

# Description:
# This tweak will make Dock to show all non-minimised windows
def DockShowAllActiveApps(passw):
    print('Showing all app windows with Dock...')  
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'single-app', '-bool', 'false'])

# Description:
# This tweak will make Dock a bit smaller
def DockSizeSmaller(passw):
    print('Making Dock a smaller size...')  
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'tilesize', '-int', '45'])

# Description:
# This tweak will make Dock a bit bigger
def DockSizeBigger(passw):
    print('Making Dock a bigger size...') 
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'tilesize', '-int', '59'])

# Description:
# This tweak will return Dock to it's stock size
def DockSizeStock(passw):
    print('Returning Dock to it\'s stock size...') 
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'tilesize', '-int', '52'])

# Description:
# This tweak will turn on Dock magnification
def DockMagnificationOn(passw):
    print('Turning on Dock magnification...')  
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'magnification', '-int', '1'])

# Description:
# This tweak will turn off Dock magnification
def DockMagnificationOff(passw):
    print('Turning off Dock magnification...')   
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'magnification', '-int', '0'])

# Description:
# This tweak will turn return Dock's magnification size small
def DockMagnificationSizeSmall(passw):
    print('Setting Dock\'s magnification size to small...')
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'largesize', '-int', '64'])

# Description:
# This tweak will turn return Dock's magnification size to stock
def DockMagnificationSizeStock(passw):
    print('Returning Dock\'s magnification size to stock...')
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'largesize', '-int', '128'])

# Description:
# This tweak will set Dock's position to the left
def DockPositionLeft(passw):
    print('Setting Dock\'s position to the left...')
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'orientation', 'left'])

# Description:
# This tweak will set Dock's position to the right
def DockPositionRight(passw):
    print('Setting Dock\'s position to the right...')
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'orientation', 'right'])

# Description:
# This tweak will set Dock's position to the bottom
def DockPositionBottom(passw):
    print('Setting Dock\'s position to the bottom...')
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'orientation', 'bottom'])

# Description:
# This tweak will set Dock's window minimizing effect to scale
def DockWindowEffectScale(passw):
    print('Setting Dock\'s window minimizing effect to scale...')
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'mineffect', 'scale'])

# Description:
# This tweak will set Dock's window minimizing effect to genie
def DockWindowEffectGenie(passw):
    print('Setting Dock\'s window minimizing effect to genie...')
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'mineffect', 'genie'])

# Description:
# This tweak will turn on Dock's minimize window to app icon feature
def DockMinimizeWindowToAppIconOn(passw):
    print('Setting Dock\'s Minimize windows to app icon...')
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'minimize-to-application', '-int', '1'])

# Description:
# This tweak will turn off Dock's minimize window to app icon feature
def DockMinimizeWindowToAppIconOff(passw):
    print('Unsetting Dock\'s Minimize windows to app icon...')
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'minimize-to-application', '-int', '0'])

# Description:
# This tweak will turn on Dock's animate opening applications feature
def DockAnimateOpeningAppOn(passw):
    print('Setting Dock\'s Animate opening applicaitions...')
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'launchanim', '-int', '1'])

# Description:
# This tweak will turn off Dock's animate opening applications feature
def DockAnimateOpeningAppOff(passw):
    print('Unsetting Dock\'s Animate opening applicaitions...')
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'launchanim', '-int', '0'])

# Description:
# This tweak will turn on Dock's autohide feature
def DockAutoHideOn(passw):
    print('Setting Dock to autohide...')
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'autohide', '-int', '1'])

# Description:
# This tweak will turn off Dock's autohide feature
def DockAutoHideOff(passw):
    print('Setting Dock to not autohide...')
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'autohide', '-int', '0'])

# Description:
# This tweak will turn on Dock's Show open applications indicators feature
def DockShowAppIndicators(passw):
    print('Setting Dock to show open app indicators...')
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'show-process-indicators', '-int', '1'])

# Description:
# This tweak will turn off Dock's Show open applications indicators feature
def DockHideAppIndicators(passw):
    print('Setting Dock to hide open app indicators...')
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'show-process-indicators', '-int', '0'])

# Description:
# This tweak will make macOS rearrange your spaces based on most recent use.
def DockRearrangeSpacesByMostRecentOn(passw):
    print('Setting Auto rearrange spaces by most recent...')
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'mru-spaces', '-int', '1'])

# Description:
# This tweak will stop macOS rearranging your spaces based on most recent use.
def DockRearrangeSpacesByMostRecentOff(passw):
    print('Unsetting Auto rearrange spaces by most recent...')
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'mru-spaces', '-int', '0'])

# Description:
# This tweak will turn on Dock's grouping of windows by application
def DockGroupWindowsByApplicationOn(passw):
    print('Setting Dock\' group windows by application...')
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'expose-group-apps', '-int', '1'])

# Description:
# This tweak will turn off Dock's grouping of windows by application
def DockGroupWindowsByApplicationOff(passw):
    print('Unsetting Dock\' group windows by application...')
    util.ext_call(['defaults', 'write', 'com.apple.dock', 'expose-group-apps', '-int', '0'])

# Description:
# This tweak will turn off macOS's dashboard
def DockDashboardOff(passw):
    print('Turning off Dashboard...')
    util.ext_call(['defaults', 'write', 'com.apple.dashboard', 'dashboard-enabled-state', '-int', '1'])

# Description:
# This tweak will set macOS's dashboard as a separate space
def DockDashboardAsSpace(passw):
    print('Setting Dashboard as a separate space...')
    util.ext_call(['defaults', 'write', 'com.apple.dashboard', 'dashboard-enabled-state', '-int', '2'])

# Description:
# This tweak will set macOS's dashboard as overlay
def DockDashboardAsOverlay(passw):
    print('Setting Dashboard as overlay...')
    util.ext_call(['defaults', 'write', 'com.apple.dashboard', 'dashboard-enabled-state', '-int', '3'])

# Description:
# Restarts Dock (this allows settings to be applied)
def DockRestart(passw):
    print('Restarting Dock...')
    util.ext_call(['killall', 'Dock'])

# Description:
# This tweak will make the Dock and Menu bar switch to a dark theme
def SystemDarkMenuAndDock(passw):
    print('Switching Dock and Menu bar to a dark theme...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleInterfaceStyle', 'Dark'])

# Description:
# This tweak will make the Dock and Menu bar switch to a light theme
def SystemLightMenuAndDock(passw):
    print('Switching Dock and Menu bar to a light theme...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleInterfaceStyle', 'Light'])

# Description:
# This tweak will start automatically hiding the menu bar
def SystemAutoHideMenuBarOn(passw):
    print('Switching Menu bar to auto hiding...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', '_HIHideMenuBar', '-int', '1'])

# Description:
# This tweak will stop automatically hiding the menu bar
def SystemAutoHideMenuBarOff(passw):
    print('Switching Menu bar to static position...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', '_HIHideMenuBar', '-int', '0'])

# Description:
# This tweak will change the color variant of buttons, menus and windows to Blue
def SystemAppearanceBlue(passw):
    print('Changing Appearance to blue...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleAquaColorVariant', '-int', '1'])

# Description:
# This tweak will change the color variant of buttons, menus and windows to Graphite
def SystemAppearanceGraphite(passw):
    print('Changing Appearance to graphite...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleAquaColorVariant', '-int', '6'])

# Description:
# This tweak will change the size of the Sidebar Icons to small
def SystemSidebarIconsSmall(passw):
    print('Changing Sidebar Icons Size to small...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'NSTableViewDefaultSizeMode', '-int', '1'])

# Description:
# This tweak will change the size of the Sidebar Icons to medium
def SystemSidebarIconsMedium(passw):
    print('Changing Sidebar Icons Size to medium...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'NSTableViewDefaultSizeMode', '-int', '2'])

# Description:
# This tweak will change the size of the Sidebar Icons to large
def SystemSidebarIconsLarge(passw):
    print('Changing Sidebar Icons Size to large...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'NSTableViewDefaultSizeMode', '-int', '3'])

# Description:
# This tweak will change the behavioiur of the scroll bars to
# show/hide automatically based on mouse or trackpad
def SystemShowScrollbarAutomatic(passw):
    print('Changing Scroll Bar behaviour to automatic...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleShowScrollBars', 'Automatic'])

# Description:
# This tweak will change the behavioiur of the scroll bars to
# show/hide when scrolling
def SystemShowScrollbarWhenScrolling(passw):
    print('Changing Scroll Bar behaviour to show/hide when scrolling...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleShowScrollBars', 'WhenScrolling'])

# Description:
# This tweak will change the behavioiur of the scroll bars to
# always show
def SystemShowScrollbarAlways(passw):
    print('Changing Scroll Bar behaviour to always show...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleShowScrollBars', 'Always'])

# Description:
# This tweak will change the behavioiur of the scroll bars to
# jump to the next page when clicked
def SystemClickScrollbarNextPage(passw):
    print('Changing Scroll Bar behaviour to jump to next page when clicked...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleScrollerPagingBehavior', '-int', '0'])

# Description:
# This tweak will change the behavioiur of the scroll bars to
# jump to to the desired spot when clicked
def SystemClickScrollbarClickedSpot(passw):
    print('Changing Scroll Bar behaviour to jump to the spot that\'s clicked...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleScrollerPagingBehavior', '-int', '1'])

# Description:
# This tweak will make macOS ask to keep changes
# in a document when closing it.
def SystemAskToKeepChanges(passw):
    print('Setting \'Ask to keep changes when closing documents\'...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'NSCloseAlwaysConfirmsChanges', '-int', '1'])

# Description:
# This tweak will make macOS stop asking to keep changes
# in a document when closing it.
def SystemDontAskToKeepChanges(passw):
    print('Unsetting \'Ask to keep changes when closing documents\'...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'NSCloseAlwaysConfirmsChanges', '-int', '0'])

# Description:
# This tweak will make macOS close app's windows when
# quitting it. When activated, open documents
# and windows won't be restored when you reopen an app.
def SystemCloseWindowsOnAppQuit(passw):
    print('Setting \'Close windows when quitting an app\'...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'NSQuitAlwaysKeepsWindows', '-int', '0'])

# Description:
# This tweak will make macOS not close app's windows when
# quitting it.
def SystemDontCloseWindowsOnAppQuit(passw):
    print('Unsetting \'Close windows when quitting an app\'...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'NSQuitAlwaysKeepsWindows', '-int', '1'])

# Description:
# This tweak will set Dock's Prefer Tabs when opening windows to Always
def SystemPreferTabsAlways(passw):
    print('Setting Prefer Tabs to Always...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleWindowTabbingMode', 'always'])

# Description:
# This tweak will set Dock's Prefer Tabs when opening windows to Fullscreen
def SystemPreferTabsFullscreen(passw):
    print('Setting Prefer Tabs to Fullscreen...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleWindowTabbingMode', 'fullscreen'])

# Description:
# This tweak will set Dock's Prefer Tabs when opening windows to Manual
def SystemPreferTabsManual(passw):
    print('Setting Prefer Tabs to Manual...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleWindowTabbingMode', 'manual'])

# Description:
# This tweak will turn off Double-Click on window title bar
def SystemDoubleClickOnTitleBarOff(passw):
    print('Unsetting Double-Click on title bar...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleActionOnDoubleClick', 'None'])

# Description:
# This tweak will set Double-Click on window title bar action to Zoom
def SystemDoubleClickOnTitleBarZoom(passw):
    print('Setting Double-Click on title bar to Zoom...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleActionOnDoubleClick', 'Maximize'])

# Description:
# This tweak will set Double-Click on window title bar action to Minimize
def SystemDoubleClickOnTitleBarMinimize(passw):
    print('Setting Double-Click on title bar to Minimize...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleActionOnDoubleClick', 'Minimize'])

# Description:
# This tweak will make macOS switch to the space of the app when you click on it
def SystemSpacesSwitchOnActivateOn(passw):
    print('Setting switch space on activating app...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleSpacesSwitchOnActivate', '-int', '1'])

# Description:
# This tweak will make macOS stop switching spaces when you click on an app
def SystemSpacesSwitchOnActivateOff(passw):
    print('Unsetting switch space on activating app...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleSpacesSwitchOnActivate', '-int', '0'])

# Description:
# This tweak will make macOS divide displays into spaces
def SystemDisplaysToSeparateSpacesOn(passw):
    print('Setting displays to separate spaces...')
    util.ext_call(['defaults', 'write', 'com.apple.spaces', 'spans-displays', '-int', '1'])

# Description:
# This tweak will make macOS stop dividing displays into spaces
def SystemDisplaysToSeparateSpacesOff(passw):
    print('Unsetting displays to separate spaces...')
    util.ext_call(['defaults', 'write', 'com.apple.spaces', 'spans-displays', '-int', '0'])

# Description:
# This tweak will change the temperature units to Celsius
def SystemTempUnitCelsius(passw):
    print('Switching temperature units to Celsius...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleTemperatureUnit', 'Celsius'])

# Description:
# This tweak will change the temperature units to Fahrenheit
def SystemTempUnitFahrenheit(passw):
    print('Switching temperature units to Fahrenheit...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'AppleTemperatureUnit', 'Fahrenheit'])

# Description:
# This tweak change the behaviour of the function keys
# to standard function keys.
# To use the special features on this keys press Fn
def SystemFnKeysDefault(passw):
    print('Switching Function keys behaviour to default function keys...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'com.apple.keyboard.fnState', '-int', '1'])

# Description:
# This tweak change the behaviour of the function keys
# to function as media, brightness etc. keys.
# To use the standard function keys press Fn
def SystemFnKeysMedia(passw):
    print('Switching Function keys behaviour to media keys...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'com.apple.keyboard.fnState', '-int', '0'])

# Description:
# This tweak set the key repeat speed to normal
def SystemKeyRepeatNormal(passw):
    print('Setting the key repeat speed to normal...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'InitialKeyRepeat', '-int', '15'])
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'KeyRepeat', '-int', '6'])

# Description:
# This tweak set the key repeat speed to fast
def SystemKeyRepeatFast(passw):
    print('Setting the key repeat speed to fast...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'InitialKeyRepeat', '-int', '15'])
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'KeyRepeat', '-int', '2'])

# Description:
# This tweak will allow tapping trackpad to make a click
def SystemTapToClickOn(passw):
    print('Enabling tap to click in trackpad...')
    util.ext_call(['defaults', 'write', 'com.apple.AppleMultitouchTrackpad', 'Clicking', '-int', '1'])
    util.ext_call(['defaults', 'write', 'com.apple.driver.AppleBluetoothMultitouch.trackpad', 'Clicking', '-int', '1'])

# Description:
# This tweak will not allow tapping trackpad to make a click
def SystemTapToClickOff(passw):
    print('Disabling tap to click in trackpad...')
    util.ext_call(['defaults', 'write', 'com.apple.AppleMultitouchTrackpad', 'Clicking', '-int', '0'])
    util.ext_call(['defaults', 'write', 'com.apple.driver.AppleBluetoothMultitouch.trackpad', 'Clicking', '-int', '0'])

# Description:
# This tweak will disable the "click" sound when clicking on the trackpad
def SystemSilentClickOn(passw):
    print('Enabling silent click in trackpad...')
    util.ext_call(['defaults', 'write', 'com.apple.AppleMultitouchTrackpad', 'ActuationStrength', '-int', '0'])

# Description:
# This tweak enable the "click" sound when clicking on the trackpad
def SystemSilentClickOff(passw):
    print('Disabling silent click in trackpad...')
    util.ext_call(['defaults', 'write', 'com.apple.AppleMultitouchTrackpad', 'ActuationStrength', '-int', '1'])

# Description:
# This tweak set the scrolling direction to natural
def SystemScrollDirectionNatural(passw):
    print('Setting scrolling direction to natural...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'com.apple.swipescrolldirection', '-int', '1'])

# Description:
# This tweak set the scrolling direction to reversed
def SystemScrollDirectionReversed(passw):
    print('Setting scrolling direction to reversed...')
    util.ext_call(['defaults', 'write', 'NSGlobalDomain', 'com.apple.swipescrolldirection', '-int', '0'])

# Description:
# This tweak will show the battery status indicator in the Menu bar
def SystemUIShowBatteryStatusIndicator(passw):
    print('Showing battery status indicator...')          
    util.ext_call(['defaults', 'write', 'com.apple.systemuiserver',
                    'NSStatusItem Visible com.apple.menuextra.battery', '-int', '1'])

    util.defaults_append_to_array('com.apple.systemuiserver', 'menuExtras',
                               '/System/Library/CoreServices/Menu Extras/Battery.menu')

# Description:
# This tweak will hide the battery status indicator in the Menu bar
def SystemUIHideBatteryStatusIndicator(passw):
    print('Hiding battery status indicator...')          
    util.ext_call(['defaults', 'write', 'com.apple.systemuiserver',
                    'NSStatusItem Visible com.apple.menuextra.battery', '-int', '0'])

    util.defaults_delete_from_array('com.apple.systemuiserver', 'menuExtras',
                               '/System/Library/CoreServices/Menu Extras/Battery.menu')

# Description:
# This tweak will show the battery percentage indicator in the Menu bar
def SystemUIShowBatteryPercentage(passw):
    print('Showing battery percentage indicator...')          
    util.ext_call(['defaults', 'write', 'com.apple.menuextra.battery', 'ShowPercent', 'YES'])

# Description:
# This tweak will hide the battery percentage indicator in the Menu bar
def SystemUIHideBatteryPercentage(passw):
    print('Hiding battery percentage indicator...')          
    util.ext_call(['defaults', 'write', 'com.apple.menuextra.battery', 'ShowPercent', 'NO'])

# Description:
# This tweak will show the volume indicator in the Menu bar
def SystemUIShowVolumeIndicator(passw):
    print('Showing volume indicator...')          
    util.ext_call(['defaults', 'write', 'com.apple.systemuiserver',
                    'NSStatusItem Visible com.apple.menuextra.volume', '-int', '1'])

    util.defaults_append_to_array('com.apple.systemuiserver', 'menuExtras',
                               '/System/Library/CoreServices/Menu Extras/Volume.menu')

# Description:
# This tweak will hide the volume indicator in the Menu bar
def SystemUIHideVolumeIndicator(passw):
    print('Hiding volume indicator...')                     
    util.ext_call(['defaults', 'write', 'com.apple.systemuiserver',
                    'NSStatusItem Visible com.apple.menuextra.volume', '-int', '0'])

    util.defaults_delete_from_array('com.apple.systemuiserver', 'menuExtras',
                               '/System/Library/CoreServices/Menu Extras/Volume.menu')

# Description:
# This tweak will show the Wi-Fi status indicator in the Menu bar
def SystemUIShowWifiStatusIndicator(passw):
    print('Showing Wi-Fi status indicator...')          
    util.ext_call(['defaults', 'write', 'com.apple.systemuiserver',
                    'NSStatusItem Visible com.apple.menuextra.airport', '-int', '1'])

    util.defaults_append_to_array('com.apple.systemuiserver', 'menuExtras',
                               '/System/Library/CoreServices/Menu Extras/AirPort.menu')

# Description:
# This tweak will hide the Wi-Fi status indicator in the Menu bar
def SystemUIHideWifiStatusIndicator(passw):
    print('Hiding Wi-Fi status indicator...')          
    util.ext_call(['defaults', 'write', 'com.apple.systemuiserver',
                    'NSStatusItem Visible com.apple.menuextra.airport', '-int', '0'])

    util.defaults_delete_from_array('com.apple.systemuiserver', 'menuExtras',
                               '/System/Library/CoreServices/Menu Extras/AirPort.menu')

# Description:
# This tweak will show the Bluetooth status indicator in the Menu bar
def SystemUIShowBluetoothStatusIndicator(passw):
    print('Showing Bluetooth status indicator...')          
    util.ext_call(['defaults', 'write', 'com.apple.systemuiserver',
                    'NSStatusItem Visible com.apple.menuextra.bluetooth', '-int', '1'])

    util.defaults_append_to_array('com.apple.systemuiserver', 'menuExtras',
                               '/System/Library/CoreServices/Menu Extras/Bluetooth.menu')

# Description:
# This tweak will hide the Bluetooth status indicator in the Menu bar
def SystemUIHideBluetoothStatusIndicator(passw):
    print('Hiding Bluetooth status indicator...')          
    util.ext_call(['defaults', 'write', 'com.apple.systemuiserver',
                    'NSStatusItem Visible com.apple.menuextra.bluetooth', '-int', '0'])

    util.defaults_delete_from_array('com.apple.systemuiserver', 'menuExtras',
                               '/System/Library/CoreServices/Menu Extras/Bluetooth.menu')

# Description:
# This tweak will show the Siri icon in the Menu bar
def SystemUIShowSiri(passw):
    print('Showing Siri in Menu bar...')          
    util.ext_call(['defaults', 'write', 'com.apple.systemuiserver',
                    'NSStatusItem Visible Siri', '-int', '1'])

    util.ext_call(['defaults', 'write', 'com.apple.Siri',
                    'StatusMenuVisible', '-int', '1'])

# Description:
# This tweak will hide the Siri icon from the Menu bar
def SystemUIHideSiri(passw):
    print('Hiding Siri from Menu bar...')          
    util.ext_call(['defaults', 'write', 'com.apple.systemuiserver',
                    'NSStatusItem Visible Siri', '-int', '0'])

    util.ext_call(['defaults', 'write', 'com.apple.Siri',
                    'StatusMenuVisible', '-int', '0'])

# Description:
# This tweak will show the Clock in the Menu bar
def SystemUIShowClock(passw):
    print('Showing the Clock in Menu bar...')          
    util.ext_call(['defaults', 'write', 'com.apple.systemuiserver',
                    'NSStatusItem Visible com.apple.menuextra.clock', '-int', '1'])

    util.defaults_append_to_array('com.apple.systemuiserver', 'menuExtras',
                               '/System/Library/CoreServices/Menu Extras/Clock.menu')

# Description:
# This tweak will hide the Clock from the Menu bar
def SystemUIHideClock(passw):
    print('Hiding the Clock from Menu bar...')          
    util.ext_call(['defaults', 'write', 'com.apple.systemuiserver',
                    'NSStatusItem Visible com.apple.menuextra.clock', '-int', '0'])

    util.defaults_delete_from_array('com.apple.systemuiserver', 'menuExtras',
                               '/System/Library/CoreServices/Menu Extras/Clock.menu')

# Description:
# This tweak will change the Clock in Menu bar to analog
def SystemUIClockAnalog(passw):
    print('Setting Clock in Menu bar to analog...')          
    util.ext_call(['defaults', 'write', 'com.apple.menuextra.clock', 'IsAnalog', '-int', '1'])

# Description:
# This tweak will change the Clock in Menu bar to digital
def SystemUIClockDigital(passw):
    print('Setting Clock in Menu bar to digital...')          
    util.ext_call(['defaults', 'write', 'com.apple.menuextra.clock', 'IsAnalog', '-int', '0'])

# Description:
# This tweak will start flashing the Clock time separators
def SystemUIClockFlashTimeSeparatorsOn(passw):
    print('Enabling the flashing of the Clock time separators...')          
    util.ext_call(['defaults', 'write', 'com.apple.menuextra.clock', 'FlashDateSeparators', '-int', '1'])

# Description:
# This tweak will stop flashing the Clock time separators
def SystemUIClockFlashTimeSeparatorsOff(passw):
    print('Disabling the flashing of the Clock time separators...')          
    util.ext_call(['defaults', 'write', 'com.apple.menuextra.clock', 'FlashDateSeparators', '-int', '0'])

# Description:
# This tweak will show the Accessibility status indicator in the Menu bar
def SystemUIShowAccessibilityIndicator(passw):
    print('Showing the Accessibility status indicator in Menu bar...')          
    util.ext_call(['defaults', 'write', 'com.apple.systemuiserver',
                    'NSStatusItem Visible com.apple.menuextra.universalaccess', '-int', '1'])

    util.defaults_append_to_array('com.apple.systemuiserver', 'menuExtras',
                               '/System/Library/CoreServices/Menu Extras/UniversalAccess.menu')

# Description:
# This tweak will hide the Accessibility status indicator in the Menu bar
def SystemUIHideAccessibilityIndicator(passw):
    print('Hiding the Accessibility status indicator in Menu bar...')          
    util.ext_call(['defaults', 'write', 'com.apple.systemuiserver',
                    'NSStatusItem Visible com.apple.menuextra.universalaccess', '-int', '0'])

    util.defaults_delete_from_array('com.apple.systemuiserver', 'menuExtras',
                               '/System/Library/CoreServices/Menu Extras/UniversalAccess.menu')

# Description:
# Restarts SystemUIServer (this allows settings to be applied)
def SystemUIRestart(passw):
    print('Restarting SystemUIServer...')
    util.ext_call(['killall', 'SystemUIServer'])

# Description:
# This tweak will set Terminal's startup window
# predefined profile to Basic
def TerminalSetStartupPredefProfileBasic(passw):
    print('Setting Terminal\'s startup profile to \'Basic\'...')          
    util.ext_call(['defaults', 'write', 'com.apple.Terminal', 'Startup Window Settings', 'Basic'])

# Description:
# This tweak will set Terminal's default
# predefined profile to Basic
def TerminalSetPredefProfileBasic(passw):
    print('Setting Terminal\'s profile to \'Basic\'...')
    util.ext_call(['defaults', 'write', 'com.apple.Terminal', 'Default Window Settings', 'Basic'])
    util.ext_call(['defaults', 'write', 'com.apple.Terminal', 'Startup Window Settings', 'Basic'])

# Description:
# This tweak will set Terminal's startup window
# predefined profile to Pro
def TerminalSetStartupPredefProfilePro(passw):
    print('Setting Terminal\'s startup profile to \'Pro\'...')          
    util.ext_call(['defaults', 'write', 'com.apple.Terminal', 'Startup Window Settings', 'Pro'])

# Description:
# This tweak will set Terminal's default
# predefined profile to Pro
def TerminalSetPredefProfilePro(passw):
    print('Setting Terminal\'s profile to \'Pro\'...')
    util.ext_call(['defaults', 'write', 'com.apple.Terminal', 'Default Window Settings', 'Pro'])
    util.ext_call(['defaults', 'write', 'com.apple.Terminal', 'Startup Window Settings', 'Pro'])

# Description:
# This tweak will set new Terminal windows
# to open with the same profile as the startup one.
def TerminalSetNewWindowSameProfile(passw):
    print('Setting new Terminal windows to open with the same profile as the startup one...')          
    util.ext_call(['defaults', 'write', 'com.apple.Terminal', 'NewWindowSettingsBehavior', '-int', '2'])

# Description:
# This tweak will set new Terminal windows
# to open with the default profile instead of
# the same as the startup window.
def TerminalSetNewWindowDefaultProfile(passw):
    print('Setting new Terminal windows to open with the default profile...')          
    util.ext_call(['defaults', 'write', 'com.apple.Terminal', 'NewWindowSettingsBehavior', '-int', '1'])

# Description:
# This tweak will set new Terminal tabs
# to open with the same profile as the startup one.
def TerminalSetNewTabSameProfile(passw):
    print('Setting new Terminal tabs to open with the same profile as the startup one...')          
    util.ext_call(['defaults', 'write', 'com.apple.Terminal', 'NewTabSettingsBehavior', '-int', '2'])

# Description:
# This tweak will set new Terminal tab
# to open with the default profile instead of
# the same as the startup window.
def TerminalSetNewTabDefaultProfile(passw):
    print('Setting new Terminal tabs to open with the default profile...')          
    util.ext_call(['defaults', 'write', 'com.apple.Terminal', 'NewTabSettingsBehavior', '-int', '1'])

# Description:
# This tweak will set new Terminal windows
# to open the same working directory as the startup one.
def TerminalSetNewWindowSameWorkDir(passw):
    print('Setting new Terminal windows to open the same work directory as the startup one...')          
    util.ext_call(['defaults', 'write', 'com.apple.Terminal', 'NewWindowWorkingDirectoryBehavior', '-int', '2'])

# Description:
# This tweak will set new Terminal windows
# to open the default working directory instead of
# the same as the startup one.
def TerminalSetNewWindowDefaultWorkDir(passw):
    print('Setting new Terminal windows to open the default work directory...')          
    util.ext_call(['defaults', 'write', 'com.apple.Terminal', 'NewWindowWorkingDirectoryBehavior', '-int', '1'])

# Description:
# This tweak will set new Terminal tabs
# to open the same working directory as the startup one.
def TerminalSetNewTabSameWorkDir(passw):
    print('Setting new Terminal tabs to open the same work directory as the startup one...')          
    util.ext_call(['defaults', 'write', 'com.apple.Terminal', 'NewTabWorkingDirectoryBehavior', '-int', '2'])

# Description:
# This tweak will set new Terminal tabs
# to open the default working directory instead of
# the same as the startup one.
def TerminalSetNewTabDefaultWorkDir(passw):
    print('Setting new Terminal tabs to open the default work directory...')          
    util.ext_call(['defaults', 'write', 'com.apple.Terminal', 'NewTabWorkingDirectoryBehavior', '-int', '1'])

# Description:
# This tweak will set Terminal
# to switch tabs with cmd + [1 - 9] keys
def TerminalSwitchTabKeysOn(passw):
    print('Setting Terminal to swtich tabs with cmd + [1 - 9] keys...')          
    util.ext_call(['defaults', 'write', 'com.apple.Terminal', 'Command1Through9SwitchesTabs', '-int', '1'])

# Description:
# This tweak will unset Terminal
# to switch tabs with cmd + [1 - 9] keys
def TerminalSwitchTabKeysOff(passw):
    print('Unsetting Terminal to swtich tabs with cmd + [1 - 9] keys...')          
    util.ext_call(['defaults', 'write', 'com.apple.Terminal', 'Command1Through9SwitchesTabs', '-int', '0'])

# Description:
# This tweak will enable Terminal's
# high contrast I beam
def TerminalHighContrastIBeamOn(passw):
    print('Enabling Terminal\'s high contrast I beam...')          
    util.ext_call(['defaults', 'write', 'com.apple.Terminal', 'UseCustomIBeamCursor', '-int', '1'])

# Description:
# This tweak will disable Terminal's
# high contrast I beam
def TerminalHighContrastIBeamOff(passw):
    print('Disabling Terminal\'s high contrast I beam...')          
    util.ext_call(['defaults', 'write', 'com.apple.Terminal', 'UseCustomIBeamCursor', '-int', '0'])

# Description:
# This tweak will export the PS1 variable to the folowing format:
# "<user>@<hostname>:<working_dir_path>$ "
# Colors:
# <user>@<hostname> - bright green
# : - default terminal foreground color (probably white)
# <working_dir_path> - bright blue
# $ - default terminal foreground color (probably white)
def TerminalSetPS1ToPreset1(passw):
    print('Setting the Terminal\'s PS1 to user preset 1...')          
    util.add_env_var({'PS1': [r'\[\e[92m\]\u@\h\[\e[m\]:\[\e[94m\]\w\[\e[m\]\\$ ']},
                        force=True)

# Description:
# This tweak will export remove any
# exported PS1 variables from .bash_profile.
def TerminalResetPS1ToDefault(passw):
    print('Resetting the Terminal\'s PS1 to default...')    
    util.remove_env_var('PS1')

if __name__ == '__main__':
    sys.exit('Please import this script into "macOS-Initial-Setup-Script.py" and use it from there')