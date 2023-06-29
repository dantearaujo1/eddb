from abc import ABC,abstractmethod
class StudentController(ABC):
    @abstractmethod
    def search_by_name(self, name):
        pass
