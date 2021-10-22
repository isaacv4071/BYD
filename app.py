import os
from flask import Flask
from flask import render_template, redirect, url_for, session
from flask.helpers import flash
#databases
from database.db import get_db
#modulos
from routes.proveedores import proveedores
from routes.usuarios import usuario
from routes.inventario import inventario
from routes.producto import productos
from forms import LoginForm
#protencción contra scripts
from markupsafe import escape
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# ruta para renderizar el login
@app.route("/", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = escape(form.name.data)
        password = escape(form.password.data)
        sql = "SELECT passwordUser_2, rol_3_idRol_3 FROM user_2 WHERE usernameUser_2=?"
        try:
            con = get_db()
            cur = con.cursor()
            consulta = cur.execute(sql, [user]).fetchone()
            if consulta != None:
                has_password = consulta[0]
                rol = consulta[1]
                if check_password_hash(has_password, password):
                    session['usuario']= user
                    session['rol'] = rol
                    return redirect(url_for('inventario.inventory'))
                else:
                    flash('Invalid password')
            else:
                flash('El usuario no esta registrado')
        except:
            con.rollback()
            print("error in operation")
        finally:
            con.close()    
            
    return render_template('index.html', form=form)

@app.route('/logout')
def logout():
    if 'usuario' in session:
        session.clear()
    return redirect(url_for('login'))


app.register_blueprint(productos)
app.register_blueprint(proveedores)
app.register_blueprint(usuario)
app.register_blueprint(inventario)

if __name__ == "__main__":
    app.run(debug=True, port=8000)