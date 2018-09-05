import sys
import os
from glob import glob
import subprocess

GIT_DIR = '/Library/Developer/CommandLineTools/usr/bin/git'

APP_DIRS = [
    '/Applications/',
    os.path.join(os.path.expanduser('~'), 'Library/Application Support/'),
	os.path.join(os.path.expanduser('~'), 'Library/Preferences/'),
	os.path.join(os.path.expanduser('~'), 'Library/Caches/'),
	os.path.join(os.path.expanduser('~'), 'Library/Saved Application State/'),
]

# Description:
# This function can be called to COMPLETELY remove an app and all
# of it's settings.
# It will first check if homebrew is installed, and if it is
# it will call it to uninstall the desired app. It will then go
# through all of the directories defined in the global variable
# 'APP_DIRS', it will search for the application names defined
# by the user, and it will delete every file/folder that matches.
#
# Usage:
#   app_names:
#       A list containing all of the application defined names.
#       This is a list, because apps typically have different
#       names in the different directories. For example an app may
#       have the following files/dirs associated with it:
#           Myapp.app       - in /Applications
#           com.myorg.myapp - in Cache/Preferences folders
#           Myorg/Myapp     - in Applicatioms support
#           -etc.
#       NOTE: A wildcard ('*') is allowed in an app name here.
#             For example one might give a 'com.myorg.myapp*'
#             as one of the app names in the list
#   passw - the sudo password that every function needs to receive
#            as argument. It will be passed to ext_call
#   misc_files_and_dirs - Default - None. A list of additional
#                         directories/files that need to be
#                         deleted and are not located in
#                         'APP_DIRS' directories
#                        NOTE: The paths given here need to be
#                              exact. No wildcards available.
#   nobrew - Default - False. If set to True, homebrew won't be
#            called to uninstall the app (in case it is even installed)
#   brewname - Needs to be provided if 'nobrew == False'. This is what
#              app's homebrew name is.
#   debug - Default - False. If set to True it disables the homebrew
#           uninstall (regardles of the 'nobrew' value) and only
#           prints (it doesn't delete them) the directories found
#           by the provided 'app_names' and 'misc_files_and_dirs'.
#           It can be used to check what will be deleted before
#           actually deleting the app.
#   ext_verbose - Default - False. If set to true every it will set
#                 every ext_call's verbose parameter to True.
def delete_app(app_names, passw, misc_files_and_dirs=None, nobrew=False,
               brewname=None, debug=False, ext_verbose=False):
    if not isinstance(app_names, list):
        raise TypeError('Provided var is not a list')
    
    if not (nobrew or debug):
        if not isinstance(brewname, str):
            raise TypeError('brewname var is not a string')
        if len(brewname) == 0:
            raise TypeError('Provided string is empty')
        if check_command_exists('brew'):
            #dummy command, so cask wont ask for password again
            ext_call([['echo']], sudopass=passw, verbose=ext_verbose)
            ext_call([['brew','cask','uninstall', brewname]], verbose=ext_verbose)
      
    if misc_files_and_dirs:
        if not isinstance(misc_files_and_dirs, list):
            raise TypeError('Provided var is not a list')         
        for item in misc_files_and_dirs:
            if os.path.exists(item):
                if not debug:
                    ext_call([['rm','-rf', item]], sudopass=passw, verbose=ext_verbose)   
                else:
                    print(item)
    
    for dir_ in APP_DIRS:
        for name in app_names:
            res = glob(os.path.join(dir_, name))
            if res:
                for item in res:
                    if not debug:
                        ext_call([['rm','-rf', item]], sudopass=passw, verbose=ext_verbose)
                    else:
                        print(item)


