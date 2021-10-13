import flask
from flask import render_template

productos = flask.Blueprint('productos', __name__)

#ruta para renderizar la pagina principal de producto
@productos.route("/producto",methods=['GET'])
def product():
    return render_template('product/producto.html')
