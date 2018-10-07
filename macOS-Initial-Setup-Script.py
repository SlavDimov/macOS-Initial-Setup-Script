#!/usr/bin/env python
# coding: utf-8

import os
import sys
import re
import sqlite3
import time
import argparse
from getpass import getpass

from util import util

import dependencies
import apps
import tweaks
import tools

for i in [dependencies, apps, tweaks, tools]:
    globals().update({k: vars(i)[k]
                      for k in vars(i) if not re.match('^__.+__$', k)})


class Run:
    def __init__(self):
        config_file = 'default-config.preset'
        self.preset_ext = '.preset'

        parser = argparse.ArgumentParser(
            description=(
                'This script aims to automate '
                'the process of setting up common features '
                'and software on your Mac as much as possible.'),
            epilog=(
                'If the script is called without any arguments, '
                'the default preset file (%s) will be used.'
                % config_file))
        parser.add_argument('-p', '--preset',
                            nargs='?', const=config_file,
                            default=None, type=str,
                            metavar='myPreset.preset',
                            help="Preset to be used.")
        parser.add_argument('-f', '--functions',
                            nargs='*',
                            default=None, type=str,
                            metavar='<function>',
                            help="Functions to be executed")
        args = parser.parse_args()

        if args.preset == None and args.functions == None:
            args.preset = config_file

        func_list = []
        if args.preset != None:
            func_list = self.read_config_file(args.preset)
        if args.functions != None:
            func_list += args.functions

        self.ask_accessibility_permition()
        self.run_func_list(func_list)

    def search_for_config(self, config):
        if os.path.exists(config):
            return config
        elif os.path.exists(config + self.preset_ext):
            return config + self.preset_ext
        else:
            sys.exit('Configuration file not found...')

    def read_config_file(self, filename):
        filename = self.search_for_config(filename)
        func_list = []
        with open(filename) as f:
            for line in f:
                line = line.partition('#')[0]
                line = line.strip()
                if not re.match(r'^\s*$', line):
                    func_list.append(line)
        return func_list

    def run_func_list(self, func_list):
        passw = getpass()
        for func in func_list:
            try:
                globals()[func](passw)
            except KeyError:
                print('Function \'%s\' not found. Skipping...' % func)

    def ask_accessibility_permition(self):
        print("Checking for required permissions...")

        check_permission_script_editor = (
            'select exists(Select allowed from access where '
            'service="kTCCServiceAccessibility" and '
            'client="com.apple.ScriptEditor2" and allowed=1);')
        check_permission_terminal = (
            'select exists(Select allowed from access where '
            'service="kTCCServiceAccessibility" and '
            'client="com.apple.Terminal" and allowed=1);')

        msg_title = (
            'Please add \'Terminal\' and \'Script Editor\' '
            'to the Accessibility Assist allowed apps')
        msg = (
            'In order for this script to work properly, '
            'please add \'Terminal\' and \'Script Editor\' '
            'apps to the Accessibility Assist allowed apps '
            'by checking their respected checkboxes or, if '
            'they are not there, click the \'+\' button and '
            'navigate to Applications->Utilities->Terminal & Script Editor')

        try:
            conn = conn = sqlite3.connect(
                '/Library/Application Support/com.apple.TCC/TCC.db')
            with conn:
                c = conn.cursor()

                script_allowed = c.execute(
                    check_permission_script_editor).fetchone()[0]
                terminal_allowed = c.execute(
                    check_permission_terminal).fetchone()[0]

                if not (script_allowed and terminal_allowed):
                    print("\n%s\n\n%s\n\n..." % (msg_title, msg))
                    util.ext_call(['osascript', 'dependencies.scpt',
                                   'AskForAccessibilityPermitions', msg_title, msg])

                    while not (script_allowed and terminal_allowed):
                        script_allowed = c.execute(
                            check_permission_script_editor).fetchone()[0]
                        terminal_allowed = c.execute(
                            check_permission_terminal).fetchone()[0]
                        time.sleep(1)
        except:
            sys.exit('Could not establish or acquire Accessibility Permissions...')


if __name__ == '__main__':
    Run()
