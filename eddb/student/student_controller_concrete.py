from fuzzywuzzy import process
from eddb.student.student_interface.student_controller import StudentController
from eddb.student.student_interface.student_repository import StudentRepository
from eddb.student.student_model import Student


class StudentControllerConcrete(StudentController):
    def __init__(self, repository: StudentRepository):
        self.repository = repository
        self.view = None

    def set_view(self, view):
        self.view = view

    def search_by_name(self, name):
        students = self.repository.get_all()
        query = name
        result = process.extract(query,students)
        result = list(map(lambda x: x[0],result))
        return result
    
    def add_student(self,name,surname):
        S = Student(name=name,surname=surname)
        return self.repository.add_item(b),[b]

    def edit_student(self,student,name,surname):
        edited = Student(id=student.id,name=name,surname=surname)
        return self.repository.edit_item(edited)

    def delete_student(self,student):
        pass
