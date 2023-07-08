from fuzzywuzzy import process

from eddb.book.book_interface.feedback_book_view import FeedbackBookView
from eddb.book.book_interface.book_controller import BookController
from eddb.book.book_interface.book_repository import BookRepository
from eddb.loan.loan_interface.loan_repository import LoanRepository
from eddb.book.book_model import Book

class BookControllerConcrete(BookController):
    def __init__(self, repository: BookRepository,loan_repository: LoanRepository):
        self.repository = repository
        self.loan_repository = loan_repository
        self.view = None

    def set_view(self, view: FeedbackBookView):
        self.view = view

    def search_by_name(self, name: str, limit: int = 5):
        books = self.repository.get_all()
        query = name
        if limit:
            result = process.extract(query,books,limit=limit)
        else:
            result = process.extract(query,books)
        result = list(map(lambda x: x[0],result))
        return result

    def get_all(self):
        return self.repository.get_all()

    def add_book(self,title: str,author: str):
        b = Book(title=title,author=author)
        return self.repository.add_item(b),[b]

    def edit_book(self,old_id: str ,new_title: str,new_author: str):
        edited = Book(id=old_id,title=new_title,author=new_author)
        return self.repository.update_item(edited),[edited]

    def delete_book(self,book : Book):
        result = None
        first = self.repository.delete_item(book)
        if first is True:
            result = self.loan_repository.delete_all_with_book_id(book.id)
        return result,[book]
