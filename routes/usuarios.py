import flask
from flask import render_template, redirect, url_for
from flask_wtf import form
from forms import UserForm

usuario = flask.Blueprint('usuario', __name__)

#pagina principal de usuarios
@usuario.route("/usuarios", methods=['GET', 'POST'])
def user():
    return render_template('user/UsersPage.html')

#ruta para renderizar la pagina de agregar usuario
@usuario.route("/usuario/agregar", methods=['GET','POST'])
def adduser():
    form = UserForm()
    if form.validate_on_submit():
        return redirect(url_for('usuario.user'))
    return render_template('user/addUserPage.html', form = form)

#ruta para renderizar la pagina de editar usuario
@usuario.route("/usuario/editar", methods=['GET','POST'])
def edituser():
    form = UserForm()
    if form.validate_on_submit():
        return redirect(url_for('usuario.user'))
    return render_template('user/editUser.html', form = form)

#ruta para renderizar la pagina de usuario
@usuario.route("/usuario", methods=['GET','POST'])
def viewuser():
    return render_template('user/UserPage.html')