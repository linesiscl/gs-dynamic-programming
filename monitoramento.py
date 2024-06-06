import numpy as np
import math

def calcular_distancia(ponto1, ponto2):
#Calcula a distância entre dois pontos. Os argumentos são as coordenadas deles, e a funçãpo retorna essa distância como um float

    return math.sqrt((ponto1[0] - ponto2[0])**2 + 
                     (ponto1[1] - ponto2[1])**2 + 
                     (ponto1[2] - ponto2[2])**2)

def encontrar_distribuicao_otima_recursiva(sensores, pontos_interesse, alocacao_atual=[], pontos_cobertos=set()):
#Encontra recursivamente a distribuição ótima dos sensores para cobrir pontos de interesse. Os argumentos são: lista de coordenadas dos sensores, lista das coordenadas dos pontos, lista com a alocação atual e conjunto dos pontos já cobertos. A função retorna uma lista com a distribuição ótima dos sensores

    if len(alocacao_atual) == len(sensores):
        return alocacao_atual

    melhor_alocacao = None
    menor_custo = float('inf')

    for i, ponto_interesse in enumerate(pontos_interesse):
        if i not in pontos_cobertos:
            novo_pontos_cobertos = pontos_cobertos.copy()
            novo_pontos_cobertos.add(i)
            novo_alocacao_atual = alocacao_atual + [i]

            custo = sum(calcular_distancia(sensores[j], ponto_interesse) for j in range(len(alocacao_atual)))

            nova_alocacao = encontrar_distribuicao_otima_recursiva(sensores, pontos_interesse, novo_alocacao_atual, novo_pontos_cobertos)

            if custo < menor_custo:
                melhor_alocacao = nova_alocacao
                menor_custo = custo

    return melhor_alocacao

if __name__ == "__main__":
    sensores = [(0, 0, 0), (1, 1, 1), (2, 2, 2)]
    pontos_interesse = [(1, 0, 0), (2, 1, 1), (3, 2, 2)]

    distribuicao_otima = encontrar_distribuicao_otima_recursiva(sensores, pontos_interesse)
    print("Distribuição Ótima dos Sensores:", distribuicao_otima)

    # Calcular as distâncias entre todos os pares de pontos de sensores e pontos de interesse
    distancias = []
    for sensor in sensores:
        distancias_sensor = []
        for ponto in pontos_interesse:
            distancia = calcular_distancia(sensor, ponto)
            distancias_sensor.append(distancia)
        distancias.append(distancias_sensor)

    distribuicao_otima = encontrar_distribuicao_otima_recursiva(sensores, pontos_interesse)
    print("Matriz de Distâncias:")
    for linha in distancias:
        print(linha)
