from abc import ABC,abstractmethod
class ControllerBookMenu(ABC):
    @abstractmethod
    def search_by_name(self, name):
        pass