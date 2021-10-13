import flask
from flask import render_template

proveedores = flask.Blueprint('proveedores', __name__)

@proveedores.route("/provider", methods=['GET'])
def provider():
    return render_template('provider/provider.html')

@proveedores.route("/agregarproveedor", methods=['GET'])
def addProvider():
    return render_template('provider/addprovider.html')