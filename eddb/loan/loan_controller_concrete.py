from loan_interface.loan_controller import LoanController
from loan_interface.loan_repository import LoanRepository
class LoanControllerConcrete(LoanController):
    def __init__(self, repository: LoanRepository):
        self.repository = repository
        self.view = None
    def set_view(self, view):
        self.view = view

    def search_by_name(self, name):
        pass
