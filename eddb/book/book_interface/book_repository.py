from abc import ABC,abstractmethod
class RepositoryBook(ABC):
    @abstractmethod
    def get_all(self):
        pass