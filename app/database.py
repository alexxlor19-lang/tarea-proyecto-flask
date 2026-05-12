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
    {"id": 3, "username": "Alex", "email": "alex@example.com", "password": "789"},
    {"id": 4, "username": "Juan", "email": "juan@example.com", "password": "987"}
    {"id": 5, "username": "Pedro", "email": "pedro@example.com", "password": "654"}
]