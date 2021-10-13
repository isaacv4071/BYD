import flask
from flask import render_template

inventario = flask.Blueprint('inventario', __name__)

#ruta para renderizar la pagina principal de inventario
@inventario.route("/inventory", methods=['GET'])
def inventory():
    return render_template('inventory/inventory.html')