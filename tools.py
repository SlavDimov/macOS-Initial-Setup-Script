import os
import sys
from util import util
import dependencies


# Description:
# Installs Google's Go language via Homebrew
def InstallGolang(passw):
    print("Installing Golang...")

    brewname = 'go'
    if not util.check_command_exists('brew'): dependencies.InstallHomebrew()
    util.install_app(brewname, passw,
                      cask=False,
                    #   ext_verbose=True,
                     )

    # adding enviroment variables to .bash_profile
    install_dir = util.ext_call(['brew', '--prefix', brewname],
                                getstdout=True).strip(' \t\n')
                                
    util.add_env_var({'GOPATH':['${HOME}', '.go']})
    util.add_env_var({'GOROOT':[install_dir, 'libexec']},
                     force=True
                    )
    util.append_to_path(['${GOPATH}','bin'],
                        ['${GOROOT}','bin'],
                        force=True
                        ) 

# Description:
# Uninstalls Google's Go language
def UninstallGolang(passw):
    print("Uninstalling Golang...")

    brewname = 'go'    
    install_dir = ''

    install_dir = os.path.join(util.get_brew_cellar(), brewname)
    
    pkg_names = list(set(util.get_symlinks(
                util.PKG_SYMLINK_DIRS,
                [util.get_file_with_parents(install_dir, 1)],
                # basename=False
            )))
    if not pkg_names: return    
    additional_dirs = [
        install_dir
	]
    util.remove_app(pkg_names, passw,
	 				 misc_files_and_dirs=additional_dirs,
					 brewname=brewname,
                     std_dirs=util.PKG_SYMLINK_DIRS,
                     cask=False,
	#				 debug=True,
	#				 nobrew=True,
    #                ext_verbose=True,
	)

    # removing enviroment variables from .bash_profile
    # Deliberately not removing 'GOPATH' since it might
    # be changed to a custom path
    util.remove_env_var('GOROOT',
                        #  'GOPATH',
                        )
    util.remove_from_path(['${GOROOT}','bin'],
                          ['${GOPATH}','bin']
                        ) 
    

# Description:
# Installs Python3 via Homebrew
def InstallPython3(passw):
    print("Installing Python3...")

    brewname = 'python3'
    if not util.check_command_exists('brew'): dependencies.InstallHomebrew()
    util.install_app(brewname, passw,
                      cask=False,
                    #   ext_verbose=True,
                     )

# Description:
# Uninstalls Python3
def UninstallPython3(passw):
    print("Uninstalling Python3...")

    brewname = 'python3'    
    package_dir_name = 'python'
    install_dir = ''
    
    install_dir = os.path.join(util.get_brew_cellar(), package_dir_name)

    pkg_names = list(set(util.get_symlinks(
                util.PKG_SYMLINK_DIRS,
                [util.get_file_with_parents(install_dir, 1)],
                # basename=False
            )))
    if not pkg_names: return
    additional_dirs = [
        install_dir
	]
    util.remove_app(pkg_names, passw,
	 				 misc_files_and_dirs=additional_dirs,
					 brewname=brewname,
                     std_dirs=util.PKG_SYMLINK_DIRS,
                     cask=False,
	#				 debug=True,
	#				 nobrew=True,
	#      			 ext_verbose=True,
    )
    
if __name__ == '__main__':
    sys.exit('Please import this script into "macOS-Initial-Setup-Script.py" and use it from there')