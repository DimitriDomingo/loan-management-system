from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from services.livro_service import (
    criar_livro_service,
    listar_livros_service,
    atualizar_livro_service,
    deletar_livro_service
)

livros_bp = Blueprint("livros", __name__)


@livros_bp.route("/livros", methods=["GET"])
def listar_livros():
    livros = listar_livros_service()

    return jsonify(livros), 200


@livros_bp.route("/livros", methods=["POST"])
@jwt_required()
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


@livros_bp.route("/livros/<int:id_livro>", methods=["PUT"])
@jwt_required()
def atualizar_livro(id_livro):
    dados = request.json

    try:
        atualizar_livro_service(id_livro, dados)

        return jsonify({
            "mensagem": "Livro atualizado com sucesso"
        }), 200

    except ValueError as erro:
        return jsonify({
            "erro": str(erro)
        }), 400

    except Exception:
        return jsonify({
            "erro": "Erro interno do servidor"
        }), 500


@livros_bp.route("/livros/<int:id_livro>", methods=["DELETE"])
@jwt_required()
def deletar_livro(id_livro):

    try:
        deletar_livro_service(id_livro)

        return jsonify({
            "mensagem": "Livro deletado com sucesso"
        }), 200

    except ValueError as erro:
        return jsonify({
            "erro": str(erro)
        }), 404

    except Exception:
        return jsonify({
            "erro": "Erro interno do servidor"
        }), 500