# services/usuario_service.py

from database.connection import conectar
from repositories.usuario_repository import (
    adicionar_usuario_,
    listar_usuarios_
)


def adicionar_usuarios_service(dados):
    nome = dados.get("nome")
    email = dados.get("email")

    if not nome:
        raise ValueError("Nome é obrigatório")

    if not email:
        raise ValueError("Email é obrigatório")

    conn = conectar()
    try:
        adicionar_usuario_(conn, dados)
    finally:
        conn.close()


def listar_usuarios_service():
    conn = conectar()
    try:
        usuarios = listar_usuarios_(conn)

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