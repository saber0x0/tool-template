import importlib
from .print import print_error, print_info, print_ok
from .exception import exception


# @exception("Error importing the module")
def load_module(path):
    print_info('Loading module...')
    my_path = path.replace("/", ".")
    my_path = "modules." + my_path
    module = importlib.import_module(my_path)
    print_ok('Module loaded!')
    return module.HomeModule()
