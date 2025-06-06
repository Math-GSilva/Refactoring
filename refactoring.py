# -*- coding: utf-8 -*-
"""Refactoring.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YycuUVIe_HPWZxiZpjDruT_yh4O0bj_r

# **Código Antigo:**
"""

import random

# Parâmetros do problema da mochila
pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidade = 5
num_itens = len(pesos)

# Parâmetros do ACO
num_formigas = 20
num_iteracoes = 50
evaporacao = 0.2
alfa = 1
beta = 5  # Foco maior no valor/peso

feromonios = [1.0 for _ in range(num_itens)]

melhores_valores = []
melhores_caminhos = []

def avaliar(solucao):
    peso_total = sum(pesos[i] for i in range(num_itens) if solucao[i])
    valor_total = sum(valores[i] for i in range(num_itens) if solucao[i])
    return valor_total if peso_total <= capacidade else 0

def construir_solucao():
    solucao = [0] * num_itens
    peso_atual = 0
    itens_nao_escolhidos = set(range(num_itens))

    while True:
        candidatos = []
        probabilidades = []

        for i in itens_nao_escolhidos:
            if peso_atual + pesos[i] <= capacidade:
                heuristica = valores[i] / pesos[i]
                prob = (feromonios[i] ** alfa) * (heuristica ** beta)
                candidatos.append(i)
                probabilidades.append(prob)

        if not candidatos:
            break

        total_prob = sum(probabilidades)
        if total_prob == 0:
            break

        r = random.uniform(0, total_prob)
        acumulado = 0
        escolhido = None
        for i, prob in zip(candidatos, probabilidades):
            acumulado += prob
            if acumulado >= r:
                escolhido = i
                break

        solucao[escolhido] = 1
        peso_atual += pesos[escolhido]
        itens_nao_escolhidos.remove(escolhido)

    return solucao

for it in range(num_iteracoes):
    todas_solucoes = []
    for _ in range(num_formigas):
        solucao = construir_solucao()
        valor = avaliar(solucao)
        todas_solucoes.append((solucao, valor))

    # Evaporação dos feromônios
    feromonios = [f * (1 - evaporacao) for f in feromonios]

    # Atualização dos feromônios com base nas soluções encontradas
    for solucao, valor in todas_solucoes:
        for i in range(num_itens):
            if solucao[i]:
                feromonios[i] += valor

    melhor_solucao = max(todas_solucoes, key=lambda x: x[1])
    melhores_valores.append(melhor_solucao[1])
    melhores_caminhos.append(melhor_solucao[0])

    print(f"Iteração {it+1}: Valor = {melhor_solucao[1]} | Itens = {melhor_solucao[0]}")

# Exibir melhor solução final
indice_final = melhores_valores.index(max(melhores_valores))
melhor_final = melhores_caminhos[indice_final]

print("\n===== Resultado Final =====")
print("Valor total:", melhores_valores[indice_final])
print("Itens escolhidos (índices):", [i for i, x in enumerate(melhor_final) if x])
print("Pesos:", [pesos[i] for i in range(num_itens) if melhor_final[i]])
print("Valores:", [valores[i] for i in range(num_itens) if melhor_final[i]])

"""# **Código Refatorado (Com testes)**"""

import unittest
import random

# ----------------------------
# Parâmetros Globais Separados
# ----------------------------
PESOS = [2, 3, 4, 5]
VALORES = [3, 4, 5, 6]
CAPACIDADE = 5
NUM_FORMIGAS = 20
NUM_ITERACOES = 50
EVAPORACAO = 0.2
ALFA = 1
BETA = 5

