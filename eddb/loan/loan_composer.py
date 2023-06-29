from loan_view import LoanView
from loan_controller_concrete import LoanControllerConcrete
from loan_repository_concrete import LoanRepositoryConcrete
class LoanComposer:
    @staticmethod
    def create() -> LoanView:
        repository = LoanRepositoryConcrete()
        controller = LoanControllerConcrete(repository)
        view = LoanView(controller)
        controller.set_view(view)
        return view
