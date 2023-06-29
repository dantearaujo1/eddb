from eddb.student.student_interface.student_controller import StudentController
from eddb.student.student_interface.feedback_student_view import FeedbackStudentView
class StudentView(FeedbackStudentView):
    def __init__(self, controller: StudentController):
        self.controller = controller
    def show_books(self, students):
        for student in students:
            print(students.name)
        pass

    def start(self):
        pass
        #É para aparecer o menu com todas as opcoes do menu livro
