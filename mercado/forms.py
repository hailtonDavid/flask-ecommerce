from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from mercado.models import User
from mercado import classes

class CadastroForm(FlaskForm):
    def validate_usuario(self, check_user):
        user = User.query.filter_by(usuario=check_user.data).first()
        if user:
            raise ValidationError("Usuário já existe! Cadastre outro nome de usuário.")
    
    def validate_email(self, check_email):
        email = User.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError("E-mail já existe! Cadastre outro e-mail.")
    
    def validate_senha(self, check_senha):
        senha = User.query.filter_by(senha=check_senha.data).first()
        if senha:
            raise ValidationError("Senha já existe! Cadastre outra senha")
        
    usuario = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='E-mail:', validators=[Email(), DataRequired()])
    senha1 = PasswordField(label='Senha:', validators=[Length(min=6), DataRequired()])
    senha2 = PasswordField(label='Confirmação de Senha:', validators=[EqualTo('senha1'), DataRequired()])
    submit = SubmitField(label='Cadastrar')
    
    
class MarcaForm(FlaskForm):
    def validate_nome(self, check_nome):
        retorno, nome = classes.Marcas.get_first(check_nome.data)
        if retorno:
            raise ValidationError("Marca já existe! Cadastre outra marca.")
        
    nome = StringField(label='Nome da Marca:', validators=[Length(min=5, max=60), DataRequired()])
    apelido = StringField(label='Apelido da Marca:', validators=[Length(min=3, max=30), DataRequired()])
    submit = SubmitField(label='Cadastrar')        
