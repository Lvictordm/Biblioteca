import sqlite3

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

# #ETAPA 1 - Criando uma tabela no banco chamada de "livros"
cursor.execute("""
 CREATE TABLE IF NOT EXISTS livros (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      titulo TEXT NOT NULL,
      autor TEXT NOT NULL,
      ano INTEGER,
      disponivel TEXT NOT NULL
      )                                 
""")
print("tabela criada comm sucesso !")


#Etapa 2 - inserindo livros no banco de dados
def cadastrar_livros ():
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()
    titulo =  input("digite o titulo do livro: ")
    autor = input ("digite o nome do autor: ")
    ano = input ("digite a data de lançamento: ")
    disponivel = ("sim")
    cursor.execute("""
    INSERT INTO livros (titulo, autor, ano, disponivel)
    VALUES (?, ?, ?, ?)                                
    """, 
    (titulo, autor, ano, disponivel))
    conexao.commit()
    conexao.close()
cadastrar_livros()
print("livro cadastrado com sucesso !")


