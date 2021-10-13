from flask import Flask
from flask import render_template
import os
from routes.proveedores import proveedores
from routes.usuarios import usuario
from routes.inventario import inventario
from routes.producto import productos

app = Flask(__name__)
app.secret_key=os.urandom(24)

# ruta para renderizar el login
@app.route("/")
def login():
    return render_template('index.html')

#ruta para inicio de sesión y validacion de credenciales
@app.route("/inicio", methods=['POST'])
def inicio():
    return render_template('inventory/inventory.html')

app.register_blueprint(productos)
app.register_blueprint(proveedores)
app.register_blueprint(usuario)
app.register_blueprint(inventario)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
