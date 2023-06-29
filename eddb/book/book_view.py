from book_interface.book_controller import BookController
from book_interface.feedback_book_view import FeedbackBookView
class BookView(FeedbackBookView):
    def __init__(self, controller: BookController):
        self.controller = controller
    def show_books(self, books):
        for book in books:
            print(book.name)
        pass

    def start(self):
        pass
        #É para aparecer o menu com todas as opcoes do menu livro
