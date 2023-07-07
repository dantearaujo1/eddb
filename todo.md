#Menus
 - Deixar o tamanho do terminal fixo (grande) ou avisar o tamanho correto dele para quem vai usar
 - Quando o usuário digita em cima da resposta já escrita, o texto vai sobreescrevendo e não "afastando" o que já tem
 - Sempre que o usuário apaga algo que escreveu, começa apagando do fim da escrita, mesmo que o cursor esteja em outra parte do escrito

+LIVRO #Dante
Menu livro {c}
    - Quando o tamanho do terminal ta grande (cabendo todas as opções) o usuário consegue ir para além da última opção inferior
    - Corrigir Menu de Livros não selecionando o correto após a alteração do menu invertido ?
Submenu Livro Procurar: {c}
    - Adicionar opção de voltar para menu livro
    - Quando selecionados alguns livros da parte superior da lista aparece uma opção de livro diferente da selecionada
Submenu Livro Cadastrar: {c}
    - Adicionar opção de voltar para menu livro
Submenu Livro Editar: {c}
    - Adicionar opção de voltar para menu livro
Submenu Livro Excluir: {c}
    - Adicionar opção de voltar para menu livro
    - Mudar a mensagem após o usuário cancelar excluir um livro pois está "Erro ao deletar o livro"
    - Quando eu excluo um livro, os empréstimos dele ainda continuam existindo no JSON

+EMPRÉSTIMOS #Dante
Menu empréstimo
    - Quando o tamanho do terminal ta grande (cabendo todas as opções) o usuário consegue ir para além da última opção inferior
Submenu Buscar Empréstimo: {c}
    - Adicionar opção de voltar para menu empréstimo
    - Quando acessa, a aplicação quebra
Submenu Fazer Empréstimo: {c}
    - Adicionar opção de voltar para menu empréstimo
    - Na fluxo de fazer empréstimo:
        - Na parte de escolher o estudante, quando o tamanho do terminal ta grande (cabendo todas as opções), o usuário consegue ir para além da última opção superior
        - Os asteriscos inferiores estão posicionados no lugar errado em todas as partes do fluxo
    - Tela de resposta que avisa se o livro está indisponível para fazer emprestimo não sai, e quebra a app se apertar uma tecla
Submenu Voltar:
    - Quando o usuário passa da última opção inferior, e depois acessa a opcao "Voltar", as vezes a aplicação quebra
    - Depois de fazer um empréstimo, quando aperta na opção "Voltar" o usuário é direcionado para fazer um emprestimo de novo, e se fizer esse emprestimo, no final dele, a aplicacao quebra


+USUÁRIO #Debora
    - Quando o tamanho do terminal ta grande (cabendo todas as opções) o usuário consegue ir para além da última opção inferior
Submenu Procurar: {c}
    - Adicionar opção de voltar para menu estudante
    - Os "Textos" das partes de inputs, eram para serem bloqueados 
    - Quando apaga mais do que o que escreveu no input ta dando erro
Submenu Cadastrar: {c}
    - Adicionar opção de voltar para menu estudante
    - Se o ID colocado como input já existir na base de dados, já deve proibir continuar o cadastro
Submenu Editar: {c}
    - Quando o tamanho do terminal ta grande (cabendo todas as opções) o usuário consegue ir para além da última opção superior
Submenu Voltar:
    - Quando o usuário passa da última opção inferior no menu estudante, e depois acessa a opcao "Voltar", a aplicação vai para a parte de cadastro de estudante
Submenu Excluir: 
    - Navgeação entre as opcoes de estudantes mostradas está louca
    - Quando excluo um estudante, os empréstimos dele continuam existindo no JSON
