# EJERCICIO 5


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
if __name__ == "__main__":
    # Ejemplo de matriz de adyacencia M
    M = [
        [False, True, False, False],
        [False, False, True, True],
        [False, False, False, False],
        [True, False, True, False]
    ]

    C = warshall(M)
    print("Matriz de caminos:")
    for row in C:
        print(row)





