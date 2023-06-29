from abc import ABC,abstractmethod
class FeedbackBookView(ABC):
    @abstractmethod
    def show_books(self, books):
        pass