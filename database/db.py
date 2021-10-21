import sqlite3
from flask import g

DATABASE = 'E:/Diplomado/Ciclo3/reto/BYD/Empresa.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db