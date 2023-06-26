import inspect
from util.util import clear_screen,move_cursor
from readchar import readkey, key
import time
from colorama import Back,Fore

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

    def procurar_livros(self):
        # escolha = self.view.get_input_usuario("Digite um livro: ")
        resposta = ''
        sair = False
        livros = []
        selection = 0
        while not sair:

            titulo = "Digite um livro: " + resposta
            tam_titulo = len(titulo)
            clear_screen()
            self.view.mostrar_mensagem(titulo)
            for i in range(len(livros)):
                if i == selection:
                    print(f"{Back.WHITE}{Fore.BLACK}{i+1}. {livros[i][0].nome}")
                else:
                    print(f"{i+1}. {livros[i][0].nome}")
            move_cursor(tam_titulo+1,0)
            k = readkey()
            if k == key.BACKSPACE:
                resposta = resposta[0:-1]
            elif k == key.ENTER:
                sair = True
            # TODO: Configurar keybinds
            elif k == key.CTRL_J or k == key.CTRL_N:
                # TODO: VIM?
                selection = (selection + 1) % len(livros)
            elif k == key.CTRL_K or k == key.CTRL_P:
                # TODO: VIM?
                selection = (selection - 1) % len(livros)
            else:
                resposta = resposta + k
            livros = self.gerenciador.get_byName(resposta)
            if len(resposta) == 0:
                livros = []
            # input()
        # self.view.mostrar_mensagem(f"Nome: {livros[selection][0].nome}")
        # self.view.mostrar_mensagem(f"Autor: {livros[selection][0].autor}")
        clear_screen()
        self.view.mostrar_detalhes_livros(livros[selection][0])
        time.sleep(10)
