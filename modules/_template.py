import requests
from _module import Module
from utils.core.print import print_info, print_error
from utils.core.dataset import Option


class HomeModule(Module):

    def __init__(self):
        information = {"Name": "Module Name",
                       "Description": "Module Description",
                       "Author": "@Mans00r"}

        options = {"option1": Option.create(name="option_name", value="default value", required="required?")}

        # Constructor of the parent class
        super(HomeModule, self).__init__(information, options)

    # This function must be always implemented, it is called by the run option
    def run(self):
        print("I'm a template")
        # Implement this function to launch module

    # If you need auxiliary functions, you can write the ones you want


HomeModule().run()
