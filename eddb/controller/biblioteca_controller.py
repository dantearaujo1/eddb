import inspect
import time
from util.util import clear_screen,move_cursor,get_terminal_size
from readchar import readkey, key
from colorama import Back,Fore,Style,init,Cursor
from controller.icontroller import IController
from model.livro import Livro

init(autoreset=True)

class BibliotecaController():
    def __init__(self,view,gerenciador_de_dados,menus):
        self.view = view
        self.menus = menus

        # Menu atual vai funcionar como um stack
        self.current_menu = []
        self.current_menu.append(self.menus[0])
        self.gerenciador = gerenciador_de_dados

    def gerenciar_menu(self):
        while True:
            # Pegando o menu mais recente do stack
            menu = self.current_menu[-1]

            self.view.show(menu)
            input_do_usuario = self.view.get_input_usuario("Selecione uma opção: ")
            try:
                # Subtraio 1 pois estou mostrando as opções começando pelo número
                # 1, mas a lista começa pelo indice 0, então a opcão 1 escolhida
                # no menu retornará o elemento 0 da lista
                opcao_escolhida = int(input_do_usuario) - 1
                if 0 <= opcao_escolhida < len(menu["opções"]):
                    acao = menu["opções"][opcao_escolhida]['próximo']

                    # Nossa ação é uma função devemos de alguma forma padronizar
                    # essa chamada de função para lidar com todos os casos
                    if inspect.isfunction(acao) or inspect.ismethod(acao):
                        clear_screen()
                        acao()

                    # Escolheu a opção de voltar retira o último menu adicionado
                    # da stack assim, no pŕoximo loop será mostrado o menu anterior
                    elif acao == 0:
                        clear_screen()
                        self.current_menu.pop()

                    # Ação -1 = Sair da aplicação
                    # TODO: [REFATORAR] Deviamos por algumas opções em ENUMS ou
                    # CONSTANTES para facilitar a leitura (ao invés de usar num)
                    elif acao == -1:
                        clear_screen()
                        self.view.sair()
                        break

                    # Caso chegue neste caso, nós temos um seguiremos para um
                    # outro menu, portanto nós adicionamos o novo menu no stack
                    # "pilha" e sempre vamos usar o último elemento do stack
                    # para renderizarmos para o usuário
                    else:
                        self.current_menu.append(self.menus[acao-1])
                        clear_screen()
                else:
                    self.view.mostrar_mensagem("Opção Inválida")
            except ValueError:
                self.view.mostrar_mensagem("Input Inválido")

    def iniciar(self):
        self.gerenciar_menu()

    def ver_livros(self):
        livros = self.gerenciador.get_all()
        for i in range(len(livros)):
            self.view.mostrar_mensagem(f"{i}. {livros[i].nome}")
        escolha = self.view.get_input_usuario("Escolha um livro: ")
        escolha = int(escolha)

        if 0 <= escolha < len(livros):
            clear_screen()
            self.view.mostrar_mensagem(f"Nome: {livros[escolha].nome}")
            self.view.mostrar_mensagem(f"Autor: {livros[escolha].autor}")
            input()

    def adicionar_livro(self):
        resposta = ''
        sair = False
        opcoes = ["nome", "autor"]
        dados = []
        selection = 0
        while not sair:

            titulo = f"Digite o {opcoes[selection]} do Livro: " + resposta
            clear_screen()
            print(titulo,end='')
            k = readkey()
            if k == key.BACKSPACE:
                resposta = resposta[0:-1]
            elif k == key.ENTER:
                selection = selection + 1
                dados.append(resposta)
                resposta = ""
                if selection >= len(opcoes):
                    sair = True
            else:
                resposta = resposta + k
        clear_screen()
        livro = Livro(nome=dados[0],autor=dados[1])
        self.gerenciador.add(livro)
        print("Livro adicionado")

    def procurar_livros(self):
        resposta = ''
        sair = False
        livros = []
        selection = 0
        while not sair:

            titulo = "Digite um livro: " + resposta
            tam_titulo = len(titulo)
            p = 0
            clear_screen()
            print(titulo,end='')
            for i in range(len(livros)):
                move_cursor(0,get_terminal_size()[1]-(i+1))
                if i == selection:
                    print(f"{Back.WHITE}{Fore.BLACK}{i+1}. {livros[i][0].nome}{Style.RESET_ALL}",end='')
                else:
                    print(f"{i+1}. {livros[i][0].nome}",end='')
            move_cursor(tam_titulo + 1,get_terminal_size()[1])
            print(titulo,end='')
            # BUG: Era pra ficar na primeira linha no local de digitar o nome do
            # livro
            k = readkey()
            if k == key.BACKSPACE:
                resposta = resposta[0:-1]
            elif k == key.ENTER:
                sair = True
            # TODO: Configurar keybinds
            elif k in (key.CTRL_J, key.CTRL_N):
                selection = (selection + 1) % len(livros)
                p = p - 1
            elif k in (key.CTRL_K, key.CTRL_P):
                selection = (selection - 1) % len(livros)
                p = p + 1
            else:
                resposta = resposta + k
            livros = self.gerenciador.get_by_name(resposta)
            if len(resposta) == 0:
                livros = []
        clear_screen()
        self.view.mostrar_detalhes_livros(livros[selection][0])
        time.sleep(10)

class LivrosController(IController):

    def __init__(self,view,repositorio):
        IController.__init__(self,view,repositorio)

    def run(self):
        while True:
            self.view.display()
    def get(self):
        pass

    def add(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass
