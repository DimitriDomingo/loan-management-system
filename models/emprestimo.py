class Emprestimo:
    def __init__(self, id, id_livro, id_usuario, devolvido):
        self.id = id
        self.id_livro = id_livro
        self.id_usuario = id_usuario
        self.devolvido = devolvido

    def to_dict(self):
        return {
            "id": self.id,
            "id do livro": self.id_livro,
            "id do usuario": self.id_usuario,
            "devolvido": self.devolvido
        }
