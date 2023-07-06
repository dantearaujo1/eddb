import time, re
from datetime import datetime,timedelta
from collections.abc import Iterable
from colorama import Back,Fore
from readchar import readkey,readchar,key

from eddb.util.util import clear_screen,get_terminal_size, move_cursor, time_utc
from eddb.util.menus import draw_scrollable_menu
from eddb.util.themes import get_theme

from eddb.loan.loan_model import Loan
from eddb.loan.loan_interface.loan_controller import LoanController
from eddb.loan.loan_interface.feedback_loan_view import FeedbackLoanView
from eddb.endview.end_composer import EndComposer

theme = get_theme("debora")

class LoanView(FeedbackLoanView):
    def __init__(self, controller: LoanController):
        self.controller = controller
        self.options = ["Buscar Empréstimos","Fazer empréstimo","Voltar","Sair"]
        self.option = 0
        self.menu = [self.show]
        self.input_method = self.get_input
        self.end = False
        self.last = None

    def set_parent(self,view):
        self.last = view

    def create_submenu(self):
        if self.option == 0:
            self.menu.append(self.get_loans)
            self.option = 0
        elif self.option == 1:
            self.menu.append(self.add_loan)
            self.option = 0
        elif self.option == 2:
            self.last.end= False
            self.last.start()
        else:
            EndComposer().create().start()
            self.end = True

    def get_loans(self):
        end = False
        anwser = ''
        all_items = self.controller.get_all()
        items = all_items
        search = False
        question = "Digite a matricula do aluno: "

        # Window variables ==================
        selected = 0
        terminal_size = get_terminal_size()
        window = terminal_size[1] - 3
        fake_selection = 0
        ini_item = 0
        end_item = window
        # ===================================
        while end is not True:
            total = len(items)

            showing_items = []
            for i in range(total):
                if total > 0:
                    item = items[i]
                    student = self.controller.get_student_by_id(item.student_id)[0]
                    book = self.controller.get_book_by_id(item.book_id)[0]
                    showing_items.append(str(student.id) + " " + student.name + " " + book.title)

            draw_scrollable_menu(showing_items,fake_selection,ini_item)
            move_cursor(0,terminal_size[1]-1)
            print(question + anwser,end='')

            search = False
            k = readkey()
            if k  == key.ENTER:
                end = True
                continue
            if k in (key.CTRL_N,key.CTRL_J,key.DOWN):
                selected -= 1
                if fake_selection > 0:
                    fake_selection -=1
                else:
                    if end_item > window:
                        ini_item -= 1
                        end_item -= 1
            elif k in (key.CTRL_P,key.CTRL_K,key.UP):
                selected += 1
                if fake_selection < window - 1:
                    fake_selection +=1
                else:
                    if ini_item < total - window - 1:
                        ini_item += 1
                        end_item += 1
            elif k in (key.BACKSPACE):
                anwser = anwser[0:-1]
                ini_item = 0
                end_item = window
                fake_selection = 0
                search = True
            else:
                anwser += k
                ini_item = 0
                end_item = window
                fake_selection = 0
                search = True
            if search:
                if len(anwser) > 0:
                    items = self.controller.search_by_student_id(anwser,10)
                else:
                    items = all_items
            if len(items) > 0:
                selected %= len(items)
            else:
                selected = 0
            end = False


        self.show_loan(items[selected])
        self.__select_option(["Editar","Excluir","Voltar"],[self.edit_loan,self.delete_loan,(lambda x: x)],items[selected])
        self.input_method = self.__back

    def __select_option(self,options,options_callback,*args):
        text = "Escolha o que deseja fazer: "
        print(text)
        for i,option in enumerate(options):
            if i < len(options) - 1:
                print(f"| {i}. {option} ",end="")
            else:
                print(f"| {i}. {option} |",end="")
        print("")
        k = readkey()
        for i,option in enumerate(options):
            if k == str(i):
                options_callback[i](*args)

    def add_loan(self):
        end = False
        anwser = ['','']
        selected = 0
        terminal_size = get_terminal_size()
        search = False
        questions = ["Digite a matricula do aluno: ","Digite o livro para emprestar:"]
        handlers = [self.controller.get_students,self.controller.get_books]
        search_handler = [self.controller.search_student_by_id,self.controller.search_book_by_id]
        all_items = [handlers[0](),handlers[1]()]
        anwser_objects = []
        menu_idx = 0
        items = all_items[menu_idx]

        # Window variables ==================
        window = terminal_size[1] - 3
        fake_selection = 0
        ini_item = 0
        end_item = window
        # ===================================
        while end is not True:
            total = len(items)

            showing_items = []
            if menu_idx == 0:
                showing_items = list(map(lambda x: x.name,items))
            if menu_idx == 1:
                showing_items = list(map(lambda x: x.title,items))

            draw_scrollable_menu(showing_items,fake_selection,ini_item)
            move_cursor(0,terminal_size[1]-1)
            print(questions[menu_idx] + anwser[menu_idx],end='')

            search = False
            k = readkey()
            if k  == key.ENTER:
                anwser_objects.append(items[selected])
                if menu_idx == 0:
                    selected = 0
                    fake_selection = 0
                menu_idx += 1
                search = True
                if menu_idx > len(questions) - 1:
                    end = True
                    continue
            if k in (key.CTRL_N,key.CTRL_J,key.DOWN):
                selected -= 1
                if fake_selection > 0:
                    fake_selection -=1
                else:
                    if end_item > window:
                        ini_item -= 1
                        end_item -= 1
            elif k in (key.CTRL_P,key.CTRL_K,key.UP):
                selected += 1
                if fake_selection < window - 1:
                    fake_selection +=1
                else:
                    if ini_item < total - window - 1:
                        ini_item += 1
                        end_item += 1
            elif k in (key.BACKSPACE):
                anwser[menu_idx] = anwser[menu_idx][0:-1]
                ini_item = 0
                end_item = window
                fake_selection = 0
                search = True
            else:
                anwser[menu_idx] += k
                ini_item = 0
                end_item = window
                fake_selection = 0
                search = True
            if search:
                if len(anwser) > 0:
                    items = search_handler[menu_idx](anwser[menu_idx],10)
                else:
                    items = all_items[menu_idx]
            if len(items) > 0:
                selected %= len(items)
            else:
                selected = 0
            end = False
        clear_screen()
        student = anwser_objects[0]
        book = anwser_objects[1]
        if self.controller.book_status_is_active(book):
            clear_screen()
            print("O livro ja está alugado")
            time.sleep(10)
        else:
            paydate = datetime.now() + timedelta(days=30)
            loan = Loan(book_id=book.id,student_id=student.id,payday=paydate,status="active")
            self.show_loan(loan)
            print("Aperte qualquer letra para voltar!")
            readchar()
            self.input_method = self.__back


    def pay_loan(self,loan):
        clear_screen()
        print("Pay Screen")
        time.sleep(3)

    def edit_loan(self,loan):
        clear_screen()
        print("Edit Screen")
        self.show_loan(loan)
        time.sleep(3)

    def delete_loan(self,loan):
        clear_screen()
        s = input("Tem certeza que deseja excluir? ")
        if re.match(r'^si?m?$',s.lower()):
            if self.controller.delete_item(loan)[0]:
                DeleteSuccessFeedbackLoanView("Ação Completa").show_feedback([loan])
                return
            DeleteFailureFeedbackLoanView("Ação Incompleta").show_feedback([loan])

    def show_feedback(self, loans):
        for loan in loans:
            print(loan["name"])

    def show_loan(self,loan):
        clear_screen()
        stu = self.controller.get_student_by_id(loan.student_id)[0]
        book = self.controller.get_book_by_id(loan.book_id)[0]
        print(f"Book: {book.title}")
        print(f"Student: {stu.name}")
        print(f"Loan Day: {loan.loan_date}")
        print(f"Payday: {loan.payday}")
        colors = []
        if loan.status == "active":
            colors = [theme["bloan_active"],theme["floan_active"]]
        elif loan.status == "inactive":
            colors = [Back.LIGHTBLACK_EX,Fore.WHITE]
        elif loan.status == "overdue":
            colors = [Back.RED,Fore.WHITE]
        print(f"Status: {colors[0]}{colors[1]}{loan.status}")

    def show(self):
        clear_screen()
        for i,option in enumerate(self.options):
            if i == self.option:
                print(f"{Back.WHITE}{Fore.BLACK}{option}")
            else:
                print(f"{option}")
        return False

    def __back(self,*args):
        self.menu.pop()
        self.option = 0
        self.input_method = self.get_input
        return False

    def get_input(self):
        k = readkey()
        if k  == key.ENTER:
            self.create_submenu()
        if k in (key.CTRL_N,key.CTRL_J,key.DOWN):
            self.option += 1
        elif k in (key.CTRL_P,key.CTRL_K,key.UP):
            self.option -= 1
        self.option %= len(self.options)
        return False

    def start(self):
        while self.end is not True:
            self.menu[-1]()
            self.end = self.input_method()


class DeleteSuccessFeedbackLoanView(FeedbackLoanView):

    def __init__(self,msg: str):
        self.message = msg

    def show_feedback(self,loans: Iterable[Loan]):
        print(f"{Back.GREEN}{Fore.WHITE}{self.message}")
        print(f"{Back.GREEN}{Fore.WHITE}Empréstimo Deletado!")

class DeleteFailureFeedbackLoanView(FeedbackLoanView):

    def __init__(self,msg: str):
        self.message = msg

    def show_feedback(self,loans: Iterable[Loan]):
        print(f"{Back.RED}{Fore.WHITE}{self.message}")
        print(f"{Back.RED}{Fore.WHITE}O Empréstimo não foi deletado, tente novamente!")

class AddFeedbackLoanView(FeedbackLoanView):

    def __init__(self,msg: str):
        self.message = msg

    def show_feedback(self,loans: Iterable[Loan]):
        clear_screen()
        print(f"{Back.GREEN}{Fore.BLACK}{self.message}")
        print(f"{Back.GREEN}{Fore.BLACK}Empréstimo Deletado!")
        time.sleep(3)
