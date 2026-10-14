from database.connection import conectar

def listar_usuarios_(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome
        FROM usuarios
    """)

    return cursor.fetchall()


def buscar_usuario_por_email(conn, email):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM usuarios
        WHERE email = ?
    """, (
        email,
    ))

    return cursor.fetchone()


def criar_usuario_(conn, dados):
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO usuarios (nome, email, senha, tipo)
        VALUES (?,?,?,?)
    """, (dados["nome"], dados["email"], dados["senha"], dados["tipo"],))

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