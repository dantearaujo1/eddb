from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def save(self):
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, ID):
        raise NotImplementedError
    @abstractmethod
    def get_by_name(self, name):
        raise NotImplementedError
    @abstractmethod
    def get_all(self):
        raise NotImplementedError
    @abstractmethod
    def delete_by_id(self, ID):
        raise NotImplementedError
    @abstractmethod
    def delete_by_name(self, name):
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
    @abstractmethod
    def update_by_name(self,name,data):
        raise NotImplementedError
    @abstractmethod
    def update_by_id(self,ID,data):
        raise NotImplementedError
    @abstractmethod
    def update_all(self,data):
        raise NotImplementedError


