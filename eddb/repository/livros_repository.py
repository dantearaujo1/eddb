from repository.irepository import IRepository
from model.livro import Livro
from util.util import open_json

from fuzzywuzzy import fuzz,process


class LivrosRepositoryJSON(IRepository):
    def __init__(self,file=None):
        self.livros = {}
        if file:
            dados = open_json(file)
            for dado_livro in dados:
                dados_do_livro = dado_livro
                livro = Livro(nome=dados_do_livro["título"],autor=dados_do_livro["autor"])
                self.livros[livro.id] = livro

    def get_byID(self, ID):
        if self.livros[ID]:
            return self.livros[ID]
        else:
            raise Exception("Esse livro não existe")

    def get_byName(self, name):
        query = name
        livros = self.get_all()

        resultado = process.extract(query,livros)
        return resultado

        # for _,livro in self.livros.items():
        #     if livro.nome == name:
        #         return livro
        #     return []
        # raise Exception("Esse livro não existe")

    def delete_byID(self, ID):
        if self.livros[ID]:
            self.livros.pop(ID)
        else:
            raise Exception("Esse livro não existe")

    def delete_byName(self, name):
        for _,livro in self.livros.items():
            if livro.nome == name:
                livro_info = livro["nome"]
                livro.pop(livro_info["id"])
        raise Exception("Esse livro não existe")

    def get_all(self):
        lista = []
        for _, livro in self.livros.items():
            lista.append(livro)
        return lista


    def delete_all(self):
        raise NotImplementedError

    def add(self, item):
        raise NotImplementedError

    def add_all(self, items):
        raise NotImplementedError

class LivrosRepositoryMemória(IRepository):
    def __init__(self,livros=None):
        if not livros:
            self.livros = {}
        else:
            self.livros = livros

    def get_byID(self, ID):
        if self.livros[ID]:
            return self.livros[ID]
        else:
            raise Exception("Esse livro não existe")

    def get_byName(self, name):
        raise NotImplementedError

    def delete_byID(self, ID):
        raise NotImplementedError

    def delete_byName(self, name):
        raise NotImplementedError

    def get_all(self):
        return self.livros

    def delete_all(self):
        raise NotImplementedError

    def add(self, item):
        if not self.livros[item["uuid"]]:
            self.livros[item["uuid"]] = item

    def add_all(self, items):
        raise NotImplementedError
