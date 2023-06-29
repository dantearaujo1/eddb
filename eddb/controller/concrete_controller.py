import inspect
import time
from util.util import clear_screen,move_cursor,get_terminal_size
from readchar import readkey, key
from colorama import Back,Fore,Style,init,Cursor
from controller.icontroller import IController
from model.livro import Livro

init(autoreset=True)

class ConcreteController():
    def __init__(self,view,repository):
        self.view = view
        self.repository = repository

    def show_menu(self):
        sair = False
        while sair != True:
            self.view.mostrar()
            sair = self.view.pegar_input()

    def add_livro(self):
        self.view.get_livro_add_input()

