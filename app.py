from flask import Flask
from flask import render_template,request,redirect,url_for,flash
import os

app = Flask(__name__)
app.secret_key=os.urandom(24)

# ruta para renderizar el login
@app.route("/")
def login():
    return render_template('index.html')

#ruta para renderizar la pagina principal de producto
@app.route("/producto",methods=['GET'])
def product():
    return render_template('product/producto.html')

#ruta para renderizar la pagina principal de User
@app.route("/user", methods=['GET'])
def adduser():
    return render_template('user/addUserPage.html')

#ruta para inicio de sesión y validacion de credenciales
@app.route("/inicio", methods=['POST'])
def inicio():
    return render_template('inventory/inventory.html')

#ruta para renderizar la pagina principal de inventario
@app.route("/inventory", methods=['GET'])
def inventory():
    return render_template('inventory/inventory.html')

#ruta para renderizar la pagina principal de Proveedores
@app.route("/provider", methods=['GET'])
def provider():
    return render_template('provider/provider.html')

#ruta para agregar proveedores
@app.route("/agregarproveedor", methods=['GET'])
def addProvider():
    return render_template('provider/addprovider.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000)
