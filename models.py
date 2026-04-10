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
    
class Usuario:
    def __init__(self, id, nome, matricola):
        self.id = id
        self.nome = nome
        self.matricola = matricola

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "matricola": self.matricola
        }
    
class Emprestimo:
    def __init__(self, id, id_livro, id_usuario, devolvido):
        self.id = id
        self.id_livro = id_livro
        self.id_usuario = id_usuario
    
    def to_dict(self):
        return {
            "id": self.id,
            "id do livro": self.id_livro,
            "id do usuario": self.id_usuario,
            "devolvido": self.devolvido
        }