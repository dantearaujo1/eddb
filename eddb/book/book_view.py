import time,sys
from collections.abc import Iterable

from readchar import readchar,readkey, key
from colorama import Back,Fore

from eddb.book.book_interface.book_controller import BookController
from eddb.book.book_model import Book
from eddb.util.util import clear_screen,move_cursor,get_terminal_size
from eddb.book.book_interface.feedback_book_view import FeedbackBookView

class BookView(FeedbackBookView):
    def __init__(self, controller: BookController):
        self.controller = controller
        self.options = ["Procurar","Cadastrar","Editar","Excluir","Sair"]
        self.option = 0
        self.end = False
        self.menu = None

    def show_books(self, books):
        for book in books:
            print(book.title)

    def show_book(self,book):
        clear_screen()
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        time.sleep(3)
        self.end = False
        self.start()

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
        if k in (key.CTRL_N,key.CTRL_J,key.DOWN):
            self.option += 1
        elif k in (key.CTRL_P,key.CTRL_K,key.UP):
            self.option -= 1
        self.option %= len(self.options)
        return False

    def get_books(self):
        """
        Retorna todos os livros do banco e permite filtrar por nomes
        """
        # TODO: Melhorar pois estamos armazenando todos os livros em all_books
        # mas estamos filtrando puxando do "banco de dados" os livros novamente
        end = False
        anwser = ''
        all_books = self.controller.get_all()
        books = all_books
        option = 0
        search = False
        question = "Digite o nome de um livro: "
        while end is not True:
            clear_screen()
            move_cursor(0,get_terminal_size()[1]-2-len(books))
            print("=====================================")
            for idx,book in enumerate(books):
                move_cursor(0,get_terminal_size()[1]-2-idx)
                if option == idx:
                    print(f"{Back.WHITE}{Fore.BLACK}{book.title}")
                else:
                    print(f"{book.title}")
            move_cursor(0,get_terminal_size()[1]-1)
            print("=====================================")
            move_cursor(0,get_terminal_size()[1]-1)
            print(question + anwser,end='')
            search = False
            k = readkey()
            if k  == key.ENTER:
                end = True
                continue
            if k in (key.CTRL_N,key.CTRL_J,key.DOWN):
                option -= 1
            elif k in (key.CTRL_P,key.CTRL_K,key.UP):
                option += 1
            elif k in (key.BACKSPACE):
                anwser = anwser[0:-1]
                search = True
            else:
                anwser += k
                search = True
            if search:
                if len(anwser) > 0:
                    books = self.controller.search_by_name(anwser,5)
                else:
                    books = all
            option %= len(books)
            end = False
        self.show_book(books[option])

    def create_submenu(self):
        if self.option == 0:
            return self.get_books
        elif self.option == 1:
            return self.add_book
        elif self.option == 2:
            return self.edit_book
        elif self.option == 3:
            return self.delete_book
        else:
            return

    def delete_book(self):
        end = False
        anwser = ''
        books = []
        option = 0
        search = False
        question = "Busca Rápida: "
        while end is not True:
            clear_screen()
            for i in range(len(books)-1,0,-1):
                book = books[i]
                if option == i:
                    print(f"{Back.WHITE}{Fore.BLACK}{book.title}")
                else:
                    print(f"{book.title}")
            move_cursor(0,get_terminal_size()[1]-1)
            print(question + anwser,end='')
            search = False
            k = readkey()
            if k  == key.ENTER:
                end = True
                continue
            if k in (key.CTRL_N,key.CTRL_J,key.DOWN):
                option += 1
            elif k in (key.CTRL_P,key.CTRL_K,key.UP):
                option -= 1
            elif k in (key.BACKSPACE):
                anwser = anwser[0:-1]
                search = True
            else:
                anwser += k
                search = True
            if search:
                books = self.controller.search_by_name(anwser,100)
            option %= len(books)
            end = False
        result = self.controller.delete_book(books[option])
        clear_screen()
        if result[0] is True:
            SuccessFeedbackBookView("Livro Deletado:").show_books(result[1])
            time.sleep(3)
            self.end = False
            self.start()
        else:
            FailureFeedbackBookView("Erro ao deletar o livro!").show_books(result[1])
            time.sleep(3)
            self.end = False
            self.start()

    def add_book(self):
        end = False
        text_input = ''
        anwser = []
        questions = ["título","autor"]
        option = 0
        question = f"Digite o {questions[option]} de um livro: "
        while end is not True:
            question = f"Digite o {questions[option]} de um livro: "
            clear_screen()
            move_cursor(0,get_terminal_size()[1]-1)
            print(question + text_input,end='')
            k = readkey()
            if k  == key.ENTER:
                option += 1
                anwser.append(text_input)
                text_input = ''
                if option >= len(questions):
                    end = True
                    continue
            elif k in (key.BACKSPACE):
                text_input = text_input[0:-1]
            else:
                text_input += k
            option %= len(questions)
            end = False
        result = self.controller.add_book(anwser[0],anwser[1])
        clear_screen()
        if result[0] is True:
            SuccessFeedbackBookView("Parabéns você adicionou um livro!").show_books(result[1])
            time.sleep(3)
            self.end = False
            self.start()
        else:
            FailureFeedbackBookView("Não foi possível adicionar este livro").show_books(result[1])
            time.sleep(3)
            self.end = False
            self.start()

    def edit_book(self):
        end = False
        anwser = ''
        books = []
        questions = ["título","autor"]
        option = 0
        search = False
        question = "Busca Rápida: "
        while end is not True:
            clear_screen()
            for i in range(len(books)-1,0,-1):
                book = books[i]
                if option == i:
                    print(f"{Back.WHITE}{Fore.BLACK}{book.title}")
                else:
                    print(f"{book.title}")
            move_cursor(0,get_terminal_size()[1]-1)
            print(question + anwser,end='')
            search = False
            k = readkey()
            if k  == key.ENTER:
                end = True
                continue
            if k in (key.CTRL_N,key.CTRL_J,key.DOWN):
                option += 1
            elif k in (key.CTRL_P,key.CTRL_K,key.UP):
                option -= 1
            elif k in (key.BACKSPACE):
                anwser = anwser[0:-1]
                search = True
            else:
                anwser += k
                search = True
            if search:
                books = self.controller.search_by_name(anwser,100)
            option %= len(books)
            end = False
        to_edit = books[option]
        questions_anwsers = [ to_edit.title, to_edit.author ]
        question_option = 0
        while question_option < len(questions):
            clear_screen()
            move_cursor(0,get_terminal_size()[1]-1)
            print("Novo " + questions[question_option] + ": " + questions_anwsers[question_option],end='')
            k = readkey()
            if k  == key.ENTER:
                question_option += 1
                continue
            if k in (key.BACKSPACE):
                questions_anwsers[question_option] = questions_anwsers[question_option][0:-1]
            else:
                questions_anwsers[question_option] = questions_anwsers[question_option] + k
        result = self.controller.edit_book(to_edit.id,questions_anwsers[0],questions_anwsers[1])
        result[1].append(to_edit)
        clear_screen()
        if result[0] is True:
            SuccessFeedbackBookView(f"Parabéns você editou o livro:").show_books(result[1])
            time.sleep(3)
            self.end = False
            self.start()
        else:
            FailureFeedbackBookView("Não foi possível editar este livro").show_books(result[1])
            time.sleep(3)
            self.end = False
            self.start()



    def start(self):
        while self.end != True:
            clear_screen()
            self.show_menu()
            self.end = self.get_input()
        sub_menu = self.create_submenu()
        if sub_menu:
            sub_menu()

class SuccessFeedbackBookView(FeedbackBookView):

    def __init__(self,msg : str):
        self.message = msg

    def show_books(self,books: Iterable[ Book ]):
        print(f"{Back.GREEN}{Fore.BLACK}{self.message }")
        if len(books) > 1:
            print("Antes:")
            print(f" ID: {books[1].id}")
            print(f" Título: {books[1].title}")
            print(f" Autor: {books[1].author}")
            print("Depois:")
            print(f" ID: {books[0].id}")
            print(f" Título: {books[0].title}")
            print(f" Autor: {books[0].author}")
        else:
            print(f"ID: {books[0].id}")
            print(f"Título: {books[0].title}")
            print(f"Autor: {books[0].author}")
        time.sleep(3)

class FailureFeedbackBookView(FeedbackBookView):

    def __init__(self,msg : str):
        self.message = msg
    def show_books(self,books: Iterable[ Book ]):
        print(f"{Back.RED}{Fore.WHITE}{self.message}")
        time.sleep(3)

