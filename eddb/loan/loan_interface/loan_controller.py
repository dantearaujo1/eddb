from abc import ABC,abstractmethod
class LoanController(ABC):
    @abstractmethod
    def search_by_name(self, name):
        pass
