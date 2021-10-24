import flask
from flask import render_template, session, request
from forms import SearchForm, ProductForm

productos = flask.Blueprint('productos', __name__)

#ruta para renderizar la pagina principal de producto
@productos.route("/productos",methods=['GET', 'POST'])
def product():
    if 'usuario' in session:
        form = SearchForm()
        user = session['usuario']
        if form.validate_on_submit():
            pass
        
        if request.method == 'GET':
            if session['rol'] == 1:
                return render_template('superAdmin/product/producto.html', form = form, username = user)
            elif session['rol'] == 2:
                return render_template('admin/product/producto.html', form = form, username = user)
            else: 
                return render_template('endUser/product/producto.html', form = form, username = user)
    else:
        return render_template('error.html')

@productos.route("/productos/agregar",methods=['GET', 'POST'])
def addproduct():
    if 'usuario' in session:
        user = session['usuario']
        form = ProductForm()
        if form.validate_on_submit():
            pass

        if session['rol'] == 1:
            return render_template('superAdmin/product/addproduct.html', form = form, username = user)
        elif session['rol'] == 2:
            return render_template('admin/product/addproduct.html', form = form, username = user)
        else: 
             return render_template('endUser/product/addproduct.html', form = form, username = user)
    else:
        return render_template('error.html')

@productos.route("/productos/editar",methods=['GET', 'POST'])
def editproduct():
    if 'usuario' in session:
        user = session['usuario']
        form = ProductForm()
        form.Description.data='this is my textarea content!'
        if form.validate_on_submit():
            pass

        if session['rol'] == 1:
            return render_template('superAdmin/product/editproduct.html', form = form, username = user)
        elif session['rol'] == 2:
            return render_template('admin/product/editproduct.html', form = form, username = user)
        else: 
             return render_template('endUser/product/editproduct.html', form = form, username = user)
    else: 
        return render_template('error.html')

@productos.route("/producto",methods=['GET', 'POST'])
def viewproduct():
    if 'usuario' in session:
        user = session['usuario']
        if session['rol'] == 1:
            return render_template('superAdmin/product/productpage.html', username = user)
        elif session['rol'] == 2:
            return render_template('admin/product/productpage.html', username = user)
        else: 
             return render_template('endUser/product/productpage.html', username = user)
    else:
        return render_template('error.html')