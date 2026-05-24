from flask import Flask
from routes.livros import livros_bp
from routes.usuarios import usuarios_bp
from routes.emprestimos import emprestimos_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(livros_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(emprestimos_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)