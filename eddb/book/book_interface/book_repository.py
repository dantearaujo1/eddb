from abc import ABC,abstractmethod
class BookRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass