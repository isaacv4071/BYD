from flask import Flask
from flask import render_template,request,redirect,url_for,flash
import os

app = Flask(__name__)
app.secret_key=os.urandom(24)

@app.route("/")
def login():
    return render_template('index.html')

@app.route("/producto",methods=['GET'])
def product():
    return render_template('product/producto.html')

@app.route("/user", methods=['GET'])
def adduser():
    """ validaciones del login """
    return render_template('user/addUserPage.html')

@app.route("/inicio", methods=['POST'])
def inicio():
    return render_template('inventory/inventory.html')

@app.route("/inventory", methods=['GET'])
def inventory():
    return render_template('inventory/inventory.html')

@app.route("/provider", methods=['GET'])
def provider():
    return render_template('provider/provider.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)
