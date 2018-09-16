import os
import sys
import re
import sqlite3
import time
from getpass import getpass

from util import util

import dependencies
globals().update({k:vars(dependencies)[k] for k in vars(dependencies) if not re.match('^__.+__$', k)})
import apps
globals().update({k:vars(apps)[k] for k in vars(apps) if not re.match('^__.+__$', k)})
import tweaks
globals().update({k:vars(tweaks)[k] for k in vars(tweaks) if not re.match('^__.+__$', k)})
import tools
globals().update({k:vars(tools)[k] for k in vars(tools) if not re.match('^__.+__$', k)})


class Run:
    __config_file   = 'default-config.preset'
    __preset_ext    = '.preset'
    __preset_opt    = 'preset='

    def __init__(self):
        self.__ask_accessibility_permition()

        func_list = []

        if len(sys.argv) == 1:
            func_list = self.__read_config_file(self.__search_for_config())
        else:
            if sys.argv[1].startswith(self.__preset_opt):
                self.__config_file = sys.argv[1][len(self.__preset_opt):]
                func_list = self.__read_config_file(self.__search_for_config())
            else:
                func_list = sys.argv[1:]    

        self.__run_func_list(func_list)

    def __search_for_config(self):
        if os.path.exists(self.__config_file):
            return self.__config_file
        elif os.path.exists(self.__config_file + self.__preset_ext):
            return self.__config_file + self.__preset_ext
        else:
            sys.exit('Configuration file not found...')
                
    def __read_config_file(self, filename):
        func_list = []
        with open(filename) as f:
            for line in f:
                line = line.partition('#')[0]
                line = line.strip()
                if not re.match('^\s*$', line): func_list.append(line)
        return func_list
    
    def __run_func_list(self, func_list):
        passw = getpass()
        for func in func_list:
            try:
                globals()[func](passw)
            except KeyError:
                sys.exit('Function \'%s\' not found...' % func)

    def __ask_accessibility_permition(self):
        print ("Checking for required permissions...")

        check_permission_script_editor = 'select exists(Select allowed from access where service="kTCCServiceAccessibility" and client="com.apple.ScriptEditor2" and allowed=1);'
        check_permission_terminal      = 'select exists(Select allowed from access where service="kTCCServiceAccessibility" and client="com.apple.Terminal" and allowed=1);'   

        msg_title = "Please add 'Terminal' and 'Script Editor' to the Accessibility Assist allowed apps"
        msg = "In order for this script to work properly, please add 'Terminal' and 'Script Editor' apps to the Accessibility Assist allowed apps by checking their respected checkboxes or, if they are not there, click the '+' button and navigate to Applications->Utilities->Terminal & Script Editor"

        try:
            conn = conn = sqlite3.connect('/Library/Application Support/com.apple.TCC/TCC.db')
            with conn:
                c = conn.cursor()

                script_allowed = c.execute(check_permission_script_editor).fetchone()[0]
                terminal_allowed = c.execute(check_permission_terminal).fetchone()[0]
                if not (script_allowed and terminal_allowed):
                    print("\n%s\n\n%s\n\n..." % (msg_title, msg))
                    util.ext_call([['osascript', 'general.scpt', 'AskForAccessibilityPermitions', msg_title, msg]])
                    while not (script_allowed and terminal_allowed):
                        script_allowed = c.execute(check_permission_script_editor).fetchone()[0]
                        terminal_allowed = c.execute(check_permission_terminal).fetchone()[0]
                        time.sleep(1)
        except:
            sys.exit('Could not establish or aquire Accessibility Permissions...')




if __name__ == '__main__':
   Run()

    
    