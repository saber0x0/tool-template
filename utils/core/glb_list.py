from prompt_toolkit import print_formatted_text, HTML
import sys
from json import dump, load
from .color import ColorSelected


class Global:
    __instance = None

    @staticmethod
    def get_instance():
        if Global.__instance is None:
            Global()
        return Global.__instance

    def __init__(self):
        if Global.__instance is None:
            Global.__instance = self
            self.variables = {}
            self.file_path = "utils/files/global.json"

    def add_value(self, key, value):
        self.variables[key] = value

    def get_variables(self):
        return self.variables

    def save_configuration(self):
        with open(self.file_path, 'w') as f:
            dump(self.variables, f)

    def load_configuration(self):
        with open(self.file_path, 'r') as f:
            self.variables = load(f)

    def show_variables(self):
        print_formatted_text(HTML(f'''
        <{ColorSelected().theme.accent}> Options (Field = Value)</{ColorSelected().theme.accent}>
        -------------------------'''))
        flag = 0
        for key, value in self.variables.items():
            flag += 1
            if flag > 1:
                print(" |")
            print(f" |_ {key} = {value}")
        print("")
