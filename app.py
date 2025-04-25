from flask import Flask, render_template, request, redirect, session
import database
import datetime

app = Flask(__name__) 
app.secret_key = "SENHA SECRETA"

@app.route('/')
def index():
    sessao = 0 
    produtos = database.ver_produtos()
    if session:
        sessao = 1
        adm=database.localizar_admin(session["email"])
        if adm[0] == 1:
            return redirect("/adm")
        
      
    return render_template('index.html', produtos=produtos, sessao =sessao)

@app.route('/login', methods=["GET", "POST"])
def login():
    render_template('login.html')
    if request.method == "POST":
        form = request.form
        if database.verificar_usuario(form) == True:
            session['email'] = form['email']
            return redirect("/")
        else:
            return redirect("/login")
    else:    
        return render_template('login.html')
    
@app.route('/cadastro', methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        form = request.form
        if database.criar_usuario(form) == True:
            return redirect('/login')
        else:
            return "Ocorreu um erro ao cadastrar usuário"
    else:    
        return render_template('cadastro.html')
    

@app.route("/adm")
def moderador():
    return render_template('moderador.html')

@app.route("/criar_produto", methods=["GET", "POST"])
def criar_produto():
    if request.method == "GET":
        return render_template('criar_produto.html')
    
    form = request.form
    database.criar_produto(form)
    return redirect('/adm')

@app.route("/ver_produto")
def ver_produto():
    produtos=database.ver_produtos()
    print(produtos)
    return render_template('ver_produtos.html', produtos=produtos)

@app.route("/excluir_produto/<id>")
def excluir_produto(id):
    database.excluir_produto(id)
    return redirect('/adm')

@app.route("/editar_produto/<id>", methods=["GET", "POST"])
def editar_produto(id):
    if request.method == "POST":
        form = request.form
        database.editar_produto(form, id)
        return redirect("/adm")
    else:
        produto=database.pegar_produto(id)
        return render_template("editar_produto.html", produto=produto)
    
@app.route("/produto/<id>", methods=["GET", "POST"])
def comprar_produto(id):
    if request.method == "GET":
        produto=database.pegar_produto(id)
        return render_template('comprar_produto.html', produto=produto)
    form = request.form
    status= "Compra efetuada" 
    preco=database.pegar_produto(id)
    data_e_horario_do_pedido = datetime.datetime.now()
    data_e_horario_de_entrega = "Entrega em até três dias úteis."   
    database.comprar_produto(id, preco[4], form, status, data_e_horario_do_pedido, data_e_horario_de_entrega)
    return redirect('/')

    

    

    

if __name__ == "__main__":
    app.run(debug=True)