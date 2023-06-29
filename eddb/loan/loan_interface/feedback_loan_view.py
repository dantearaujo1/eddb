from abc import ABC,abstractmethod
class FeedbackLoanView(ABC):
    @abstractmethod
    def show_loans(self, loans):
        pass
