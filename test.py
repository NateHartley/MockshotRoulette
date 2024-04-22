from rich.console import Console
from rich.markdown import Markdown
import sys
import main
import shotgun
#import waiver

console = Console()


def coloured_text(): # Works!
    print(u"\u001b[41;1m A \u001b[43;1m B \u001b[42;1m C \u001b[46;1m D \u001b[44;1m E \u001b[45;1m F \u001b[0m\n")
    
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
        print (u"\u001b[0m")

    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
        print (u"\u001b[0m")


def print_markdown_text(): # Works!
    with open("waiver.md", "r+") as waiver_txt:
        console.print(Markdown(waiver_txt.read()))


def testing(gun: shotgun.Shotgun):
    print(">>>>>>>>>>gin ", gun.rounds)
    pass