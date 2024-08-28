from os import system, name, getcwd, chdir
from os.path import dirname, abspath
from utils.shell.banner import banner
from utils.shell.prompt import prompt
from utils.shell.shell_options import ShellOptions
from utils.shell.command_parser import CommandParser
from utils.core.color import ColorSelected, colors_terminal


class Shell:

    def __init__(self):
        home = dirname(abspath(__file__))
        if home != getcwd():
            chdir(home)
        self.command_parser = CommandParser()
        self.shell_options = ShellOptions.get_instance()
        self.color_selected = ColorSelected(colors_terminal["dark"])

    def console(self):
        banner()
        while True:
            try:
                module_name = self.command_parser.get_module_name()
                options = self.shell_options.get_shell_options()
                user_input = prompt(options, module_name).strip(" ")
                self.command_parser.parser(user_input)
            except KeyboardInterrupt:
                print("CTRL^C")


if __name__ == "__main__":
    system('cls' if name == 'nt' else 'clear')
    Shell().console()
