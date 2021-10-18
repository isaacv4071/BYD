import flask
from flask import render_template, redirect, url_for
from forms import SearchForm, ProviderForm

proveedores = flask.Blueprint('proveedores', __name__)

@proveedores.route("/proveedores", methods=['GET', 'POST'])
def provider():
    form = SearchForm()
    if form.validate_on_submit():
        pass
    return render_template('provider/provider.html', form = form)

@proveedores.route("/proveedor/agregar", methods=['GET', 'POST'])
def addProvider():
    form = ProviderForm()
    if form.validate_on_submit():
        pass
    return render_template('provider/addprovider.html',form= form)

@proveedores.route("/proveedor/editar", methods=['GET', 'POST'])
def editProvider():
    form = ProviderForm()
    if form.validate_on_submit():
        pass
    return render_template('provider/editprovider.html',form= form)