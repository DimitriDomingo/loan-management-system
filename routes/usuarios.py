from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from services.usuario_service import (
    listar_usuarios_service,
    criar_usuario_service,
    atualizar_usuario_service,
    deletar_usuario_service
)

usuarios_bp = Blueprint("usuarios", __name__)


@usuarios_bp.route("/usuarios", methods=["GET"])
@jwt_required()
def listar_usuarios():
    usuarios = listar_usuarios_service()

    return jsonify(usuarios), 200


@usuarios_bp.route("/usuarios", methods=["POST"])
@jwt_required()
def adicionar_usuario():
    dados = request.json

    try:
        criar_usuario_service(dados)

        return jsonify({
            "mensagem": "Usuário cadastrado com sucesso"
        }), 201

    except ValueError as erro:
        return jsonify({
            "erro": str(erro)
        }), 400

    except Exception:
        return jsonify({
            "erro": "Erro interno do servidor"
        }), 500


@usuarios_bp.route("/usuarios/<int:id_usuario>", methods=["PUT"])
@jwt_required()
def atualizar_usuario(id_usuario):
    dados = request.json

    try:
        atualizar_usuario_service(id_usuario, dados)

        return jsonify({
            "mensagem": "Usuário atualizado com sucesso"
        }), 200

    except ValueError as erro:
        return jsonify({
            "erro": str(erro)
        }), 400

    except Exception:
        return jsonify({
            "erro": "Erro interno do servidor"
        }), 500


@usuarios_bp.route("/usuarios/<int:id_usuario>", methods=["DELETE"])
@jwt_required()
def deletar_usuario(id_usuario):

    try:
        deletar_usuario_service(id_usuario)

        return jsonify({
            "mensagem": "Usuário deletado com sucesso"
        }), 200

    except ValueError as erro:
        return jsonify({
            "erro": str(erro)
        }), 404

    except Exception:
        return jsonify({
            "erro": "Erro interno do servidor"
        }), 500