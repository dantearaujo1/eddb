from eddb.loan.loan_view import LoanView
from eddb.loan.loan_controller_concrete import LoanControllerConcrete
from eddb.loan.loan_repository_concrete import LoanRepositoryConcrete
from eddb.book.book_repository_concrete import BookRepositoryConcrete
from eddb.student.student_repository_concrete import StudentRepositoryConcrete
class LoanComposer:
    @staticmethod
    def create() -> LoanView:
        repository = LoanRepositoryConcrete("eddb/db_teste.json")
        s_repository = StudentRepositoryConcrete("eddb/db_teste.json")
        b_repository = BookRepositoryConcrete("eddb/db_teste.json")
        controller = LoanControllerConcrete(repository,s_repository,b_repository)
        view = LoanView(controller)
        controller.set_view(view)
        return view
