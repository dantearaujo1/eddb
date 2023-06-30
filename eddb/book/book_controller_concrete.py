from fuzzywuzzy import process

from eddb.book.book_interface.book_controller import BookController
from eddb.book.book_interface.book_repository import BookRepository
from eddb.book.book_model import Book

class BookControllerConcrete(BookController):
    def __init__(self, repository: BookRepository):
        self.repository = repository
        self.view = None

    def set_view(self, view):
        self.view = view

    def search_by_name(self, name):
        books = self.repository.get_all()
        query = name
        result = process.extract(query,books)
        result = list(map(lambda x: x[0],result))
        return result

    def add_book(self,title,author):
        b = Book(title=title,author=author)
        return self.repository.add_item(b),[b]

    def edit_book(self,book,title,author):
        edited = Book(id=book.id,title=title,author=author)
        return self.repository.edit_item(edited)

    def delete_book(self,book):
        pass
