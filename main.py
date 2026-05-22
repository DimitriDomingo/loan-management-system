from flask import Flask, render_template
from database.setup import criar_tabelas
from routes.livros import livros_bp
from routes.usuarios import usuarios_bp
from routes.emprestimos import emprestimos_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(livros_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(emprestimos_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app


if __name__ == "__main__":
    criar_tabelas()
    app = create_app()
    app.run(debug=True)