# services/emprestimo_service.py

from database.connection import conectar


def listar_emprestimos_service():
    conn = conectar()

    try:
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

        emprestimos = cursor.fetchall()

        lista_emprestimos = []

        for emprestimo in emprestimos:
            lista_emprestimos.append({
                "id": emprestimo[0],
                "usuario": emprestimo[1],
                "livro": emprestimo[2],
                "devolvido": bool(emprestimo[3])
            })

        return lista_emprestimos

    finally:
        conn.close()


def emprestar_service(dados):
    id_usuario = dados.get("id_usuario")
    id_livro = dados.get("id_livro")

    if not id_usuario:
        raise ValueError("ID do usuário é obrigatório")

    if not id_livro:
        raise ValueError("ID do livro é obrigatório")

    conn = conectar()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT quantidade
            FROM livros
            WHERE id = ?
        """, (id_livro,))

        livro = cursor.fetchone()

        if livro is None:
            raise ValueError("Livro não encontrado")

        if livro[0] <= 0:
            raise ValueError("Livro indisponível")

        cursor.execute("""
            INSERT INTO emprestimos (
                id_usuario,
                id_livro,
                devolvido
            )
            VALUES (?, ?, 0)
        """, (id_usuario, id_livro))

        cursor.execute("""
            UPDATE livros
            SET quantidade = quantidade - 1
            WHERE id = ?
        """, (id_livro,))

        conn.commit()

    finally:
        conn.close()


def devolver_livro_service(id):
    conn = conectar()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE emprestimos
            SET devolvido = 1
            WHERE id = ?
            AND devolvido = 0
        """, (id,))

        if cursor.rowcount == 0:
            raise ValueError(
                "Empréstimo não encontrado ou já devolvido"
            )

        cursor.execute("""
            SELECT id_livro
            FROM emprestimos
            WHERE id = ?
        """, (id,))

        livro = cursor.fetchone()

        cursor.execute("""
            UPDATE livros
            SET quantidade = quantidade + 1
            WHERE id = ?
        """, (livro[0],))

        conn.commit()

        return "Devolução realizada com sucesso"

    finally:
        conn.close()