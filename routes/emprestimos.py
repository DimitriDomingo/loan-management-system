from flask import Blueprint, jsonify, request

from services.emprestimo_service import (
    listar_emprestimos_service,
    emprestar_service,
    devolver_livro_service
)

emprestimos_bp = Blueprint("emprestimos", __name__)


@emprestimos_bp.route("/emprestimos", methods=["GET"])
def listar_emprestimos():
    emprestimos = listar_emprestimos_service()

    return jsonify(emprestimos), 200


@emprestimos_bp.route("/emprestimos", methods=["POST"])
def emprestar():
    dados = request.json

    try:
        emprestar_service(dados)

        return jsonify({
            "mensagem": "Livro emprestado com sucesso"
        }), 201

    except ValueError as erro:
        return jsonify({
            "erro": str(erro)
        }), 400

    except Exception:
        return jsonify({
            "erro": "Erro interno do servidor"
        }), 500


@emprestimos_bp.route("/emprestimos/<int:id_emprestimo>", methods=["PUT"])
def devolver_livro(id_emprestimo):

    try:
        devolver_livro_service(id_emprestimo)

        return jsonify({
            "mensagem": "Livro devolvido com sucesso"
        }), 200

    except ValueError as erro:
        return jsonify({
            "erro": str(erro)
        }), 400

    except Exception:
        return jsonify({
            "erro": "Erro interno do servidor"
        }), 500