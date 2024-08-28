from random import choice
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.formatted_text import FormattedText
from utils.core.color import ColorSelected
from time import sleep


info = '''
    ☠  Ragdoll -  a Hacking Tool  Template ☠                 

       Created with ♥  by: 'Mans00r'        

            Version: '0.0.1a'                         
'''

# Thanks to http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
# Thanks to https://tool.catzone.net/ascii_art
banner1 = """

                             _           _   _ 
  _ __    __ _    __ _    __| |   ___   | | | |
 | '__|  / _` |  / _` |  / _` |  / _ \  | | | |
 | |    | (_| | | (_| | | (_| | | (_) | | | | |
 |_|     \__,_|  \__, |  \__,_|  \___/  |_| |_|
                 |___/                         

"""


banner2 = """

 ██▀███   ▄▄▄        ▄████ ▓█████▄  ▒█████   ██▓     ██▓    
▓██ ▒ ██▒▒████▄     ██▒ ▀█▒▒██▀ ██▌▒██▒  ██▒▓██▒    ▓██▒    
▓██ ░▄█ ▒▒██  ▀█▄  ▒██░▄▄▄░░██   █▌▒██░  ██▒▒██░    ▒██░    
▒██▀▀█▄  ░██▄▄▄▄██ ░▓█  ██▓░▓█▄   ▌▒██   ██░▒██░    ▒██░    
░██▓ ▒██▒ ▓█   ▓██▒░▒▓███▀▒░▒████▓ ░ ████▓▒░░██████▒░██████▒
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ░▒   ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░▓  ░░ ▒░▓  ░
  ░▒ ░ ▒░  ▒   ▒▒ ░  ░   ░  ░ ▒  ▒   ░ ▒ ▒░ ░ ░ ▒  ░░ ░ ▒  ░
  ░░   ░   ░   ▒   ░ ░   ░  ░ ░  ░ ░ ░ ░ ▒    ░ ░     ░ ░   
   ░           ░  ░      ░    ░        ░ ░      ░  ░    ░  ░
                            ░                      

"""


def little_animation():
    msg = "ragdoll >>"
    index = 0
    while True:
        print(msg[index], end="", flush=True)
        index += 1
        if index == len(msg):
            break
        sleep(0.1)

    print("\033[A")


def banner(animation=True):
    banners = [banner1, banner2]
    color = ColorSelected()
    text = FormattedText([
        (color.theme.banner, choice(banners)),
        (color.theme.primary, info)
    ])
    print_formatted_text(text)
    if animation:
        little_animation()
