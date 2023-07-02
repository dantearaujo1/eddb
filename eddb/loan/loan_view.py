import time, re
from collections.abc import Iterable
from colorama import Back,Fore
from readchar import readkey,readchar,key

from eddb.util.util import clear_screen,get_terminal_size, move_cursor

from eddb.loan.loan_model import Loan
from eddb.loan.loan_interface.loan_controller import LoanController
from eddb.loan.loan_interface.feedback_loan_view import FeedbackLoanView
from eddb.endview.end_composer import EndComposer

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
        # elif self.option == 2:
        #     self.menu.append(self.pay_loan)
        #     self.option = 0
        # elif self.option == 3:
        #     self.menu.append(self.edit_loan)
        elif self.option == 2:
            #     self.option = 0
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
        option = 0
        search = False
        question = "Digite a matricula do aluno: "
        while end is not True:
            clear_screen()
            move_cursor(0,get_terminal_size()[1]-2-len(items))
            print("=====================================")
            for idx,item in enumerate(items):
                move_cursor(0,get_terminal_size()[1]-2-idx)
                if option == idx:
                    print(f"{Back.WHITE}{Fore.BLACK}{item.id}")
                else:
                    print(f"{item.id}")
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
                    items = self.controller.search_by_name(anwser,5)
                else:
                    items = all_items
            option %= len(items)
            end = False
        self.show_loan(items[option])
        self.__select_option(["Editar","Excluir"],[self.edit_loan,self.delete_loan],items[option])
        self.input_method = self.__back

    def __select_option(self,options,options_callback,*args):
        text = "Escolha o que deseja fazer: "
        print(text)
        for i,option in enumerate(options):
            print(f"{i}. {option} |",end="")
        print("")
        k = readchar()
        for i,option in enumerate(options):
            if k == str(i):
                options_callback[i](*args)


    def add_loan(self):
        end = False
        anwser = ''
        everything = self.controller.get_all_books_students()
        all_books = everything[0]
        all_students = everything[1]

        show_data = [all_students,all_books]
        options = [show_data[0],show_data[1]]
        option = 0

        selected = 0
        search = False

        questions = ["Digite a matricula do aluno: ","Escolha um livro: "]
        data = []
        while end is not True:
            clear_screen()
            move_cursor(0,get_terminal_size()[1]-2-len(options[option]))
            print("=====================================")
            for idx,item in enumerate(options[option]):
                move_cursor(0,get_terminal_size()[1]-2-idx)
                if selected == idx:
                    if hasattr(item,'name'):
                        print(f"{Back.WHITE}{Fore.BLACK}{item.name}")
                    else:
                        print(f"{Back.WHITE}{Fore.BLACK}{item.title}")
                else:
                    if hasattr(item,'name'):
                        print(f"{item.name}")
                    else:
                        print(f"{item.title}")
            move_cursor(0,get_terminal_size()[1]-1)
            print("=====================================")
            if len(data) > 0:
                print(f"Aluno Selecionado: {data[0].name}")
            else:
                print("Aluno Selecionado: ")
            print("=====================================")
            move_cursor(0,get_terminal_size()[1]-1)
            print(questions[option] + anwser,end='')
            search = False
            k = readkey()
            if k  == key.ENTER:
                data.append(options[option][selected])
                option += 1
                anwser = ''
                if option >= len(questions):
                    end = True
                continue
            if k in (key.CTRL_N,key.CTRL_J,key.DOWN):
                selected -= 1
            elif k in (key.CTRL_P,key.CTRL_K,key.UP):
                selected += 1
            elif k in (key.BACKSPACE):
                anwser = anwser[0:-1]
                search = True
            elif k in (key.CTRL_B):
                option -= 1
                anwser = ''
                data.pop()
            else:
                anwser += k
                search = True
            if search:
                if len(anwser) > 0:
                    # TODO: Consertar essa search_by_filter
                    options[option] = self.controller.search_by_filter(anwser,options[option][0],5)
                else:
                    options[option] = show_data[option]
            selected %= len(options[option])
            end = False
        # self.show_loan(items[option])
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
        print(f"ID: {loan.id}")
        print(f"ID_BOOK: {loan.book_id}")
        print(f"ID_STUDENT: {loan.student_id}")
        print(f"Loan Day: {loan.loan_date}")
        print(f"Payday: {loan.payday}")
        print(f"Status: {loan.status}")

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
