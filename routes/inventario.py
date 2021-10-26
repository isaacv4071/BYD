import flask
from flask import render_template, session, request
from werkzeug.utils import redirect
from forms import InventoryForm
from markupsafe import escape
from database.db import get_db

inventario = flask.Blueprint('inventario', __name__)

#ruta para renderizar la pagina principal de inventario
@inventario.route("/inventario", methods=['GET', 'POST'])
def inventory():
    if 'usuario' in session:
        form = InventoryForm()
        user = session['usuario']
        sql = "SELECT idProducts_4, nameProduct_4 FROM products_4 ;"
        sql1= "SELECT idSales_8,nameProduct_4,amountSold_8 FROM sales_8,products_4 WHERE products_4_idProducts_4 = idProducts_4;"
        try:
            con = get_db()
            cur = con.cursor()
            productos = cur.execute(sql).fetchall()
            con.commit()
            ventas = cur.execute(sql1).fetchall()
            con.commit()
        except:
            con.rollback()
            print("error in operation")
        finally:
            con.close()
        
        form.select.choices = productos

        if session['rol'] == 1:
            return render_template('superAdmin/inventory/inventory.html', form = form, username = user, ventas=ventas)
        elif session['rol'] == 2:
            return render_template('admin/inventory/inventory.html', form = form, username = user, ventas=ventas)
        else: 
            return render_template('endUser/inventory/inventory.html', form = form, username = user, ventas=ventas)
    else:
        return render_template('error.html')


@inventario.route('/venta', methods = ['POST'])
def venta():
    if 'usuario' in session:
        form = InventoryForm()
        valor = escape(form.valor.data)
        producto = form.select.data
        sql ="UPDATE products_4 SET availableQuantity_4 = (availableQuantity_4 - ?) WHERE idProducts_4 = ?"
        data = (valor, producto)
        try:
            con = get_db()
            cur = con.cursor()
            cur.execute(sql, data)
            con.commit()
            cur.execute("INSERT INTO sales_8(idSales_8, products_4_idProducts_4, amountSold_8) VALUES (NULL, ?,?)", (producto,valor))
            con.commit()
        except:
            con.rollback()
            print("error in operation")
        finally:
            con.close()
        return redirect('/inventario')
    else:
        return render_template('error.html')