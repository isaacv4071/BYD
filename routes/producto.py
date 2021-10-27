import os
import flask
from flask import render_template, session, request, redirect
from database.db import get_db
from forms import SearchForm, ProductForm
from datetime import datetime
from markupsafe import escape

productos = flask.Blueprint('productos', __name__)

#ruta para renderizar la pagina principal de producto
@productos.route("/productos",methods=['GET', 'POST'])
def product():
    if 'usuario' in session:
        form = SearchForm()
        user = session['usuario']
        productos =""
        if form.validate_on_submit():
            search = escape(form.search.data)
            sql = "SELECT idProducts_4,photoProduct_4,nameProduct_4,nameVendor_5 FROM products_4, productVendor_6, vendors_5 WhERE nameProduct_4 LIKE ? AND idProducts_4 = products_4_idProducts_4 AND vendors_5_idVendors_5 = idVendors_5;"
            try:
                con = get_db()
                cur = con.cursor()
                productos = cur.execute(sql, (search+"%",)).fetchall()
                con.commit()
            except:
                con.rollback()
                print("error in operation")
            finally:
                con.close()
            
            if session['rol'] == 1:
                return render_template('superAdmin/product/producto.html', form = form, username = user, productos=productos)
            elif session['rol'] == 2:
                return render_template('admin/product/producto.html', form = form, username = user, productos=productos)
            else: 
                return render_template('endUser/product/producto.html', form = form, username = user, productos=productos)

        sql = "SELECT idProducts_4,photoProduct_4,nameProduct_4,nameVendor_5 FROM products_4, productVendor_6, vendors_5 WhERE idProducts_4 = products_4_idProducts_4 AND vendors_5_idVendors_5 = idVendors_5;"
        try:
            con = get_db()
            cur = con.cursor()
            productos = cur.execute(sql).fetchall()
            con.commit()
        except:
            con.rollback()
            print("error in insert operation")
        finally:
            con.close()
    
        if session['rol'] == 1:
            return render_template('superAdmin/product/producto.html', form = form, username = user, productos=productos)
        elif session['rol'] == 2:
            return render_template('admin/product/producto.html', form = form, username = user, productos=productos)
        else: 
            return render_template('endUser/product/producto.html', form = form, username = user, productos=productos)
    else:
        return render_template('error.html')

@productos.route("/productos/agregar",methods=['GET', 'POST'])
def addproduct():
    if 'usuario' in session:
        user = session['usuario']
        form = ProductForm()
        sql = "SELECT idVendors_5, nameVendor_5 FROM vendors_5"
        try:
            con = get_db()
            cur = con.cursor()
            proveedores = cur.execute(sql).fetchall()
            con.commit()
            form.provider.choices=proveedores
        except:
            con.rollback()
            print("error in operation")
        finally:
            con.close() 

        if session['rol'] == 1:
            return render_template('superAdmin/product/addproduct.html', form = form, username = user)
        elif session['rol'] == 2:
            return render_template('admin/product/addproduct.html', form = form, username = user)
        else: 
             return render_template('error.html')
    else:
        return render_template('error.html')

@productos.route("/producto/<int:id>",methods=['GET', 'POST'])
def viewproduct(id):
    if 'usuario' in session:
        user = session['usuario']
        sql = "SELECT nameProduct_4,nameVendor_5,minimumQuantity_4,availableQuantity_4,descriptionProduct_4, photoProduct_4 FROM products_4,productVendor_6,vendors_5 WHERE idProducts_4 =? AND idProducts_4 = products_4_idProducts_4 AND vendors_5_idVendors_5 = idVendors_5 ;"
        try:
            con = get_db()
            cur = con.cursor()
            producto = cur.execute(sql, (id,)).fetchone()
            con.commit()
        except:
            con.rollback()
            print("error in operation")
        finally:
            con.close() 

        if session['rol'] == 1:
            return render_template('superAdmin/product/productpage.html', username = user, producto=producto)
        elif session['rol'] == 2:
            return render_template('admin/product/productpage.html', username = user, producto=producto)
        else: 
             return render_template('endUser/product/productpage.html', username = user, producto=producto)
    else:
        return render_template('error.html')

