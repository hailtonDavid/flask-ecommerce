from mercado import app
from flask import render_template, redirect, url_for, flash
from mercado.models import Item, User
from mercado.forms import CadastroForm
from mercado.forms import MarcaForm
from mercado import db
from mercado import bancodedados
from mercado import classes

@app.route('/')
def page_home():
    return render_template("home.html")

@app.route('/marcas', methods=['GET', 'POST'])
def page_marcas():
    form = MarcaForm()
    if form.validate_on_submit():
        if (classes.Marcas.inserir(form.nome.data, form.apelido.data)):
            return redirect(url_for('page_produto'))
        else:
            flash(f"Erro ao cadastrar a Marca", category="danger")
            return render_template("marca.html", form=form)
    if form.errors != {}:
        for err in form.errors.values():
            flash(f"Erro ao cadastrar a Marca {err}", category="danger")
    return render_template("marca.html", form=form)

@app.route('/todos')
def page_todos():
    pagina = []
    cidade = []
    estado = []
    data = []
    hora = []
    
    sql = "select campo, cidade, regiao, DATE_FORMAT(datahora, '%d-%m-%Y') aS data, "
    sql = sql + "TIME_FORMAT(datahora,'%r') as hora from clicks "
    sql = sql+ " where datahora >= '2024-02-27 00:00:00' "
    sql = sql+ " and datahora <= '2024-12-31 23:59:59' "
    sql = sql+ " order by regiao, cidade, data, hora, campo, ip;"
    
    myresult = bancodedados.get_sql(sql)

    for x in myresult:
        pagina.append(x[0].replace('"', ""))
        cidade.append(x[1].replace('"', ""))
        estado.append(x[2].replace('"', ""))
        data.append(x[3].replace('"', ""))
        hora.append(x[4].replace('"', ""))    
    
    return render_template(
        "sql.html",
        pagina=pagina,
        cidade=cidade,
        estado=estado,
        data=data,
        hora=hora,
        numero_linhas=len(pagina),
    )
    

@app.route('/produtos')
def page_produto():
    itens = Item.query.all()
    return render_template("produtos.html", itens=itens)

@app.route('/cadastro', methods=['GET', 'POST'])
def page_cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        usuario = User(
            usuario = form.usuario.data,
            email = form.email.data,
            senha = form.senha1.data
        )
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('page_produto'))
    if form.errors != {}:
        for err in form.errors.values():
            flash(f"Erro ao cadastrar usuário {err}", category="danger")
    return render_template("cadastro.html", form=form)
