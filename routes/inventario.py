import flask
from flask import render_template, redirect
from forms import InventoryForm

inventario = flask.Blueprint('inventario', __name__)

#ruta para renderizar la pagina principal de inventario
@inventario.route("/inventario", methods=['GET', 'POST'])
def inventory():
    form = InventoryForm()
    if form.validate_on_submit():
        return redirect("/inventario")
    return render_template('inventory/inventory.html', form = form)