# Description:
# It uses subprocess to make calls to bash commands.
# Usage:
#   cmd_list - a list of lists ( [ [], [], ...] ) with all the commands (passed the
#       way 'subprocess.Popen()' expects them) that need to be executed.
#       If more than one sublist(command) is present inside the main list it will be piped
#       to the next command.
#       For example a list of 3 commands: mylist = [cmd1, cmd2, cmd3] will be piped as:
#       cmd1 | cmd2 | cmd3
#       Of course , as discussed, cmd1, cmd2 and cmd3 are lists and it will be passed
#       directly to subprocess.Popen()
#   getstdout - Default - False. If set to True the result (stdout) of the
#       given (chain of) commands will be returned.
#       stdout = ext_call(...)
#   sudopass - Default - None. If set to the user's sudo pass it will add a
#       "echo '<pass>' | sudo -S ..." to the beginning of the user specified
#       (chain of) commands, resulting in execution as root.
#   verbose - Default - False. If set to true it will allow every executed
#       command's stdout and stderr to be printed in the terminal. Normally
#       this is only needed for debugging purposes.
def ext_call(cmd_list, getstdout=False, sudopass=None, verbose=False):
    if not isinstance(cmd_list, list): raise TypeError('Provided var is not a list')
    if len(cmd_list) == 0: raise ValueError('List is empty')
    if not any(isinstance(i, list) for i in cmd_list): 
        raise TypeError('One or more elements of the provided list is not a list')
    if any(not i for i in cmd_list): 
        raise TypeError('One or more elements of the provided list is an empty list')
    if any(not isinstance(y, str) for x in cmd_list for y in x): 
        raise TypeError('One or more of the nested lists elements is not a string')
    if any(not y for x in cmd_list for y in x): 
        raise TypeError('One or more of the nested lists elements is an empty string')
    
    process = None
    next_process = None
    cmd_list_last_idx = len(cmd_list) - 1

    DEVNULL = None
    try:
        DEVNULL = subprocess.DEVNULL
    except:
        DEVNULL = open(os.devnull, 'w')

    for i, cmd in enumerate(cmd_list):
        if i == 0:
            std_dict = {}
            if not verbose: std_dict.update({"stderr":DEVNULL,
                                             "stdout":DEVNULL})
            if sudopass:
                sudo_echo_cmd = ['echo', "%s\n" % sudopass.strip('\n')]
                cmd = ['sudo', '-S'] + cmd
                process = subprocess.Popen(sudo_echo_cmd, stdout=subprocess.PIPE,
                                           **({"stderr":DEVNULL} if not verbose else {}))
                std_dict.update({'stdin':process.stdout})

            if cmd_list_last_idx > 0 or getstdout:
                std_dict.update({'stdout': subprocess.PIPE})

            next_process = subprocess.Popen(cmd, **std_dict)
            process = next_process

        if i < cmd_list_last_idx:
            std_dict = {'stdin':process.stdout,
                        'stdout':subprocess.PIPE}
            if not verbose: std_dict.update({'stderr':DEVNULL})

            next_process = subprocess.Popen(cmd, **std_dict)
            # Allow process to receive a SIGPIPE if next_process exits.
            process.stdout.close()
            process = next_process

        else:
            if i != 0:
                std_dict = {}
                if not verbose: std_dict.update({"stderr":DEVNULL,
                                                 "stdout":DEVNULL})
                std_dict.update({'stdin':process.stdout})
                if getstdout:
                    std_dict.update({'stdout': subprocess.PIPE})
                next_process = subprocess.Popen(cmd, **std_dict)
                process = next_process
            
            stdout, _ = process.communicate()
            if getstdout: return stdout
    try:
        DEVNULL.close()
    except:
        pass

# Checks if a given bash commands exists
# check_command_exists('echo')
def check_command_exists(cmd):
    try:
        ext_call([[cmd]]) 
    except OSError as e:
        if e.errno == os.errno.ENOENT:        
            # sometimes command remains cached and checks decides
            # that the command exists even though it doesn't
            ext_call([['hash', '-d', cmd]])
            return False
        else:
            sys.exit('Error while trying to run %s', cmd)
    return True

# checks if a given directory/file exists
def check_path_exists(path):
    return os.path.exists(path)


if __name__ == '__main__':
    sys.exit('Please do not call this script directly. It is called by the other mods when needed...')