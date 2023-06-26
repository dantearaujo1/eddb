from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def get_byID(self, ID):
        raise NotImplementedError

    @abstractmethod
    def get_byName(self, name):
        raise NotImplementedError

    @abstractmethod
    def get_all(self):
        raise NotImplementedError

    @abstractmethod
    def delete_byID(self, ID):
        raise NotImplementedError

    @abstractmethod
    def delete_byName(self, name):
        raise NotImplementedError


    @abstractmethod
    def delete_all(self):
        raise NotImplementedError

    @abstractmethod
    def add(self, item):
        raise NotImplementedError

    @abstractmethod
    def add_all(self, items):
        raise NotImplementedError
