from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from services.usuario_service import buscar_usuario_por_email_service
import bcrypt

auth_bp =  Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():

    dados = request.json

    usuario = buscar_usuario_por_email_service(dados["email"])

    if not usuario:
        return jsonify({"erro":"Usuário não encontrado"}), 404
    
    senha_correta = bcrypt.checkpw(
        dados["senha"].encode("utf-8"),
        usuario["senha"].encode("utf-8")
    )

    if not senha_correta:
        return jsonify({"erro": "Senhaa inválida"}), 401
    
    token = create_access_token(
        identity=usuario["id"]
    )

    return jsonify({"token": token}), 200