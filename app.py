from flask import Flask
from flask import render_template,request,redirect,url_for,flash
import os

app = Flask(__name__)
app.secret_key=os.urandom(24)

@app.route("/")
def login():
    return render_template('index.html')

@app.route("/inicio", methods=['POST'])
def adduser():
    return render_template('user/addUserPage.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)