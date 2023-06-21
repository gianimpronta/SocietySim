class Evento:
    def __init__(self, nome, efeito):
        self.nome = nome
        self.efeito = efeito

    def ocorrência(self, mundo):
        print(f"Ocorreu um {self.nome}!")
        self.efeito(mundo)
