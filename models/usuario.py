class Usuario:
    def __init__(self, id, nome, email,senha, tipo):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "tipo": self.tipo

        }
