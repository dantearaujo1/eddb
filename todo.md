#Menus
 - Deixar o tamanho do terminal fixo (grande) ou avisar o tamanho correto dele para quem vai usar
 - Quando o usuário digita em cima da resposta já escrita, o texto vai sobreescrevendo e não "afastando" o que já tem {cm:2023-07-07}
 - Sempre que o usuário apaga algo que escreveu, começa apagando do fim da escrita, mesmo que o cursor esteja em outra parte do escrito {cm:2023-07-07}

+LIVRO #Dante
Menu livro {c}
    - Quando o tamanho do terminal ta grande (cabendo todas as opções) o usuário consegue ir para além da última opção inferior {cm:2023-07-07}
    - Corrigir Menu de Livros não selecionando o correto após a alteração do menu invertido {cm:2023-07-07}
Submenu Livro Procurar: {c}
    - Adicionar opção de voltar para menu livro {cm:2023-07-07}
    - Quando selecionados alguns livros da parte superior da lista aparece uma opção de livro diferente da selecionada {cm:2023-07-07}
Submenu Livro Cadastrar: {c}
    - Adicionar opção de voltar para menu livro {cm:2023-07-07}
    - Resultado de add_books mostrando no inicio da tela ao invés do fim {cm:2023-07-07}
    - Ao terminar de adicionar deve voltar para o menu principal da view {cm:2023-07-07}
Submenu Livro Editar: {c}
    - Adicionar opção de voltar para menu livro {cm:2023-07-07}
Submenu Livro Excluir: {c}
    - Adicionar opção de voltar para menu livro {cm:2023-07-07}
    - Mudar a mensagem após o usuário cancelar excluir um livro pois está "Erro ao deletar o livro" {cm:2023-07-07}
    - Corrigir o apertar uma tecla duas vezes para subir ou descer para uma vez @book_view {cm:2023-07-04}
    - Corrigir exceções das partes de input dos menus (backspace, sobrescrever...) @book_view {cm:2023-07-04}
    - Corrigir Menu de Livros não selecionando o correto após a alteração do menu invertido {cm:2023-07-04}
    - Corrigir o apertar uma tecla duas vezes para subir ou descer para uma vez @book_view {cm:2023-07-04}
    - Corrigir Menu de Livros não selecionando o correto após a alteração do {cm:2023-07-07}
    - Quando eu excluo um livro, os empréstimos dele ainda continuam existindo no JSON @loan_view (A) {cm:2023-07-07}
    - Corrigir exceções das partes de input dos menus (backspace, sobrescrever...) @book_view
    - Adicionar possibilidade de voltar do menu com alguma tecla #feature
    - A busca de livro pelo nome ta dando erro {cm:2023-07-07}
    - Quando apaga mais do que o que escreveu no input ta dando erro #Bugs {cm:2023-07-07}
    - Resultado de get_books mostrando no inicio da tela ao invés do fim {cm:2023-07-07}

+EMPRÉSTIMOS #Dante
Menu empréstimo
    - Quando o tamanho do terminal ta grande (cabendo todas as opções) o usuário consegue ir para além da última opção inferior
Submenu Buscar Empréstimo: {c}
    - Adicionar opção de voltar para menu empréstimo {cm:2023-07-07}
    - Quando acessa, a aplicação quebra {cm:2023-07-07}
Submenu Fazer Empréstimo: {c}
    - Adicionar opção de voltar para menu empréstimo {cm:2023-07-07}
    - Na parte de escolher o estudante, quando o tamanho do terminal ta grande (cabendo todas as opções), o usuário consegue ir para além da última opção superior {cm:2023-07-07}
    - Os asteriscos inferiores estão posicionados no lugar errado em todas as partes do fluxo {cm:2023-07-07}
    - Tela de resposta que avisa se o livro está indisponível para fazer emprestimo não sai, e quebra a app se apertar uma tecla {cm:2023-07-07}
Submenu Voltar:
    - Quando o usuário passa da última opção inferior, e depois acessa a opcao "Voltar", as vezes a aplicação quebra {cm:2023-07-07}
    - Depois de fazer um empréstimo, quando aperta na opção "Voltar" o usuário é direcionado para fazer um emprestimo de novo, e se fizer esse emprestimo, no final dele, a aplicacao quebra {cm:2023-07-07}

+EMPRÉSTIMOS #Dante
- Pergunta em cima da borda do menu em buscar empréstimo e fazer empréstimo {cm:2023-07-07}
- TextInput em cima da borda do menu {cm:2023-07-07}
- Quando entro no menu emprestimo e volto, e depois entro no meu estudante e vou em Sair, volta pro menu emprestimo e se vou em Voltar, volta pro menu estudante {cm:2023-07-07}

+USUÁRIO #Debora
    - Quando o tamanho do terminal ta grande (cabendo todas as opções) o usuário consegue ir para além da última opção inferior
Submenu Procurar: {c}
    - Adicionar opção de voltar para menu estudante {cm:2023-07-07}
    - Os "Textos" das partes de inputs, eram para serem bloqueados
    - Quando apaga mais do que o que escreveu no input ta dando erro
Submenu Cadastrar: {c}
    - Adicionar opção de voltar para menu estudante {cm:2023-07-07}
    - Se o ID colocado como input já existir na base de dados, já deve proibir continuar o cadastro #feature
Submenu Editar:
    - Não está mostrando o primeiro resultado do student {cm:2023-07-04}
    - Quando vai editar uma coisa escrita no input, ele sobreescreve a palavra que ja tem
Submenu Excluir: OK

+MENUS #Dante
Menu Principal:
    - Ta sendo permitido dar loop nas escolhas {cm:2023-07-07}
- Conseguindo ir além da quantidade de opções, provavelmente em todos os
menus no modo fullscreen, exceto no mainmenu que tem apenas 4 opções {cm:2023-07-07}

+COMPONENTES #Dante
