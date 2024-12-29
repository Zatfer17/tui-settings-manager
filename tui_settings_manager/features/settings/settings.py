import subprocess
import json
from distutils.spawn import find_executable


def run(command):
    return subprocess.run(command.split(' '), capture_output=True, text=True).stdout

class Settings():

    TERM_LIST = ["x-terminal-emulator", "konsole", "gnome-terminal", "urxvt", "rxvt", "termit", "terminator", "Eterm", "aterm", "uxterm", "xterm", "roxterm", "xfce4-terminal", "termite", "lxterminal", "mate-terminal", "terminology", "st", "qterminal", "lilyterm", "tilix", "terminix", "kitty", "guake", "tilda", "alacritty", "hyper"]
    #list taken from https://github.com/i3/i3/blob/next/i3-sensible-terminal

    @staticmethod
    def get_options():
        parsed_json = json.loads(run('pipx list --json'))
        return [x for x in parsed_json['venvs'] if ('tui-' in x)&(x != 'tui-settings-manager')]

    @staticmethod
    def is_not_executable(name):
        return find_executable(name) is None

    def get_terminal(self):        
        i = 0
        for term in self.TERM_LIST:
            if self.is_not_executable(term):
                i += 1
            else:
                break
        return self.TERM_LIST[i]

    def run_option(self, option):
        terminal = self.get_terminal()
        print(f'TERMINAL {terminal}')
        print(f'OPTION {option}')
        return run(f'{terminal} -e bash -c "{option}"')