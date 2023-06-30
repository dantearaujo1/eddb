from abc import ABC,abstractmethod
import time
class FeedbackBookView(ABC):
    @abstractmethod
    def show_books(self, books):
        pass


class SuccessFeedbackAddBookView(FeedbackBookView):

    def show_books(self,books):
        print(f"Parabéns, você adicionou o livro: ")
        print(f"Título: {books[0].title}")
        print(f"Autor: {books[0].author}")
        time.sleep(3)

class FailureFeedbackAddBookView(FeedbackBookView):

    def show_books(self,books):
        print(f"Não foi possível adicionar o livro!")
        time.sleep(3)
