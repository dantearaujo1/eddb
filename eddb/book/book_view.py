from readchar import readkey, key
from colorama import Back,Fore

from eddb.book.book_interface.book_controller import BookController
from eddb.book.book_interface.feedback_book_view import FeedbackBookView

class BookView(FeedbackBookView):
    def __init__(self, controller: BookController):
        self.controller = controller
        self.options = ["Procurar","Cadastrar","Editar","Excluir","Sair"]
        self.option = 0

    def show_books(self, books):
        for book in books:
            print(book.name)

    def show_menu(self):
        for i in range(len(self.options)):
            if i == self.option:
                print(f"{Back.WHITE}{self.options[i]}")
            else:
                print(f"{self.options[i]}")


    def get_input(self):
        k = readkey()
        if k in (key.CTRL_N,key.CTRL_J):
            self.option += 1 % len(self.options)
        if k in (key.Return):
            print("Escolher")


    def start(self):
        pass
        #É para aparecer o menu com todas as opcoes do menu livro
