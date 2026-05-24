def listar_livros_(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, titulo, autor, quantidade
        FROM livros
    """)

    return cursor.fetchall()


def criar_livro_(conn, dados):
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO livros (titulo, autor, quantidade)
        VALUES (?, ?, ?)
    """, (dados["titulo"], dados["autor"], dados["quantidade"]))

    conn.commit()
