import sqlite3

def conectar_banco():
    conexao = sqlite3.connect("produtos.db")
    
def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''create table if not exists usuarios
                   (email text primary key,cpf text,senha text, admin integer)''')
    
    cursor.execute('''create table if not exists produtos 
                   (id integer primary key, nome_produto text, imagem_produto text, 
                   descricao text, preco integer''')
    cursor.execute('''''')
