import flask
from flask import render_template
from forms import SearchForm, ProductForm

productos = flask.Blueprint('productos', __name__)

#ruta para renderizar la pagina principal de producto
@productos.route("/productos",methods=['GET', 'POST'])
def product():
    form = SearchForm()
    if form.validate_on_submit():
        pass
    return render_template('product/producto.html', form = form)

@productos.route("/productos/agregar",methods=['GET', 'POST'])
def addproduct():
    form = ProductForm()
    if form.validate_on_submit():
        pass
    return render_template('product/addproduct.html', form = form)

@productos.route("/productos/editar",methods=['GET', 'POST'])
def editproduct():
    form = ProductForm()
    form.Description.data='this is my textarea content!'
    if form.validate_on_submit():
        pass
    return render_template('product/editproduct.html', form = form)

@productos.route("/producto",methods=['GET', 'POST'])
def viewproduct():
    return render_template('product/productpage.html')