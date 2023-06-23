from view.iview import IView
import inspect
from colorama import init,Back, Fore, Style
from util.util import *

init(autoreset=True)

class Console(IView):
    def __init__(self,initial_option):
        self.current_options = initial_option

    def show(self):
        resposta = 0
        while self.current_options != -1:
            clear_screen();
            self.printMenu("Sistema de Biblioteca",self.current_options)
            resposta = int(input("Qual opção vc deseja?\n"))
            self.handleOptions(resposta)

    def printMenu(self,title,options):
        # print(Style.BRIGHT + Back.BLUE + Fore.WHITE + "=" * (len(title)+6))
        # print(Style.BRIGHT + Back.BLUE + Fore.WHITE + "|| {} ||".format(title))
        # print(Style.BRIGHT + Back.BLUE + Fore.WHITE + "=" * (len(title)+6))
        print("=" * (len(title)+6))
        print("|| {} ||".format(title))
        print("=" * (len(title)+6))
        self.printOptions(options)

    def printOptions(self,op):
        for i in range(len(op)):
            print("{}. {}".format(i+1,op[i]["entry"]))
            # print(Back.YELLOW + Fore.BLACK + "{}. {}".format(i+1,op[i]["entry"]))

    def handleOptions(self,resp):
        self.current_options = self.current_options[resp-1]["out_opt"]
        if inspect.isfunction(self.current_options):
            self.current_options = self.current_options()
