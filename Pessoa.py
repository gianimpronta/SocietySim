class Pessoa:
    def __init__(self, nome, idade, local, nivel_estudo, emprego):
        self.nome = nome
        self.idade = idade
        self.local = local
        self.nivel_estudo = nivel_estudo
        self.emprego = emprego

        self.saude = 100
        self.felicidade = 0

        self.necessidades = {
            'fome': 0,
            'sede': 0,
            'seguranca_financeira': 0,
            'solidao': 0,
            'autoconhecimento': 0
        }

    def comer(self):
        self.necessidades['fome'] -= 10

    def beber(self):
        self.necessidades['sede'] -= 10

    def trabalhar(self):
        self.necessidades['seguranca_financeira'] -= 10

    def interagir(self, pessoa):
        self.necessidades['solidao'] -= 10

    def estudar(self):
        self.necessidades['autoconhecimento'] -= 10

    def migrar(self, novo_local):
        self.local = novo_local

    def calcular_saude(self):
        # Implemente a lógica para calcular a saúde com base nas necessidades e no local
        pass

    def calcular_felicidade(self):
        # Implemente a lógica para calcular a felicidade com base nas necessidades e na saúde
        pass
 
