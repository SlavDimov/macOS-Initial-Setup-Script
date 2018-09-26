import sys
import os
import re
from glob import glob
import subprocess

GIT_DIR = '/Library/Developer/CommandLineTools/usr/bin/git'
BASH_PROFILE = os.path.join(os.path.expanduser('~'), '.bash_profile')
BREW_PKG_DEFAULT_DIR = '/usr/local/Cellar'
PKG_SYMLINK_DIRS = [
    '/usr/local/bin/',
    '/usr/local/opt/',
]
APP_DIRS = [
    '/Applications/',
    os.path.join(os.path.expanduser('~'), 'Library/Application Support/'),
	os.path.join(os.path.expanduser('~'), 'Library/Preferences/'),
	os.path.join(os.path.expanduser('~'), 'Library/Caches/'),
	os.path.join(os.path.expanduser('~'), 'Library/Saved Application State/'),
]

# Description:
# Adds a path(s) to the PATH variable in .bash_profile.
# This function checks if the path is already
# exported in the file itself or in the system and
# adds it if needed.
# Parameters:
#   values - lists ([], [], ...), with each
#            list containing a set of strings forming a path
#   force - Default - False. If set to true it will
#           delete any already exported path from the PATH variable
#           in .bash_profile that is the same as the one being added
#           and it will append the new one(s) at the bottom.
# Example:
#   append_to_path(['${MYVAR}'],
#                  ['${MYVAR}', 'with', 'extra', 'path'],
#                  ['other', 'path'],
#                  force=True/False)
# Result:
# In .bash_profile:
#   ...
#   export PATH="$PATH:${MYVAR}:${MYVAR}/with/extra/path:other/path"
#   ...
def append_to_path(*values, **kwargs):
    force = kwargs.pop('force', False)
    if len(values) == 0: raise IndexError('At least one value must be provided')
    if not any(isinstance(i, list) for i in values): 
        raise TypeError('One or more elements of the provided list is not a list')
    if any(not i for i in values): 
        raise ValueError('One or more elements of the provided list is an empty list')
    if any(not isinstance(y, str) for x in values for y in x): 
        raise TypeError('One or more of the lists elements is not a string')
    if any(not y for x in values for y in x): 
        raise ValueError('One or more of the lists elements is an empty string')

    file_contents = ''
    values_to_append = []
    
    joint_values = []
    exp_joint_values = []
    for value in values:
        tmp = ''
        tmp_exp = ''
        for val in value:
            # not stripping it, because those chars might actually be needed at some case
            # it is the user's responcibility to type the right value name
            # val = val.strip(' \t\'"')
            tmp = os.path.join(tmp, val)
            if val.strip('${}') in os.environ:
                tmp_exp = os.path.join(tmp_exp, os.environ[val.strip('${}')])
            else:
                tmp_exp = os.path.join(tmp_exp, val)
        joint_values.append(tmp)
        exp_joint_values.append(tmp_exp)

    try:
        with open(BASH_PROFILE, 'r') as f:
            for line in f: file_contents += line
    except:
        # file doesn't exist
        pass

    for i, _ in enumerate(exp_joint_values):
        regex_esc = joint_values[i].replace('$', '\$').replace('{','\{').replace('}', '\}')
        regex = re.search('\s*export\s+PATH=".*%s:?.*' % regex_esc, file_contents)
        if (exp_joint_values[i] in os.environ['PATH'] or regex) and not force:
            continue
        values_to_append.append(joint_values[i])    
    
    if force and file_contents:
        values_to_remove = []
        for value in values_to_append: values_to_remove.append(value.split(os.sep))
        file_contents = remove_from_path(*values_to_remove, file_contents=file_contents)

    if values_to_append:
        file_contents += '\nexport PATH="$PATH'
        for value in values_to_append:
            file_contents += ':%s' % value
        file_contents += '"\n'
    
    with open(BASH_PROFILE, 'w') as f:
        for line in file_contents:
            f.write(line)

