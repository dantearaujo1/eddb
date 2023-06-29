from repository.livros_repository import LivrosRepositoryJSON


def test_add_livro():
    l = LivrosRepositoryJSON("eddb/livros_test.json")
    livros = l.get_all()
    print(livros)
    assert True
