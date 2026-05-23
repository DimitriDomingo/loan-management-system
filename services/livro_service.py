# services/livro_service.py

from database.connection import conectar


def listar_livros_service():
    conn = conectar()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, titulo, autor, quantidade
            FROM livros
        """)

        livros = cursor.fetchall()

        lista_livros = []

        for livro in livros:
            lista_livros.append({
                "id": livro[0],
                "titulo": livro[1],
                "autor": livro[2],
                "quantidade": livro[3]
            })

        return lista_livros

    finally:
        conn.close()


def criar_livro_service(dados):
    titulo = dados.get("titulo")
    autor = dados.get("autor")
    quantidade = dados.get("quantidade")

    if not titulo:
        raise ValueError("Título é obrigatório")

    if not autor:
        raise ValueError("Autor é obrigatório")

    conn = conectar()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO livros (titulo, autor, quantidade)
            VALUES (?, ?, ?)
        """, (titulo, autor, quantidade))

        conn.commit()

    finally:
        conn.close()