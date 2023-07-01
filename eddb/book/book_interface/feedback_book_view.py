from abc import ABC,abstractmethod
import time
class FeedbackBookView(ABC):
    @abstractmethod
    def show_books(self, books):
        pass


