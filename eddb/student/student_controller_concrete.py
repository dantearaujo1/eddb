from eddb.student.student_interface.student_controller import StudentController
from eddb.student.student_interface.student_repository import StudentRepository
class StudentControllerConcrete(StudentController):
    def __init__(self, repository: StudentRepository):
        self.repository = repository
        self.view = None
    def set_view(self, view):
        self.view = view

    def search_by_name(self, name):
        pass
