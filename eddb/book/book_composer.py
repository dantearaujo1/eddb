from book_view import BookView
from book_controller_concrete import BookControllerConcrete
from book_repository_concrete import BookRepositoryConcrete
class BookComposer:
    @staticmethod
    def create() -> BookView:
        repository = BookRepositoryConcrete()
        controller = BookControllerConcrete(repository)
        view = BookView(controller)
        controller.set_view(view)
        return view