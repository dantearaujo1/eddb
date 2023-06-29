from book_interface.book_controller import BookController
from book_interface.book_repository import BookRepository
class BookControllerConcrete(BookController):
    def __init__(self, repository: BookRepository):
        self.repository = repository
        self.view = None
    def set_view(self, view):
        self.view = view

    def search_by_name(self, name):
        pass