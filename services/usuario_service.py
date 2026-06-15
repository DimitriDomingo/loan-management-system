import bcrypt
from database.connection import conectar
from repositories.usuario_repository import (
    listar_usuarios_,
    criar_usuario_,
    atualizar_usuario_,
    deletar_usuario_,
    buscar_usuario_por_email
)

def buscar_usuario_por_email_service(email):
    conn = conectar()

    try:
        buscar_usuario_por_email(email)

        raise ValueError("Email é obrigatório")
    
    finally:
        conn.close


def listar_usuarios_service():
    conn = conectar()

    try:
        usuarios = listar_usuarios_(conn)

        lista_usuarios = []

        for usuario in usuarios:
            lista_usuarios.append({
                "id": usuario[0],
                "nome": usuario[1]
            })

        return lista_usuarios

    finally:
        conn.close()


def criar_usuario_service(dados):
    nome = dados.get("nome")

    senha_hash = bcrypt.hashpw(dados["senha"].encode("utf-8"),
                               bcrypt.gensalt())
    
    dados["senha"] = senha_hash.decode("utf-8")

    if not nome:
        raise ValueError("Nome é obrigatório")

    conn = conectar()

    try:
        criar_usuario_(conn, dados)

    finally:
        conn.close()


def atualizar_usuario_service(id_usuario, dados):
    nome = dados.get("nome")

    if not nome:
        raise ValueError("Nome é obrigatório")

    conn = conectar()

    try:
        linhas_afetadas = atualizar_usuario_(conn, id_usuario, dados)

        if linhas_afetadas == 0:
            raise ValueError("Usuário não encontrado")

    finally:
        conn.close()


def deletar_usuario_service(id_usuario):
    conn = conectar()

    try:
        linhas_afetadas = deletar_usuario_(conn, id_usuario)

        if linhas_afetadas == 0:
            raise ValueError("Usuário não encontrado")

    finally:
        conn.close()