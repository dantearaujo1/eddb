import time
from colorama import init,Back, Fore
from view.iview import IView
from util.util import clear_screen

init(autoreset=True)

class Console(IView):

    def show(self,menu):
        self.printMenu("Sistema de Biblioteca", menu)

    def sair(self):
        self.mostrar_mensagem("=" * (len("Até logo!")+6))
        self.mostrar_mensagem("|| {} ||".format("Até logo!"))
        self.mostrar_mensagem("=" * (len("Até logo!")+6))
        time.sleep(2)
        clear_screen()

    def get_input_usuario(self,texto):
        return input(texto)

    def printMenu(self,title,menu):
        # print(Style.BRIGHT + Back.BLUE + Fore.WHITE + "=" * (len(title)+6))
        # print(Style.BRIGHT + Back.BLUE + Fore.WHITE + "|| {} ||".format(title))
        # print(Style.BRIGHT + Back.BLUE + Fore.WHITE + "=" * (len(title)+6))
        print("=" * (len(title)+6))
        print("|| {} ||".format(title))
        print("=" * (len(title)+6))
        # Alinhado na direita
        # print("=" * (len(title)+6 - (len(menu["titulo"]))), end='')
        # TODO: Ajeitar o tamanho de forma genérica
        # para que o texto fique centralizado
        print("=" * (len(menu["titulo"])+2), end='')
        print(f" {menu['titulo']} ", end='')
        print("=" * (len(menu["titulo"])+5))
        self.printOptions(menu["opções"])

    def printOptions(self,op):
        for i in range(len(op)):
            print("{}. {}".format(i+1,op[i]["entry"]))
            # print(Back.YELLOW + Fore.BLACK + "{}. {}".format(i+1,op[i]["entry"]))

    def mostrar_mensagem(self,msg):
        print(msg)

    def mostrar_detalhes_livros(self,item):
        title = "Detalhes Livro"
        attrb = item.__dict__
        print("=" * (len(title)+6))
        print(f"|| {title} ||")
        print("=" * (len(title)+6))
        for k,v in attrb.items():
            print(f"{k.capitalize()}: {v}")

    def mostrar_detalhes_usuario(self,item):
        title = "Detalhes Usuário"
        print("=" * (len(title)+6))
        print("|| {} ||".format(title))
        print("=" * (len(title)+6))
        print(f"Nome: {item.nome}")
        print(f"Autor: {item.autor}")

