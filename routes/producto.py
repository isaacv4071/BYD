import flask
from flask import render_template

productos = flask.Blueprint('productos', __name__)

#ruta para renderizar la pagina principal de producto
@productos.route("/productos",methods=['GET'])
def product():
    return render_template('product/producto.html')

@productos.route("/productos/agregar",methods=['GET'])
def addproduct():
    return render_template('product/addproduct.html')

@productos.route("/productos/editar",methods=['GET'])
def editproduct():
    return render_template('product/editproduct.html')

@productos.route("/producto",methods=['GET'])
def viewproduct():
    return render_template('product/productpage.html')