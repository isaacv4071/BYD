import flask
from flask import render_template, redirect, session, request
from forms import UserForm
from database.db import get_db
#protencción contra scripts
from markupsafe import escape
#librerias hash
from werkzeug.security import generate_password_hash, check_password_hash

usuario = flask.Blueprint('usuario', __name__)

#pagina principal de usuarios
@usuario.route("/usuarios", methods=['GET', 'POST'])
def user():
    if 'usuario' in session:
        user = session['usuario']
        usuarios=""
        if session['rol'] == 1:
            sql = "SELECT * FROM user_2"
            try:
                con = get_db()
                cur = con.cursor()
                usuarios = cur.execute(sql).fetchall()
                con.commit()
            except:
                con.rollback()
                print("error in operation")
            finally:
                con.close()

            return render_template('superAdmin/user/UsersPage.html', username = user, usuarios=usuarios)
        else:
            sql = "SELECT * FROM user_2 WHERE rol_3_idRol_3 = ?"
            try:
                con = get_db()
                cur = con.cursor()
                usuarios = cur.execute(sql, (3,)).fetchall()
                con.commit()
            except:
                con.rollback()
                print("error in operation")
            finally:
                con.close()

            return render_template('admin/user/UsersPage.html', username = user, usuarios=usuarios)
    else: 
        return render_template('error.html') 

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
        return render_template('error.html')


#ruta para renderizar la pagina de editar usuario
@usuario.route("/usuario/editar/<int:id>", methods=['GET','POST'])
def edituser(id):
    if 'usuario' in session:
        form = UserForm()
        user = session['usuario']
        sql1="SELECT * FROM user_2, rol_3 WHERE user_2.iduser_2 = ? and user_2.rol_3_idRol_3 = rol_3.idRol_3;"
        try:
            con = get_db()
            cur = con.cursor()
            usuario = cur.execute(sql1, (id,)).fetchone()
            con.commit()
        except:
            con.rollback()
            print("error in insert operation")
        finally:
            con.close()

        form.role.default = usuario[1]
        form.process()
        form.name.data = usuario[2]
        form.lastname.data = usuario[3]
        form.Email.data = usuario[4]
        form.username.data = usuario[5]
            
        if session['rol'] == 1:
            return render_template('superAdmin/user/editUser.html', username = user, form = form, usuario=usuario)
        else:
            return render_template('admin/user/editUser.html', username = user, form = form, usuario=usuario)
    else:
        return render_template('error.html')


@usuario.route("/usuario/update", methods=['POST'])
def updates():
    form = UserForm()
    id = request.form['txtid']
    name = escape(form.name.data)
    lastname = escape(form.lastname.data)
    Email = escape(form.Email.data)
    username = escape(form.username.data)
    role = escape(form.role.data)
    sql = "UPDATE user_2 SET rol_3_idRol_3 =?, nameUser_2=?, lastNameUser_2=?, emailUser_2=?, usernameUser_2=? WHERE iduser_2 = ?"
    datos = (role, name, lastname, Email, username, id)
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

#ruta para renderizar la pagina de usuario
@usuario.route("/usuario/<int:id>", methods=['GET','POST'])
def viewuser(id):
    if 'usuario' in session:
        user = session['usuario']
        sql = "SELECT * FROM user_2, rol_3 WHERE user_2.iduser_2 = ? and user_2.rol_3_idRol_3 = rol_3.idRol_3;"
        try:
            con = get_db()
            cur = con.cursor()
            usuario = cur.execute(sql, (id,)).fetchone()
            con.commit()
        except:
            con.rollback()
            print("error in operation")
        finally:
            con.close()

        if session['rol'] == 1:
            return render_template('superAdmin/user/UserPage.html', username = user, usuario=usuario)
        else:
            return render_template('admin/user/UserPage.html', username = user, usuario=usuario)
    else: 
        return render_template('error.html')

@usuario.route("/usuario/destroy/<int:id>", methods = ['POST', 'GET'])
def destroy(id):
    if 'usuario' in session:
        sql = "DELETE FROM user_2 WHERE iduser_2 = ?"
        try:
            con = get_db()
            cur = con.cursor()
            usuario = cur.execute(sql, (id,))
            con.commit()
        except:
            con.rollback()
            print("error in operation")
        finally:
            con.close()
        return redirect('/usuarios')
    else:
        return render_template('error.html')