# Description:
# Removes a path(s) from the PATH variable in .bash_profile.
# Parameters:
#   values - lists ([], [], ...), with each
#            list containing a set of strings forming a path
#   file_contents - Default None. If None .bash_profile
#                   will be read to get it's contents and then
#                   rewritten with the new contents.
#                   If it is set to a non-empty string that
#                   string will be manipulated and then returned
#                   with the new contents. In that case .bash_profile
#                   won't be changed.
#                   
# Example:
#   remove_from_path([
#                   ['${MYVAR}'],
#                   ['${MYVAR}', 'with', 'extra', 'path'],
#                   ['other', 'path']
#                 ],
#                 file_contents="..."/None)
# Result:
#   ...
#   export PATH="$PATH:${MYVAR}:${MYVAR}/with/extra/path:other/path:Some/other/not/included/path"
#   ...
#   Will be changed to:
#   ...
#   export PATH="$PATH:Some/other/not/included/path"
#   ...
def remove_from_path(*values, **kwargs):
    file_contents = kwargs.pop('file_contents', None)
    if len(values) == 0: raise IndexError('At least one value must be provided')
    if not any(isinstance(i, list) for i in values): 
        raise TypeError('One or more elements of the provided list is not a list')
    if any(not i for i in values): 
        raise ValueError('One or more elements of the provided list is an empty list')
    if any(not isinstance(y, str) for x in values for y in x): 
        raise TypeError('One or more of the lists elements is not a string')
    if any(not y for x in values for y in x): 
        raise ValueError('One or more of the lists elements is an empty string')
    
    from_file = False
    if not file_contents:
        from_file = True
        file_contents = ''
        try:
            with open(BASH_PROFILE, 'r') as f:
                for line in f: file_contents += line
        except:
            # file doesn't exist
            return  '' 
    elif not isinstance(file_contents, str):
        raise TypeError('file_contents is not a string')

    for value in values:
        value = os.path.join(*value)
        regex_esc = value.replace('$', '\$').replace('{','\{').replace('}', '}')
        # remove duplicating values in path
        file_contents = re.sub('(\s*export\s+PATH=".*)(?:%s:)(.*)' % regex_esc, '\\1\\2', file_contents)
        file_contents = re.sub('(\s*export\s+PATH=".*)(?:%s)(".*)' % regex_esc, '\\1\\2', file_contents)

        # remove empty path exports
        file_contents = re.sub('\s*export\s+PATH=":?\$PATH:?"', '', file_contents)
        # remove any trailing colons in path
        file_contents = re.sub('(\s*export\s+PATH=".*)(?::")(.*)', '\\1"\\2', file_contents)
    
    if from_file:
        with open(BASH_PROFILE, 'w') as f:
            for line in file_contents:
                f.write(line)
    else:
        return file_contents

# Description:
# Exports an enviroment variable(s) to .bash_profile
# This function checks if the variable is already
# exported in the file itself or in the system and
# adds it if needed.
# Parameters:
#   variables - a dictionary, containing:
#       key: the variable's name
#       vaue: a list of strings forming a path
#   force - Default - False. If set to true it will
#           delete any already exported variable
#           with the same name from .bash_profile
#           and append the new one at the bottom.
# Example:
#   add_env_var({'MYVAR': ['my', 'path']}, force=True/False)
# Result:
# In .bash_profile:
#   ...
#   export MYVAR="my/path"
#   ...
def add_env_var(variables, force=False):
    if not isinstance(variables, dict): raise TypeError('Provided var is not a dictionary')
    if len(variables) == 0: raise ValueError('Dictionary is empty')
    if not any(isinstance(i, str) for i in variables): 
        raise TypeError('One or more keys of the provided dictionary is not a string')
    if any(not i for i in variables): 
        raise ValueError('One or more keys of the provided dictionary is an empty string')
    if any(not isinstance(variables[i], list) for i in variables): 
        raise TypeError('One or more values of the provided dictionary is not a list')
    if any(not variables[i] for i in variables): 
        raise ValueError('One or more of the values lists is empty')
    if any(not isinstance(y, str) for x in variables for y in variables[x]): 
        raise TypeError('One or more of the value lists elements is not a string')
    if any(not y for x in variables for y in variables[x]): 
        raise ValueError('One or more of the value lists elements is an empty string')
    file_contents = ''
    vars_to_append = dict()

    try:
        with open(BASH_PROFILE, 'r') as f:
            for line in f: file_contents += line
    except:
        # file doesn't exist
        pass
    
    for var in variables:      
        regex = re.search('\s*export\s+%s=[^\n]+\n' % var, file_contents)
        if (var in os.environ or regex) and not force:
            continue
        vars_to_append.update({var:os.path.join(*variables[var])})
    
    if force and file_contents:
        vars_to_remove = []
        for key in vars_to_append: vars_to_remove.append(key)
        file_contents = remove_env_var(*vars_to_remove, file_contents=file_contents)

    for var in vars_to_append:
        # not stripping it from (' \t\'"'), because those chars might actually
        # be needed at some case it is the user's responsibility to type the
        # right value name
        value = vars_to_append[var]
        file_contents += '\nexport %s="%s"\n' % (var, value)
    
    with open(BASH_PROFILE, 'w') as f:
        for line in file_contents:
            f.write(line)

