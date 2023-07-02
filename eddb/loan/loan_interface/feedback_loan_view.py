from abc import ABC,abstractmethod
class FeedbackLoanView(ABC):
    @abstractmethod
    def show_feedback(self, loans):
        pass
