# routes/emprestimo_routes.py

from flask import Blueprint, jsonify, request

from services.emprestimo_service import (
    listar_emprestimos_service,
    emprestar_service,
    devolver_livro_service
)

emprestimos_bp = Blueprint("emprestimos", __name__)


@emprestimos_bp.route("", methods=["GET"])
def listar_emprestimos():
    emprestimos = listar_emprestimos_service()

    return jsonify(emprestimos), 200


@emprestimos_bp.route("", methods=["POST"])
def emprestar():
    dados = request.json

    try:
        emprestar_service(dados)

        return jsonify({
            "mensagem": "Empréstimo realizado com sucesso"
        }), 201

    except ValueError as erro:
        return jsonify({
            "erro": str(erro)
        }), 400

    except Exception:
        return jsonify({
            "erro": "Erro interno do servidor"
        }), 500


@emprestimos_bp.route("/devolver/<int:id>", methods=["PUT"])
def devolver(id):
    try:
        mensagem = devolver_livro_service(id)

        return jsonify({
            "mensagem": mensagem
        }), 200

    except ValueError as erro:
        return jsonify({
            "erro": str(erro)
        }), 404

    except Exception:
        return jsonify({
            "erro": "Erro interno do servidor"
        }), 500