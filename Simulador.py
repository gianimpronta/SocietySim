import time


class Simulador:
    def __init__(self, mundo, duracao, passo_tempo):
        self.mundo = mundo
        self.duracao = duracao
        self.passo_tempo = passo_tempo

    def iniciar(self):
        for t in range(0, self.duracao, self.passo_tempo):
            print(f"Dia {t}")

            # Atualiza o mundo
            self.mundo.atualizar()

            # Aqui você pode inserir outras funcionalidades, como a geração de eventos, a migração de pessoas, etc.

            time.sleep(self.passo_tempo)

    def finalizar(self):
        print("A simulação foi finalizada.")
        # Aqui você pode adicionar qualquer lógica que queira executar no final da simulação, como salvar os
        # resultados, exibir gráficos, etc.
