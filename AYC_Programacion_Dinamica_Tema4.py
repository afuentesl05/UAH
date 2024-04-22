# EJERCICIO 5
import math


def warshall(M):
    n = len(M)
    C = [[False] * n for _ in range(n)]

    # Inicializar C con la matriz de adyacencia M
    for i in range(n):
        for j in range(n):
            C[i][j] = M[i][j]

    # Rellenar Matriz
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j:
                    C[i][j] = False
                else:
                    C[i][j] = C[i][j] or (C[i][k] and C[k][j])

    return C

# Ejemplo de uso
#if __name__ == "__main__":
#    # Ejemplo de matriz de adyacencia M
#    M = [
#        [False, True, False, False],
#        [False, False, True, True],
#        [False, False, False, False],
#        [True, False, True, False]
#    ]
#
#    C = warshall(M)
#    print("Matriz de caminos:")
#    for row in C:
#        print(row)


#EJERCICIO 6


def calcular_probabilidades_vc(vc):
    total_vc = sum(vc)
    probabilidades = [valor / total_vc for valor in vc]
    return probabilidades

def calcular_probabilidad_ganar_1_partido(probabilidades):
    probabilidades_ganar = []
    for i, prob in enumerate(probabilidades):
        probabilidad_ganar = prob
        for j, otra_prob in enumerate(probabilidades):
            if i != j:
                probabilidad_ganar *= (1 - otra_prob)
        probabilidades_ganar.append(probabilidad_ganar)
    return probabilidades_ganar

def calcular_ganancias(vc, N, D):
    probabilidades = calcular_probabilidades_vc(vc)
    probabilidades_ganar = calcular_probabilidad_ganar_1_partido(probabilidades)
    
    probabilidad_grifos_ganar = math.pow(probabilidades_ganar[0], N) #en la lista en la posicion 0 esta la probabilidad de ganar de los grifos 1 partido

    ganancias_maximas = D / probabilidad_grifos_ganar

    return ganancias_maximas

# Ejemplo de uso
if __name__ == "__main__":
    vc = [5, 4, 3, 2]  # Valores de Calidad de los equipos (Grifos, Serpientes, Cuervos, Tejones)
    N = 3  # Cantidad de partidos que debe ganar un equipo para ganar el torneo
    D = 100  # Cantidad de dinero apostado por Javi Potter

    ganancias = calcular_ganancias(vc, N, D)
    print("Posibles ganancias si ganan los Grifos:", ganancias)


