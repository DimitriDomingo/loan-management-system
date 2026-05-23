# routes/livro_routes.py

from flask import Blueprint, jsonify, request

from services.livro_service import (
    criar_livro_service,
    listar_livros_service
)

livros_bp = Blueprint("livros", __name__)


@livros_bp.route("/livros", methods=["GET"])
def listar_livros():
    livros = listar_livros_service()

    return jsonify(livros), 200


@livros_bp.route("/livros", methods=["POST"])
def adicionar_livro():
    dados = request.json

    try:
        criar_livro_service(dados)

        return jsonify({
            "mensagem": "Livro cadastrado com sucesso"
        }), 201

    except ValueError as erro:
        return jsonify({
            "erro": str(erro)
        }), 400

    except Exception:
        return jsonify({
            "erro": "Erro interno do servidor"
        }), 500