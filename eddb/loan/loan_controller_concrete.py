import time
from eddb.util.util import clear_screen
from fuzzywuzzy import process
from eddb.loan.loan_interface.loan_controller import LoanController
from eddb.loan.loan_interface.loan_repository import LoanRepository
from eddb.book.book_interface.book_repository import BookRepository
from eddb.student.student_interface.student_repository import StudentRepository
from eddb.book.book_model import Book
from eddb.loan.loan_model import Loan
from eddb.student.student_model import Student

class LoanControllerConcrete(LoanController):
    def __init__(self, repository: LoanRepository,s_repository: StudentRepository, b_repository: BookRepository):
        self.repository = repository
        self.view = None
        self.student_repository = s_repository
        self.book_repository = b_repository

    def set_view(self, view):
        self.view = view

    def search_by_name(self, name, limit=5):
        return self.get_all()

    def search_by_book_name(self,name,limit=5):
        pass
    def search_by_student_name(self,name,limit=5):
        pass
    def search_by_student_id(self,ID,limit=5):
        loans = self.repository.get_all()
        students_ids = list(map(lambda l: str(l.student_id),loans))
        query = str(ID)
        result = []
        if limit:
            result = process.extract(query,students_ids,limit=limit)
        else:
            result = process.extract(query,students_ids)
        result = list(filter(lambda x: x[1] > 60,result))
        clear_screen()
        result = set(map(lambda x: x[0],result))
        matches = []
        for loan in loans:
            for match in result:
                if loan.student_id == int(match):
                    matches.append(loan)
        return matches

    def search_by_book_id(self,ID,limit=5):
        loans = self.repository.get_all()
        books_ids = list(map(lambda l: str(l.book_id),loans))
        query = str(ID)
        result = []
        if limit:
            result = process.extract(query,books_ids,limit=limit)
        else:
            result = process.extract(query,books_ids)
        result = list(map(lambda x: x[0],result))
        return result

    def search_book_by_id(self,ID,limit=5):
        books = self.book_repository.get_all()
        query = ID
        result = []
        if limit:
            result = process.extract(query,books,limit=limit)
        else:
            result = process.extract(query,books)
        result = list(map(lambda x: x[0],result))
        return result

    def search_student_by_id(self,ID,limit=5):
        students = self.student_repository.get_all()
        query = ID
        result = []
        if limit:
            result = process.extract(query,students,limit=limit)
        else:
            result = process.extract(query,students)
        result = list(map(lambda x: x[0],result))
        return result

    def get_all(self):
        return self.repository.get_all()

    def get_all_books_students(self):
        return [self.book_repository.get_all(),self.student_repository.get_all()]

    def get_book_by_id(self,ID):
        book = self.book_repository.get_by_id(ID)
        if book[0] is not None:
            return book
        else:
            return []
    def get_students(self):
        return self.student_repository.get_all()
    def get_books(self):
        return self.book_repository.get_all()

    def get_student_by_id(self,ID):
        student = self.student_repository.get_by_id(ID)
        if student[0] is not None:
            return student
        else:
            return []

    def update_item(self,item,data):
        item.id_book = data["id_book"]
        item.id_student = data["id_book"]
        item.loan_date = data["loan_date"]
        item.payday = data["payday"]
        item.status = data["status"]
        self.repository.update_item(item)

    def delete_item(self,item):
        return self.repository.delete_item(item),[item]

    def get_loan_by_book_id(self,ID):
        loans = self.repository.get_all()
        result = []
        for loan in loans:
            if loan.book_id == ID:
                result.append(loan)
        return result

    def book_status_is_active(self,book):
        loans = self.get_loan_by_book_id(book.id)
        for loan in loans:
            if loan.status == "active" or loan.status == "overdue":
                return True
        return False
    
    def add_loan(self,item):
        return self.repository.add_item(item),[item]