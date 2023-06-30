from readchar import readkey, key
from colorama import Back,Fore

from eddb.book.book_interface.book_controller import BookController
from eddb.book.book_interface.feedback_book_view import FeedbackBookView,SuccessFeedbackAddBookView, FailureFeedbackAddBookView
from eddb.util.util import clear_screen,move_cursor,get_terminal_size

from eddb.loan.loan_composer import LoanComposer
from eddb.student.student_composer import StudentComposer

class BookView(FeedbackBookView):
    def __init__(self, controller: BookController):
        self.controller = controller
        self.options = ["Procurar","Cadastrar","Editar","Excluir","Sair"]
        self.option = 0
        self.end = False

    def show_books(self, books):
        for book in books:
            print(book.title)

    def show_book(self,book):
        clear_screen()
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        input()

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

    def get_books(self):
        end = False
        anwser = ''
        books = []
        option = 0
        search = False
        question = "Digite o nome de um livro: "
        while end is not True:
            clear_screen()
            for i in range(len(books)):
                book = books[i]
                if option == i:
                    print(f"{Back.WHITE}{Fore.BLACK}{book.title}")
                else:
                    print(f"{book.title}")
                # print(f"{book[0].nome}")
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
                books = self.controller.search_by_name(anwser)
            option %= len(books)
            end = False
        self.show_book(books[option])

    def create_submenu(self):
        if self.option == 0:
            return self.get_books
        elif self.option == 1:
            return self.add_book
        elif self.option == 2:
            return None

    def add_book(self):
        end = False
        text_input = ''
        anwser = []
        questions = ["title","author"]
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
            SuccessFeedbackAddBookView().show_books(result[1])
        else:
            FailureFeedbackAddBookView().show_books(result[1])


    def start(self):
        while self.end != True:
            clear_screen()
            self.show_menu()
            self.end = self.get_input()
        sub_menu = self.create_submenu()
        print(sub_menu)
        if sub_menu:
            sub_menu()
        #É para aparecer o menu com todas as opcoes do menu livro
