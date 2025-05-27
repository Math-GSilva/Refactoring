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
