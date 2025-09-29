import sqlite3

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

# # #ETAPA 1 - Criando uma tabela no banco chamada de "livros"
# cursor.execute("""
#  CREATE TABLE IF NOT EXISTS livros (
#       id INTEGER PRIMARY KEY AUTOINCREMENT,
#       titulo TEXT NOT NULL,
#       autor TEXT NOT NULL,
#       ano INTEGER,
#       disponivel TEXT NOT NULL
#       )                                 
# """)
# print("tabela criada comm sucesso !")


#Etapa 2 - Inserindo livros no banco de dados
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


#Etapa 3 - Listando Livros
def listar_livros ():
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    if not livros:
        print("nao exite livros")
    else:
        print("lista de livros: ")
        for livro in livros:
            id, titulo, autor, ano, disponivel = livro
            print(f"ID: {id}, titulo: {titulo}, autor: {autor}, ano: {ano}, disponivel{disponivel}")


#Etapa 4 - Atualização de Disponibilidade
def alterar_disponibilidade(id_livros):
    cursor.execute("SELECT disponivel FROM biblioteca WHERE id = ?", {id_livros,})
    resultado = cursor.fetchone()

    disponivel_atual = resultado[0]
    novo_valor = "nao" if disponivel_atual == "sim" else "sim"

    cursor.execute("UPDATE biblioteca SET Disponivel == ? WHERE id =?", [novo_valor, id_livros])
    conexao.commit()
    print(f"Disponibilidade do livro ID {id_livros} alterada para '{novo_valor}'.")


#Etapa 5 - Removendo livros
def remover_livros():
    try:
        id_livro = int(input("Digite o ID do livro que deseja remover: "))
        cursor.execute("DELETE FROM biblioteca WHERE id = ?", {id_livro,})
        conexao.commit()

        if cursor.rowcount > 0: #Para exibir quantas linhas foram deletadas
            print("Livro removido com sucesso !")
        else:
            print("nenhum livro encontrado com esse ID")
    except Exception as erro:
        print(f"erro ao tentar excluir livro {erro}")



#Etapa 6 – Menu Interativo no Console
def menu():
    while True:
        print("\nMenu biblioteca")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Atualizar disponivilidade")
        print("4. Remover livro")
        print("5. Sair")


        opcao = input("Escolha uma opção: ")


        if opcao == "1":
            cadastrar_livros()
        elif opcao ==  "2":
            listar_livros()
        elif opcao == "3":
            try:
                id_livro = int(input("Digite o ID do livro para atualizar disponibilidade: "))
                alterar_disponibilidade(id_livro)
            except ValueError:
                print("ID invalido")
        elif opcao == "5":
            print("saindo")
            break
        else:
            print("opcao invalida")
menu()

        







   
        