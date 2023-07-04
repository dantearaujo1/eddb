import time

from readchar import readkey, key
from colorama import Back,Fore

from eddb.loan.loan_composer import LoanComposer
from eddb.student.student_composer import StudentComposer
from eddb.book.book_composer import BookComposer
from eddb.endview.end_view import EndView
from eddb.util.util import clear_screen


class MainMenuView():
    def __init__(self):
        self.options = ["Menu Livro","Menu Empréstimos","Menu Usuário","Sair"]
        self.option = 0
        self.end = False

    def show_menu(self):
        for i in range(len(self.options)):
            if i == self.option:
                print(f"{Back.WHITE}{Fore.BLACK}{self.options[i]}")
            else:
                print(f"{self.options[i]}")

    def get_input(self):
        k = readkey()
        if k  == key.ENTER:
            return True
        elif k in (key.CTRL_N,key.CTRL_J,key.DOWN):
            self.option += 1
        elif k in (key.CTRL_P,key.CTRL_K,key.UP):
            self.option -= 1
        self.option %= len(self.options)
        return False

    def create_menu(self):
        if self.option == 0:
            return BookComposer.create()
        if self.option == 1:
            view = LoanComposer.create()
            view.set_parent(self)
            return view
        if self.option == 2:
            return StudentComposer.create()
        if self.option == len(self.options)-1:
            return EndView().start()


    def start(self):
        while self.end is not True:
            clear_screen()
            self.show_menu()
            self.end = self.get_input()
        sub_menu = self.create_menu()
        if sub_menu:
            sub_menu.start()
