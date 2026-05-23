# routes/usuario_routes.py

from flask import Blueprint, jsonify, request

from services.usuario_service import (
    listar_usuarios_service,
    adicionar_usuarios_service
)

usuarios_bp = Blueprint("usuarios", __name__)


@usuarios_bp.route("/usuarios", methods=["POST"])
def adicionar_usuario():
    dados = request.json

    try:
        adicionar_usuarios_service(dados)

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


@usuarios_bp.route("/usuarios", methods=["GET"])
def listar_usuarios():
    usuarios = listar_usuarios_service()

    return jsonify(usuarios), 200