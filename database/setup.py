from .connection import conectar

def criar_tabelas():
    conn = conectar()
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS livros (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT NOT NULL,
                   autor TEXT NOT NULL,
                   quantidade INTEGER)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                   id INTEGER PRIMARY KEY,
                   nome TEXT NOT NULL,
                   email TEXT UNIQUE NOT NULL,
                   senha TEXT NOT NULL)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS emprestimos (
                   id INTEGER PRIMARY KEY,
                   id_livro INTEGER,
                   id_usuario INTEGER,
                   devolvido INTEGER DEFAULT 0,
                   
                   FOREIGN KEY (id_livro) REFERENCES livros(id),
                   FOREIGN KEY (id_usuario) REFERENCES usuarios(id));""")

    conn.commit()
    conn.close()
