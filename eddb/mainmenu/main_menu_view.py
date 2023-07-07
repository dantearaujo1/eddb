import time

from readchar import readkey, key
from colorama import Back,Fore

from eddb.loan.loan_composer import LoanComposer
from eddb.student.student_composer import StudentComposer
from eddb.book.book_composer import BookComposer
from eddb.endview.end_view import EndView
from eddb.util.util import clear_screen
from eddb.util.menus import draw_scrollable_menu


class MainMenuView():
    def __init__(self):
        self.options = ["Menu Livro","Menu Empréstimos","Menu Estudantes","Sair"]
        self.option = 0
        self.end = False
        self.menu = [self.show_menu]
        self.input_method = self.get_input

    def show_menu(self):
        draw_scrollable_menu(self.options,self.option,0,True)


    def get_input(self):
        k = readkey()
        if k  == key.ENTER:
            self.create_menu()
            pass
            # return True
        elif k in (key.CTRL_N,key.CTRL_J,key.DOWN):
            self.option += 1
        elif k in (key.CTRL_P,key.CTRL_K,key.UP):
            self.option -= 1
        self.option %= len(self.options)
        return False

    def create_menu(self):
        if self.option == 0:
            return BookComposer.create().start()
        if self.option == 1:
            return LoanComposer.create().start()
        if self.option == 2:
            return StudentComposer.create().start()
        return EndView().start()


    def start(self):
        while self.end is not True:
            clear_screen()
            self.menu[-1]()
            self.end = self.input_method()
