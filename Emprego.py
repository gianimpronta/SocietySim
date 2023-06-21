class Emprego:
    def __init__(self, nome, educacao_necessaria, salario, horas_trabalho, beneficios, satisfacao_trabalho,
                 risco_acidente, crescimento_carreira, demanda_trabalho, ambiente_trabalho):
        self.nome = nome
        self.educacao_necessaria = educacao_necessaria
        self.salario = salario
        self.horas_trabalho = horas_trabalho
        self.beneficios = beneficios
        self.satisfacao_trabalho = satisfacao_trabalho
        self.risco_acidente = risco_acidente
        self.crescimento_carreira = crescimento_carreira
        self.demanda_trabalho = demanda_trabalho
        self.ambiente_trabalho = ambiente_trabalho

    def __str__(self):
        return self.nome
