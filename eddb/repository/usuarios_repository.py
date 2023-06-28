from repository.irepository import IRepository
from model.usuario import Usuario
from util.util import open_json,write_data
from fuzzywuzzy import process


class UsuarioRepositoryJson(IRepository):
    def __init__(self,file=None):
        self.usuarios = {}
        self.file = file
        if file:
            json = open_json(file)
            for usuario in json["usuários"]:
                usuario_objeto = Usuario(id=usuario["id"],nome=usuario["nome"],sobrenome=usuario["sobrenome"],matricula=usuario["matrícula"])
                self.usuarios[usuario_objeto.id] = usuario_objeto

    def get_by_id(self, ID):
        if self.usuarios[ID]:
            return self.usuarios[ID]
        raise Exception("Esse usuario não existe")


    def get_by_name(self, name):
        for _, usuario in self.usuarios.items():
            if usuario.nome == name:
                return usuario

        # Isso aqui mostra as matches n queria por aqui
        # query = name
        # livros = self.get_all()
        #
        # resultado = process.extract(query,livros)
        # return resultado

        raise Exception("Esse usuario não existe")

    def get_all(self):
        usuarios = []
        for _, usuario in self.usuarios.items():
            usuarios.append(usuario)
        return usuarios

    def delete_by_id(self, ID):
        if self.usuarios[ID]:
            self.usuarios.pop(ID)
        else:
            raise Exception("Esse ID de usuário não existe! Não houve nada para deletar")

    def delete_by_name(self, name):
        for _,usuario in self.usuarios.items():
            if usuario.nome == name:
                usuario_info = usuario["nome"]
                self.usuarios.pop(usuario_info["id"])
        raise Exception("Esse usuário não existe! Não houve nada para deletar")

    def delete_all(self):
        self.usuarios.clear()
        self.save()

    def add(self, item):
        if not self.usuarios.get(item.id):
            self.usuarios[item.id] = item
            self.save()
            return True
        raise Exception("Um usuários com esse id ja existe")

    def add_all(self, items):
        for i in items:
            self.add(i)

    def update_by_name(self,name,data):
        usuario = self.get_by_name(name)
        self.usuarios[usuario.id]
        livro = data

    def update_by_id(self,ID,data):
        pass
        # livro = self.get_by_id(ID)
        # livro = data
    def update_all(self,data):
        pass

    def save(self):
        if self.file:
            dados = open_json(self.file)
            lista = []
            for _,l in self.usuarios.items():
                lista.append(vars(l)())
            dados["usuários"] = lista
            write_data(self.file,dados)