@productos.route("/store", methods=["POST"])
def store():
    if 'usuario' in session:
        form = ProductForm()
        name = escape(form.name.data)
        provider = escape(form.provider.data)
        Minimumquantityrequired = escape(form.Minimumquantityrequired.data)
        Quantityavailable = escape(form.Quantityavailable.data)
        Description = escape(form.Description.data)
        _foto = request.files['txtFoto']
        now=datetime.now() #capturar el tiempo actual del sistema
        tiempo=now.strftime("%Y%H%M%S") #formato del tiempo
        if _foto.filename !='':
            nuevoNombreFoto=tiempo+_foto.filename #se da el nuevo nombre de la foto
            _foto.save('uploads/'+nuevoNombreFoto)
        datos = (name, Minimumquantityrequired,Quantityavailable, Description, nuevoNombreFoto)
        sql = "INSERT INTO products_4 (idProducts_4,nameProduct_4,minimumQuantity_4,availableQuantity_4,descriptionProduct_4,photoProduct_4) VALUES (NULL,?,?,?,?,?);"
        sql1 = "SELECT * FROM products_4 WHERE idProducts_4 = (SELECT MAX(idProducts_4) FROM products_4);"
        sql2 = "INSERT INTO productVendor_6 (products_4_idProducts_4, vendors_5_idVendors_5) VALUES (?,?);"
        try:
            con = get_db()
            cur = con.cursor()
            cur.execute(sql, datos)
            con.commit()
            producto = cur.execute(sql1).fetchone()
            con.commit()
            lastid = producto[0]
            data = (lastid, provider)
            cur.execute(sql2, data)
            con.commit()
        except:
            con.rollback()
            print("error in operation")
        finally:
            con.close()
        return redirect('/productos') 
    else:
        return render_template('error.html')

@productos.route("/productos/editar/<int:id>",methods=['GET', 'POST'])
def editproduct(id):
    if 'usuario' in session:
        user = session['usuario']
        form = ProductForm()
        sql = "SELECT nameProduct_4,nameVendor_5,minimumQuantity_4,availableQuantity_4,descriptionProduct_4, photoProduct_4,idVendors_5,idProducts_4  FROM products_4,productVendor_6,vendors_5 WHERE idProducts_4 =? AND idProducts_4 = products_4_idProducts_4 AND vendors_5_idVendors_5 = idVendors_5 ;"
        sql1 = "SELECT idVendors_5, nameVendor_5 FROM vendors_5"
        try:
            con = get_db()
            cur = con.cursor()
            producto = cur.execute(sql, (id,)).fetchone()
            con.commit()
            proveedores = cur.execute(sql1).fetchall()
            con.commit()
        except:
            con.rollback()
            print("error in operation")
        finally:
            con.close() 
  
        form.provider.choices=proveedores  
        form.provider.default = producto[6]
        form.process()
        form.name.data = producto[0]
        form.Minimumquantityrequired.data = producto[2]
        form.Quantityavailable.data = producto[3]
        form.Description.data = producto[4]
        
        if session['rol'] == 1:
            return render_template('superAdmin/product/editproduct.html', form = form, username = user, producto=producto )
        elif session['rol'] == 2:
            return render_template('admin/product/editproduct.html', form = form, username = user, producto=producto)
        else: 
             return render_template('endUser/product/editproduct.html', form = form, username = user, producto=producto)
    else: 
        return render_template('error.html')

@productos.route("/lista",methods=['POST', 'GET'])
def list():
    if 'usuario' in session:
        form = SearchForm()
        user = session['usuario']

        if form.validate_on_submit():
            search = escape(form.search.data)
            sql = "SELECT idProducts_4,photoProduct_4,nameProduct_4,nameVendor_5 FROM products_4, productVendor_6, vendors_5 WhERE nameProduct_4 LIKE ? AND idProducts_4 = products_4_idProducts_4 AND vendors_5_idVendors_5 = idVendors_5;"
            try:
                con = get_db()
                cur = con.cursor()
                productos = cur.execute(sql, (search+"%",)).fetchall()
                con.commit()
            except:
                con.rollback()
                print("error in operation")
            finally:
                con.close()
            
            if session['rol'] == 1:
                return render_template('superAdmin/product/producto.html', form = form, username = user, productos=productos)
            elif session['rol'] == 2:
                return render_template('admin/product/producto.html', form = form, username = user, productos=productos)
            else: 
                return render_template('endUser/product/producto.html', form = form, username = user, productos=productos)

        sql = "SELECT idProducts_4,photoProduct_4,nameProduct_4,nameVendor_5 FROM products_4, productVendor_6, vendors_5 WhERE availableQuantity_4 < minimumQuantity_4 AND idProducts_4 = products_4_idProducts_4 AND vendors_5_idVendors_5 = idVendors_5;"
        try:
            con = get_db()
            cur = con.cursor()
            productos = cur.execute(sql).fetchall()
            con.commit()
        except:
            con.rollback()
            print("error in operation")
        finally:
            con.close()

        if session['rol'] == 1:
            return render_template('superAdmin/product/producto.html', form = form, username = user, productos=productos)
        elif session['rol'] == 2:
            return render_template('admin/product/producto.html', form = form, username = user, productos=productos)
        else: 
            return render_template('endUser/product/producto.html', form = form, username = user, productos=productos)
    else:
        return render_template("error.html")
""" @♥ """