from view.menu_view import MenuView
from controller.biblioteca_controller import BibliotecaController
from repository.livros_repository import LivrosRepositoryJSON
from repository.usuarios_repository import UsuarioRepositoryJson


from gerenciado_de_biblioteca import GerenciadorBibliotecario

from util.util import get_root

def main():
    cadastro_opt = []
    livros_opt = []
    emprestimos_opt = []
    inicio_opt = []

    inicio_opt.append({"entry": "Menu Livros", "próximo": 4})
    inicio_opt.append({"entry": "Menu Empréstimos", "próximo": 5})
    inicio_opt.append({"entry": "Menu Cadastro", "próximo": 2})
    inicio_opt.append({"entry": "Sair", "out_opt": -1, "próximo": -1})

    cadastro_opt.append({"entry": "Cadastrar Aluno", "próximo": 6})
    cadastro_opt.append({"entry": "Editar Aluno", "próximo": 7})
    cadastro_opt.append({"entry": "Apagar Aluno", "próximo": 8})
    cadastro_opt.append({"entry": "Cadastrar Livro", "próximo": 9})
    cadastro_opt.append({"entry": "Editar Livro", "próximo": 10})
    cadastro_opt.append({"entry": "Apagar Livro", "próximo": 11})
    cadastro_opt.append({"entry": "Voltar", "próximo": 0})
    cadastro_opt.append({"entry": "Sair", "próximo": -1})

    livros_opt.append({"entry": "Pesquisar Livro", "próximo": 12})
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

    # db_path = get_root(__file__) + "/livros.json"
    # repo = LivrosRepositoryJSON(db_path)
    # urepo = UsuarioRepositoryJson(db_path)
    # view = MenuView()
    #
    # controller = BibliotecaController(view, repo, menus)
    # app = GerenciadorBibliotecario(view,controller,repo)
    #
    #
    # livros_opt[1]["próximo"] = controller.ver_livros
    # livros_opt[0]["próximo"] = controller.procurar_livros
    # cadastro_opt[3]["próximo"] = controller.adicionar_livro
    # app.mostrar()

    # TESTES
    # from view.livro_menu_view import ConsoleView
    # from controller.concrete_controller import ConcreteController
    from book.book_composer import BookComposer
    from student.student_composer import StudentComposer
    from loan.loan_composer import LoanComposer
    from book.book_repository_concrete import BookRepositoryConcrete
    # view2 = ConsoleView("Início",["Menu Livros","Menu Empréstimo", "Menu Usuarios"])
    #
    # c = ConcreteController(view2,repo)
    print(BookRepositoryConcrete("eddb/livros.json").get_all())
    print(BookComposer.create())



    # print(urepo.usuarios)
    # print(urepo.usuarios['0'])
    # print(urepo.get_by_name("Dante"))
    # print(urepo.get_all())
    # controller.adicionar_livro()
    # l = LivroMenuView()
    # l.run()

if __name__ == "__main__":
    main()
