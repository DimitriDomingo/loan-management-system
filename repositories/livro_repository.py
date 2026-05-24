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


def atualizar_livro_(conn, id_livro, dados):
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE livros
        SET titulo = ?, autor = ?, quantidade = ?
        WHERE id = ?
    """, (
        dados["titulo"],
        dados["autor"],
        dados["quantidade"],
        id_livro
    ))

    conn.commit()

    return cursor.rowcount


def deletar_livro_(conn, id_livro):
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM livros
        WHERE id = ?
    """, (id_livro,))

    conn.commit()

    return cursor.rowcount