# Description:
# Removes an enviroment variable(s) from .bash_profile
# Parameters:
#   variables - strings, each containing an
#               exported variable name
#   file_contents - Default None. If None .bash_profile
#                   will be read to get it's contents and then
#                   rewritten with the new contents.
#                   If it is set to a non-empty string that
#                   string will be manipulated and then returned
#                   with the new contents. In that case .bash_profile
#                   won't be changed.
#
# Example:
#   remove_env_var('MYVAR', 'MYOTHERVAR',
#                  file_contents="..."/None)
# Result:
#   ...
#   export MYVAR="my/path"
#   export MYVAROTHERVAR="my/other/path"
#   export SOMEVAR="some/path"
#   ...
#   Will be changed to:
#   ...
#   export SOMEVAR="some/path"
#   ...
def remove_env_var(*variables, **kwargs):
    file_contents = kwargs.pop('file_contents', None)
    if len(variables) == 0: raise IndexError('At least one variable must be provided')
    if not any(isinstance(i, str) for i in variables): 
        raise TypeError('One or more elements of the provided list is not a string')
    if any(not i for i in variables): 
        raise ValueError('One or more elements of the provided list is an empty string')

    from_file = False
    if not file_contents:
        from_file = True
        file_contents = ''
        try:
            with open(BASH_PROFILE, 'r') as f:
                for line in f: file_contents += line
        except:
            # file doesn't exist
            return ''  
    elif not isinstance(file_contents, str):
        raise TypeError('file_contents is not a string')
        
    for var in variables:
        file_contents = re.sub('(\s*export\s+%s=)([^\n]+)\n' % var, '', file_contents)
    
    if from_file:
        with open(BASH_PROFILE, 'w') as f:
            for line in file_contents:
                f.write(line)
    else:
        return file_contents

# Description:
# This function can be called to install an app via Homebrew
# Parameters:
#   app - the homebrew name of the app
#   passw - the sudo password that every function needs to receive
#            as argument. It will be passed to ext_call
#   ext_verbose - Default - False. If set to true every it will set
#                 every ext_call's verbose parameter to True.
#   cask - Default - True. This determines if the called ext command
#          should be 'brew cask ...' (for graphical apps) or just
#          'brew ...' (for non graphical apps). Check Homebrew docs
#          for additional information
#
# TODO: Find a way to not crash if brew is not installed.
# (Currently crashes because i don't want to create import loops with dependencies.py)
def install_app(app, passw, ext_verbose=False, cask=True):
    if not check_command_exists('brew'):
        sys.exit('Homebrew is not installed, cannot install app...')
    brew = ['brew']
    if cask: brew.append('cask')
    # if app is not installed
    if not ext_call(brew + ['list', app], getstdout=True):
        # dummy command, so cask won't ask for password again
        ext_call(['echo'], sudopass=passw)
        ext_call(brew + ['install', app], verbose=ext_verbose)

# Description:
# This function can be called to COMPLETELY remove an app and all
# of it's settings.
# It will first check if homebrew is installed, and if it is
# it will call it to uninstall the desired app. It will then go
# through all of the directories defined in the global variable
# 'APP_DIRS', it will search for the application names defined
# by the user, and it will delete every file/folder that matches.
#
# Parameters:
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
#   std_dirs - Default - APP_DIRS. A list of standard directories
#              defined at the top of this file.
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
#   cask - Default - True. This determines if the called ext command
#          should be 'brew cask ...' (for graphical apps) or just
#          'brew ...' (for non graphical apps). Check Homebrew docs
#          for additional information
#
# TODO: The whole delete app process of a non Homebrew cask app needs to be refactored
def remove_app(app_names, passw, std_dirs=APP_DIRS, misc_files_and_dirs=None, nobrew=False,
               brewname=None, debug=False, ext_verbose=False, cask=True):
    if not isinstance(app_names, list):
        raise TypeError('Provided var is not a list')
    
    if not (nobrew or debug):
        if not isinstance(brewname, str):
            raise TypeError('brewname var is not a string')
        if len(brewname) == 0:
            raise ValueError('Provided string is empty')
        if check_command_exists('brew'):
            brew = ['brew']
            if cask: brew.append('cask')
            # dummy command, so cask wont ask for password again
            ext_call(['echo'], sudopass=passw, verbose=ext_verbose)
            ext_call(brew + ['uninstall', brewname], verbose=ext_verbose)
      
    if misc_files_and_dirs:
        if not isinstance(misc_files_and_dirs, list):
            raise TypeError('Provided var is not a list')         
        for item in misc_files_and_dirs:
            if os.path.exists(item):
                if not debug:
                    ext_call(['rm','-rf', item], sudopass=passw, verbose=ext_verbose)   
                else:
                    print(item)
    
    for dir_ in std_dirs:
        for name in app_names:
            res = glob(os.path.join(dir_, name))
            if res:
                for item in res:
                    if not debug:
                        ext_call(['rm','-rf', item], sudopass=passw, verbose=ext_verbose)
                    else:
                        print(item)


