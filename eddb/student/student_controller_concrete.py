from student_interface.book_controller import StudentController
from student_interface.book_repository import StudentRepository
class StudentControllerConcrete(StudentController):
    def __init__(self, repository: StudentRepository):
        self.repository = repository
        self.view = None
    def set_view(self, view):
        self.view = view

    def search_by_name(self, name):
        pass
