[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)


# Estrutura de Dados - Gerenciamento Bibliotecário (EDDB)


Esse é um trabalho para a cadeira de Estrutura de Dados do curso de Sistemas e
Mídias Digitais Noturno.

Alunos:
Dante de Araújo Clementino - 509015
Débora Samaque Correia Santiago - 511714

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
| Fazer Empréstimo | | REQ12 | Concluído |
| Realizar Devolução | | REQ13 | Concluído |
| Voltar para Menu Principal | | REQ14 | Concluído |
| Sair da Aplicação | | REQ15 | Concluído |

## Teclas que podem ser utilizadas
 - **UP** (SETA PARA CIMA) - **CTRL**-**K** - **CTRL**-**P**: para navegar para cima dentre as opções apresentadas
 - **DOWN** (SETA PARA BAIXO) - **CTRL**-**J** - **CTRL**-**N**: para navegar para baixo dentre as opções apresentadas
 - **RIGHT** (SETA PARA DIREITA): para navegar para a direita entre as letras do que você escreveu como resposta
 - **LEFT** (SETA PARA ESQUERDA): para navegar para a esquerda entre as letras do que você escreveu como resposta
 - **ENTER** (ENTER): para selecionar a opção que deseja
 - **BACKSPACE** (APAGAR): para apagar o que você escreveu como resposta

## Executando o projeto

<center><b>PS: Utilizar no terminal, pois o console da sua IDE talvez não interprete os ANSI
ESCAPE CODE amplamente utilizada na aplicação tornando ela inutilizável!</b></center>

---

## Instruções de Configuração do Projeto para Ambiente de Desenvolvimento

Caso deseje rodar o projeto no seu ambiente de desenvolvimento, você pode
utilizar o poetry ou baixar as dependências do projeto listadas abaixo e
rodar o arquivo main.py

### ANTES DE TUDO CLONE O PROJETO

```zsh
git clone https://github.com/dantearaujo1/eddb.git
cd eddb

```

## Usando o poetry

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
### Usando o pip e requirements.txt (NAO FUNCIONA SE N EXPORTAR O PYTHONPATH, USE O POETRY)
- Link de tutorial em vídeo: https://drive.google.com/file/d/1FC6jm-X1Jae-gsnn2LCJfyVAUB8vXNRw/view?usp=sharing
```zsh
# se vc tiver o pip instalado
pip install -r requirements.txt
# então no terminal vc pode setar seu PYTHONPATH enviroment variable
export PYTHONPATH=$PYTHONPATH:'pwd'
# para executar basta chamar após a instalação
python eddb/main.py
#caso seu terminal use python3
python3 eddb/main.py
```

