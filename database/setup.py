from .connection import conectar


def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS livros (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT NOT NULL,
                   autor TEXT NOT NULL,
                   quantidade INTEGER)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                   id INTEGER PRIMARY KEY,
                   nome TEXT NOT NULL,
                   matricola TEXT UNIQUE NOT NULL)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS emprestimos (
                   id INTEGER PRIMARY KEY,
                   id_livro INTEGER,
                   id_usuario INTEGER,
                   devolvido INTEGER DEFAULT 0)""")

    conn.commit()
    conn.close()
