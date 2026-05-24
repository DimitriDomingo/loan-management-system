def listar_emprestimos_(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            emprestimos.id,
            usuarios.nome,
            livros.titulo,
            emprestimos.devolvido

        FROM emprestimos

        JOIN usuarios
            ON emprestimos.id_usuario = usuarios.id

        JOIN livros
            ON emprestimos.id_livro = livros.id
    """)

    return cursor.fetchall()


def buscar_usuario_(conn, id_usuario):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id
        FROM usuarios
        WHERE id = ?
    """, (id_usuario,))

    return cursor.fetchone()


def buscar_livro_(conn, id_livro):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT quantidade
        FROM livros
        WHERE id = ?
    """, (id_livro,))

    return cursor.fetchone()


def criar_emprestimo_(conn, dados):
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO emprestimos (id_usuario, id_livro)
        VALUES (?, ?)
    """, (
        dados["id_usuario"],
        dados["id_livro"]
    ))

    cursor.execute("""
        UPDATE livros
        SET quantidade = quantidade - 1
        WHERE id = ?
    """, (dados["id_livro"],))

    conn.commit()


def devolver_livro_(conn, id_emprestimo):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id_livro
        FROM emprestimos
        WHERE id = ?
    """, (id_emprestimo,))

    livro = cursor.fetchone()

    cursor.execute("""
        UPDATE emprestimos
        SET devolvido = 1
        WHERE id = ?
        AND devolvido = 0
    """, (id_emprestimo,))

    if cursor.rowcount == 0:
        return 0

    cursor.execute("""
        UPDATE livros
        SET quantidade = quantidade + 1
        WHERE id = ?
    """, (livro[0],))

    conn.commit()

    return 1