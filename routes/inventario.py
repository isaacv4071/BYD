import flask
from flask import render_template, session, request
from forms import InventoryForm

inventario = flask.Blueprint('inventario', __name__)

#ruta para renderizar la pagina principal de inventario
@inventario.route("/inventario", methods=['GET', 'POST'])
def inventory():
    if 'usuario' in session:
        form = InventoryForm()
        user = session['usuario']
        if form.validate_on_submit():
            pass

        if session['rol'] == 1:
            return render_template('superAdmin/inventory/inventory.html', form = form, username = user)
        elif session['rol'] == 2:
            return render_template('admin/inventory/inventory.html', form = form, username = user)
        else: 
            return render_template('endUser/inventory/inventory.html', form = form, username = user)
    else:
        return "No tienes permiso pa entra"