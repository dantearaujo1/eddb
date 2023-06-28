from abc import ABC, abstractmethod

class IController(ABC):

    @abstractmethod
    def get(self):
        raise NotImplementedError

    @abstractmethod
    def add(self):
        raise NotImplementedError

    @abstractmethod
    def delete(self,item):
        raise NotImplementedError

    @abstractmethod
    def update(self,item):
        raise NotImplementedError
