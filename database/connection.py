import sqlite3

def conectar():
    """Retorna uma conexão com o banco de dados SQLite."""
    return sqlite3.connect("biblioteca.db")
