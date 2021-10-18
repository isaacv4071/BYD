from flask import Flask
from flask import render_template, redirect, url_for
import os
from routes.proveedores import proveedores
from routes.usuarios import usuario
from routes.inventario import inventario
from routes.producto import productos
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# ruta para renderizar el login
@app.route("/",methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('inventario.inventory'))
    return render_template('index.html', form=form)


app.register_blueprint(productos)
app.register_blueprint(proveedores)
app.register_blueprint(usuario)
app.register_blueprint(inventario)

if __name__ == "__main__":
    app.run(debug=True, port=8000)