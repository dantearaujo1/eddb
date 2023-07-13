from fuzzywuzzy import process

from eddb.student.student_interface.feedback_student_view import FeedbackStudentView
from eddb.student.student_interface.student_controller import StudentController
from eddb.student.student_interface.student_repository import StudentRepository
from eddb.loan.loan_interface.loan_repository import LoanRepository
from eddb.student.student_model import Student


class StudentControllerConcrete(StudentController):
    def __init__(self, repository: StudentRepository, loan_repo: LoanRepository):
        self.repository = repository
        self.loan_repo = loan_repo
        self.view = None

    def set_view(self, view: FeedbackStudentView):
        self.view = view

    def search_by_name(self, name: str, limit: int = 5):
        students = self.repository.get_all()
        query = name
        if limit:
            result = process.extract(query,students,limit=limit)
        else:
            result = process.extract(query,students)
        result = list(map(lambda x: x[0],result))
        return result

    def get_all(self):
        return self.repository.get_all()

    def add_student(self,id: int, name: str,surname: str, email: str):
        s = Student(id=int (id), name=name,surname=surname, email=email)
        return self.repository.add_item(s),[s]

    def edit_student(self,old_id: str, new_id: str ,new_name: str,new_surname: str, new_email: str):
        edited = Student(id=int(new_id),name=new_name,surname=new_surname, email=new_email)
        return self.repository.update_item(edited, old_id),[edited]

    def delete_student(self,student : Student):
        result = None
        first = self.repository.delete_item(student)
        if first is True:
            result = self.loan_repo.delete_all_with_student_id(student.id)
        return result,[student]
    
    def verify_id_exist(self, id):
        list_students = self.repository.get_by_id(id)
        if list_students:
            return True
        else:
            return False

        
