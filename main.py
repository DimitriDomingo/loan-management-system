from flask import Flask
from flask_jwt_extended import JWTManager, jwt_required
from database.setup import criar_tabelas
from routes.livros import livros_bp
from routes.usuarios import usuarios_bp
from routes.emprestimos import emprestimos_bp
from routes.auth import auth_bp


def create_app():
    app = Flask(__name__)

    app.config["JWT_SECRET_KEY"] = "Dimitri132.."

    JWTManager(app)

    criar_tabelas()

    app.register_blueprint(auth_bp)
    app.register_blueprint(livros_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(emprestimos_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)