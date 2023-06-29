from abc import ABC,abstractmethod
class StudentRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass
