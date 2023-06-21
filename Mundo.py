class Mundo:
    def __init__(self, locais):
        self.locais = locais  # Uma lista de todos os objetos Local no mundo.

    def populacao_total(self):
        return sum(local.populacao for local in self.locais)

    def crescimento_populacional(self):
        # Implementar a lógica para calcular a taxa de crescimento populacional

    def taxa_mortalidade(self):
        # Implementar a lógica para calcular a taxa de mortalidade

    def taxa_natalidade(self):
        # Implementar a lógica para calcular a taxa de natalidade

    def media_felicidade(self):
        total_felicidade = sum(pessoa.felicidade for local in self.locais for pessoa in local.pessoas)
        total_pessoas = self.populacao_total()
        return total_felicidade / total_pessoas

    def idh(self):
        # Implementar a lógica para calcular o Índice de Desenvolvimento Humano

    def indice_gini(self):
        # Implementar a lógica para calcular o Índice de Gini

    def nivel_medio_educacao(self):
        total_educacao = sum(pessoa.nivel_educacao for local in self.locais for pessoa in local.pessoas)
        total_pessoas = self.populacao_total()
        return total_educacao / total_pessoas

    def taxa_desemprego(self):
        # Implementar a lógica para calcular a taxa de desemprego

    def recursos_disponiveis(self):
        return sum(local.recursos for local in self.locais)

    def expectativa_vida_media(self):
        # Implementar a lógica para calcular a expectativa de vida média

    def qualidade_vida_media(self):
        # Implementar a lógica para calcular a qualidade de vida média

    def migracao(self):
        # Implementar a lógica para calcular a migração
