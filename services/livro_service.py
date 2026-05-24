# services/livro_service.py

from database.connection import conectar
from repositories.livro_repository import (
    criar_livro_,
    listar_livros_
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

    conn = conectar()
    try:
        criar_livro_(conn, dados)
    finally:
        conn.close()
