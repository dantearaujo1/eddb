"""
    Class that will handle our data management using JSON as the stored
    File
"""
from eddb.util.util import open_json,write_data
from eddb.book.book_interface.book_repository import BookRepository
from eddb.model.livro import Livro

class BookRepositoryConcrete(BookRepository):
    def __init__(self,file):
        self.books = {}
        self.file = file
        # if file:
        #     dados = open_json(file)
        #     for dado_livro in dados["livros"]:
        #         dados_do_livro = dado_livro
        #         livro = Livro(id=dados_do_livro["id"],nome=dados_do_livro["titulo"],autor=dados_do_livro["autor"])
        #         self.livros[livro.id] = livro



    """
    Return a list of dictionary objects that with data
    """
    def get_all(self):
        if self.file:
            json_data = open_json(self.file)
            return json_data["livro"]
        return []
            # for livro in dados["livros"]:
            #     livro_obj = Livro(id=livro["id"],nome=livro["titulo"],autor=livro["autor"])