# ----------------------------
# Classe ACO Encapsulada
# ----------------------------
class ACO:
    def __init__(self, pesos, valores, capacidade):
        self.pesos = pesos
        self.valores = valores
        self.capacidade = capacidade
        self.num_itens = len(pesos)
        self.feromonios = [1.0 for _ in range(self.num_itens)]
        self.melhores_valores = []
        self.melhores_caminhos = []

    def avaliar(self, solucao):
        peso_total = sum(self.pesos[i] for i in range(self.num_itens) if solucao[i])
        valor_total = sum(self.valores[i] for i in range(self.num_itens) if solucao[i])
        return valor_total if peso_total <= self.capacidade else 0

    def construir_solucao(self):
        solucao = [0] * self.num_itens
        peso_atual = 0
        itens_nao_escolhidos = set(range(self.num_itens))

        while True:
            candidatos = []
            probabilidades = []

            for i in itens_nao_escolhidos:
                if peso_atual + self.pesos[i] <= self.capacidade:
                    heuristica = self.valores[i] / self.pesos[i]
                    prob = (self.feromonios[i] ** ALFA) * (heuristica ** BETA)
                    candidatos.append(i)
                    probabilidades.append(prob)

            if not candidatos or sum(probabilidades) == 0:
                break

            r = random.uniform(0, sum(probabilidades))
            acumulado = 0
            escolhido = None
            for i, prob in zip(candidatos, probabilidades):
                acumulado += prob
                if acumulado >= r:
                    escolhido = i
                    break

            solucao[escolhido] = 1
            peso_atual += self.pesos[escolhido]
            itens_nao_escolhidos.remove(escolhido)

        return solucao

    def executar(self, num_formigas=NUM_FORMIGAS, num_iteracoes=NUM_ITERACOES):
        for iteracao in range(num_iteracoes):
            todas_solucoes = []
            for _ in range(num_formigas):
                solucao = self.construir_solucao()
                valor = self.avaliar(solucao)
                todas_solucoes.append((solucao, valor))

            self.feromonios = [f * (1 - EVAPORACAO) for f in self.feromonios]

            for solucao, valor in todas_solucoes:
                for i in range(self.num_itens):
                    if solucao[i]:
                        self.feromonios[i] += valor

            melhor_solucao = max(todas_solucoes, key=lambda x: x[1])
            self.melhores_valores.append(melhor_solucao[1])
            self.melhores_caminhos.append(melhor_solucao[0])

            # Print da iteração
            print(f"Iteração {iteracao + 1}: Valor = {melhor_solucao[1]} | Itens = {melhor_solucao[0]}")

        return self.resultado_final()

    def resultado_final(self):
        indice = self.melhores_valores.index(max(self.melhores_valores))
        melhor = self.melhores_caminhos[indice]
        print("\n===== Resultado Final =====")
        print(f"Valor total: {self.melhores_valores[indice]}")
        print(f"Itens escolhidos (índices): {[i for i, escolhido in enumerate(melhor) if escolhido]}")
        print(f"Pesos: {[self.pesos[i] for i, escolhido in enumerate(melhor) if escolhido]}")
        print(f"Valores: {[self.valores[i] for i, escolhido in enumerate(melhor) if escolhido]}")
        return melhor, self.melhores_valores[indice]

# ----------------------------
# Execução do Algoritmo
# ----------------------------
aco_solver = ACO(PESOS, VALORES, CAPACIDADE)
melhor_caminho_encontrado, melhor_valor_encontrado = aco_solver.executar(NUM_FORMIGAS, NUM_ITERACOES)

# ----------------------------
# Testes Unitários com unittest
# ----------------------------
# Motivo da refatoração: Garantia de estabilidade do código após mudanças
class TestACO(unittest.TestCase):

    def test_avaliar_valido(self):
        aco = ACO([2, 3], [3, 4], 5)
        resultado = aco.avaliar([1, 1])  # peso total = 5, valor = 7
        self.assertEqual(resultado, 7)

    def test_avaliar_excede_peso(self):
        aco = ACO([2, 3], [3, 4], 4)
        resultado = aco.avaliar([1, 1])  # peso total = 5 > capacidade
        self.assertEqual(resultado, 0)

    def test_construir_solucao_valida(self):
        aco = ACO(PESOS, VALORES, CAPACIDADE)
        solucao = aco.construir_solucao()
        peso_solucao = sum(aco.pesos[i] for i in range(aco.num_itens) if solucao[i])
        self.assertLessEqual(peso_solucao, aco.capacidade)
        self.assertTrue(any(solucao))  # Garante que pelo menos um item foi selecionado

if __name__ == "__main__":
    import sys
    sys.argv = ['first-arg-is-ignored']
    unittest.main(exit=False)