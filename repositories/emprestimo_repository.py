

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


def selecionar_qtd_(conn, dados):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT quantidade
        FROM livros
        WHERE id = ?
    """, (dados["id_livro"],))

    return cursor.fetchone()


def realizar_emprestimo_(conn, dados):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO emprestimos (
            id_usuario,
            id_livro,
            devolvido
        )
        VALUES (?, ?, 0)
    """, (dados["id_usuario"], dados["id_livro"]))

    cursor.execute("""
        UPDATE livros
        SET quantidade = quantidade - 1
        WHERE id = ?
    """, (dados["id_livro"],))

    conn.commit()


def devolver_livro_(conn, id):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id_livro
        FROM emprestimos
        WHERE id = ?
        AND devolvido = 0
    """, (id,))

    livro = cursor.fetchone()
    if livro is None:
        return 0

    cursor.execute("""
        UPDATE emprestimos
        SET devolvido = 1
        WHERE id = ?
    """, (id,))

    cursor.execute("""
        UPDATE livros
        SET quantidade = quantidade + 1
        WHERE id = ?
    """, (livro[0],))

    conn.commit()

    return cursor.rowcount
