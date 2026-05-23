# services/usuario_service.py

from database.connection import conectar


def adicionar_usuarios_service(dados):
    nome = dados.get("nome")
    email = dados.get("email")

    if not nome:
        raise ValueError("Nome é obrigatório")

    if not email:
        raise ValueError("Email é obrigatório")

    conn = conectar()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO usuarios (nome, email)
            VALUES (?, ?)
        """, (nome, email))

        conn.commit()

    finally:
        conn.close()


def listar_usuarios_service():
    conn = conectar()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome, email
            FROM usuarios
        """)

        usuarios = cursor.fetchall()

        lista_usuarios = []

        for usuario in usuarios:
            lista_usuarios.append({
                "id": usuario[0],
                "nome": usuario[1],
                "email": usuario[2]
            })

        return lista_usuarios

    finally:
        conn.close()