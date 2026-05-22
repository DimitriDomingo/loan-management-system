class Livro:
    def __init__(self, id, titulo, autor, quantidade):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.quantidade = quantidade

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "quantidade": self.quantidade
        }
