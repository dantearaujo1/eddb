import time, re,copy
from datetime import datetime,timedelta
from collections.abc import Iterable
from colorama import Back,Fore,Style
from readchar import readkey,readchar,key

from eddb.util.util import clear_screen,get_terminal_size, move_cursor
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
        self.options = ["Procurar","Emprestar","Devolver","Voltar","Sair"]
        self.option = 0
        self.menu = [self.show]
        self.input_method = self.get_input
        self.end = False
        self.last = None

        self.window = get_terminal_size()[1] - 3
        self.init_option = 0
        self.end_option = self.window
        self.fake_selection = 0

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
            self.menu.append(self.pay_loan)
            self.option = 0
        elif self.option == 3:
            return True
        else:
            EndComposer().create().start()

    def get_loans(self):
        end = False
        anwser = ''
        anwser_objs = []
        books_loaned = []
        loans_from_student = []
        search = False
        questions = [ "Pesquise por matrícula ou nome do aluno: ","Pesquise o livro emprestado: " ]
        handlers = [self.controller.get_students, self.controller.get_books]
        searches = [self.controller.search_student_by_id, self.controller.search_student_from_list]
        items = handlers[0]()

        # Window variables ==================
        menu_idx = 0
        selected = 0
        terminal_size = get_terminal_size()
        window = terminal_size[1] - 3
        fake_selection = 0
        ini_item = 0
        end_item = window
        # ===================================
        pos_na_string = 0
        while end is not True:
            total = len(items)

            showing_items = []
            for i in range(total):
                item = items[i]
                if menu_idx < 1:
                    showing_items.append(str(item.id) + " " + item.name)
                else:
                    status = item[2][0]
                    bg = theme['fsilver'] if status == 'i' else theme['fred'] if status == 'o' else theme['fgreen']
                    showing_items.append(item[0].title + f" {Style.RESET_ALL}[{bg}{status}{Style.RESET_ALL}]")


            draw_scrollable_menu(showing_items,fake_selection,ini_item)
            move_cursor(0,terminal_size[1])
            print(questions[menu_idx] + anwser,end='')
            move_cursor( len(questions[menu_idx]) + pos_na_string + 1,get_terminal_size()[1])


            search = False
            k = readkey()
            if k  == key.ENTER:
                pos_na_string = 0
                if menu_idx < len(questions) - 1:
                    menu_idx += 1
                    if len(items) > 0:
                        stu = items[selected]
                        anwser_objs.append(stu)
                        loans_from_student = self.controller.get_loans_by_student_id(stu.id)
                        books_loaned = [(self.controller.get_book_by_id(x.book_id)[0],i,x.status) for i,x in enumerate(loans_from_student)]
                        items = books_loaned
                        anwser = ''
                        selected = 0
                        fake_selection = 0
                        continue
                else:
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
                    if menu_idx == 0:
                        items = searches[menu_idx](anwser,10)
                    elif menu_idx == 1:
                        items = searches[menu_idx](books_loaned,anwser,10)
                else:
                    if menu_idx == 0:
                        items = handlers[menu_idx]()
                    elif menu_idx == 1:
                        items = books_loaned
            end = False
        if len(items) > 0:
            result = loans_from_student[items[selected][1]]
            self.show_loan(result)
            self.__select_option(["Excluir","Voltar"],[self.delete_loan,(lambda x: x)],items[selected])
        else:
            NoneFeedbackLoanView("Nenhum dado selecionado!").show_feedback([])
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
        # text_input = ''

        questions = ["Digite a matricula ou nome do aluno(a): ","Digite o livro para emprestar: "]
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
        pos_na_string = 0
        while end is not True:
            total = len(items)
            question = questions[menu_idx]
            text_input = anwser[menu_idx]

            showing_items = []
            if menu_idx == 0:
                showing_items = list(map(lambda x: x.name,items))
            if menu_idx == 1:
                showing_items = list(map(lambda x: x.title,items))


            draw_scrollable_menu(showing_items,fake_selection,ini_item)
            move_cursor(0,terminal_size[1])
            print(question + text_input,end='')
            move_cursor( len(question) + pos_na_string + 1,get_terminal_size()[1])

            search = False
            k = readkey()
            if k  == key.ENTER:
                if len(items) > 0:
                    anwser_objects.append(items[selected])
                    if menu_idx == 0:
                        selected = 0
                        fake_selection = 0
                        pos_na_string = 0
                    menu_idx += 1
                    search = True
                    if menu_idx > len(questions) - 1:
                        end = True
                        continue
            elif k == key.LEFT:
                pos_na_string -= 1
                pos_na_string = max(pos_na_string,0)
            elif k == key.RIGHT:
                pos_na_string += 1
                pos_na_string = min(pos_na_string,len(text_input))
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
                    text_input = text_input[0:pos_na_string-1] + text_input[pos_na_string:]
                pos_na_string = max(pos_na_string,1)
                pos_na_string -= 1
                anwser[menu_idx] = text_input
                ini_item = 0
                end_item = window
                fake_selection = 0
                search = True
            else:
                if len(text_input) == 0:
                    text_input += k
                elif pos_na_string == 0:
                    text_input = k + text_input
                else:
                    text_input = text_input[:pos_na_string]+ k + text_input[pos_na_string:]
                anwser[menu_idx] = text_input
                pos_na_string += 1
                ini_item = 0
                end_item = window
                fake_selection = 0
                search = True
            if search:
                if len(text_input) > 0:
                    items = search_handler[menu_idx](text_input,10)
                else:
                    items = all_items[menu_idx]
            end = False
        clear_screen()
        student = anwser_objects[0]
        book = anwser_objects[1]
        if self.controller.book_status_is_active(book):
            clear_screen()
            print("Este livro já está alugado...")
            print("Aperte qualquer tecla para voltar ao menu empréstimo")
            readkey()
            self.input_method = self.__back
        else:
            paydate = datetime.now() + timedelta(days=30)
            loan = Loan(book_id=book.id,student_id=int(student.id),payday=paydate,status="active")
            self.controller.add_loan(loan)
            self.show_loan(loan)
            print("Aperte qualquer tecla para voltar ao menu empréstimo")
            readkey()
            self.input_method = self.__back


    def pay_loan(self):
        end = False
        anwser = ''
        anwser_objs = []
        books_loaned = []
        loans_from_student = []
        search = False
        questions = [ "Pesquise por matrícula ou nome do aluno: ","Pesquise o livro para devolver: " ]
        handlers = [self.controller.get_students, self.controller.get_books]
        searches = [self.controller.search_student_by_id, self.controller.search_student_from_list]
        items = handlers[0]()

        # Window variables ==================
        menu_idx = 0
        selected = 0
        terminal_size = get_terminal_size()
        window = terminal_size[1] - 3
        fake_selection = 0
        ini_item = 0
        end_item = window
        # ===================================
        pos_na_string = 0
        while end is not True:
            total = len(items)

            showing_items = []
            for i in range(total):
                item = items[i]
                if menu_idx < 1:
                    showing_items.append(str(item.id) + " " + item.name)
                else:
                    showing_items.append(item[0].title)


            draw_scrollable_menu(showing_items,fake_selection,ini_item)
            move_cursor(0,terminal_size[1])
            print(questions[menu_idx] + anwser,end='')
            move_cursor( len(questions[menu_idx]) + pos_na_string + 1,get_terminal_size()[1])


            search = False
            k = readkey()
            if k  == key.ENTER:
                pos_na_string = 0
                if menu_idx < len(questions) - 1:
                    menu_idx += 1
                    if len(items) > 0:
                        stu = items[selected]
                        anwser_objs.append(stu)
                        loans_from_student = self.controller.get_loans_by_student_id(stu.id)
                        loans_from_student = list(filter(lambda x: x.status != "inactive",loans_from_student))
                        books_loaned = [(self.controller.get_book_by_id(x.book_id)[0],i) for i,x in enumerate(loans_from_student)]
                        items = books_loaned
                        anwser = ''
                        continue
                else:
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
                    if menu_idx == 0:
                        items = searches[menu_idx](anwser,10)
                    elif menu_idx == 1:
                        items = searches[menu_idx](books_loaned,anwser,10)
                else:
                    if menu_idx == 0:
                        items = handlers[menu_idx]()
                    elif menu_idx == 1:
                        items = books_loaned
            end = False
        if len(items) > 0:
            result = loans_from_student[items[selected][1]]
            self.show_loan(result)
            self.__select_option(["Pagar","Adiar","Voltar"],[self.pay,self.delay,(lambda x: x)],result)
        else:
            NoneFeedbackLoanView("Nenhum dado selecionado!").show_feedback([])
        self.input_method = self.__back

    def pay(self,loan):
        data = {
            "book_id": loan.book_id,
            "student_id": loan.student_id,
            "loan_date": loan.loan_date,
            "payday": datetime.now(),
            "status": 'inactive',
        }
        result = self.controller.update_item(loan,data)
        self.show_loan(result[1])
        print(f"{theme['bloan_active']}{theme['floan_active']} Empréstimo Pago")
        print("Aperte qualquer tecla para voltar ao menu empréstimo")
        move_cursor(0,get_terminal_size()[1])
        readkey()

    def delay(self,loan):
        data = {
            "book_id": loan.book_id,
            "student_id": loan.student_id,
            "loan_date": loan.loan_date,
            "payday": loan.payday + timedelta(days=15),
            "status": 'active',
        }
        result = self.controller.update_item(loan,data)
        clear_screen()
        self.show_loan(result[1])
        print(f"{theme['bloan_active']}{theme['floan_active']} Empréstimo Postergado")
        print("Aperte qualquer tecla para voltar ao menu empréstimo")
        readkey()

    def delete_loan(self,loan):
        ficar = True
        while ficar:
            clear_screen()
            move_cursor(0,get_terminal_size()[1])
            s = input("Tem certeza que deseja excluir esse empréstimo? Escreva sim ou não: ")
            if re.match(r'^si?m?$',s.lower()):
                if self.controller.delete_item(loan)[0]:
                    DeleteSuccessFeedbackLoanView("O empréstimo foi excluído").show_feedback([loan])
                    print("Aperte qualquer tecla para voltar ao menu empréstimo",end="")
                    readkey()
                    self.input_method = self.__back
                    return
                DeleteFailureFeedbackLoanView("O empréstimo não pôde ser excluído.").show_feedback([loan])
                print("Aperte qualquer tecla para voltar ao menu empréstimo",end="")
                readkey()
                ficar = False
            elif re.match(r'^n(a?ã?)o?$',s.lower()):
                DeleteFailureFeedbackLoanView("Operação cancelada.").show_feedback([loan])
                print("Aperte qualquer tecla para voltar ao menu empréstimo",end="")
                readkey()
                ficar = False
            else:
                DeleteFailureFeedbackLoanView("Escreva Sim ou Não. Aperte enter para tentar novamente").show_feedback([loan])
                readkey()
        self.input_method = self.__back

    def show_feedback(self, loans):
        for loan in loans:
            print(loan["name"])

    def show_loan(self,loan):
        clear_screen()
        move_cursor(0,get_terminal_size()[1])
        stu = self.controller.get_student_by_id(loan.student_id)[0]
        book = self.controller.get_book_by_id(loan.book_id)[0]
        print(f"Livro: {book.title}")
        print(f"Estudante: {stu.name}")
        print(f"Dia do Empréstimo: {loan.loan_date}")
        print(f"Dia da Devolução: {loan.payday}")
        colors = []
        if loan.status == "active":
            colors = [theme["bloan_active"],theme["floan_active"]]
        elif loan.status == "inactive":
            colors = [Back.LIGHTBLACK_EX,Fore.WHITE]
        elif loan.status == "overdue":
            colors = [Back.RED,Fore.WHITE]
        print(f"Status: {colors[0]}{colors[1]}{loan.status}")
        # print("Aperte Qualquer Tecla para Sair!")
        # readkey()

    def show(self):
        draw_scrollable_menu(self.options,self.fake_selection,self.init_option,reverse=True)

    def __back(self,*args):
        self.menu.pop()
        self.option = 0
        self.fake_selection = 0
        self.input_method = self.get_input
        return False

    def get_input(self):
        total = len(self.options)
        k = readkey()
        if k  == key.ENTER:
            return self.create_submenu()
        if k in (key.CTRL_N,key.CTRL_J,key.DOWN):
            if self.option < len(self.options)-1:
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
        # print(f"{Back.GREEN}{Fore.WHITE}Empréstimo Deletado!")
        # print("Aperte qualquer tecla para voltar ao menu empréstimo",end="")
        # readkey()

