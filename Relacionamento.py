import random


class Relacionamento:
    def __init__(self, tipo_de_relacionamento, pessoas_envolvidas):
        self.tipo_de_relacionamento = tipo_de_relacionamento
        self.pessoas_envolvidas = pessoas_envolvidas
        self.duracao = 0
        self.forca = 50
        self.interacoes = []

    def interagir(self):
        interacao = random.choice(self.interacoes)
        if interacao == 'ajuda':
            self.forca += 10
        elif interacao == 'conflito':
            self.forca -= 10
        elif interacao == 'apoio':
            self.forca += 5
        self.forca = min(max(self.forca, 0), 100)

    def atualizar_duracao(self):
        self.duracao += 1

    def terminar(self):
        for pessoa in self.pessoas_envolvidas:
            pessoa.relacionamentos.remove(self)

    def iniciar(self):
        for pessoa in self.pessoas_envolvidas:
            pessoa.relacionamentos.add(self)
