import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def conectar_banco():
    conexao = sqlite3.connect("produtos.db")
    return conexao
    
def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''create table if not exists usuarios
                   (email text primary key,cpf text,senha text, admin integer)''')
    
    cursor.execute('''create table if not exists produtos 
                   (id integer primary key, nome_produto text, imagem_produto text, 
                   descricao text, preco integer)''')
    
    cursor.execute('''create table if not  exists vendas
                    (id integer primary key, produto_id integer, preco interger,
                    pagamento integer, status text, data_e_horario_do_pedido,
                    data_e_horario_de_entrega)''')

    conexao.commit()
    
def criar_usuario (formulario):
    # Verificar se o email já existe no Banco de Dados
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''SELECT COUNT (email) FROM usuarios WHERE email=?''',(formulario['email'],))
    
    quantidade_de_emails_cadastrados = cursor.fetchone()
    
    if(quantidade_de_emails_cadastrados[0] > 0):
        print("LOG: Já existe esse e-mail cadastrado no banco!")
        return False 
    
    cursor.execute('''INSERT INTO usuarios (email, cpf, senha) 
                   VALUES (?, ?, ?)''', (formulario ['email'],
                    formulario['cpf'], generate_password_hash (formulario['senha'],)))
    conexao.commit()
    return True

def verificar_usuario (formulario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''SELECT senha FROM usuarios WHERE email=?''',(formulario['email'],) )
    
    usuario = cursor.fetchone()
    
    if usuario is None:
        return False
        
    else:
        if check_password_hash(usuario[0], (formulario ["senha"])):
            return True
        else:
            return False

def login(formulario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    #Verificando se o e-mail existe no banco de dados
    cursor.execute('''SELECT COUNT(email) FROM usuarios WHERE email=?''',(formulario['email'],))
    conexao.commit()
    
    quantidade_de_emails = cursor.fetchone()
    print(quantidade_de_emails)
    
    #Se o e-mail não estiver cadastrado, retorna False
    
    if quantidade_de_emails[0] == 0:
        print("E-mail não cadastrado! Tente novamente")
        return False
    
    #Obtenha a senha criptografada do usuário no banco
    
    cursor.execute('''SELECT senha FROM usuarios WHERE email=?''', (formulario['email'],))
    conexao.commit()
    senha_criptografada = cursor.fetchone()
    
    #Verificando se a senha fornecida corresponde à senha armazenada
    return check_password_hash(senha_criptografada[0], formulario['senha'])

def permissao_admin(email):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute('''UPDATE usuarios SET admin=? WHERE email=?''', (1, email))
    conexao.commit()
    
def localizar_admin(email):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute('''SELECT admin FROM usuarios WHERE email=?''', (email,))
    return cursor.fetchone()

def criar_produto(formulario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute('''INSERT INTO produtos (nome_produto, imagem_produto, descricao, preco) 
                   VALUES (?, ?, ?, ?)''', (formulario ['nome_produto'],
                    formulario['imagem_produto'],formulario['descricao'], formulario['preco']))
    conexao.commit()
    
def ver_produtos():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute('''SELECT * FROM produtos''')
    return cursor.fetchall()
    

if __name__=="__main__":
    criar_tabelas()
    permissao_admin("dayanealvescox@email.com")