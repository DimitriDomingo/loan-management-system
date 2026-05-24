# services/emprestimo_service.py
from database.connection import conectar
from repositories.emprestimo_repository import (
    listar_emprestimos_,
    selecionar_qtd_,
    realizar_emprestimo_,
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
        raise ValueError("ID do usuário é obrigatório")

    if not id_livro:
        raise ValueError("ID do livro é obrigatório")

    conn = conectar()
    try:
        quantidade = selecionar_qtd_(conn, dados)

        if quantidade is None:
            raise ValueError("Livro não encontrado")

        if quantidade[0] <= 0:
            raise ValueError("Livro indisponível")

        realizar_emprestimo_(conn, dados)
    finally:
        conn.close()


def devolver_livro_service(id):
    conn = conectar()
    try:
        atualizados = devolver_livro_(conn, id)

        if atualizados == 0:
            raise ValueError("Empréstimo não encontrado ou já devolvido")

        return "Devolução realizada com sucesso"
    finally:
        conn.close()

        