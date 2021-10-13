import flask
from flask import render_template

usuario = flask.Blueprint('usuario', __name__)

#ruta para renderizar la pagina principal de User
@usuario.route("/user", methods=['GET'])
def adduser():
    return render_template('user/addUserPage.html')