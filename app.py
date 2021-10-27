import os
from flask import Flask, render_template, redirect, url_for, session, send_from_directory, request
from flask.helpers import flash
from datetime import datetime
#databases
from database.db import get_db
#modulos
from routes.proveedores import proveedores
from routes.usuarios import usuario
from routes.inventario import inventario
from routes.producto import productos
from forms import LoginForm, ProductForm
#protencción contra scripts
from markupsafe import escape
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

CARPETA=os.path.join('uploads')
app.config['CARPETA']=CARPETA

@productos.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
    return send_from_directory(app.config['CARPETA'], nombreFoto)

@productos.route("/producto/update", methods = ['POST'])
def update():
    form = ProductForm()
    id = request.form['txtid']
    name = escape(form.name.data)
    provider = form.provider.data
    Minimumquantityrequired = escape(form.Minimumquantityrequired.data)
    Quantityavailable = escape(form.Quantityavailable.data)
    Description = escape(form.Description.data)
    _foto = request.files['txtFoto']
    now=datetime.now() #capturar el tiempo actual del sistema
    tiempo=now.strftime("%Y%H%M%S") #formato del tiempo
    sql ="UPDATE products_4 SET nameProduct_4=?, minimumQuantity_4=?, availableQuantity_4=?, descriptionProduct_4=? WHERE idProducts_4 = ?"
    datos = (name, Minimumquantityrequired, Quantityavailable, Description, id)
    if _foto.filename !='':
        nuevoNombreFoto=tiempo+_foto.filename #se da el nuevo nombre de la foto
        _foto.save('uploads/'+nuevoNombreFoto)
        try:
            con = get_db()
            cur = con.cursor()
            cur.execute("SELECT photoProduct_4 FROM products_4 WHERE idProducts_4 =?", (id,))
            fila=cur.fetchall()
            os.remove(os.path.join(app.config['CARPETA'], fila[0][0]))
            cur.execute("UPDATE products_4 SET photoProduct_4 = ? WHERE idProducts_4 = ?", (nuevoNombreFoto, id))
            con.commit()
        except:
            con.rollback()
            print("error in insert operation")
    try:
        con = get_db()
        cur = con.cursor()
        cur.execute(sql, datos)
        con.commit()
        cur.execute("UPDATE productVendor_6 SET vendors_5_idVendors_5 = ? WHERE products_4_idProducts_4 = ?", (provider, id))
        con.commit()
    except:
        con.rollback()
        print("error in insert operation")
    finally:
        con.close()
    return redirect('/productos')


@productos.route("/producto/destroy/<int:id>", methods=["GET", "POST"])
def destroy(id):
    try:
        con = get_db()
        cur = con.cursor()
        cur.execute("SELECT photoProduct_4 FROM products_4 WHERE idProducts_4 = ?", (id,))
        fila = cur.fetchall()
        os.remove(os.path.join(app.config['CARPETA'], fila[0][0]))
        cur.execute("DELETE FROM products_4 WHERE idProducts_4 = ?", (id,))
        cur.execute("DELETE FROM productVendor_6 WHERE products_4_idProducts_4 = ?", (id,))
        con.commit()
    except:
        con.rollback()
        print("error in operation")
    finally:
        con.close()
    return redirect('/productos')

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
                    flash('Contraseña incorrecta')
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