import flask
from flask import render_template

usuario = flask.Blueprint('usuario', __name__)

#pagina principal de usuarios
@usuario.route("/usuarios", methods=['GET', 'POST'])
def user():
    return render_template('user/UsersPage.html')

#ruta para renderizar la pagina de agregar usuario
@usuario.route("/usuario/agregar", methods=['GET', 'POST'])
def adduser():
    return render_template('user/addUserPage.html')

#ruta para renderizar la pagina de edditar usuario
@usuario.route("/usuario/editar", methods=['GET', 'POST'])
def edituser():
    return render_template('user/editUser.html')

#ruta para renderizar la pagina de usuario
@usuario.route("/usuario", methods=['GET', 'POST'])
def viewuser():
    return render_template('user/UserPage.html')