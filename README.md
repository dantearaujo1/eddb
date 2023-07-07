[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)


# Estrutura de Dados - Gerenciamento Bibliotecário (EDDB)


Esse é um trabalho para a cadeira de Estrutura de Dados do curso de Sistemas e
Mídias Digitais Noturno.


O trabalho visa criar um simples sistema de gerenciamento de biblioteca
utilizando python. O sistema deve ser todo em CLI (Command Line Interface)
mas caso haja tempo, pode-se gerar uma GUI (Graphical User Interface).


## Requisitos Funcionais


| Requisito | Arquivo | COD | Status |
| -------- | ------- | --- | ------ |
| Adicionar Livro | | REQ01 | Concluído |
| Pesquisa Livro por Título | | REQ02 | Concluído |
| Pesquisa Livro por Author | | REQ03 | Concluído |
| Alterar Informações do Livro | | REQ04 | Concluído |
| Remover Livro | | REQ05 | Concluído |
| Adicionar Estudante | | REQ06 | Concluído |
| Pesquisa Estudante por Matrícula | | REQ07 | Concluído |
| Pesquisa Estudante por Nome | | REQ08 | Concluído |
| Alterar Informações do Estudante | | REQ09 | Concluído |
| Remover Estudante | | REQ10 | Concluído |
| Buscar Empréstimo | | REQ11 | Concluído |
| Fazer Empréstimo | | REQ12 | Desenvolvimento |
| Realizar Devolução | | REQ13 | Desenvolvimento |
| Voltar para Menu Principal | | REQ14 | Concluído |
| Sair da Aplicação | | REQ15 | Concluído |

## Instruções de Uso

Entre no diretório raiz

Certifique-se de ter instalado o [ Poetry ]( https://python-poetry.org/docs/ ) para fazer o gerenciamento de pacotes da
aplicação.

```
python -m pip install poetry
```

Após a instalação do poetry, podemos instalar os pacotes necessários para a
utilização da aplicação com:

```
poetry install
```

Em seguida pode rodar a aplicação com o commando:

```
poetry run python eddb/main.py
```

## Teclas que podem ser utilizadas
 - UP (SETA PARA CIMA): para navegar para cima dentre as opções apresentadas
 - DOWN (SETA PARA BAIXO): para navegar para baixo dentre as opções apresentadas
 - RIGHT (SETA PARA DIREITA): para navegar para a direita entre as letras do que você escreveu como resposta
 - LEFT (SETA PARA ESQUERDA): para navegar para a esquerda entre as letras do que você escreveu como resposta
 - ENTER (ENTER): para selecionar a opção que deseja
 - BACKSPACE (APAGAR): para apagar o que você escreveu como resposta


