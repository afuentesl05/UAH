# EJERCICIO 5
import math

def warshall(M):
    n = len(M)
    C = [[False] * n for _ in range(n)]

    # Inicializar C con la matriz de adyacencia Mw
    for i in range(n):
        for j in range(n):
            C[i][j] = M[i][j]

    # Rellenar Matriz bottom-up
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j:
                    C[i][j] = False
                else:
                    C[i][j] = C[i][j] or (C[i][k] and C[k][j])

    return C

# Ejemplo de uso ejercicio 5

# # Ejemplo de matriz de adyacencia M
# M = [
#     [False, True, False, False],
#     [False, False, True, True],
#     [False, False, False, False],
#     [True, False, True, False]]
# 
# C = warshall(M)
# print("Matriz de caminos:")
# for row in C:
#     print(row)


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

# Ejemplo de uso ejercicio 6

#vc = [5, 4, 3, 2]  # Valores de Calidad de los equipos (Grifos, Serpientes, Cuervos, Tejones)
#N = 3  # Cantidad de partidos que debe ganar un equipo para ganar el torneo
#D = 100  # Cantidad de dinero apostado por Javi Potter

#ganancias = calcular_ganancias(vc, N, D)
#print("Posibles ganancias si ganan los Grifos:", ganancias)


#EJERCICIO 7
def subsecuencia_comun_mas_larga(A, B):
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Llenar la matriz dp
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruir la subsecuencia común más larga
    lcs_length = dp[m][n]
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            lcs.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs_length, lcs[::-1]

# Ejemplo de uso ejercicio 7
#
#A = [0, 1, 1, 0, 1, 0, 1, 0]
#B = [1, 0, 1, 0, 0, 1, 0, 0, 

#longitud, secuencia = subsecuencia_comun_mas_larga(A, B)
#print("Longitud de la subsecuencia común más larga:", longitud)
#print("Subsecuencia común más larga:", secuencia)



