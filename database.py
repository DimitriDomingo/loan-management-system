import sqlite3

def conectar():
    return sqlite3.connect("biblioteca.db")

# FUNÇÃO PARA CRIAR AS TABELAS DO BANCO DE DADOS
def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

# TABELA DOS LIVROS
    cursor.execute("""CREATE TABLE IF NOT EXISTS livros (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT NOT NULL,
                   autor TEXT NOT NULL,
                   quantidade INTEGER)""")

# TABELA DOS USUARIOS    
    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                   id INTEGER PRIMARY KEY,
                   nome TEXT NOT NULL,
                   matricola TEXT UNIQUE NOT NULL)""")

# TABELA DE EMPRESTIMOS    
    cursor.execute("""CREATE TABLE IF NOT EXISTS emprestimos (
                   id INTEGER PRIMARY KEY,
                   id_livro INTEGER,
                   id_usuario INTEGER,
                   devolvido INTEGER DEFAULT 0)""")

    conn.commit()
    conn.close