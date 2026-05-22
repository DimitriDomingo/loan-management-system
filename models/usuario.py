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
