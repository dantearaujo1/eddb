# from textual.app import App, ComposeResult
# from textual.widgets import Header, Footer
import time
from view.console import Console
from controller.biblioteca_controller import BibliotecaController
from repository.livros_repository import LivrosRepositoryJSON

# class Console(App):
#
#     BINDINGS = [ ("Ctrl-C", "exit", "Sair") ]
#
#     def compose(self):
#         yield Header(name="Biblioteca")
#         yield Footer()


def main():
    cadastro_opt = []
    livros_opt = []
    emprestimos_opt = []

    inicio_opt = [
        {"entry": "Menu Livros", "out_opt": livros_opt, "próximo": 4},
        {"entry": "Menu Empréstimos", "out_opt": emprestimos_opt, "próximo": 5},
        {"entry": "Menu Cadastro", "out_opt": cadastro_opt, "próximo": 2},
        {"entry": "Sair", "out_opt": -1, "próximo": -1},
    ]
    cadastro_opt.append({"entry": "Cadastrar Aluno", "próximo": 6})
    cadastro_opt.append({"entry": "Editar Aluno", "próximo": 7})
    cadastro_opt.append({"entry": "Apagar Aluno", "próximo": 8})
    cadastro_opt.append({"entry": "Cadastrar Livro", "próximo": 9})
    cadastro_opt.append({"entry": "Editar Livro", "próximo": 10})
    cadastro_opt.append({"entry": "Apagar Livro", "próximo": 11})
    cadastro_opt.append({"entry": "Voltar", "próximo": 0})
    cadastro_opt.append({"entry": "Sair", "próximo": -1})

    livros_opt.append({"entry": "Procurar Livro", "próximo": 12})
    livros_opt.append({"entry": "Ver Livros", "próximo": 13})
    livros_opt.append({"entry": "Voltar", "próximo": 0})
    livros_opt.append({"entry": "Sair", "próximo": -1})

    emprestimos_opt.append({"entry": "Buscar Empréstimo", "próximo": 14})
    emprestimos_opt.append({"entry": "Ver empréstimos de Aluno", "próximo": 15})
    emprestimos_opt.append({"entry": "Ver empréstimo de Livro", "próximo": 16})
    emprestimos_opt.append({"entry": "Voltar", "próximo": 0})
    emprestimos_opt.append({"entry": "Sair", "próximo": -1})

    menus = [
        {"titulo": "Inicio", "opções": inicio_opt},
        {"titulo": "Cadastros", "opções": cadastro_opt},
        {"titulo": "Alunos", "opções": inicio_opt},
        {"titulo": "Livros", "opções": livros_opt},
        {"titulo": "Empréstimo", "opções": emprestimos_opt},
    ]

    repositorio_de_livros = LivrosRepositoryJSON("eddb/livros.json")
    view = Console()
    biblioteca = BibliotecaController(view, repositorio_de_livros, menus)

    livros_opt[1]["próximo"] = biblioteca.ver_livros
    livros_opt[0]["próximo"] = biblioteca.procurar_livros
    biblioteca.iniciar()


def cadastrar():
    print("Cadastrei!")
    time.sleep(2)
    return inicio_opt


if __name__ == "__main__":
    main()
