+MENUS
 - Deixar o tamanho do terminal fixo (grande) ou avisar o tamanho correto dele para quem vai usar
 - Quando o usuário digita em cima da resposta já escrita, o texto vai sobreescrevendo e não "afastando" o que já tem {cm:2023-07-07}
 - Sempre que o usuário apaga algo que escreveu, começa apagando do fim da escrita, mesmo que o cursor esteja em outra parte do escrito {cm:2023-07-07}
 Menu Principal: {cm:2023-07-13}
- Ta sendo permitido dar loop nas escolhas {cm:2023-07-07}
- Conseguindo ir além da quantidade de opções, provavelmente em todos os menus no modo fullscreen, exceto no mainmenu que tem apenas 4 opções {cm:2023-07-07}

+LIVRO {cm:2023-07-13}
Menu livro {c} {cm:2023-07-08}
    - Quando o tamanho do terminal ta grande (cabendo todas as opções) o usuário consegue ir para além da última opção inferior {cm:2023-07-07}
    - Corrigir Menu de Livros não selecionando o correto após a alteração do menu invertido {cm:2023-07-07}
Submenu Livro Procurar: {cm:2023-07-08} {c}
    - Adicionar opção de voltar para menu livro {cm:2023-07-07}
    - Quando selecionados alguns livros da parte superior da lista  de livro aparece uma opção de livro diferente da selecionada #Bugs {cm:2023-07-08}
Submenu Livro Cadastrar: {c} {cm:2023-07-08}
    - Adicionar opção de voltar para menu livro {cm:2023-07-07}
    - Resultado de add_books mostrando no inicio da tela ao invés do fim {cm:2023-07-07}
    - Ao terminar de adicionar deve voltar para o menu principal da view {cm:2023-07-07}
    - Corrigir exceções das partes de input (backspace, sobrescrever, lef e right...) #Bugs {cm:2023-07-08}
Submenu Livro Editar: {cm:2023-07-08} {c}
    - Adicionar opção de voltar para menu livro {cm:2023-07-07}
    - Corrigir exceções das partes de input (backspace, sobrescrever, lef e right...) #Bugs {cm:2023-07-08}
Submenu Livro Excluir: {cm:2023-07-13} {c}
    - Adicionar opção de voltar para menu livro {cm:2023-07-07}
    - Mudar a mensagem após o usuário cancelar excluir um livro pois está "Erro ao deletar o livro" {cm:2023-07-07}
    - Corrigir o apertar uma tecla duas vezes para subir ou descer para uma vez @book_view {cm:2023-07-04}
    - Corrigir Menu de Livros não selecionando o correto após a alteração do menu invertido {cm:2023-07-04}
    - Corrigir o apertar uma tecla duas vezes para subir ou descer para uma vez @book_view {cm:2023-07-04}
    - Corrigir Menu de Livros não selecionando o correto após a alteração do {cm:2023-07-07}
    - Quando eu excluo um livro, os empréstimos dele ainda continuam existindo no JSON @loan_view (A) {cm:2023-07-07}
    - Corrigir exceções das partes de input na resposta de confirmacao do excluir (backspace, sobrescrever...) @book_view {cm:2023-07-13}
    - Adicionar possibilidade de voltar do menu com alguma tecla #feature {cm:2023-07-13}
    -Quando eu excluo livros, ainda fica aparecendo dentro das opcoes de livro do menu procurar #Bugs {cm:2023-07-13}
    - A busca de livro pelo nome ta dando erro {cm:2023-07-07}
    - Quando apaga mais do que o que escreveu no input ta dando erro #Bugs {cm:2023-07-07}
    - Resultado de get_books mostrando no inicio da tela ao invés do fim {cm:2023-07-07}

+EMPRÉSTIMOS
Menu empréstimo {cm:2023-07-08} {c}
    - Pergunta em cima da borda do menu em buscar empréstimo e fazer empréstimo {cm:2023-07-07}
    - TextInput em cima da borda do menu {cm:2023-07-07}
    - Quando entro no menu emprestimo e volto, e depois entro no meu estudante e vou em Sair, volta pro menu emprestimo e se vou em Voltar, volta pro menu estudante {cm:2023-07-07}
    - Quando o tamanho do terminal ta grande (cabendo todas as opções) o usuário consegue ir para além da última opção inferior #Bugs {cm:2023-07-08}
Submenu Buscar Empréstimo: {c}
    - Adicionar opção de voltar para menu empréstimo {cm:2023-07-07}
    - Quando acessa, a aplicação quebra {cm:2023-07-07}
    - Quando não tiver nenhum empréstimo feito pelo aluno da matrícula que foi passada, deve aparecer tela com mensagem "Esse aluno não fez nenhum empréstimo de livro"
    - Corrigir exceções das partes de input (backspace, sobrescrever, left, right...) {cm:2023-07-13}
Submenu Fazer Empréstimo: {cm:2023-07-13} {c}
    - Adicionar opção de voltar para menu empréstimo {cm:2023-07-07}
    - Na parte de escolher o estudante, quando o tamanho do terminal ta grande (cabendo todas as opções), o usuário consegue ir para além da última opção superior {cm:2023-07-07}
    - Os asteriscos inferiores estão posicionados no lugar errado em todas as partes do fluxo {cm:2023-07-07}
    - Tela de resposta que avisa se o livro está indisponível para fazer emprestimo não sai, e quebra a app se apertar uma tecla {cm:2023-07-07}
    - *Não ta salvando o empréstimo na base de dados* {cm:2023-07-08}
    - Corrigir exceções das partes de input (backspace, sobrescrever, left, right...) {cm:2023-07-13}
