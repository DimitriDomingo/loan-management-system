from flask import Blueprint, jsonify, request
from database.connection import conectar
from models.usuario import Usuario

usuarios_bp = Blueprint('usuarios', __name__)


@usuarios_bp.route("/usuarios", methods=["GET"])
def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    dados = cursor.fetchall()

    usuarios = [Usuario(*U).to_dict() for U in dados]
    conn.close()
    return jsonify(usuarios)


@usuarios_bp.route("/usuarios", methods=["POST"])
def adicionar_usuarios():
    dados = request.json

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO usuarios (nome, matricola) VALUES (?, ?)", (dados["nome"], dados["matricola"]))

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "usuário cadastrado"})
