from flask import Flask, render_template, request, redirect, session
import database

app = Flask(__name__) 
app.secret_key = "SENHA SECRETA"

@app.route('/')
def index():
    produtos = database.ver_produtos()
    adm=database.localizar_admin(session["email"])
    if adm[0] == 1:
        return redirect("/adm")
    print (adm)
    return render_template('index.html', produtos=produtos, adm=adm)

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
    
@app.route("/comprar_produto/<id>", methods=["GET", "POST"])
def comprar_produto(id):
    if request.method == "POST":
       form = request.form 

    

    

    

if __name__ == "__main__":
    app.run(debug=True)