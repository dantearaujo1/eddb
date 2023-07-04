import time,sys
from collections.abc import Iterable

from readchar import readchar, readkey, key
from colorama import Back,Fore

from eddb.student.student_interface.student_controller import StudentController
from eddb.student.student_model import Student
from eddb.student.student_interface.feedback_student_view import FeedbackStudentView
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
        print(f"id: {student.id}")
        print(f"name: {student.name}")
        print(f"surname: {student.surname}")
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
        # Lidando com  CTRL_C Exit Key
        exit_key = readchar()
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
                    students = all
            option %= len(students)
            end = False
        self.show_student(students[option])

    def create_submenu(self):
        if self.option == 0:
            return self.get_students
        elif self.option == 1:
            return self.add_student
        elif self.option == 2:
            return None

    def add_student(self):
        end = False
        text_input = ''
        anwser = []
        questions = ["name","surname"]
        option = 0
        question = f"Digite o {questions[option]} do estudante: "
        while end is not True:
            question = f"Digite o {questions[option]} do estudante: "
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
        result = self.controller.add_student(anwser[0],anwser[1])
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
            print("Depois:")
            print(f" ID: {students[0].id}")
            print(f" Nome: {students[0].name}")
            print(f" Sobrenome: {students[0].surname}")
        else:
            print(f"ID: {students[0].id}")
            print(f"Nome: {students[0].name}")
            print(f"Sobrenome: {students[0].surname}")
        time.sleep(3)

class FailureFeedbackStudentView(FeedbackStudentView):

    def __init__(self,msg : str):
        self.message = msg
    def show_students(self,students: Iterable[ Student ]):
        print(f"{Back.RED}{Fore.WHITE}{self.message}")
        time.sleep(3)