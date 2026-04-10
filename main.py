from flask import Flask, jsonify, request
from database import conectar, criar_tabelas
from models import Livro, Usuario, Emprestimo

app = Flask(__name__)

@app.route("/livros", methods=["GET"])
def listar_livros():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute ("SELECT * FROM livros")
    dados = cursor.fetchall()

    livros = [Livro(*I).to_dict() for I in dados]
    conn.close()
    return jsonify(livros)

@app.route("/livros", methods = ["POST"])
def adicionar_livros():
    dados = request.json

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO livros (titulo, autor, quantidade) VALUES (?, ?, ?)", (dados["titulo"], dados ["autor"], dados ["quantidade"]))

    conn.commit()
    conn.close()

    return jsonify ({"mensagem": "livro cadastrado"})

@app.route("/usuarios", methods = ["GET"])
def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    dados = cursor.fetchall()

    usuarios = [Usuario(*U).to_dict() for U in dados]
    conn.close()
    return jsonify(usuarios)

@app.route("/usuarios", methods = ["POST"])
def adicionar_usuarios():
    dados = request.json

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO usuarios (nome, matricola) VALUES (?, ?)", (dados["nome"], dados ["matricola"]))

    conn.commit()
    conn.close()

    return jsonify ({"mensagem": "usuário cadastrado"})

@app.route("/emprestimos", methods = ["GET"])
def listar_emprestimos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM emprestimos")
    dados = cursor.fetchall()

    emprestimos = [Emprestimo(*E).to_dict() for E in dados]
    conn.close()
    return jsonify(emprestimos)

@app.route("/emprestimos", methods = ["POST"])
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

@app.route("/emprestimos/<int:id>", methods = ["PUT"])
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

if __name__ == "__main__":
    criar_tabelas()
    app.run(debug=True)