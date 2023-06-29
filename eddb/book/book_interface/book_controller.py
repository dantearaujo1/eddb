from abc import ABC,abstractmethod
class BookController(ABC):
    @abstractmethod
    def search_by_name(self, name):
        pass