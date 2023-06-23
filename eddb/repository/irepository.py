from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def get_byID(self, id):
        pass

    @abstractmethod
    def get_byName(self, name):
        pass

    @abstractmethod
    def delete_byID(self, id):
        pass

    @abstractmethod
    def delete_byName(self, name):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def delete_all(self):
        pass
