import re
from collections.abc import Iterable

from readchar import readchar, readkey, key
from colorama import Back,Fore

from eddb.student.student_interface.student_controller import StudentController
from eddb.student.student_model import Student
from eddb.student.student_interface.feedback_student_view import FeedbackStudentView
from eddb.endview.end_composer import EndComposer
from eddb.util.util import clear_screen,move_cursor,get_terminal_size
from eddb.util.menus import draw_scrollable_menu

class StudentView(FeedbackStudentView):
    def __init__(self, controller: StudentController):
        self.controller = controller
        self.options = ["Procurar","Cadastrar","Editar","Excluir","Voltar","Sair"]
        self.option = 0
        self.end = False
        self.menu = [self.show]
        self.input_method = self.get_input
        self.last = None

        self.window = get_terminal_size()[1] - 3
        self.init_option = 0
        self.end_option = self.window
        self.fake_selection = 0

    def __back(self,*args):
        self.menu.pop()
        self.input_method = self.get_input
        self.option = 0
        self.fake_selection = 0
        return False

    def set_parent(self,view):
        self.last = view

    def show_students(self, students):
        for student in students:
            print(student.name)

    def show_student(self, student):
        clear_screen()
        move_cursor(0,get_terminal_size()[1])
        print(f"Matrícula: {student.id}")
        print(f"Nome: {student.name}")
        print(f"Sobrenome: {student.surname}")
        print(f"Email: {student.email}")
        print("Aperte qualquer tecla para voltar ao menu estudante")
        readkey()

    def show(self):
        draw_scrollable_menu(self.options,self.fake_selection,self.init_option,reverse=True)

    def get_input(self):
        total = len(self.options)
        a = readkey()
        if a  == key.ENTER:
            return self.create_submenu()
        if a in (key.CTRL_N,key.CTRL_J,key.DOWN):
            if self.option < len(self.options)-1:
                self.option += 1
            if self.fake_selection < min(self.end_option - self.init_option - 1,total-1):
                self.fake_selection += 1
            else:
                if self.end_option < len(self.options):
                    self.init_option += 1
                    self.end_option += 1

        elif a in (key.CTRL_P,key.CTRL_K,key.UP):
            if self.option > 0:
                self.option -= 1
            if self.fake_selection > 0:
                self.fake_selection -= 1
            else:
                if self.init_option > 0:
                    self.init_option -= 1
                    self.end_option -= 1
        return False

    def get_students(self):
        """
        Retorna todos os estudantes do banco e permite filtrar por nomes
        """
        end = False
        anwser = ''
        all_students = self.controller.get_all()
        students = all_students
        search = False
        question = "Digite o nome de um estudante: "

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
            showed_items = list(map(lambda x: x.name,students))
            total= len(showed_items)
            terminal_size = get_terminal_size()
            window = terminal_size[1] - 3

            draw_scrollable_menu(showed_items,fake_selection,ini_item)
            print(question + anwser,end='')
            move_cursor( len(question) + pos_na_string + 1,get_terminal_size()[1])
            search = False
            k = readkey()
            if k  == key.ENTER:
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
                    students = self.controller.search_by_name(anwser,5)
                else:
                    students = all_students
            end = False
        self.show_student(students[selected])
        self.input_method = self.__back

    def create_submenu(self):
        if self.option == 0:
            self.menu.append(self.get_students)
            self.option = 0
        elif self.option == 1:
            self.menu.append(self.add_student)
            self.option = 0
        elif self.option == 2:
            self.menu.append(self.edit_student)
            self.option = 0
        elif self.option == 3:
            self.menu.append(self.delete_student)
            self.option = 0
        elif self.option == 4:
            return True
        elif self.option == 5:
            EndComposer.create().start()

    def delete_student(self):
        end = False
        anwser = ''
        students = self.controller.get_all()
        search = False
        question = "Digite o nome ou matrícula do aluno: "

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
            showed_items = list(map(lambda x: x.name,students))
            total = len(showed_items)
            terminal_size = get_terminal_size()
            window = terminal_size[1] - 3

            draw_scrollable_menu(showed_items,fake_selection,ini_item)
            print(question + anwser,end='')
            move_cursor( len(question) + pos_na_string + 1,get_terminal_size()[1])
            search = False
            k = readkey()
            if k  == key.ENTER:
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
            elif k in (key.CTRL_G):
                self.input_method = self.__back
                return
            elif k in (key.BACKSPACE):
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
                students = self.controller.search_by_name(anwser,100)
            #selected %= len(students)
            end = False

        result = [False]
        while result:
            clear_screen()
            move_cursor(0,window+3)
            certeza = input("Tem certeza que deseja excluir? Escreva Sim ou Não: ")
            if re.match(r'^si?m?$',certeza.lower()):
                result = self.controller.delete_student(students[selected])
                break
            elif re.match(r'^n(a?ã?)o?$',certeza.lower()):
                FailureFeedbackStudentView("Estudante não deletado!").show_students(result)
                print("Aperte qualquer tecla para voltar ao menu estudante.")
                readkey()
                self.input_method = self.__back
                return
            else:
                # result.append(False)
                # result.append([])
                FailureFeedbackStudentView("Escreva Sim ou Não").show_students(result)
                print("Aperte enter para tentar novamente.")
                readkey()
        clear_screen()
        if result[0] is True:
            SuccessFeedbackStudentView("Estudante deletado:").show_students(result[1])
        else:
            FailureFeedbackStudentView("Erro ao deletar o estudante!").show_students(result[1])
        self.input_method = self.__back

    def add_student(self):
        end = False
        text_input = ''
        anwser = []
        questions = ["a matrícula","o nome","o sobrenome", "o email"]
        option = 0
        question = f"Digite {questions[option]} do estudante: "
        pos_na_string = 0
        while end is not True:
            question = f"Digite {questions[option]} do estudante: "
            clear_screen()
            move_cursor(0,get_terminal_size()[1])
            print(question + text_input,end='')
            move_cursor( len(question) + pos_na_string + 1,get_terminal_size()[1])
            k = readkey()
            if k  == key.ENTER:
                if option == 0:
                    verify = self.controller.verify_id_exist(text_input)
                    if verify:
                        clear_screen()
                        move_cursor(0,get_terminal_size()[1])
                        print('Matricula já cadastrada, tente outra. Aperte qualquer tecla para voltar')
                        readkey()
                        continue
                    option += 1
                    anwser.append(text_input)
                    text_input = ''
                    pos_na_string = 0
                    if option >= len(questions):
                        end = True
                        continue  
                else:
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
            elif k == key.UP:
                pass
            elif k == key.DOWN:
                pass
            elif k in (key.BACKSPACE):
                if pos_na_string != 0:
                    text_input = text_input[0:pos_na_string-1] + text_input[pos_na_string:]
                pos_na_string = max(pos_na_string,1)
                pos_na_string -= 1
            else:       
                if option == 0:
                    if re.match(r'[0-9]',k):
                        if len(text_input) == 0:
                            text_input += k
                        elif pos_na_string == 0:
                            text_input = k + text_input
                        else:
                            text_input = text_input[:pos_na_string]+ k + text_input[pos_na_string:]
                        pos_na_string += 1
                    else:
                        move_cursor( len(question) + pos_na_string + 1,get_terminal_size()[1])
                else:
                    if len(text_input) == 0:
                        text_input += k
                    elif pos_na_string == 0:
                        text_input = k + text_input
                    else:
                        text_input = text_input[:pos_na_string]+ k + text_input[pos_na_string:]
                    pos_na_string += 1
                
            end = False
        result = self.controller.add_student(anwser[0],anwser[1],anwser[2], anwser[3])
        clear_screen()
        if result[0] is True:
            SuccessFeedbackStudentView("Parabéns você adicionou um estudante!").show_students(result[1])
        else:
            FailureFeedbackStudentView("Não foi possível adicionar este estudante").show_students(result[1])
        self.input_method = self.__back

    def edit_student(self):
        end = False
        anwser = ''
        all_students = self.controller.get_all()
        students = all_students
        questions = ["Nova matrícula","Novo nome","Novo sobrenome", "Novo email"]
        search = False
        question = "Digite o nome ou matrícula do aluno: "

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
            showed_items = list(map(lambda x: x.name,students))
            total = len(showed_items)
            terminal_size = get_terminal_size()
            window = terminal_size[1] - 3

            draw_scrollable_menu(showed_items,fake_selection,ini_item)
            print(question + anwser,end='')
            move_cursor( len(question) + pos_na_string + 1,get_terminal_size()[1])
            search = False

            k = readkey()
            if k  == key.ENTER:
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
                if fake_selection < min(window - 1,total - 1):
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
                    students = self.controller.search_by_name(anwser,5)
                else:
                    students = all_students
            end = False

        anwser = ''
        to_edit = students[selected]
        old_id = to_edit.id
        questions_anwsers = [ str(to_edit.id), to_edit.name, to_edit.surname, to_edit.email ]
        question_option = 0
        anwser = questions_anwsers[question_option]
        pos_na_string = len(anwser)

        while question_option < len(questions):
            tamanho = len(questions[question_option])

            clear_screen()
            move_cursor(0,get_terminal_size()[1])
            print(questions[question_option] + ": " + anwser,end='')
            move_cursor( tamanho + pos_na_string + 3 ,get_terminal_size()[1])

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

        result = self.controller.edit_student(old_id, questions_anwsers[0],questions_anwsers[1],questions_anwsers[2],questions_anwsers[3])
        result[1].append(to_edit)
        clear_screen()
        if result[0] is True:
            SuccessFeedbackStudentView(f"Parabéns você editou o estudante:").show_students(result[1])
        else:
            FailureFeedbackStudentView("Não foi possível editar este estudante").show_students(result[1])
        self.input_method = self.__back

    def start(self):
        while self.end != True:
            clear_screen()
            self.menu[-1]()
            self.end = self.input_method()

