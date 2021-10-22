import flask
from flask import render_template, redirect, url_for, session
from forms import UserForm
from database.db import get_db
#protencción contra scripts
from markupsafe import escape
#librerias hash
import hashlib
from werkzeug.security import generate_password_hash

usuario = flask.Blueprint('usuario', __name__)

#pagina principal de usuarios
@usuario.route("/usuarios", methods=['GET', 'POST'])
def user():
    if 'usuario' in session:
        user = session['usuario']
        if session['rol'] == 1:
            return render_template('superAdmin/user/UsersPage.html', username = user)
        else: 
            return render_template('admin/user/UsersPage.html', username = user)    
    else: 
        return "no valid" 

#ruta para renderizar la pagina de agregar usuario
@usuario.route("/usuario/agregar", methods=['GET','POST'])
def adduser():
    if 'usuario' in session:
        user = session['usuario']
        form = UserForm()
        if form.validate_on_submit():
            name = escape(form.name.data)
            lastname = escape(form.lastname.data)
            Email = escape(form.Email.data)
            username = escape(form.username.data)
            password = escape(form.password.data)
            role = escape(form.role.data)
            has_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
            datos = (role, name, lastname, Email, username, has_password) 
            sql = "INSERT INTO user_2(iduser_2, rol_3_idRol_3, nameUser_2, lastNameUser_2, emailUser_2, usernameUser_2, passwordUser_2) VALUES (NULL,?,?,?,?,?,?)"
            try:
                con = get_db()
                cur = con.cursor()
                cur.execute(sql, datos)
                con.commit()
            except:
                con.rollback()
                print("error in insert operation")
            finally:
                con.close()
            return redirect('/usuarios')
        
        if session['rol'] == 1:
            return render_template('superAdmin/user/addUserPage.html', username = user, form = form)
        else:
            form.role.choices = [(3,'Usuario final')]
            return render_template('admin/user/addUserPage.html',username = user, form = form)
    else:
        return "no valid"


#ruta para renderizar la pagina de editar usuario
@usuario.route("/usuario/editar", methods=['GET','POST'])
def edituser():
    if 'usuario' in session:
        user = session['usuario']
        form = UserForm()
        if form.validate_on_submit():
            return redirect(url_for('usuario.user'))
        
        if session['rol'] == 1:
            return render_template('superAdmin/user/editUser.html', username = user, form = form)
        else:
            return render_template('admin/user/editUser.html', username = user, form = form)
    else:
        return "no valid"

#ruta para renderizar la pagina de usuario
@usuario.route("/usuario", methods=['GET','POST'])
def viewuser():
    if 'usuario' in session:
        if session['rol'] == 1:
            return render_template('superAdmin/user/UserPage.html', username = user)
        else:
            return render_template('admin/user/UserPage.html', username = user)
    else: 
        return "no valid"
        