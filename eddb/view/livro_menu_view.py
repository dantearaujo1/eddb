from view.iview import IView
from colorama import Back,Fore
from util.util import clear_screen
from readchar import readkey, key
from util.util import route

class ConsoleView(IView):
    def __init__(self,title="Título",options=[]):
        self.selection = 0
        self.title = title
        self.options = options
        self.options.append("Voltar")
        self.options.append("Sair")
        self.title_length = len(self.title)

    def show(self,menu):
        pass

    @route("menu")
    def mostrar_menu_inicial(self):
        clear_screen()
        print((self.title_length+2) * "=")
        print(f"|{self.title}|")
        print((self.title_length+2) * "=")
        for i in range(len(self.options)):
            if(i == self.selection):
                print(f"{Back.WHITE}{Fore.BLACK}{self.options[i]}")
            else:
                print(f"{self.options[i]}")

    def pegar_input(self):
        k = readkey()
        if k in (key.CTRL_J,key.CTRL_N):
            self.selection = self.selection + 1
        elif k in (key.CTRL_K,key.CTRL_P):
            self.selection = self.selection - 1
        elif k in (key.CTRL_D):
            return True
        elif k in (key.CTRL_E):
            return "Test"
        self.selection = self.selection % len(self.options)

    def get_livro_add_input(self):
        resposta = ''
        sair = False
        opcoes = ["nome", "autor"]
        dados = []
        opcao_atual = 0
        while not sair:
            titulo = f"Digite o {opcoes[opcao_atual]} do Livro: " + resposta
            clear_screen()
            print(titulo,end='')
            k = readkey()
            if k == key.BACKSPACE:
                resposta = resposta[0:-1]
            elif k == key.ENTER:
                opcao_atual = opcao_atual + 1
                dados.append(resposta)
                resposta = ""
                if selection >= len(opcoes):
                    sair = True
            else:
                resposta = resposta + k
        clear_screen()
        livro = Livro(nome=dados[0],autor=dados[1])
        return livro
        print("Livro adicionado")


    def sair(self):
        pass

