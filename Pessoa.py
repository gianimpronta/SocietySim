import random

import utils


def realizar_escolha_probabilistica(probabilidades):
    soma_probabilidades = sum(probabilidades)
    probabilidades_normalizadas = [p / soma_probabilidades for p in probabilidades]
    escolha = random.choices(range(len(probabilidades)), probabilidades_normalizadas)
    return escolha[0] if escolha else None


def calcular_probabilidade_amizade(pessoa):
    # Cálculo da probabilidade de formar uma nova amizade com a pessoa
    probabilidade_base = 0.5  # Valor base de exemplo (50%)
    # Outros cálculos e influências para determinar a probabilidade de formar amizade
    return probabilidade_base


class Pessoa:
    FASES_VIDA = {
        'bebe': {
            'acoes': [],
            'transicao': 'jovem',
            'idade_maxima': 3
        },
        'jovem': {
            'acoes': ['estudar', 'socializar'],
            'transicao': 'adulto',
            'idade_maxima': 18
        },
        'adulto': {
            'acoes': ['trabalhar', 'socializar', 'estudar', 'cuidar_da_familia'],
            'transicao': 'idoso',
            'idade_maxima': 65
        },
        'idoso': {
            'acoes': ['cuidar_da_familia', 'morrer'],
            'transicao': None,
            'idade_maxima': None
        }
    }

    def __init__(self, local, pai=None, mae=None, idade=random.randint(18, 40)):
        self.amizades = []
        p = random.choice(utils.lista_pessoas)
        self.nome = p['nome']
        self.sexo = p['sexo']
        self.idade = idade
        self.local = local
        self.nivel_estudo = 0
        self.emprego = None
        self.pai = pai
        self.mae = mae
        self.saude = 100
        self.felicidade = 0
        self.dinheiro = 0
        self.satisfacao_amizade = 0
        self.classe_socioeconomica = self.herdar_classe_socioeconomica()
        self.parceiro = None
        self.estadocivil = 'solteiro'  # Pode ser 'solteiro' ou 'casado'
        self.fase_vida = self.definir_fase_vida()
        self.necessidades = {
            'fisiologicas': {
                'fome': 100,
                'sede': 100,
                'sono': 100
            },
            'seguranca': {
                'seguranca_fisica': 100,
                'seguranca_financeira': 100,
                'saude': 100
            },
            'sociais': {
                'amizade': 0,
                'amor': 0
            },
            'estima': {
                'autoestima': 0
            },
            'autorrealizacao': {
                'crescimento_pessoal': 0,
                'autodesenvolvimento': 0,
                'realizacao_potencial': 0
            }
        }
        self.filhos = []

    def herdar_classe_socioeconomica(self):
        if self.pai and self.mae:
            # Se ambos os pais estão presentes, a classe socioeconômica é herdada
            # Exemplo de lógica para herança:
            # Se pelo menos um dos pais pertence à classe alta, a pessoa também pertence à classe alta.
            # Caso contrário, se pelo menos um dos pais pertence à classe média, a pessoa pertence à classe média.
            # Caso contrário, a pessoa pertence à classe baixa.

            if self.pai.classe_socioeconomica == 'alta' or self.mae.classe_socioeconomica == 'alta':
                return 'alta'
            elif self.pai.classe_socioeconomica == 'media' or self.mae.classe_socioeconomica == 'media':
                return 'media'
            else:
                return 'baixa'
        else:
            # Se um dos pais estiver ausente, a classe socioeconômica da pessoa é definida aleatoriamente ou por outras regras definidas por você.
            # Aqui, vamos definir como 'media' por padrão.
            return random.choice(['alta', 'media', 'baixa'])

    def comer(self):
        satisfacao = min(1, self.local.recursos['comida'] / len(self.local.populacao))
        quantidade = 1

        if self.classe_socioeconomica == 'baixa':
            quantidade *= satisfacao * 0.7
        elif self.classe_socioeconomica == 'media':
            quantidade *= satisfacao
        elif self.classe_socioeconomica == 'alta':
            quantidade *= satisfacao * 1.2

        self.modificar_necessidade(self.necessidades['fisiologicas']['fome'], quantidade)

    def beber(self):
        satisfacao = min(1, self.local.recursos['agua'] / len(self.local.populacao))
        quantidade = 1

        if self.classe_socioeconomica == 'baixa':
            quantidade *= satisfacao * 0.7
        elif self.classe_socioeconomica == 'media':
            quantidade *= satisfacao
        elif self.classe_socioeconomica == 'alta':
            quantidade *= satisfacao * 1.2

        self.modificar_necessidade(self.necessidades['fisiologicas']['sede'], quantidade)

    def dormir(self):
        satisfacao = min(1, self.local.qualidade_vida / len(self.local.populacao))
        horas = 1

        if self.classe_socioeconomica == 'baixa':
            horas *= satisfacao * 0.7
        elif self.classe_socioeconomica == 'media':
            horas *= satisfacao
        elif self.classe_socioeconomica == 'alta':
            horas *= satisfacao * 1.2

        self.modificar_necessidade(self.necessidades['fisiologicas']['sono'], horas)

    def buscar_seguranca_fisica(self):
        satisfacao = self.local.qualidade_vida / len(self.local.populacao)

        if self.classe_socioeconomica == 'baixa':
            satisfacao *= 0.7
        elif self.classe_socioeconomica == 'alta':
            satisfacao *= 1.2

        self.modificar_necessidade(self.necessidades['seguranca']['seguranca_fisica'], satisfacao)

    def buscar_seguranca_financeira(self):
        satisfacao = self.local.economia / len(self.local.populacao)

        if self.classe_socioeconomica == 'baixa':
            satisfacao *= 0.7
        elif self.classe_socioeconomica == 'alta':
            satisfacao *= 1.2

        if self.emprego:
            satisfacao *= self.emprego.satisfacao_trabalho

        self.modificar_necessidade(self.necessidades['seguranca']['seguranca_financeira'], satisfacao)

    def buscar_saude(self):
        satisfacao = self.local.qualidade_saude / len(self.local.populacao)

        if self.classe_socioeconomica == 'baixa':
            satisfacao *= 0.7
        elif self.classe_socioeconomica == 'alta':
            satisfacao *= 1.2

        self.modificar_necessidade(self.necessidades['seguranca']['saude'], satisfacao)

    def buscar_amizades(self):
        satisfacao_amizades = 0

        for amigo in self.amizades:
            satisfacao_amizades += amigo.satisfacao_amizade

        satisfacao_amizades /= len(self.amizades) if len(self.amizades) > 0 else 1

        self.modificar_necessidade(self.necessidades['sociais']['amizade'], satisfacao_amizades)

    def buscar_amor(self):
        satisfacao_amor = 0

        if self.pai and self.mae:
            satisfacao_amor += self.pai.satisfacao_amor
            satisfacao_amor += self.mae.satisfacao_amor

        satisfacao_amor /= 2 if self.pai and self.mae else 1

        if self.estadocivil == 'casado' and self.parceiro:
            satisfacao_amor += self.parceiro.satisfacao_amor

        self.modificar_necessidade(self.necessidades['sociais']['amor'], satisfacao_amor)

    def influenciar_autoestima(self):
        satisfacao_autoestima = 0

        if self.saude >= 80:  # Exemplo: se a saúde for maior ou igual a 80%
            satisfacao_autoestima += 10

        if self.emprego:
            satisfacao_autoestima += self.emprego.satisfacao_trabalho

        self.modificar_necessidade(self.necessidades['estima']['autoestima'], satisfacao_autoestima)

    def buscar_crescimento_pessoal(self):
        if self.idade >= 18:
            self.modificar_necessidade(self.necessidades['autorrealizacao']['crescimento_pessoal'], 1)

    def buscar_autodesenvolvimento(self):
        if self.nivel_estudo >= 12:  # Exemplo: nível mínimo de estudo necessário
            self.modificar_necessidade(self.necessidades['autorrealizacao']['autodesenvolvimento'], 1)

    def buscar_realizacao_potencial(self):
        if self.emprego and self.emprego.satisfacao_trabalho >= 0.8:  # Exemplo: nível mínimo de satisfação no emprego
            self.modificar_necessidade(self.necessidades['autorrealizacao']['realizacao_potencial'], 1)

    def realizar_acoes_diarias(self):
        fase_atual = self.FASES_VIDA[self.fase_vida]
        acoes_diarias = fase_atual['acoes']

        for categoria, necessidades_categoria in self.necessidades.items():
            for necessidade, valor in necessidades_categoria.items():
                self.necessidades[categoria][necessidade] = max(min(valor - 1.2, 100), -100)

        for acao in acoes_diarias:
            self.executar_acao(acao)

        self.comer()
        self.beber()
        self.dormir()
        self.buscar_seguranca_fisica()
        self.buscar_seguranca_financeira()
        self.buscar_saude()
        self.buscar_amizades()
        self.buscar_amor()
        self.influenciar_autoestima()
        self.buscar_crescimento_pessoal()
        self.buscar_autodesenvolvimento()
        self.buscar_realizacao_potencial()

    def definir_fase_vida(self):
        for fase, config in self.FASES_VIDA.items():
            if self.idade <= config['idade_maxima']:
                return fase

    def executar_acao(self, acao):
        if acao == 'estudar':
            self.estudar()
        elif acao == 'socializar':
            self.socializar()
        elif acao == 'trabalhar':
            self.trabalhar()
        elif acao == 'cuidar_da_familia':
            self.cuidar_da_familia()
        elif acao == 'morrer':
            self.verificar_morte()

    def socializar(self):
        felicidade = self.felicidade
        necessidades_estima = sum(self.necessidades['estima'].values())
        necessidades_sociais = sum(self.necessidades['sociais'].values())

        influencia_felicidade = 0.4  # Fator de influência da felicidade
        influencia_necessidades_estima = 0.3  # Fator de influência das necessidades de estima
        influencia_necessidades_sociais = 0.3  # Fator de influência das necessidades sociais

        influencia_total = (felicidade * influencia_felicidade) + (
                necessidades_estima * influencia_necessidades_estima) + (
                                   necessidades_sociais * influencia_necessidades_sociais)

        # Cálculo da probabilidade de socializar
        probabilidade_socializar = influencia_total / 100

        # Verificação se a pessoa irá socializar
        if random.random() < probabilidade_socializar:
            pass

    def iniciar_amizade(self):
        pessoas_local = self.local.pessoas  # Lista de pessoas no mesmo local
        pessoas_sem_amizade = [p for p in pessoas_local if
                               p != self and self not in p.amizades]  # Pessoas sem relação de amizade com a pessoa atual

        if pessoas_sem_amizade:
            probabilidades_amizade = [calcular_probabilidade_amizade(p) for p in
                                      pessoas_sem_amizade]  # Lista de probabilidades de formar amizade

            indice_amizade = realizar_escolha_probabilistica(
                probabilidades_amizade)  # Índice escolhido com base nas probabilidades

            if indice_amizade is not None:
                nova_amizade = pessoas_sem_amizade[
                    indice_amizade]  # Pessoa selecionada para formar a nova amizade
                self.amizades.append(
                    nova_amizade)  # Adicionar a nova amizade à lista de amizades da pessoa atual
                nova_amizade.amizades.append(
                    self)  # Adicionar a pessoa atual à lista de amizades da nova amizade

    def estudar(self):
        qualidade_educacao_local = self.local.qualidade_educacao
        classe_economica_map = {'baixa': 1, 'media': 2, 'alta': 3}
        peso_classe_socioeconomica = classe_economica_map[self.classe_socioeconomica]

        influencia_qualidade_educacao = 0.5  # Fator de influência da qualidade da educação
        influencia_classe_socioeconomica = 0.3  # Fator de influência da classe socioeconômica

        # Modificação no nível de estudo com base nas influências
        modificacao_nivel_estudo = (qualidade_educacao_local * influencia_qualidade_educacao) + (
                peso_classe_socioeconomica * influencia_classe_socioeconomica)

        # Incremento no nível de estudo da pessoa
        self.nivel_estudo += modificacao_nivel_estudo

        # Limitação do nível de estudo máximo
        nivel_estudo_maximo = 100  # Valor máximo para o nível de estudo
        self.nivel_estudo = min(self.nivel_estudo, nivel_estudo_maximo)

        # Incremento nas necessidades de autorrealização relacionadas ao crescimento pessoal e autodesenvolvimento
        self.modificar_necessidade(self.necessidades['autorrealizacao']['crescimento_pessoal'], modificacao_nivel_estudo)
        self.modificar_necessidade(self.necessidades['autorrealizacao']['autodesenvolvimento'], modificacao_nivel_estudo)

    def trabalhar(self):
        economia_local = self.local.economia
        classe_economica_map = {'baixa': 1, 'media': 2, 'alta': 3}
        peso_classe_socioeconomica = classe_economica_map[self.classe_socioeconomica]
        emprego = self.emprego

        if not emprego:
            self.buscar_emprego()
            return

        influencia_economia = 0.4  # Fator de influência da economia local
        influencia_classe_socioeconomica = 0.3  # Fator de influência da classe socioeconômica
        influencia_emprego = 0.3  # Fator de influência do emprego

        satisfacao_trabalho = emprego.satisfacao_trabalho

        # Cálculo da influência total considerando os fatores de influência
        influencia_total = (economia_local * influencia_economia) + (
                peso_classe_socioeconomica * influencia_classe_socioeconomica) + (
                                   satisfacao_trabalho * influencia_emprego)

        # # Modificação na satisfação do trabalho
        # modificacao_satisfacao_trabalho = influencia_total
        #
        # # Atualização da satisfação do trabalho no emprego da pessoa
        # emprego.satisfacao_trabalho += modificacao_satisfacao_trabalho

        # Aumento de salário com base na satisfação do trabalho
        # aumento_salario = emprego.salario * (modificacao_satisfacao_trabalho / 100)

        # Incremento do salário da pessoa
        # self.dinheiro += aumento_salario

    def cuidar_da_familia(self):
        membros_familia = self.obter_membros_familia()

        for membro in membros_familia:
            membro.saude += 10  # Incremento na saúde do membro da família
            membro.felicidade += 5  # Incremento na felicidade do membro da família

    def obter_membros_familia(self):
        membros_familia = []

        if self.pai:
            membros_familia.append(self.pai)

        if self.mae:
            membros_familia.append(self.mae)

        membros_familia.extend(self.filhos)
        return membros_familia

    def verificar_morte(self):
        idade = self.idade
        saude = self.saude
        expectativa_vida_local = self.local.expectativa_vida
        qualidade_vida_local = self.local.qualidade_vida

        fator_idade = idade / expectativa_vida_local
        fator_saude = saude / 100
        fator_qualidade_vida = qualidade_vida_local / 100

        probabilidade_morte = fator_idade * fator_saude * fator_qualidade_vida

        if random.random() < probabilidade_morte:
            return True  # A pessoa morre
        else:
            return False  # A pessoa sobrevive

    def migrar(self, novo_local):
        self.local = novo_local

    def calcular_saude(self):
        idade = self.idade
        necessidades_basicas = sum(self.necessidades['fisiologicas'].values())
        qualidade_vida_local = self.local.qualidade_vida

        fator_idade = 1 - (idade / self.local.expectativa_vida)
        # Quanto maior a idade, menor o fator de influência da
        # idade na saúde
        fator_necessidades_basicas = necessidades_basicas / 100
        fator_qualidade_vida = qualidade_vida_local / 100

        saude = (fator_idade + fator_necessidades_basicas + fator_qualidade_vida) / 3 * 100

        self.saude = saude

    def calcular_felicidade(self):
        necessidades = self.necessidades
        relacionamentos = self.amizades + [self.parceiro] if self.parceiro else self.amizades
        satisfacao_trabalho = self.emprego.satisfacao_trabalho if self.emprego else 0

        fator_necessidades = utils.calcular_soma(necessidades) / (len(necessidades) * 100)
        fator_relacionamentos = len(relacionamentos) / 10  # Supondo que mais relacionamentos geram maior felicidade
        fator_satisfacao_trabalho = satisfacao_trabalho / 100

        felicidade = (fator_necessidades + fator_relacionamentos + fator_satisfacao_trabalho) / 3 * 100

        self.felicidade = felicidade
        return self.felicidade

    def decidir_casar(self):
        if self.estadocivil == 'solteiro':
            parceiro_em_potencial = self.encontrar_parceiro_em_potencial()

            if parceiro_em_potencial and parceiro_em_potencial.estadocivil == 'solteiro' and self.sexo != parceiro_em_potencial.sexo:
                # Outros critérios de compatibilidade podem ser adicionados aqui

                if self.decidir_buscar_parceiro():
                    self.parceiro = parceiro_em_potencial
                    self.estadocivil = 'casado'
                    parceiro_em_potencial.parceiro = self
                    parceiro_em_potencial.estadocivil = 'casado'
                    return True

        return False

    def decidir_buscar_parceiro(self):
        # Lógica para decidir se a pessoa irá buscar um parceiro
        # Considere adicionar critérios como idade, desejo pessoal, entre outros

        idade_minima_busca_parceiro = 18  # Idade mínima para buscar um parceiro
        if self.idade < idade_minima_busca_parceiro:
            return False  # Se a pessoa for menor de idade, não busca um parceiro
        # Aqui você pode adicionar lógicas adicionais com base em outros critérios, como desejo pessoal
        return True  # Retorna True se a pessoa deseja buscar um parceiro

    def encontrar_parceiro_em_potencial(self):
        pessoas_disponiveis = [p for p in self.local.pessoas if p != self and p.estadocivil == 'solteiro']

        if pessoas_disponiveis:
            return random.choice(pessoas_disponiveis)

        return None

    def decidir_ter_filhos(self):
        # Lógica para decidir se a pessoa irá ter filhos
        # Considere adicionar critérios como idade, estado civil, disponibilidade, entre outros

        idade_minima_ter_filhos = 18  # Idade mínima para ter filhos
        idade_maxima_ter_filhos = 50  # Idade máxima para ter filhos

        if self.estadocivil != 'casado':
            return False  # Se a pessoa não estiver casada, não pode ter filhos

        if self.idade < idade_minima_ter_filhos or self.idade > idade_maxima_ter_filhos:
            return False  # Se a pessoa estiver abaixo da idade mínima ou acima da idade máxima, não pode ter filhos

        # Aqui você pode adicionar lógicas adicionais com base em outros critérios, como disponibilidade,
        # desejo pessoal, entre outros

        return True  # Retorna True se a pessoa deseja ter filhos

    def ter_filho(self, nome):
        if self.decidir_ter_filhos():
            filho = Pessoa(pai=self if self.sexo == 'masculino' else self.parceiro,
                           mae=self if self.sexo == 'feminino' else self.parceiro, local=self.local, idade=0)
            self.local.adicionar_pessoa(filho)
            self.filhos.append(filho)
            return filho

        return None

    def buscar_emprego(self):
        if not self.emprego:
            for emprego in self.local.empregos_disponiveis:
                if emprego.educacao_necessaria <= self.nivel_estudo:
                    self.emprego = emprego
                    self.local.remover_emprego(
                        emprego)  # remover o emprego da lista de empregos disponíveis
                    return True
        return False

    def modificar_necessidade(self, necessidade, valor):
        """
        Modifica o valor de uma necessidade específica.

        :param necessidade: A necessidade a ser modificada.
        :param valor: O valor a ser adicionado à necessidade.
        """

        necessidade += valor
        # Certificando-se de que a necessidade não vai além de 100 ou abaixo de 0
        if necessidade > 100:
            necessidade = 100
        elif necessidade < -100:
            necessidade = -100
