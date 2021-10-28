import flask
from flask import render_template, session, request, redirect
from flask.helpers import flash
from markupsafe import escape
from database.db import get_db
from forms import change_passwordForm
#librerias hash
from werkzeug.security import generate_password_hash, check_password_hash

config = flask.Blueprint('config', __name__)

#Cambiar password
@config.route('/configuracion',methods=["GET", "POST"] )
def change_password():
    if 'usuario' in session:
        form = change_passwordForm()
        user = session['usuario']

        if session['rol'] == 1:
            return render_template('superAdmin/config/configuracion.html', form = form, username = user)
        elif session['rol'] == 2:
            return render_template('admin/config/configuracion.html', form = form, username = user)
        else: 
            return render_template('endUser/config/configuracion.html', form = form, username = user)
    else:
        return render_template('error.html')

@config.route('/changepassword',methods=["POST"])
def change():
    if 'usuario' in session:
        form = change_passwordForm()
        password = escape(form.password.data)
        confirmpassword = escape(form.confirmpassword.data)
        if password != confirmpassword:
            flash('Las contraseñas no coiciden')
            return redirect('/configuracion')
        else:
            sql = "UPDATE user_2 SET passwordUser_2 = ? WHERE iduser_2 = ?"
            has_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
            data = (has_password,session['iduser'])
            try:
                con = get_db()
                cur = con.cursor()
                cur.execute(sql, data)
                con.commit()
            except:
                con.rollback()
                print("error in insert operation")
            finally:
                con.close()
            return redirect('/configuracion')
    else:
        return render_template('error.html')