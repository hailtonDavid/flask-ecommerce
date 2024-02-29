from mercado import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(length=30), nullable= False, unique=True)
    email = db.Column(db.String(length=50), nullable= False, unique=True)
    senha = db.Column(db.String(length=60), nullable= False)
    valor = db.Column(db.Double, nullable= False, default = 5000.00)
    itens = db.relationship('Item', backref='dono_user', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=30), nullable= False, unique=True)
    preco = db.Column(db.Double, nullable= False)
    cod_barra = db.Column(db.String(length=12), nullable= False, unique=True)
    descricao = db.Column(db.String(length=1024), nullable= False, unique=True)
    dono = db.Column(db.Integer, db.ForeignKey('user.id'))    
    
    def __repr__(self) -> str:
        super().__repr__()
        return f"Item {self.nome}" 
    