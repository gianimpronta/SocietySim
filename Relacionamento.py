class Relacionamento:
    def __init__(self, tipo_de_relacionamento, pessoas_envolvidas):
        self.tipo_de_relacionamento = tipo_de_relacionamento
        self.pessoas_envolvidas = pessoas_envolvidas
        self.duração = 0
        self.força = 50
        self.interações = []

    def interagir(self):
        interação = random.choice(self.interações)
        if interação == 'ajuda':
            self.força += 10
        elif interação == 'conflito':
            self.força -= 10
        elif interação == 'apoio':
            self.força += 5
        self.força = min(max(self.força, 0), 100)

    def atualizar_duração(self):
        self.duração += 1

    def terminar(self):
        for pessoa in self.pessoas_envolvidas:
            pessoa.relacionamentos.remove(self)

    def iniciar(self):
        for pessoa in self.pessoas_envolvidas:
            pessoa.relacionamentos.add(self)
