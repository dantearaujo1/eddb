from controller.biblioteca_controller import BibliotecaController
from view.menu_view import MenuView

from repository.irepository import IRepository
from controller.icontroller import IController
from view.iview import IView

class GerenciadorBibliotecario():
    def __init__(self, view : IView, controller : IController, repo : IRepository):
        self.controlador = controller
        self.view = view
        self.repository = repo

    def mostrar(self):
        self.controlador.iniciar()
