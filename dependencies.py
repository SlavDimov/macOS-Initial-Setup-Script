import sys
from util import util


# Description:
# This function will install/re-install the XCode Command Developer tools
# for your Mac. These tools are needed for the script to function properly
# and provide many more tools, such as gcc, make, git etc.
def InstallXCodeCmdDevTools(passw):
    print('Installing XCode Command Line Developer Tools...')
    util.ext_call([['osascript', 'general.scpt', 'InstallXCodeCmdDevTools']])

# Description:
# This function will remove the XCode Command Developer Tools
def UninstallXCodeCmdDevTools(passw):
    print('Uninstalling XCode Command Line Developer Tools...')
    util.ext_call([['rm','-rf','/Library/Developer/CommandLineTools']], sudopass=passw)

    
# Description:
# This function will install Homebrew
def InstallHomebrew(passw):
    print("Installing Homebrew...")
    if util.check_command_exists('brew'): return
    if not util.check_path_exists(util.GIT_DIR): InstallXCodeCmdDevTools(passw)
    script = util.ext_call([['curl', '-fsSL', 
    'https://raw.githubusercontent.com/Homebrew/install/master/install']], getstdout=True, sudopass=passw)
    util.ext_call([['echo', '-ne', '\'\n\''],
              ['/usr/bin/ruby', '-e', script]])

# Description:
# This function will uninstall Homebrew
def UninstallHomebrew(passw):
    print("Uninstalling Homebrew...")
    if not util.check_command_exists('brew'): return
    if not util.check_path_exists(util.GIT_DIR): InstallXCodeCmdDevTools(passw)
    script = util.ext_call([['curl', '-fsSL', 
    'https://raw.githubusercontent.com/Homebrew/install/master/uninstall']], getstdout=True, sudopass=passw)
    util.ext_call([['echo', '-ne', '\'\n\''],
              ['/usr/bin/ruby', '-e', script]])


if __name__ == '__main__':
    sys.exit('Please import this script into "macOS-Initial-Setup-Script.py" and use it from there')