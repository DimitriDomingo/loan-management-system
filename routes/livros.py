from flask import Blueprint, jsonify, request
from database.connection import conectar
from models.livro import Livro

livros_bp = Blueprint('livros', __name__)


@livros_bp.route("/livros", methods=["GET"])
def listar_livros():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")
    dados = cursor.fetchall()

    livros = [Livro(*I).to_dict() for I in dados]
    conn.close()
    return jsonify(livros)


@livros_bp.route("/livros", methods=["POST"])
def adicionar_livros():
    dados = request.json

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO livros (titulo, autor, quantidade) VALUES (?, ?, ?)", (dados["titulo"], dados["autor"], dados["quantidade"]))

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "livro cadastrado"})