Submenu Voltar: {c} {cm:2023-07-08}
    - Quando o usuário passa da última opção inferior, e depois acessa a opcao "Voltar", as vezes a aplicação quebra {cm:2023-07-07}
    - Depois de fazer um empréstimo, quando aperta na opção "Voltar" o usuário é direcionado para fazer um emprestimo de novo, e se fizer esse emprestimo, no final dele, a aplicacao quebra {cm:2023-07-07}
Submenu Devolução: #feature {c}
    - Fazer submenu {cm:2023-07-13}

+ESTUDANTES {cm:2023-07-08} {c}
    - Quando o tamanho do terminal ta grande (cabendo todas as opções) o usuário consegue ir para além da última opção inferior {cm:2023-07-08} #Bugs
Submenu Procurar: {cm:2023-07-08} {c}
    - Quando o usuário digita em cima da resposta já escrita, o texto vai sobreescrevendo e não "afastando" o que já tem #Bugs {cm:2023-07-08}
    - Adicionar opção de voltar para menu estudante #feature {cm:2023-07-08}
    - Os "Textos" das partes de inputs, eram para serem bloqueados {cm:2023-07-08}
    - Quando apaga mais do que o que escreveu no input ta dando erro {cm:2023-07-08}
    - Ajeitar "Aperte Qualquer Teclar para Sair" para "Aperte qualquer tecla para voltar" {cm:2023-07-08}
    - Corrigir exceções das partes de input dos menus (backspace, sobrescrever...) {cm:2023-07-08} Submenu Cadastrar: {c} - Quando o usuário digita em cima da resposta já escrita, o texto vai sobreescrevendo e não "afastando" o que já tem {cm:2023-07-08}
    - Se o ID colocado como input já existir na base de dados, já deve proibir continuar o cadastro #feature
    - Corrigir exceções das partes de input (backspace, sobrescrever, lef e right...) #Bugs {cm:2023-07-08}
        - Quando apaga, a patir do meio, mais do que escreveu, buga #Bugs {cm:2023-07-08}
    - Adicionar opção de voltar para menu estudante {cm:2023-07-07}
Submenu Editar: {cm:2023-07-08} {c}
    - Não está mostrando o primeiro resultado do student {cm:2023-07-04}
    - Corrigir exceções das partes de input (backspace, sobrescrever, lef e right...) #Bugs {cm:2023-07-08}
Submenu Voltar: {c} {cm:2023-07-08}
    - Quando o usuário passa da última opção inferior no menu estudante, e depois acessa a opcao "Voltar", a aplicação vai para a parte de cadastro de estudante {cm:2023-07-08}
Submenu Excluir: {cm:2023-07-13} {c}
    - Navgeação entre as opcoes de estudantes mostradas está louca {cm:2023-07-08}
    - Quando excluo um estudante, os empréstimos dele devem ser apagados da base de dados #feature {cm:2023-07-13}
    - Adicionar opção de voltar para menu estudante {cm:2023-07-07}
    - Os "Textos" das partes de inputs, eram para serem bloqueados {cm:2023-07-08}
    - Quando apaga mais do que o que escreveu no input ta dando erro {cm:2023-07-13}



ÚLTIMO CONFERE

+ Books:
-> Procurar: OK
-> Cadastrar: OK
-> Editar: OK
-> Excluir: OK

+ Students:
-> Procurar: OK
-> Cadastrar: OK
-> Editar: OK
-> Excluir: OK

+ Loans:

-> Procurar:
 - Ta procurando apenas por matrícula do estudante (passar objeto inteiro 'id e nome?') 
 - A lista empréstimo deve o nome dos estudantes e quando acessar o estudante, mostrar os emprestimos ativos e os inativos

-> Emprestar:
 - Não ta aparecendo a lista de livros assim que abre a tela de escolher o livro que vai emprestar, só dps de digitar algo

-> Devolver:
 - Emprestimos inativos não deviam aparecer (A) 
 - Depois que aperta 0 (pagar emprestimo) nao ta descendo total (precisando da o clearscreen)
 - Apertar backspace na hora de procurar ta dando erro) (TypeError: LoanControllerConcrete.get_students() takes 1 positional argument but 3 were given)

 - Para estudantes que não possuem emprestimos, poderia aparecer a tela "O estudante selecionado não possui nenhum empréstimo realizado ou devolvido" #ft
 - Na hnora de cadastrar estudante, se ja estiver cadastro um aluno com a matricula passada, mostrar a tela de "matricula ja cadastrada, tente outra" #ft




- ajeitei as keys do procurar emprestimos
- ajeitei pequenos detalhes dos inputs do menu emprestimo

## DANTE

- Ajeitei apertar enter quando n tem nada selecionado no book_view [TODOS OS
SUBMENUS]
- Ajeitei n ter nenhum dado digitado no cadastrar da book_view
- Ajeitei o caso de n existir arquivo de bando de dados {OK}
