📚 Sistema de Biblioteca em SQLite

Um sistema simples de gerenciamento de livros usando Python e SQLite, com funcionalidades para cadastrar, listar, atualizar e remover livros de um banco de dados local.

⚙️ Funcionalidades

📁 Criar a tabela livros no banco de dados SQLite (biblioteca.db)

➕ Cadastrar novos livros (título, autor, ano de lançamento e status de disponibilidade)

📄 Listar todos os livros cadastrados

🔄 Atualizar a disponibilidade de um livro (sim ou nao)

❌ Remover livros pelo ID

🧭 Menu interativo no console para fácil navegação entre opções

🛠️ Tecnologias Utilizadas

🐍 Python 3

🗃️ SQLite3 (biblioteca padrão do Python)

🚀 Como Usar

Clone o repositório (ou copie o código para um arquivo .py):

git clone <url-do-repositorio>


Execute o script Python:

python biblioteca.py

📋 Menu Interativo

Ao executar o script, será exibido um menu como este:

Menu Biblioteca

1. Cadastrar livro
2. Listar livros
3. Atualizar disponibilidade
4. Remover livro
5. Sair


Digite o número da opção desejada para realizar a ação correspondente.

🗄️ Estrutura do Banco de Dados

O sistema utiliza uma tabela chamada livros com as seguintes colunas:

Coluna	Tipo	Descrição
id	INTEGER	Identificador único (autoincrement)
titulo	TEXT	Título do livro (obrigatório)
autor	TEXT	Nome do autor (obrigatório)
ano	INTEGER	Ano de lançamento
disponivel	TEXT	Indica se o livro está disponível (sim ou nao)
📝 Observações Importantes

O banco de dados biblioteca.db será criado automaticamente no mesmo diretório do script, caso não exista.

A função de atualização de disponibilidade alterna entre "sim" e "nao".

Para remover um livro, é necessário informar o ID exibido na listagem.

Todo o sistema é operado via entrada de dados pelo console.

📌 Exemplo de Uso
Digite a opção desejada:
1
Digite o título do livro: Dom Casmurro
Digite o nome do autor: Machado de Assis
Digite o ano de lançamento: 1899
Livro cadastrado com sucesso!

📎 Licença

Este projeto é de uso livre para fins de aprendizado.
