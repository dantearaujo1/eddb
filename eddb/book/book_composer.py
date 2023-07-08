from eddb.book.book_view import BookView
from eddb.book.book_controller_concrete import BookControllerConcrete
from eddb.book.book_repository_concrete import BookRepositoryConcrete
from eddb.loan.loan_repository_concrete import LoanRepositoryConcrete
class BookComposer:
    @staticmethod
    def create() -> BookView:
        repository = BookRepositoryConcrete("eddb/db_teste.json")
        loan_repo = LoanRepositoryConcrete("eddb/db_teste.json")
        controller = BookControllerConcrete(repository,loan_repo)
        view = BookView(controller)
        controller.set_view(view)
        return view