# Description:
# It uses subprocess to make calls to bash commands.
# Parameters:
#   cmds - lists ([], [], ...) with all the commands (passed the
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
def ext_call(*cmds, **kwargs):
    getstdout = kwargs.pop('getstdout', False)
    sudopass  = kwargs.pop('sudopass', None)
    verbose   = kwargs.pop('verbose', False)
    if len(cmds) == 0: raise IndexError('At least one command needs to be provided')
    if not any(isinstance(i, list) for i in cmds): 
        raise TypeError('One or more elements of the provided list is not a list')
    if any(not i for i in cmds): 
        raise ValueError('One or more elements of the provided list is an empty list')
    if any(not isinstance(y, str) for x in cmds for y in x): 
        raise TypeError('One or more of the lists elements is not a string')
    if any(not y for x in cmds for y in x): 
        raise ValueError('One or more of the lists elements is an empty string')
    
    process = None
    next_process = None
    cmds_last_idx = len(cmds) - 1

    DEVNULL = None
    try:
        DEVNULL = subprocess.DEVNULL
    except:
        DEVNULL = open(os.devnull, 'w')

    for i, cmd in enumerate(cmds):
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

            if cmds_last_idx > 0 or getstdout:
                std_dict.update({'stdout': subprocess.PIPE})

            next_process = subprocess.Popen(cmd, **std_dict)
            process = next_process

        if i < cmds_last_idx:
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
            if getstdout: 
                if sys.version_info >= (3,0):
                    stdout = stdout.decode('utf-8')
                return stdout
    try:
        DEVNULL.close()
    except:
        pass

# Description:
# Checks if a given bash commands exists
def check_command_exists(cmd):
    try:
        ext_call([cmd]) 
    except OSError as e:
        if e.errno == os.errno.ENOENT:        
            # sometimes command remains cached and checks decides
            # that the command exists even though it doesn't
            ext_call(['hash', '-d', cmd])
            return False
        else:
            sys.exit('Error while trying to run %s', cmd)
    return True

# Description:
# Checks if a given directory/file exists
def check_path_exists(path):
    return os.path.exists(path)

# Description:
# Returns a filepath with a given number
# of parent dirs attached to it.
def get_file_with_parents(filepath, parent_dirs=1):
    common = filepath
    for i in range(parent_dirs + 1):
        common = os.path.dirname(common)
    return os.path.relpath(filepath, common)

# Description:
# Returns all simplinks that can be found in
# the given list of directories, whose targes
# are one of the specified targets
# Parameters:
#   dirs - a list of strings, containing the full
#          path to a dirrectory
#   targets - a list of strings, containing the
#           a possible target path of the symlink 
#   basename - Default True. Whether or not to return
#              the full path of the symlink or just the
#              symlink itself
def get_symlinks(dirs, targets, basename=True):
    res = []
    for dir_ in dirs:
        if dir_[-1] != '*': dir_ += '*'
        for item in glob(dir_):
            if os.path.islink(item):
                for tgt in targets:
                    if tgt in os.readlink(item):
                        if basename:
                            item = os.path.basename(item)
                        res.append(item)
    return res
    
# Description:
# Writes an array value in a plist to a given domain and key, using the defaults command
def defaults_append_to_array(domain, key, value):
    value = '"%s"' % value.strip('"')
    arr_contents = ext_call(['defaults', 'read', domain,
                    key], getstdout=True)
    if not re.search(re.escape(value), arr_contents):
        ext_call(['defaults', 'write', domain,
                    key, '-array-add', value])

# Description:
# Deletes an array value from a plist in given domain and key, using the defaults command
def defaults_delete_from_array(domain, key, value):
    value = '"%s"' % value.strip('"')
    arr_contents = ext_call(['defaults', 'read', domain,
                    key], getstdout=True)
    if re.search('[\(\);]', arr_contents):
        # if it is indeed an array
        arr_contents = re.sub('[\n\(\);]', '', arr_contents)
        arr_contents = re.sub(',\s+', ',', arr_contents)
        arr_contents = arr_contents.strip(', ')
        arr_contents = arr_contents.split(',')
        arr_contents.remove(value)
        cmd_arr = ['defaults', 'write', domain,
                        key, '-array']
        for item in arr_contents: cmd_arr.append(item)
        ext_call(['defaults', 'delete', domain, key])
        ext_call(cmd_arr)

if __name__ == '__main__':
    sys.exit('Please do not call this script directly. It is called by the other mods when needed...')