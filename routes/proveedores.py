import flask
from flask import render_template

proveedores = flask.Blueprint('proveedores', __name__)

@proveedores.route("/proveedores", methods=['GET', 'POST'])
def provider():
    return render_template('provider/provider.html')

@proveedores.route("/proveedor/agregar", methods=['GET', 'POST'])
def addProvider():
    return render_template('provider/addprovider.html')

@proveedores.route("/proveedor/editar", methods=['GET', 'POST'])
def editProvider():
    return render_template('provider/editprovider.html')