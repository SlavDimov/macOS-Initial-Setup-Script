import os
import sys
from util import util
import dependencies


# Description:
# Installs Microsoft's Visual Studio Code editor via Homebrew
def InstallVSCode(passw):
	print("Installing Visual Studio Code...")
	if not util.check_command_exists('brew'): dependencies.InstallHomebrew()
	util.install_app('visual-studio-code', passw,
                    #   ext_verbose=True
                     )

# Description:
# Uninstalls Microsoft's Visual Studio Code editor
def UninstallVSCode(passw):
	print("Uninstalling Visual Studio Code...")

	cfg_file = 'com.microsoft.VSCode*'
	recents = 'com.microsoft.vscode*'
	app_dir = 'Visual Studio Code.app'
	support_dir = 'Code'
	brewname = 'visual-studio-code'
	additional_dirs = [
		os.path.join(os.path.expanduser('~'), '.vscode')
	]
	util.remove_app([cfg_file, app_dir, support_dir, recents], passw,
	 				 misc_files_and_dirs=additional_dirs,
					 brewname=brewname,
	#				 debug=True,
	#				 nobrew=True,
	#				 ext_verbose=True,
	)

# Description:
# Installs Microsoft's Skype via Homebrew
def InstallSkype(passw):
	print("Installing Skype...")
	if not util.check_command_exists('brew'): dependencies.InstallHomebrew()
	util.install_app('skype', passw,
                    #   ext_verbose=True
                     )

# Description:
# Uninstalls Microsoft's Skype
def UninstallSkype(passw):
	print("Uninstalling Skype...")

	cfg_file = 'com.skype.skype*'
	app_dir = 'Skype.app'
	support_dir = 'Skype*'
	other = [
		'ByHost/com.skype.skype*',
		'T/Skype*',
		'CrashReporter/Skype*',
	]
	brewname = 'skype'
	additional_dirs = [
		os.path.join(os.path.expanduser('~'), 'Library/Address Book Plug-Ins/Skype*'),
		os.path.join(os.path.expanduser('~'), 'Library/WebKit/com.skype.skype*'),

	]
	util.remove_app([cfg_file, app_dir, support_dir] + other, passw,
	 				 misc_files_and_dirs=additional_dirs,
					 brewname=brewname,
	#				 debug=True,
	#				 nobrew=True,
	#				 ext_verbose=True,
	)

# Description:
# Installs Google Chrome via Homebrew
def InstallChrome(passw):
	print("Installing Chrome...")
	if not util.check_command_exists('brew'): dependencies.InstallHomebrew()
	util.install_app('google-chrome', passw,
                    #   ext_verbose=True
                     )

# Description:
# Uninstalls Google Chrome
def UninstallChrome(passw):
	print("Uninstalling Chrome...")

	cfg_file = 'com.google.Chrome*'
	recents = 'com.google.chrome*'
	app_dir = 'Google Chrome.app'
	support_dir = 'Google/Chrome'
	brewname = 'google-chrome'
	additional_dirs = [
        '/Library/Google/Google Chrome Brand*',
		os.path.join(os.path.expanduser('~'), 'Library/Google/Google Chrome Brand*'),
		os.path.join(os.path.expanduser('~'), 'Library/WebKit/com.google.Chrome*'),
	]
	util.remove_app([cfg_file, app_dir, support_dir, recents], passw,
	 				 misc_files_and_dirs=additional_dirs,
					 brewname=brewname,
	#				 debug=True,
	#				 nobrew=True,
	#				 ext_verbose=True,
	)

# Description:
# Installs Spotify via Homebrew
def InstallSpotify(passw):
	print("Installing Spotify...")
	if not util.check_command_exists('brew'): dependencies.InstallHomebrew()
	util.install_app('spotify', passw,
                    #   ext_verbose=True
                     )

# Description:
# Uninstalls Spotify
def UninstallSpotify(passw):
	print("Uninstalling Spotify...")

	cfg_file = 'com.spotify.client*'
	app_dir = 'Spotify.app'
	support_dir = 'Spotify'
	brewname = 'spotify'
	additional_dirs = [
	]
	util.remove_app([cfg_file, app_dir, support_dir], passw,
	 				 misc_files_and_dirs=additional_dirs,
					 brewname=brewname,
	#				 debug=True,
	#				 nobrew=True,
	#				 ext_verbose=True,
	)

# Description:
# Installs VLC via Homebrew
def InstallVLC(passw):
	print("Installing VLC...")
	if not util.check_command_exists('brew'): dependencies.InstallHomebrew()
	util.install_app('vlc', passw,
                    #   ext_verbose=True
                     )

# Description:
# Uninstalls Spotify
def UninstallVLC(passw):
	print("Uninstalling VLC...")

	cfg_file = 'org.videolan.vlc*'
	app_dir = 'VLC.app'
	support_dir = 'VLC'
	brewname = 'vlc'
	additional_dirs = [
	]
	util.remove_app([cfg_file, app_dir], passw,
	 				 misc_files_and_dirs=additional_dirs,
					 brewname=brewname,
	#				 debug=True,
	#				 nobrew=True,
	#				 ext_verbose=True,
	)

# Description:
# Installs Libre Office via Homebrew
def InstallLibreOffice(passw):
	print("Installing Libre Office...")
	if not util.check_command_exists('brew'): dependencies.InstallHomebrew()
	util.install_app('libreoffice', passw,
                    #   ext_verbose=True
                     )

# Description:
# Uninstalls Libre Office
def UninstallLibreOffice(passw):
	print("Uninstalling Libre Office...")

	cfg_file = 'org.libreoffice*'
	app_dir = 'LibreOffice.app'
	support_dir = 'LibreOffice'
	brewname = 'libreoffice'
	additional_dirs = [
	]
	util.remove_app([cfg_file, app_dir, support_dir], passw,
	 				 misc_files_and_dirs=additional_dirs,
					 brewname=brewname,
	#				 debug=True,
	#				 nobrew=True,
	#				 ext_verbose=True,
	)

# Description:
# Installs Rocket Chat via Homebrew
def InstallRocketChat(passw):
	print("Installing Rocket Chat...")
	if not util.check_command_exists('brew'): dependencies.InstallHomebrew()
	util.install_app('rocket-chat', passw,
                    #   ext_verbose=True
                     )

# Description:
# Uninstalls Rocket Chat
def UninstallRocketChat(passw):
	print("Uninstalling Rocket Chat...")

	cfg_file = 'chat.rocket*'
	app_dir = 'Rocket.Chat.app'
	support_dir = 'Rocket.Chat'
	brewname = 'rocket-chat'
	additional_dirs = [
	]
	util.remove_app([cfg_file, app_dir, support_dir], passw,
	 				 misc_files_and_dirs=additional_dirs,
					 brewname=brewname,
	#				 debug=True,
	#				 nobrew=True,
	#				 ext_verbose=True,
	)


if __name__ == '__main__':
    sys.exit('Please import this script into "macOS-Initial-Setup-Script.py" and use it from there')