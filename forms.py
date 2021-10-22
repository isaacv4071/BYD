from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, SubmitField,IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    name = StringField(label="Usuario", validators=[DataRequired(message="No dejar vacío este campo"), 
    Length(min=3, max=20, message="Su usuario debe tener mas de 3 caracteres")])
    password = PasswordField(label="Contraseña", validators=[DataRequired(message="No dejar vacío este campo"), 
    Length(min=6, max=20, message="Su contraseña debe tener minimo 6 caracteres")])
    submit=SubmitField(label="Iniciar sesión")

class InventoryForm(FlaskForm):
    valor = IntegerField(label="Valor", validators=[DataRequired(message="No dejar vacío este campo")])
    select = SelectField(label="Selección", choices=[(1,"Seleccione una opción"),(2,"producto 1"),
							(3,"producto 2"),(4,"producto 3")], default=1)

class UserForm(FlaskForm):
    name= StringField(label="Nombres", validators=[DataRequired(message="No dejar vacío este campo"), 
    Length(min=3, max=20, message="Su nombre debe tener mas de 3 caracteres")])
    lastname = StringField(label="Apellidos", validators=[DataRequired(message="No dejar vacío este campo"), 
    Length(min=3, max=20, message="Su Apellido debe tener mas de 3 caracteres")])
    Email = EmailField(label="Correo Electronico", validators=[DataRequired(message="No dejar vacío este campo"), 
    Email(message="El correo no cumple con el formato indicado")])
    username = StringField(label="Username", validators=[DataRequired(message="No dejar vacío este campo"), 
    Length(min=3, max=20, message="Su usuario debe tener mas de 3 caracteres")])
    password = PasswordField(label="Contraseña", validators=[DataRequired(message="No dejar vacío este campo"), 
    Length(min=6, max=20, message="Su contraseña debe tener minimo 6 caracteres")])
    role = SelectField(label="role", choices=[(1,"Super Administrador"),
							(2,"Administrador"),(3,"Usuario final")], default=3)

class SearchForm(FlaskForm):
    search = StringField(label="Search", validators=[DataRequired(message="No dejar vacío este campo")])

class ProviderForm(FlaskForm):
    name= StringField(label="Nombres", validators=[DataRequired(message="No dejar vacío este campo"), 
    Length(min=3, max=20, message="Su nombre debe tener mas de 3 caracteres")])
    lastname = StringField(label="Apellidos", validators=[DataRequired(message="No dejar vacío este campo"), 
    Length(min=3, max=20, message="Su apellido debe tener mas de 3 caracteres")])
    telephone = IntegerField(label="Valor", validators=[DataRequired(message="No dejar vacío este campo")])
    Email = EmailField(label="Correo Electronico", validators=[DataRequired(message="No dejar vacío este campo"), 
    Email(message="El correo no cumple con el formato indicado")])

class ProductForm(FlaskForm):
    name = StringField(label="Product", validators=[DataRequired(message="No dejar vacío este campo"), 
    Length(min=3, max=20, message="El nombre del producto debe tener mas de 3 caracteres")])
    provider = SelectField(label="Provider", choices=[(1,'Seleccionar'),(2, 'prooveedor1'), (3, 'prooveedor2'), (4, 'prooveedor3')], default=1)
    Minimumquantityrequired = IntegerField(label="Valor", validators=[DataRequired(message="No dejar vacío este campo")])
    Quantityavailable= IntegerField(label="Quantity", validators=[DataRequired(message="No dejar vacío este campo")])
    Description = TextAreaField('message', validators=[DataRequired()])
    photo = FileField(validators=[FileRequired(message="Por favor suba una foto")])


