from repository.irepository import IRepository
from model.livro import Livro
from util.util import open_json,write_data, get_root
from fuzzywuzzy import process


class LivrosRepositoryJSON(IRepository):
    def __init__(self,file=None):
        self.livros = {}
        self.file = file
        if file:
            dados = open_json(file)
            for dado_livro in dados["livros"]:
                dados_do_livro = dado_livro
                livro = Livro(id=dados_do_livro["id"],nome=dados_do_livro["titulo"],autor=dados_do_livro["autor"])
                self.livros[livro.id] = livro

    def get_by_id(self, ID):
        if self.livros[ID]:
            return self.livros[ID]
        raise Exception("Esse livro não existe")


    def get_by_name(self, name):
        for _, livro in self.livros.items():
            if livro.nome == name:
                return livro

        # Isso aqui mostra as matches n queria por aqui
        # query = name
        # livros = self.get_all()
        #
        # resultado = process.extract(query,livros)
        # return resultado

        # raise Exception("Esse livro não existe")

    def get_all(self):
        lista = []
        for _, livro in self.livros.items():
            lista.append(livro)
        return lista

    def delete_by_id(self, ID):
        if self.livros[ID]:
            self.livros.pop(ID)
        else:
            raise Exception("Esse livro não existe")

    def delete_by_name(self, name):
        for _,livro in self.livros.items():
            if livro.nome == name:
                livro_info = livro["nome"]
                livro.pop(livro_info["id"])
        raise Exception("Esse livro não existe")

    def delete_all(self):
        self.livros.clear()

    def add(self, item):
        if not self.livros.get(item.id):
            self.livros[item.id] = item
            self.save()
            return
        raise Exception("Ja tem esse livro")

    def add_all(self, items):
        for i in items:
            self.add(i)

    def update_by_name(self,name,data):
        livro = self.get_by_name(name)
        livro = data
    def update_by_id(self,ID,data):
        livro = self.get_by_id(ID)
        livro = data
    def update_all(self,data):
        pass

    def save(self):
        if self.file:
            dados = open_json(self.file)
            lista = []
            for _,l in self.livros.items():
                lista.append(vars(l)())
            dados["livros"] = lista
            write_data(self.file,dados)


