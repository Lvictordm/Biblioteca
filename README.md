Sistema de Biblioteca em SQLite

Este projeto é um sistema simples de gerenciamento de livros usando Python e SQLite. Ele permite cadastrar, listar, atualizar a disponibilidade e remover livros de uma biblioteca armazenada em um banco de dados local.

Funcionalidades

Criar uma tabela livros no banco de dados SQLite (biblioteca.db)

Cadastrar novos livros com título, autor, ano de lançamento e status de disponibilidade

Listar todos os livros cadastrados

Atualizar a disponibilidade de um livro (disponível ou não)

Remover livros pelo ID

Menu interativo no console para navegar entre as opções

Tecnologias Utilizadas

Python 3

SQLite3 (biblioteca padrão do Python)

Como usar

Clone o repositório (ou copie o código para um arquivo .py):

git clone <url-do-repositorio>


Execute o script Python:

python biblioteca.py


Menu Interativo

Ao rodar o programa, será exibido um menu com as opções:

Menu biblioteca
1. Cadastrar livro
2. Listar livros
3. Atualizar disponibilidade
4. Remover livro
5. Sair


Digite o número da opção desejada para executar a ação correspondente.

Estrutura do Banco de Dados

Tabela livros com as colunas:

Coluna	Tipo	Descrição
id	INTEGER	Identificador único (autoincrement)
titulo	TEXT	Título do livro (obrigatório)
autor	TEXT	Nome do autor (obrigatório)
ano	INTEGER	Ano de lançamento
disponivel	TEXT	Indica se o livro está disponível ("sim" ou "nao")
Observações Importantes

O banco de dados SQLite (biblioteca.db) será criado automaticamente no mesmo diretório do script, se não existir.

A função de atualização de disponibilidade alterna entre "sim" e "nao".

Ao remover um livro, é necessário informar o ID do livro listado.

Atualmente, o sistema usa entrada pelo console para todas as interações.