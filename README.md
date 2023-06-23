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
| Adicionar Livro | | REQ01 | Desenvolvimento |
| Alterar Informações do Livro | | REQ02 | Desenvolvimento |
| Remover Livro | | REQ03 | Desenvolvimento |
| Adicionar Usuário | | REQ04 | Desenvolvimento |
| Alterar Informações do Usuário | | REQ05 | Desenvolvimento |
| Remover Usuário | | REQ06 | Desenvolvimento |
| Realizar Empréstimo | | REQ07 | Desenvolvimento |
| Realizar Devolução | | REQ08 | Análise |
| Pesquisa Livro por Título | | REQ09 | Análise |
| Pesquisa Livro por Author | | REQ10 | Análise |
| Gerar Relatório do Usuário | | REQ11 | Análise |

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


