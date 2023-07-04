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

    def search_by_filter(self, query, filter, limit=5):
        if isinstance(filter,Book):
            return self.book_repository.get_all()
        if isinstance(filter,Loan):
            return self.get_all()
        if isinstance(filter,Student):
            return self.student_repository.get_all()

    def get_all(self):
        return self.repository.get_all()

    def get_all_books_students(self):
        return [self.book_repository.get_all(),self.student_repository.get_all()]

    def get_book_by_id(self,ID):
        book = self.book_repository.get_by_id(ID)
        return book
    def get_student_by_id(self,ID):
        student = self.student_repository.get_by_id(ID)
        return student

    def update_item(self,item,data):
        item.id_book = data["id_book"]
        item.id_student = data["id_book"]
        item.loan_date = data["loan_date"]
        item.payday = data["payday"]
        item.status = data["status"]
        self.repository.update_item(item)

    def delete_item(self,item):
        return self.repository.delete_item(item),[item]

