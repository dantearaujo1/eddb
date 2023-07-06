import time,sys
from collections.abc import Iterable

from readchar import readchar, readkey, key
from colorama import Back,Fore

from eddb.student.student_interface.student_controller import StudentController
from eddb.student.student_model import Student
from eddb.student.student_interface.feedback_student_view import FeedbackStudentView
from eddb.endview.end_composer import EndComposer
from eddb.util.util import clear_screen,move_cursor,get_terminal_size

class StudentView(FeedbackStudentView):
    def __init__(self, controller: StudentController):
        self.controller = controller
        self.options = ["Procurar","Cadastrar","Editar","Excluir","Sair"]
        self.option = 0
        self.end = False
        self.menu = None

    def show_students(self, students):
        for student in students:
            print(students.name)

    def show_student(self, student):
        clear_screen()
        print(f"Matrícula: {student.id}")
        print(f"Nome: {student.name}")
        print(f"Sobrenome: {student.surname}")
        print(f"Email: {student.email}")
        #input(f"{Back.LIGHTBLACK_EX}{Fore.WHITE}Aperte qualquer tecla para voltar")
        time.sleep(5)
        self.end = False
        self.start()

    def show_menu(self):
        for i in range(len(self.options)):
            if i == self.option:
                print(f"{Back.WHITE}{Fore.BLACK}{self.options[i]}")
            else:
                print(f"{self.options[i]}")

    def get_input(self):
        # Lidando com  CTRL_C Exit Key
        a = readkey()
        if a  == key.ENTER:
            return True
        elif a in (key.CTRL_N,key.CTRL_J,key.DOWN):
            self.option += 1
        elif a in (key.CTRL_P,key.CTRL_K,key.UP):
            self.option -= 1
        self.option %= len(self.options)
        return False

    def get_students(self):
        """
        Retorna todos os estudantes do banco e permite filtrar por nomes
        """
        end = False
        anwser = ''
        all_students = self.controller.get_all()
        students = all_students
        option = 0
        search = False
        question = "Digite o nome de um estudante: "
        while end is not True:
            clear_screen()
            move_cursor(0,get_terminal_size()[1]-2-len(students))
            print("=====================================")
            for idx,student in enumerate(students):
                move_cursor(0,get_terminal_size()[1]-2-idx)
                if option == idx:
                    print(f"{Back.WHITE}{Fore.BLACK}{student.name}")
                else:
                    print(f"{student.name}")
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
                    students = self.controller.search_by_name(anwser,5)
                else:
                    students = all_students
            option %= len(students)
            end = False
        self.show_student(students[option])

    def create_submenu(self):
        if self.option == 0:
            return self.get_students
        elif self.option == 1:
            return self.add_student
        elif self.option == 2:
            return self.edit_student
        elif self.option == 3:
            return self.delete_student
        elif self.option == 4:
            EndComposer.create().start()


    def delete_student(self):
        end = False
        anwser = ''
        students = []
        option = 0
        search = False
        question = "Digite o nome ou matrícula do aluno: "
        while end is not True:
            clear_screen()
            for i in range(len(students)-1,-1,-1):
                student = students[i]
                if option == i:
                    print(f"{Back.WHITE}{Fore.BLACK}{student.name}")
                else:
                    print(f"{student.name}")
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
                students = self.controller.search_by_name(anwser,100)
            option %= len(students)
            end = False
        result = self.controller.delete_student(students[option])
        clear_screen()
        if result[0] is True:
            SuccessFeedbackStudentView("Estudante deletado:").show_students(result[1])
            time.sleep(3)
            self.end = False
            self.start()
        else:
            FailureFeedbackStudentView("Erro ao deletar o estudante!").show_students(result[1])
            time.sleep(3)
            self.end = False
            self.start()

    def add_student(self):
        end = False
        text_input = ''
        anwser = []
        questions = ["a matrícula","o nome","o sobrenome", "o email"]
        option = 0
        question = f"Digite {questions[option]} do estudante: "
        while end is not True:
            question = f"Digite {questions[option]} do estudante: "
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
            #option %= len(questions)
            end = False
        result = self.controller.add_student(anwser[0],anwser[1],anwser[2], anwser[3])
        clear_screen()
        if result[0] is True:
            SuccessFeedbackStudentView("Parabéns você adicionou um estudante!").show_students(result[1])
            time.sleep(3)
            self.end = False
            self.start()
        else:
            FailureFeedbackStudentView("Não foi possível adicionar este estudante").show_students(result[1])
            time.sleep(3)
            self.end = False
            self.start()

    def edit_student(self):
        end = False
        anwser = ''
        students = []
        questions = ["Nova matrícula","Novo nome","Novo sobrenome", "Novo email"]
        option = 0
        search = False
        question = "Digite o nome ou matrícula do aluno: "
        while end is not True:
            clear_screen()
            for i in range(len(students)-1,-1,-1):
                student = students[i]
                if option == i:
                    print(f"{Back.WHITE}{Fore.BLACK}{student.name}")
                else:
                    print(f"{student.name}")
            #move_cursor(0,get_terminal_size()[1]-2)
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
                if len(anwser) > 0:
                    anwser = anwser[0:-1]
                search = True
            else:
                anwser += k
                search = True
            if search:
                students = self.controller.search_by_name(anwser,100)
            option %= len(students)
            end = False
        to_edit = students[option]
        old_id = to_edit.id
        questions_anwsers = [ to_edit.id, to_edit.name, to_edit.surname, to_edit.email ]
        question_option = 0
        while question_option < len(questions):
            clear_screen()
            move_cursor(0,get_terminal_size()[1]-1)
            print(questions[question_option] + ": " + questions_anwsers[question_option],end='')
            k = readkey()
            if k  == key.ENTER:
                question_option += 1
                continue
            if k in (key.BACKSPACE):
                questions_anwsers[question_option] = questions_anwsers[question_option][0:-1]
            else:
                questions_anwsers[question_option] = questions_anwsers[question_option] + k
        result = self.controller.edit_student(old_id, questions_anwsers[0],questions_anwsers[1],questions_anwsers[2],questions_anwsers[3])
        #result[1].append(to_edit)
        clear_screen()
        if result[0] is True:
            SuccessFeedbackStudentView(f"Parabéns você editou o estudante:").show_students(result[1])
            #input()
            time.sleep(4)
            self.end = False
            self.start()
        else:
            FailureFeedbackStudentView("Não foi possível editar este estudante").show_students(result[1])
            time.sleep(4)
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

class SuccessFeedbackStudentView(FeedbackStudentView):

    def __init__(self,msg : str):
        self.message = msg

    def show_students(self,students: Iterable[ Student ]):
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
        time.sleep(3)

class FailureFeedbackStudentView(FeedbackStudentView):

    def __init__(self,msg : str):
        self.message = msg
    def show_students(self,students: Iterable[ Student ]):
        print(f"{Back.RED}{Fore.WHITE}{self.message}")
        time.sleep(3)
