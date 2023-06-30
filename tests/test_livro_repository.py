from repository.livros_repository import LivrosRepositoryJSON


def test_add_livro():
    l = LivrosRepositoryJSON("eddb/db_teste.json")
    livros = l.get_all()
    print(livros)
    assert True
