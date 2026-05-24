def listar_usuarios_(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome, email
        FROM usuarios
    """)

    return cursor.fetchall()


def adicionar_usuario_(conn, dados):
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO usuarios (nome, email)
        VALUES (?, ?)
    """, (dados["nome"], dados["email"]))

    conn.commit()
