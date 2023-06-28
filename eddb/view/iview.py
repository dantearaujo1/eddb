from abc import ABC,abstractmethod


class IView(ABC):

    @abstractmethod
    def show(self,menu) -> None:
        pass

    @abstractmethod
    def get_input(self) -> str:
        pass

    @abstractmethod
    def sair(self) -> int:
        pass

    def run(self) -> None:
        while(True):
            self.show()
            self.get_input()
        self.sair()
