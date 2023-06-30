'''
    Class that will handle our data management using JSON as the stored
    File
'''
from eddb.util.util import open_json,write_data
from eddb.book.book_interface.book_repository import BookRepository

class BookRepositoryConcrete(BookRepository):
    def __init__(self,file):
        self.file = file
        # self.books = {}
        # if file:
        #     dados = open_json(file)
        #     for dado_livro in dados["livros"]:
        #         dados_do_livro = dado_livro
        #         livro = Livro(id=dados_do_livro["id"],nome=dados_do_livro["titulo"],autor=dados_do_livro["autor"])
        #         self.livros[livro.id] = livro

    def __open(self):
        json_data = None
        if self.file:
            json_data = open_json(self.file)
        return json_data

    def get_all(self):
        '''
        Return a list of dictionary objects that with data
        '''
        json_data = self.__open()
        if json_data:
            return json_data["books"]
        return []
            # for livro in dados["livros"]:
            #     livro_obj = Livro(id=livro["id"],nome=livro["titulo"],autor=livro["autor"])

    def add_item(self,item):
        return True

