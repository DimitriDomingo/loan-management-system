from flask import Blueprint, jsonify, request
from database.connection import conectar
from models.emprestimo import Emprestimo

emprestimos_bp = Blueprint('emprestimos', __name__)


@emprestimos_bp.route("/emprestimos", methods=["GET"])
def listar_emprestimos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM emprestimos")
    dados = cursor.fetchall()

    emprestimos = [Emprestimo(*E).to_dict() for E in dados]
    conn.close()
    return jsonify(emprestimos)


@emprestimos_bp.route("/emprestimos", methods=["POST"])
def emprestar():
    dados = request.json
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT quantidade FROM livros WHERE id = ?", (dados["id_livro"],))
    livro = cursor.fetchone()

    if not livro or livro[0] <= 0:
        return jsonify({"erro": "Livro indisponível"})
    
    cursor.execute("INSERT INTO emprestimos (id_usuario, id_livro) VALUES (?, ?)", (dados["id_usuario"], dados["id_livro"]))

    cursor.execute("UPDATE livros SET quantidade = quantidade - 1 WHERE id = ?", (dados["id_livro"],))

    conn.commit()
    conn.close()

    return jsonify ({"mensagem": "Emprestimo realizado"})


@emprestimos_bp.route("/emprestimos/<int:id>", methods=["PUT"])
def devolver(id):
    conn = conectar()
    try:
        cursor = conn.cursor()

        cursor.execute("UPDATE emprestimos SET devolvido = 1 WHERE id = ? AND devolvido = 0", (id,))

        if cursor.rowcount == 0:
            return jsonify ({"erro": "Empréstimo não encontrado ou já devolvido"}),404
        
        cursor.execute("SELECT id_livro FROM emprestimos WHERE id = ?", (id,))
        livro = cursor.fetchone()

        cursor.execute("UPDATE livros SET quantidade = quantidade + 1 WHERE id = ?", (livro[0],))

        conn.commit()
        return jsonify ({"mensagem": "Devolução realizada"})
    
    finally:
        conn.close()
