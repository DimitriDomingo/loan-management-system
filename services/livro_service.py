from database.connection import conectar

from repositories.livro_repository import (
    criar_livro_,
    listar_livros_,
    atualizar_livro_,
    deletar_livro_
)


def listar_livros_service():
    conn = conectar()

    try:
        livros = listar_livros_(conn)

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

    if quantidade is None:
        raise ValueError("Quantidade é obrigatória")

    conn = conectar()

    try:
        criar_livro_(conn, dados)

    finally:
        conn.close()


def atualizar_livro_service(id_livro, dados):
    titulo = dados.get("titulo")
    autor = dados.get("autor")
    quantidade = dados.get("quantidade")

    if not titulo:
        raise ValueError("Título é obrigatório")

    if not autor:
        raise ValueError("Autor é obrigatório")

    if quantidade is None:
        raise ValueError("Quantidade é obrigatória")

    conn = conectar()

    try:
        linhas_afetadas = atualizar_livro_(conn, id_livro, dados)

        if linhas_afetadas == 0:
            raise ValueError("Livro não encontrado")

    finally:
        conn.close()


def deletar_livro_service(id_livro):
    conn = conectar()

    try:
        linhas_afetadas = deletar_livro_(conn, id_livro)

        if linhas_afetadas == 0:
            raise ValueError("Livro não encontrado")

    finally:
        conn.close()