import sqlite3
from flask import g

def get_db_connection():
    if 'db' not in g:
        g.db = sqlite3.connect("basedatos.db")
        g.db.row_factory = sqlite3.Row
    return g.db

# app/models.py

# Simulación de base de datos en memoria
users_db = [
    {"id": 1, "username": "jorge", "email": "jorge@example.com", "password": "123"},
    {"id": 2, "username": "pepe", "email": "pepe@example.com", "password": "456"}
]