from eddb.book.book_view import BookView
from eddb.book.book_controller_concrete import BookControllerConcrete
from eddb.book.book_repository_concrete import BookRepositoryConcrete
class BookComposer:
    @staticmethod
    def create() -> BookView:
        repository = BookRepositoryConcrete("livros.json")
        controller = BookControllerConcrete(repository)
        view = BookView(controller)
        controller.set_view(view)
        return view
