from eddb.loan.loan_view import LoanView
from eddb.loan.loan_controller_concrete import LoanControllerConcrete
from eddb.loan.loan_repository_concrete import LoanRepositoryConcrete
class LoanComposer:
    @staticmethod
    def create() -> LoanView:
        repository = LoanRepositoryConcrete()
        controller = LoanControllerConcrete(repository)
        view = LoanView(controller)
        controller.set_view(view)
        return view
