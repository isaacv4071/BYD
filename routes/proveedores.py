import flask
from flask import render_template, session, request
from forms import SearchForm, ProviderForm

proveedores = flask.Blueprint('proveedores', __name__)

@proveedores.route("/proveedores", methods=['GET', 'POST'])
def provider():
    if 'usuario' in session:
        form = SearchForm()
        user = session['usuario']
        if form.validate_on_submit():
            pass

        if session['rol'] == 1:
            return render_template('superAdmin/provider/provider.html', form = form, username = user)
        elif session['rol'] == 2:
                return render_template('admin/provider/provider.html', form = form, username = user)
        else: 
            return render_template('endUser/provider/provider.html', form = form, username = user)
    else:
        return "no valid"

@proveedores.route("/proveedor/agregar", methods=['GET', 'POST'])
def addProvider():
    if 'usuario' in session:
        form = ProviderForm()
        user = session['usuario']
        if form.validate_on_submit():
            pass

        if session['rol'] == 1:
            return render_template('superAdmin/provider/addprovider.html', form = form, username = user)
        elif session['rol'] == 2:
            return render_template('admin/provider/addprovider.html', form = form, username = user)
        else: 
            return render_template('endUser/provider/addprovider.html', form = form, username = user)
    else: 
        return "no valid"

@proveedores.route("/proveedor/editar", methods=['GET', 'POST'])
def editProvider():
    if 'usuario' in session:
        form = ProviderForm()
        user = session['usuario']
        if form.validate_on_submit():
            pass

        if session['rol'] == 1:
            return render_template('superAdmin/provider/editprovider.html', form = form, username = user)
        elif session['rol'] == 2:
            return render_template('admin/provider/editprovider.html', form = form, username = user)
        else: 
            return render_template('endUser/provider/editprovider.html', form = form, username = user)
    else:
        return "no valid"