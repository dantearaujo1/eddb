import time,re
from collections.abc import Iterable

from readchar import readchar,readkey, key
from colorama import Back,Fore

from eddb.book.book_interface.book_controller import BookController
from eddb.book.book_model import Book
from eddb.book.book_interface.feedback_book_view import FeedbackBookView
from eddb.endview.end_composer import EndComposer
from eddb.util.util import clear_screen,move_cursor,get_terminal_size
from eddb.util.menus import draw_scrollable_menu

class BookView(FeedbackBookView):
    def __init__(self, controller: BookController):
        self.controller = controller
        self.options = ["Procurar","Cadastrar","Editar","Excluir","Voltar","Sair"]
        self.option = 0
        self.end = False
        self.menu = [self.show]
        self.input_method = self.get_input
        self.books = self.controller.get_all()

        self.window = get_terminal_size()[1] - 3
        self.init_option = 0
        self.end_option = self.window
        self.fake_selection = 0

    def show_books(self, books):
        for book in books:
            print(book.title)

    def show_book(self,book):
        clear_screen()
        move_cursor(0,get_terminal_size()[1]-3)
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print("Aperte qualquer tecla para voltar ao menu livro",end="")
        readkey()

    def show(self):
        draw_scrollable_menu(self.options,self.fake_selection,self.init_option,reverse=True)

    def get_input(self):
        total = len(self.options)
        k = readkey()
        if k  == key.ENTER:
            return self.create_submenu()
        if k  == key.SPACE:
            clear_screen()
            print(f"Window Size:{ self.window }")
            print(f"Fake Option:{ self.fake_selection }")
            print(f"Option:{ self.option }")
            print(f"Ini Option:{ self.init_option }")
            print(f"End Option:{ self.end_option }")
            time.sleep(3)
        if k in (key.CTRL_N,key.CTRL_J,key.DOWN):
            if self.option < total-1:
                self.option += 1
            if self.fake_selection < min(self.end_option - self.init_option - 1,total-1):
                self.fake_selection += 1
            else:
                if self.end_option < len(self.options):
                    self.init_option += 1
                    self.end_option += 1

        elif k in (key.CTRL_P,key.CTRL_K,key.UP):
            if self.option > 0:
                self.option -= 1
            if self.fake_selection > 0:
                self.fake_selection -= 1
            else:
                if self.init_option > 0:
                    self.init_option -= 1
                    self.end_option -= 1
        return False

    def get_books(self):
        """
        Retorna todos os livros do banco e permite filtrar por nomes
        """
        end = False
        anwser = ''
        books = self.controller.get_all()
        search = False
        question = "Digite o nome ou o autor de um livro: "

        # Window variables ==================
        selected = 0
        terminal_size = get_terminal_size()
        window = terminal_size[1] - 3
        fake_selection = 0
        ini_item = 0
        end_item = window
        # ===================================
        pos_na_string = 0
        while end is not True:
            showed_items = list(map(lambda x: x.title,books))
            total= len(showed_items)
            terminal_size = get_terminal_size()
            window = terminal_size[1] - 3

            draw_scrollable_menu(showed_items,fake_selection,ini_item)
            print(question + anwser,end='')
            move_cursor( len(question) + pos_na_string + 1,get_terminal_size()[1])
            search = False
            k = readkey()
            window = terminal_size[1] - 3
            if k  == key.ENTER:
                if total >0:
                    end = True
                    continue
            if k == key.LEFT:
                pos_na_string -= 1
                pos_na_string = max(pos_na_string,0)
            elif k == key.RIGHT:
                pos_na_string += 1
                pos_na_string = min(pos_na_string,len(anwser))
            elif k in (key.CTRL_N,key.CTRL_J,key.DOWN):
                selected -= 1
                selected = max(selected,0)
                if fake_selection > 0:
                    fake_selection -=1
                else:
                    if end_item > window:
                        ini_item -= 1
                        end_item -= 1
            elif k in (key.CTRL_P,key.CTRL_K,key.UP):
                selected += 1
                selected = min(total-1,selected)
                if fake_selection < min(window - 1,total-1):
                    fake_selection +=1
                else:
                    if ini_item < total - window:
                        ini_item += 1
                        end_item += 1
            elif k in (key.BACKSPACE):
                if pos_na_string != 0:
                    anwser = anwser[0:pos_na_string-1] + anwser[pos_na_string:]
                pos_na_string = max(pos_na_string,1)
                search = True
                end_item = window
                ini_item = 0
                fake_selection = 0
                pos_na_string -= 1
            else:
                if len(anwser) == 0:
                    anwser += k
                elif pos_na_string == 0:
                    anwser = k + anwser
                else:
                    anwser = anwser[:pos_na_string]+ k + anwser[pos_na_string:]
                pos_na_string += 1
                search = True
                ini_item = 0
                end_item = window
                fake_selection = 0
            if search:
                if len(anwser) > 0:
                    books = self.controller.search_by_name(anwser,10)
                else:
                    books = self.books
            end = False
        self.show_book(books[selected])
        self.input_method = self.__back

    def create_submenu(self):
        if self.option == 0:
            self.menu.append(self.get_books)
            self.option = 0
        if self.option == 1:
            self.menu.append(self.add_book)
            self.option = 0
        if self.option == 2:
            self.menu.append(self.edit_book)
            self.option = 0
        if self.option == 3:
            self.menu.append(self.delete_book)
            self.option = 0
        if self.option == 4:
            return True
        if self.option == 5:
            EndComposer.create().start()

    def __back(self,*args):
        self.menu.pop()
        self.input_method = self.get_input
        self.option = 0
        self.fake_selection = 0
        return False

    def delete_book(self):
        end = False
        anwser = ''
        books = self.books
        search = False
        question = "Digite o nome de um livro: "

        # Window variables ==================
        selected = 0
        terminal_size = get_terminal_size()
        window = terminal_size[1] - 3
        fake_selection = 0
        ini_item = 0
        end_item = window
        # ===================================
        pos_na_string = 0
        while end is not True:
            showed_items = list(map(lambda x: x.title,books))
            total = len(showed_items)
            terminal_size = get_terminal_size()
            window = terminal_size[1] - 3

            draw_scrollable_menu(showed_items,fake_selection,ini_item)
            print(question + anwser,end='')
            move_cursor( len(question) + pos_na_string + 1,get_terminal_size()[1])
            search = False
            k = readkey()
            if k  == key.ENTER:
                if total >0:
                    end = True
                    continue
            if k == key.LEFT:
                pos_na_string -= 1
                pos_na_string = max(pos_na_string,0)
            elif k == key.RIGHT:
                pos_na_string += 1
                pos_na_string = min(pos_na_string,len(anwser))
            elif k in (key.CTRL_N,key.CTRL_J,key.DOWN):
                selected -= 1
                selected = max(selected,0)
                if fake_selection > 0:
                    fake_selection -=1
                else:
                    if end_item > window:
                        ini_item -= 1
                        end_item -= 1
            elif k in (key.CTRL_P,key.CTRL_K,key.UP):
                selected += 1
                selected = min(total-1,selected)
                if fake_selection < min(window - 1,total-1):
                    fake_selection +=1
                else:
                    if ini_item < total - window:
                        ini_item += 1
                        end_item += 1
            elif k in (key.BACKSPACE):
                if pos_na_string != 0:
                    anwser = anwser[0:pos_na_string-1] + anwser[pos_na_string:]
                pos_na_string = max(pos_na_string,1)
                search = True
                end_item = window
                ini_item = 0
                fake_selection = 0
                pos_na_string -= 1
            else:
                if len(anwser) == 0:
                    anwser += k
                elif pos_na_string == 0:
                    anwser = k + anwser
                else:
                    anwser = anwser[:pos_na_string]+ k + anwser[pos_na_string:]
                pos_na_string += 1
                search = True
                ini_item = 0
                end_item = window
                fake_selection = 0
            if search:
                books = self.controller.search_by_name(anwser,100)
            end = False
        result = [False]
        while result:
            clear_screen()
            move_cursor(0,get_terminal_size()[1])
            certeza = input("Tem certeza que deseja excluir esse livro? Escreva Sim ou Não: ")
            if re.match(r'^si?m?$',certeza.lower()):
                result = self.controller.delete_book(books[selected])
                break
            elif re.match(r'^n(a?ã?)o?$',certeza.lower()):
                FailureFeedbackBookView("Operação Cancelada").show_books(result)
                print("Aperte qualquer tecla para voltar ao menu livros.")
                readkey()
                self.input_method = self.__back
                return
            else:
                FailureFeedbackBookView("Escreva Sim ou Não").show_books(result)
                print("Aperte enter para tentar novamente.")
                readkey()
                #self.input_method = self.__back
                #return
        clear_screen()
        if result[0] is True:
            SuccessFeedbackBookView("Livro deletado!").show_books(result[1])
            self.input_method = self.__back
        else:
            FailureFeedbackBookView("Erro ao deletar o livro!").show_books(result[1])
            self.input_method = self.__back

    def add_book(self):
        end = False
        text_input = ''
        anwser = []
        questions = ["título","autor"]
        option = 0
        question = f"Digite o {questions[option]} de um livro: "

        pos_na_string = 0
        while end is not True:
            question = f"Digite o {questions[option]} de um livro: "
            clear_screen()
            move_cursor(0,get_terminal_size()[1])
            print(question + text_input,end='')
            move_cursor( len(question) + pos_na_string + 1,get_terminal_size()[1])
            k = readkey()
            if k  == key.ENTER:
                if len(text_input) > 0:
                    option += 1
                    anwser.append(text_input)
                    text_input = ''
                    pos_na_string = 0
                    if option >= len(questions):
                        end = True
                        continue
            elif k == key.LEFT:
                pos_na_string -= 1
                pos_na_string = max(pos_na_string,0)
            elif k == key.RIGHT:
                pos_na_string += 1
                pos_na_string = min(pos_na_string,len(text_input))
            elif k in (key.BACKSPACE):
                if pos_na_string != 0:
                    text_input = text_input[0:pos_na_string-1] + text_input[pos_na_string:]
                pos_na_string = max(pos_na_string,1)
                pos_na_string -= 1
            else:
                if len(text_input) == 0:
                    text_input += k
                elif pos_na_string == 0:
                    text_input = k + text_input
                else:
                    text_input = text_input[:pos_na_string]+ k + text_input[pos_na_string:]
                pos_na_string += 1
            option %= len(questions)
            end = False
        result = self.controller.add_book(anwser[0],anwser[1])
        clear_screen()
        if result[0] is True:
            SuccessFeedbackBookView("Parabéns você adicionou um livro!").show_books(result[1])
            self.input_method = self.__back
        else:
            FailureFeedbackBookView("Não foi possível adicionar este livro").show_books(result[1])
            self.input_method = self.__back

    def edit_book(self):
        end = False
        anwser = ''
        all_books = self.controller.get_all()
        books = all_books
        search = False
        question = "Digite o nome de um livro: "

        # Window variables ==================
        selected = 0
        terminal_size = get_terminal_size()
        window = terminal_size[1] - 3
        fake_selection = 0
        ini_item = 0
        end_item = window
        # ===================================
        pos_na_string = 0
        while end is not True:
            showed_items = list(map(lambda x: x.title,books))
            total = len(showed_items)
            terminal_size = get_terminal_size()
            window = terminal_size[1] - 3

            draw_scrollable_menu(showed_items,fake_selection,ini_item)
            print(question + anwser,end='')
            move_cursor( len(question) + pos_na_string + 1,get_terminal_size()[1])
            search = False
            k = readkey()
            if k  == key.ENTER:
                if total >0:
                    end = True
                    anwser = ''
                    pos_na_string = 0
                    continue
            if k == key.LEFT:
                pos_na_string -= 1
                pos_na_string = max(pos_na_string,0)
            elif k == key.RIGHT:
                pos_na_string += 1
                pos_na_string = min(pos_na_string,len(anwser))
            elif k in (key.CTRL_N,key.CTRL_J,key.DOWN):
                selected -= 1
                selected = max(0,selected)
                if fake_selection > 0:
                    fake_selection -=1
                else:
                    if end_item > window:
                        ini_item -= 1
                        end_item -= 1
            elif k in (key.CTRL_P,key.CTRL_K,key.UP):
                selected += 1
                selected = min(total-1,selected)
                if fake_selection < min(window - 1,total-1):
                    fake_selection +=1
                else:
                    if ini_item < total - window:
                        ini_item += 1
                        end_item += 1
            elif k in (key.BACKSPACE):
                if pos_na_string != 0:
                    anwser = anwser[0:pos_na_string-1] + anwser[pos_na_string:]
                pos_na_string = max(pos_na_string,1)
                search = True
                end_item = window
                ini_item = 0
                fake_selection = 0
                pos_na_string -= 1
            else:
                if len(anwser) == 0:
                    anwser += k
                elif pos_na_string == 0:
                    anwser = k + anwser
                else:
                    anwser = anwser[:pos_na_string]+ k + anwser[pos_na_string:]
                pos_na_string += 1
                search = True
                ini_item = 0
                end_item = window
                fake_selection = 0
            if search:
                if len(anwser) > 0:
                    books = self.controller.search_by_name(anwser,5)
                else:
                    books = all_books
            # selected %= len(books)
            end = False

        anwser = ''
        to_edit = books[selected]
        questions = ["título","autor"]
        questions_anwsers = [ to_edit.title, to_edit.author ]
        question_option = 0
        anwser = questions_anwsers[question_option]
        pos_na_string = len(anwser)

        while question_option < len(questions):
            tamanho = len(questions[question_option])

            clear_screen()
            move_cursor(0,get_terminal_size()[1])
            print("Novo " + questions[question_option] + ": " + anwser,end='')
            move_cursor( tamanho + pos_na_string + 8 ,get_terminal_size()[1])

            k = readkey()
            if k  == key.ENTER:
                questions_anwsers[question_option] = anwser
                question_option += 1
                if question_option < len(questions):
                    anwser = questions_anwsers[question_option]
                pos_na_string = len(anwser)
                continue
            if k == key.LEFT:
                pos_na_string -= 1
                pos_na_string = max(pos_na_string,0)
            elif k == key.RIGHT:
                pos_na_string += 1
                pos_na_string = min(pos_na_string,len(anwser))
            elif k in (key.CTRL_N,key.CTRL_J,key.DOWN):
                pass
            elif k in (key.CTRL_P,key.CTRL_K,key.UP):
                pass
            elif k in (key.BACKSPACE):
                if pos_na_string != 0:
                    anwser = anwser[0:pos_na_string-1] + anwser[pos_na_string:]
                pos_na_string = max(pos_na_string,1)
                search = True
                end_item = window
                ini_item = 0
                fake_selection = 0
                pos_na_string -= 1
            else:
                if len(anwser) == 0:
                    anwser += k
                elif pos_na_string == 0:
                    anwser = k + anwser
                else:
                    anwser = anwser[:pos_na_string]+ k + anwser[pos_na_string:]
                pos_na_string += 1
                search = True
                ini_item = 0
                end_item = window
                fake_selection = 0
        result = self.controller.edit_book(to_edit.id,questions_anwsers[0],questions_anwsers[1])
        result[1].append(to_edit)
        clear_screen()
        if result[0] is True:
            SuccessFeedbackBookView(f"Parabéns você editou o livro:").show_books(result[1])
            self.input_method = self.__back
        else:
            FailureFeedbackBookView("Não foi possível editar este livro").show_books(result[1])
            self.input_method = self.__back

    def start(self):
        while self.end is not True:
            self.menu[-1]()
            self.end = self.input_method()

class SuccessFeedbackBookView(FeedbackBookView):

    def __init__(self,msg : str):
        self.message = msg

    def show_books(self,books: Iterable[ Book ]):
        move_cursor(0,get_terminal_size()[1])
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
        print("Aperte qualquer tecla para voltar ao menu livros")
        readkey()

class FailureFeedbackBookView(FeedbackBookView):

    def __init__(self,msg : str):
        self.message = msg
    def show_books(self,books: Iterable[ Book ]):
        print(f"{Back.RED}{Fore.WHITE}{self.message}")
        # print("Aperte qualquer tecla para voltar ao menu livros")
        # readkey()
