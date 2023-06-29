from eddb.loan.loan_interface.loan_controller import LoanController
from eddb.loan.loan_interface.feedback_loan_view import FeedbackLoanView
class LoanView(FeedbackLoanView):
    def __init__(self, controller: LoanController):
        self.controller = controller
    def show_loans(self, loans):
        for loan in loans:
            print(loan.name)
        pass

    def start(self):
        pass
        #É para aparecer o menu com todas as opcoes do menu livro
