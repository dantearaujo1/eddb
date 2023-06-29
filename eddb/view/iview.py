from abc import ABC,abstractmethod


class IView(ABC):

    @abstractmethod
    def show(self,data) -> None:
        pass

    @abstractmethod
    def sair(self,length=5) -> int:
        pass

