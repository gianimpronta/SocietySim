from Emprego import Emprego
from Local import Local
from Pessoa import Pessoa


def main():
    # Criação do local
    local = Local(
        {'comida': 100, 'agua': 100},
        5000,
        80,
        75,
        73,
        80,
        []
    )

    emprego1 = Emprego("Desenvolvedor de Software", 10, 5000, 40, "Plano de saúde",
                       0.8, "Baixa", "Médio", "Alta", "Ambiente colaborativo")
    emprego2 = Emprego("Analista de Dados", 15, 6000, 40, "Vale-refeição",
                       0.9, "Baixa", "Alto", "Média", "Ambiente dinâmico")
    emprego3 = Emprego("Engenheiro Civil", 16, 8000, 40,
                       "Plano de saúde, Vale-alimentação",
                       0.7, "Médio", "Alto", "Alta", "Ambiente de trabalho externo")
    emprego4 = Emprego("Designer Gráfico", 10, 4000, 40,
                       "Flexibilidade de horário",
                       0.7, "Baixa", "Baixo", "Média", "Ambiente criativo")
    emprego5 = Emprego("Enfermeiro(a)", 15, 4500, 36, "Plano de saúde, Vale-transporte",
                       0.9, "Médio", "Médio", "Alta", "Ambiente hospitalar")
    emprego6 = Emprego("Professor(a) de Inglês", 9, 3500, 20,
                       "Flexibilidade de horário",
                       0.8, "Baixa", "Baixo", "Média", "Ambiente educacional")
    emprego7 = Emprego("Chef de Cozinha", 7, 6000, 45, "Vale-refeição",
                       0.9, "Médio", "Médio", "Média", "Ambiente de alta pressão")
    emprego8 = Emprego("Engenheiro de Software", 4, 7000,
                       40, "Plano de saúde, Vale-alimentação", 0.8, "Baixa", "Alto", "Alta",
                       "Ambiente de desenvolvimento")
    emprego9 = Emprego("Consultor de Marketing", 4, 5500, 40,
                       "Plano de saúde, Vale-transporte", 0.7, "Baixa", "Médio", "Média",
                       "Ambiente corporativo")

    local.disponibilizar_emprego(emprego1)
    local.disponibilizar_emprego(emprego2)
    local.disponibilizar_emprego(emprego3)
    local.disponibilizar_emprego(emprego4)
    local.disponibilizar_emprego(emprego5)
    local.disponibilizar_emprego(emprego6)
    local.disponibilizar_emprego(emprego7)
    local.disponibilizar_emprego(emprego8)
    local.disponibilizar_emprego(emprego9)

    # Criação de pessoas
    pessoa1 = Pessoa(local=local)
    pessoa2 = Pessoa(local=local)
    pessoa3 = Pessoa(local=local)
    pessoa4 = Pessoa(local=local)

    # Definição de relacionamentos
    pessoa1.amizades = [pessoa2, pessoa3]
    pessoa2.amizades = [pessoa1, pessoa4]
    pessoa3.amizades = [pessoa1]
    pessoa4.amizades = [pessoa2]

    # Adição das pessoas ao local
    local.adicionar_pessoa(pessoa1)
    local.adicionar_pessoa(pessoa2)
    local.adicionar_pessoa(pessoa3)
    local.adicionar_pessoa(pessoa4)

    for _ in range(100):
        # Execução das ações diárias
        pessoa1.realizar_acoes_diarias()
        pessoa2.realizar_acoes_diarias()
        pessoa3.realizar_acoes_diarias()
        pessoa4.realizar_acoes_diarias()

    for _ in range(10):
        pessoa1.realizar_acoes_diarias()

    # Exibição dos resultados
    print(f"Nome: {pessoa1.nome}")
    print(f"Felicidade: {pessoa1.calcular_felicidade()}")
    print(f"Necessidades: {pessoa1.necessidades}")

    print(f"Nome: {pessoa2.nome}")
    print(f"Felicidade: {pessoa2.calcular_felicidade()}")
    print(f"Necessidades: {pessoa2.necessidades}")

    print(f"Nome: {pessoa3.nome}")
    print(f"Felicidade: {pessoa3.calcular_felicidade()}")
    print(f"Necessidades: {pessoa3.necessidades}")

    print(f"Nome: {pessoa4.nome}")
    print(f"Felicidade: {pessoa4.calcular_felicidade()}")
    print(f"Necessidades: {pessoa4.necessidades}")


# Execução da função main
main()
