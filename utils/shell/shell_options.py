from os import walk
from os.path import join
from utils.core.color import colors_terminal


class ShellOptions:
    __instance = None

    @staticmethod
    def get_instance():
        if ShellOptions.__instance is None:
            ShellOptions()
        return ShellOptions.__instance

    def __init__(self):
        if ShellOptions.__instance is None:
            ShellOptions.__instance = self
            modules_list = self._get_list_modules()
            self.options_to_del = ["set", "unset", "show", "back", "run", "global"]
            self.shell_options = {
                "load": modules_list,
                "help": [],
                "banner": [],
                "find": [],
                "import": [],
                "export": [],
                "modules": list(set([module.split("/")[0] for module in modules_list])),
                "tasks": ["kill", "list"],
                "theme": colors_terminal.keys(),
                "exit": None,
                "quit": None
            }

    def get_shell_options(self):
        return self.shell_options

    def add_set_option_values(self, op, value):
        if type(value) != type([]):
            value = [value]
        try:
            self.shell_options["set"][op].append(value)
        except Exception as e:
            print(e)

    def add_module_options(self, options_name=None, new_functions=None):
        if new_functions is None:
            new_functions = []
        if options_name is None:
            options_name = []
        self.shell_options["set"] = self.shell_options["global"] = {}
        self.shell_options["unset"] = options_name
        for name in options_name:
            self.shell_options["set"][name] = self.shell_options["global"][name] = []
        self.shell_options["run"] = []
        self.shell_options["back"] = []
        self.shell_options["show"] = ["options", "info"]
        for f in new_functions:
            if f not in list(self.shell_options.keys()):
                self.shell_options[f] = []
                self.options_to_del.append(f)

    def del_module_options(self):
        self.shell_options["show"] = ["banner"]
        for c in self.options_to_del:
            try:
                del self.shell_options[c]
            except:
                self.options_to_del.remove(c)

    @staticmethod
    def _get_list_modules(pwd="./modules"):
        file_list = []
        for (p, d, files) in walk(pwd):
            file_list.extend([join(p.replace("./modules/", ""), f.replace(".py", "")) for f in files if
                              ("_" not in f) and ("_" not in p)])
        return file_list
