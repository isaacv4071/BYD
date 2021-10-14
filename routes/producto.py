import flask
from flask import render_template

productos = flask.Blueprint('productos', __name__)

#ruta para renderizar la pagina principal de producto
@productos.route("/products",methods=['GET'])
def product():
    return render_template('product/producto.html')

@productos.route("/addproducto",methods=['GET'])
def addproduct():
    return render_template('product/addproduct.html')

@productos.route("/editproducto",methods=['GET'])
def editproduct():
    return render_template('product/editproduct.html')

@productos.route("/product",methods=['GET'])
def viewproduct():
    return render_template('product/productpage.html')