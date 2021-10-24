from os import name
import flask
from flask import render_template, session, redirect, request
from forms import SearchForm, ProviderForm
from database.db import get_db
#protencción contra scripts
from markupsafe import escape

proveedores = flask.Blueprint('proveedores', __name__)

@proveedores.route("/proveedores", methods=['GET', 'POST'])
def provider():
    if 'usuario' in session:
        form = SearchForm()
        user = session['usuario']
        sql = "SELECT * FROM vendors_5"
        try:
            con = get_db()
            cur = con.cursor()
            proveedores = cur.execute(sql).fetchall()
            con.commit()
        except:
            con.rollback()
            print("error in operation")
        finally:
            con.close() 

        if session['rol'] == 1:
            return render_template('superAdmin/provider/provider.html', form = form, username = user, proveedores=proveedores)
        elif session['rol'] == 2: 
            return render_template('admin/provider/provider.html', form = form, username = user, proveedores=proveedores)
        else:
            return render_template('enduser/provider/provider.html', form = form, username = user, proveedores=proveedores)
    else:
        return render_template('error.html')

@proveedores.route("/proveedor/agregar", methods=['GET', 'POST'])
def addProvider():
    if 'usuario' in session:
        form = ProviderForm()
        user = session['usuario']
        if form.validate_on_submit():
            nit = escape(form.nit.data)
            name = escape(form.name.data)
            lastname = escape(form.lastname.data)
            telephone = escape(form.telephone.data)
            email = escape(form.Email.data)
            datos = (nit,name,lastname,telephone,email)
            sql = "INSERT INTO vendors_5(idVendors_5, nitVendor_5, nameVendor_5, lastnameVendor_5 , emailVendor_5, contactVendor_5) VALUES (NULL,?,?,?,?,?)"
            try:
                con = get_db()
                cur = con.cursor()
                cur.execute(sql, datos)
                con.commit()
            except:
                con.rollback()
                print("error in insert operation")
            finally:
                con.close()
            return redirect('/proveedores')
        if session['rol'] == 1:
            return render_template('superAdmin/provider/addprovider.html', form = form, username = user)
        elif session['rol'] == 2:
            return render_template('admin/provider/addprovider.html', form = form, username = user)
        else:
            return render_template('endUser/provider/addprovider.html', form = form, username = user)
    else: 
        return render_template('error.html')

@proveedores.route("/proveedor/editar/<int:id>", methods=['GET', 'POST'])
def editProvider(id):
    if 'usuario' in session:
        form = ProviderForm()
        user = session['usuario']
        proveedor = ""
        sql = "SELECT * FROM vendors_5 WHERE idVendors_5 = ?"
        try:
            con = get_db()
            cur = con.cursor()
            proveedor = cur.execute(sql, (id,)).fetchone()
            con.commit()
        except:
            con.rollback()
            print("error in insert operation")
        finally:
            con.close()
            
        form.nit.data = proveedor[1]
        form.name.data = proveedor[2]
        form.lastname.data = proveedor[3]
        form.telephone.data = proveedor[4]
        form.Email.data = proveedor[5]

        if session['rol'] == 1:
            return render_template('superAdmin/provider/editprovider.html' ,form = form, username = user, proveedor=proveedor)
        elif session['rol'] == 2:
            return render_template('admin/provider/editprovider.html' ,form = form, username = user, proveedor=proveedor)
        else:
            return render_template('endUser/provider/editprovider.html' ,form = form, username = user, proveedor=proveedor)    
    else:
        return render_template('error.html')


@proveedores.route("/proveedor/destroy/<int:id>", methods = ['POST', 'GET'])
def destroy(id):
    if 'usuario' in session:
        sql = "DELETE FROM vendors_5 WHERE idVendors_5 = ?"
        try:
            con = get_db()
            cur = con.cursor()
            cur.execute(sql, (id,))
            con.commit()
        except:
            con.rollback()
            print("error in operation")
        finally:
            con.close()
        return redirect('/proveedores')
    else:
        return render_template('error.html')


@proveedores.route("/proveedor/<int:id>", methods=["GET", "POST"])
def viewProvider(id):
    if 'usuario' in session:
        user = session['usuario']
        sql="SELECT * FROM vendors_5 WHERE idVendors_5 = ?"
        try:
            con = get_db()
            cur = con.cursor()
            proveedor = cur.execute(sql, (id,)).fetchone()
            con.commit()
        except:
            con.rollback()
            print("error in operation")
        finally:
            con.close()
        
        if session['rol'] == 1:
            return render_template('superAdmin/provider/viewprovider.html', username = user, proveedor=proveedor)
        elif session['rol'] == 2:
            return render_template('admin/provider/viewprovider.html', username = user, proveedor=proveedor)
        else:
            return render_template('endUser/provider/viewprovider.html', username = user, proveedor=proveedor) 
    else:
        return render_template('error.html')


@proveedores.route("/proveedor/update", methods=["POST"])
def update():
    form = ProviderForm()
    id = request.form['txtid']
    nit = escape(form.nit.data)
    name = escape(form.name.data)
    lastname = escape(form.lastname.data)
    telephone = escape(form.telephone.data)
    Email = escape(form.Email.data)
    sql = "UPDATE vendors_5 SET nitVendor_5 =?, nameVendor_5 =?, lastnameVendor_5=?, emailVendor_5=?, contactVendor_5=? WHERE idVendors_5 =?"
    datos = (nit,name,lastname, telephone, Email, id)
    try:
        con = get_db()
        cur = con.cursor()
        cur.execute(sql, datos)
        con.commit()
    except:
        con.rollback()
        print("error in insert operation")
    finally:
        con.close()
    return redirect('/proveedores')