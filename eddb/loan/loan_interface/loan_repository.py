from abc import ABC,abstractmethod
class LoanRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass
