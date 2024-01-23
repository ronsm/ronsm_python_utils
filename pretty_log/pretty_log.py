from colorama import Fore, Style
import inspect
import re
from enum import Enum
import os

STATES = {
    0 : 'ready',
    1 : 'wait',
    -1 : 'error'
}

class PrettyLog(object):
    def __init__(self, config):
        self.config = config
        os.system('cls' if os.name == 'nt' else 'clear')

    def welcome(self):
        package_name_str = ' ' + self.config['package_name']
        package_git_str = ' ' + self.config['package_git']
        author_name_str = ' Author: ' + self.config['author_name']
        if self.config['author_git'].startswith('@'):
            self.config['author_git'] = self.config['author_git'][1:]
        author_git_str = ' GitHub: ' + self.config['author_git'] + ' (https://github.com/' + self.config['author_git']  + ')'
        author_email_str = ' Email:  ' + self.config['author_email']

        print(Fore.YELLOW + '* * * * * * * * * * * * * * * * * * * * * * * * *')
        print()
        print(Style.BRIGHT + package_name_str + Style.RESET_ALL + Fore.YELLOW)
        print(package_git_str)
        print()
        print(author_name_str)
        print(author_email_str)
        print(author_git_str)
        print()
        print('* * * * * * * * * * * * * * * * * * * * * * * * *')

        self.log_state(0)

    def get_caller_id(self):
        stack = inspect.stack()
        caller_class = stack[2][0].f_locals['self'].__class__.__name__
        caller_method = stack[2][0].f_code.co_name

        class_id = re.sub(r'(?<!^)(?=[A-Z])', '_', caller_class).lower()
        method_id = re.sub(r'(?<!^)(?=[A-Z])', '_', caller_method).lower()

        caller_tag = '[' + class_id + ']' + '[' + method_id + ']'

        return caller_tag
    
    def log_state(self, state):
        caller_tag = self.get_caller_id()
        try:
            state_str = STATES[state]
            print(Fore.CYAN + caller_tag + Fore.MAGENTA + '[s]' + Fore.RESET + ' state switched to: ' + Fore.MAGENTA + state_str, Fore.RESET)
        except KeyError:
            self.log_bad('Invalid state provided.')
    
    def log_normal(self, msg):
        caller_tag = self.get_caller_id()
        print(Fore.CYAN + caller_tag + Fore.MAGENTA + '[m]', Fore.RESET + msg)

    def log_math(self, msg):
        caller_tag = self.get_caller_id()
        print(Fore.CYAN + caller_tag + Fore.MAGENTA + '[m]', Fore.YELLOW + msg, Fore.RESET)
    
    def log_bad(self, msg):
        caller_tag = self.get_caller_id()
        print(Fore.CYAN + caller_tag + Fore.MAGENTA + '[m]', Fore.LIGHTRED_EX + msg, Fore.RESET)

    def log_good(self, msg):
        caller_tag = self.get_caller_id()
        print(Fore.CYAN + caller_tag + Fore.MAGENTA + '[m]', Fore.GREEN + msg, Fore.RESET)

    def log_mini_header(self, msg):
        caller_tag = self.get_caller_id()
        print('- break -')
        print(Fore.CYAN + caller_tag + Fore.MAGENTA + '[h]', Fore.YELLOW + '* ' + msg + ' *' + Style.RESET_ALL, Fore.RESET)