class SuccessFeedbackStudentView(FeedbackStudentView):

    def __init__(self,msg : str):
        self.message = msg

    def show_students(self,students: Iterable[ Student ]):
        clear_screen()
        move_cursor(0,get_terminal_size()[1])
        print(f"{Back.GREEN}{Fore.BLACK}{self.message }")
        if len(students) > 1:
            print("Antes:")
            print(f" ID: {students[1].id}")
            print(f" Nome: {students[1].name}")
            print(f" Sobrenome: {students[1].surname}")
            print(f" Email: {students[1].email}")
            print("Depois:")
            print(f" ID: {students[0].id}")
            print(f" Nome: {students[0].name}")
            print(f" Sobrenome: {students[0].surname}")
            print(f" Email: {students[0].email}")
        else:
            print(f"ID: {students[0].id}")
            print(f"Nome: {students[0].name}")
            print(f"Sobrenome: {students[0].surname}")
            print(f"Email: {students[0].email}")
        print("Aperte qualquer tecla para voltar")
        readkey()

class FailureFeedbackStudentView(FeedbackStudentView):

    def __init__(self,msg : str):
        self.message = msg
    def show_students(self,students: Iterable[ Student ]):
        clear_screen()
        move_cursor(0,get_terminal_size()[1])
        print(f"{Back.RED}{Fore.WHITE}{self.message}")
        # print("Aperte qualquer tecla para voltar")
        # readkey()