class DeleteFailureFeedbackLoanView(FeedbackLoanView):

    def __init__(self,msg: str):
        self.message = msg

    def show_feedback(self,loans: Iterable[Loan]):
        print(f"{Back.RED}{Fore.WHITE}{self.message}")
        # print(f"{Back.RED}{Fore.WHITE}O Empréstimo não foi deletado, tente novamente!")
        # print("Aperte qualquer tecla para voltar ao menu empréstimo",end="")
        # readkey()

class AddFeedbackLoanView(FeedbackLoanView):

    def __init__(self,msg: str):
        self.message = msg

    def show_feedback(self,loans: Iterable[Loan]):
        clear_screen()
        print(f"{Back.GREEN}{Fore.BLACK}{self.message}")
        print(f"{Back.GREEN}{Fore.BLACK}Empréstimo Deletado!")
        print("Aperte qualquer tecla para voltar ao menu empréstimo",end="")
        readkey()

class NoneFeedbackLoanView(FeedbackLoanView):

    def __init__(self,msg: str):
        self.message = msg

    def show_feedback(self,loans: Iterable[Loan]):
        clear_screen()
        print(f"{Back.LIGHTBLACK_EX}{Fore.WHITE}{self.message}")
        print("Aperte qualquer tecla para voltar ao menu empréstimo",end="")
        readkey()
