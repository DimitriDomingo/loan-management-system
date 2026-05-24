from database.connection import conectar

from repositories.emprestimo_repository import (
    listar_emprestimos_,
    buscar_usuario_,
    buscar_livro_,
    criar_emprestimo_,
    devolver_livro_
)


def listar_emprestimos_service():
    conn = conectar()

    try:
        emprestimos = listar_emprestimos_(conn)

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
        raise ValueError("Id do usuário é obrigatório")

    if not id_livro:
        raise ValueError("Id do livro é obrigatório")

    conn = conectar()

    try:
        usuario = buscar_usuario_(conn, id_usuario)

        if usuario is None:
            raise ValueError("Usuário não encontrado")

        livro = buscar_livro_(conn, id_livro)

        if livro is None:
            raise ValueError("Livro não encontrado")

        if livro[0] <= 0:
            raise ValueError("Livro indisponível")

        criar_emprestimo_(conn, dados)

    finally:
        conn.close()


def devolver_livro_service(id_emprestimo):
    conn = conectar()

    try:
        devolvido = devolver_livro_(conn, id_emprestimo)

        if devolvido == 0:
            raise ValueError(
                "Empréstimo não encontrado ou livro já devolvido"
            )

    finally:
        conn.close()