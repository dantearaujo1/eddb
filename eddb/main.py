# from textual.app import App, ComposeResult
# from textual.widgets import Header, Footer
import time
from view.console import Console

# class Console(App):
#
#     BINDINGS = [ ("Ctrl-C", "exit", "Sair") ]
#
#     def compose(self):
#         yield Header(name="Biblioteca")
#         yield Footer()

if __name__ == "__main__":
    cadastro_opt = []
    livros_opt = []
    emprestimos_opt = []

    inicio_opt= [
        {"entry":"Menu Cadastro", "out_opt":cadastro_opt},
        {"entry":"Menu Livros", "out_opt":livros_opt},
        {"entry":"Menu Empréstimos", "out_opt":emprestimos_opt},
        {"entry":"Sair", "out_opt":-1},
    ]

    def cadastrar():
        print("Cadastrei!")
        time.sleep(2)
        return inicio_opt

    cadastro_opt.append({"entry":"Cadastrar Aluno", "out_opt":cadastrar})
    cadastro_opt.append({"entry":"Editar Aluno", "out_opt":inicio_opt})
    cadastro_opt.append({"entry":"Apagar Aluno", "out_opt":inicio_opt})
    cadastro_opt.append({"entry":"Cadastrar Livro", "out_opt":inicio_opt})
    cadastro_opt.append({"entry":"Editar Livro", "out_opt":inicio_opt})
    cadastro_opt.append({"entry":"Apagar Livro", "out_opt":inicio_opt})
    cadastro_opt.append({"entry":"Voltar", "out_opt":inicio_opt})
    cadastro_opt.append({"entry":"Sair", "out_opt":-1})

    livros_opt.append({"entry":"Procurar Livro", "out_opt":inicio_opt})
    livros_opt.append({"entry":"Ver Livros", "out_opt":inicio_opt})
    livros_opt.append({"entry":"Voltar", "out_opt":inicio_opt})
    livros_opt.append({"entry":"Sair", "out_opt":-1})

    emprestimos_opt.append({"entry":"Buscar Empréstimo", "out_opt":inicio_opt})
    emprestimos_opt.append({"entry":"Ver empréstimos de Aluno", "out_opt":inicio_opt})
    emprestimos_opt.append({"entry":"Ver empréstimo de Livro", "out_opt":inicio_opt})
    emprestimos_opt.append({"entry":"Voltar", "out_opt":inicio_opt})
    emprestimos_opt.append({"entry":"Sair", "out_opt":-1})
    app = Console(inicio_opt)
    app.show()
