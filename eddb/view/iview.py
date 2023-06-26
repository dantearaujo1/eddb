from abc import ABC,abstractmethod


class IView(ABC):

    @abstractmethod
    def show(self,menu):
        pass

    @abstractmethod
    def mostrar_mensagem(self,msg):
        pass

    @abstractmethod
    def sair(self):
        pass
