def listar_usuarios_(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome
        FROM usuarios
    """)

    return cursor.fetchall()


def buscar_usuario_por_email(conn, dados):
    cursor = conn.currsor()

    cursor.execute("""
        SELECT email
        FROM usuarios
        WHERE email = ?
    """, (
        dados["email"],
    ))


def criar_usuario_(conn, dados):
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO usuarios (nome)
        VALUES (?)
    """, (dados["nome"],))

    conn.commit()


def atualizar_usuario_(conn, id_usuario, dados):
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE usuarios
        SET nome = ?
        WHERE id = ?
    """, (
        dados["nome"],
        id_usuario
    ))

    conn.commit()

    return cursor.rowcount


def deletar_usuario_(conn, id_usuario):
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM usuarios
        WHERE id = ?
    """, (id_usuario,))

    conn.commit()

    return cursor.rowcount