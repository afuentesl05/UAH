# PECL_2 ALGORITMIA Y COMPLEJIDAD 2023-2024

# CUADERNO TEMA 4: PROGRAMACIÓN DINÁMICA

# EJERCICIO 4

"""
Alí Babá ha conseguido entrar en la cueva de los ciento un mil ladrones, y ha llevado
consigo su camello junto con dos grandes alforjas; el problema es que se encuentra con
tanto tesoro que no sabe ni qué llevarse. Los tesoros son joyas talladas, obras de arte,
cerámica… es decir, son objetos únicos que no pueden partirse ya que entonces su valor
se reduciría a cero.
Afortunadamente los ladrones tienen todo muy bien organizado y se encuentra con una
lista de todos los tesoros que hay en la cueva, donde se refleja el peso de cada pieza y su
valor en el mercado de Damasco. Por su parte, Alí sabe la capacidad de peso que tiene
cada una de las alforjas.
Diseñar un algoritmo que, teniendo como datos los pesos y valor de las piezas, y la
capacidad de las dos alforjas, permita obtener el máximo beneficio que podrá sacar Alí
Babá de la cueva de las maravillas.
"""

def mochila(valores, pesos, capacidad):
    """ 
     ARGS: valores, pesos, capacidad --> list, list, int
     OBJ: Mediante programación dinámica se gestionan unas listas de valores, pesos y la capacidad de la mochila para dar 
          el valor máximo de un conjunto de objetos para una capacidad limitada.
     RETURN: Elemento final de la tabla, lista seleccionados
    """
    n = len(valores)
    # Creamos una tabla para almacenar los resultados de subproblemas
    tabla = [[0] * (capacidad + 1) for _ in range(n + 1)]

    # Llenamos la tabla de manera bottom-up
    for i in range(1, n + 1):
        for w in range(1, capacidad + 1):
            # Si el peso del elemento actual es menor o igual a la capacidad actual
            if pesos[i - 1] <= w:
                # Tomamos el máximo entre incluir o no incluir el elemento en la mochila
                tabla[i][w] = max(valores[i - 1] + tabla[i - 1][w - pesos[i - 1]], tabla[i - 1][w])
            else:
                # Si el peso del elemento actual es mayor que la capacidad actual, no lo incluimos
                tabla[i][w] = tabla[i - 1][w]

    # La solución estará en la esquina inferior derecha de la tabla
    valor_maximo = tabla[n][capacidad]

    # Reconstruimos los elementos seleccionados
    seleccionados = []
    w = capacidad
    for i in range(n, 0, -1):
        if valor_maximo <= 0:
            break
        # Si el valor en la celda actual es diferente al valor en la celda anterior, entonces el elemento actual fue seleccionado
        if valor_maximo != tabla[i - 1][w]:
            seleccionados.append(i - 1)
            valor_maximo -= valores[i - 1]
            w -= pesos[i - 1]

    seleccionados.reverse()  # Invertimos la lista para obtener los índices de los elementos seleccionados en orden
    return tabla[n][capacidad], seleccionados


def alforjas(valores, pesos, capacidad1, capacidad2):
    """ 
     ARGS: valores, pesos, capacidad1, capacidad2 --> list, list, int, int
     OBJ: Esta función, mediante el uso del problema de la mochila, gestiona dos alforjas (mochilas), y tras realizar el beneficio de uno 
          eliminamos los objetos ya seleccionados de la lista inicial, y rehacemos el problema para los objetos restantes y rellenamos la 
          segunda alforja. Finalmente tenemos los pesos de los beneficios de ambos, lo sumamos y obtenemos el resultado beneficio final
     RETURN: Máximo beneficio de las alforjas (int)
    """
    max_valor_alf1, items_seleccionados_alf1 = mochila(valores, pesos, capacidad1) # Alforja 1

    for i in range(len(items_seleccionados_alf1)): # eliminar los elementos ya seleccionados
            valores.remove(valores[i])
            pesos.remove(pesos[i])

    max_valor_afl2, items_seleccionados_alf2 = mochila(valores, pesos, capacidad2) # Alforja 2

    return max_valor_alf1 + max_valor_afl2 # beneficio final

# Ejemplo de uso problema 4
valores = [120, 190, 100, 60]
pesos = [1, 12, 2, 11]
print(alforjas(valores, pesos, 10, 12))


# EJERCICIO 6

"""
¡Llega el torneo de EscobaBall, y más salvaje que nunca! Este año, en el Colegio de
Magia y Hechicería han decidido que los cuatro equipos (Grifos, Serpientes, Cuervos y
Tejones) jueguen en cada partido todos contra todos, y como siempre que ningún partido
termine en empate. El torneo acabará cuando un mismo equipo haya ganado un total de
N partidos (no necesariamente consecutivos).
El aprendiz de mago Javi Potter quiere apostar algo de dinero por su equipo, los Grifos,
así que se dirige a la casa de apuestas de los gnomos para ver cuánto le darían si gana su
equipo: sus ganancias serían iguales a la cantidad de dinero apostado dividido por la
probabilidad de que el equipo gane el campeonato (por ejemplo, si los Grifos tuviesen un
50% de ganar el campeonato y Javi apuesta 10 monedas de oro, sus posibles ganancias
serían 10/0’5 = 20 monedas de oro; si tuviesen un 20% de ganar, el beneficio posible sería
de 10/0’2 = 50 monedas de oro, mayor recompensa al ser más difícil de conseguir).
Para obtener esta probabilidad, la casa de apuestas tiene un Valor de Calidad asignado a
cada equipo (que mide la habilidad de los jugadores, su motivación, etc, y que es un valor
fijo para el equipo e independiente del partido que esté jugando) de manera que cuanto
mayor es el VC de un equipo, más probabilidades tiene de ganar un partido. Por ejemplo,
si los cuatro equipos tuviesen igual VC todos tendrían un 25% de ganar un partido. Si tres
equipos tuviesen el mismo VC y el cuarto equipo tuviese el doble de esa cantidad, los
primeros tendrían un 20% y el último un 40%. Como los partidos no pueden terminar en
empate, la suma de las probabilidades siempre es el 100%.
Teniendo como datos los Valores de Calidad de los equipos, la cantidad de partidos N
que debe ganar un equipo para conseguir ganar el torneo, y el dinero D apostado por Javi
Potter, obtener cuáles serían las ganancias si ganasen los Grifos.
"""
import math

def calcular_probabilidades_vc(vc):
    """
     ARGS: Valores de calidad --> list
     OBJ: calcula las probabilidades de victoria de cada equipo y las almacena en una lista ordenada (Grifos, Serpientes, Cuervos, Tejones)
     RETURN: devuelve una lista (list)
    """
    total_vc = sum(vc)
    probabilidades = [valor / total_vc for valor in vc]
    return probabilidades

def calcular_probabilidad_ganar_1_partido(probabilidades):
    """
     ARGS: probabilidades --> list
     OBJ: Mediante una lista de probabilidades, devuelve las probabilidades de ganar un partido de cada equipo y las almacena en una lista
     RETURN: Devuelve una lista con las probabilidades de ganar un partido
    """
    probabilidades_ganar = []
    # indice, probabilidad en enumerate([n, m, ..])
    for i, prob in enumerate(probabilidades): 
        probabilidad_ganar = prob
        for j, otra_prob in enumerate(probabilidades):
            if i != j:
                # multiplicar la probabilidad para calcular la total
                probabilidad_ganar *= (1 - otra_prob) 
        probabilidades_ganar.append(probabilidad_ganar)
    return probabilidades_ganar

def calcular_ganancias(vc, N, D):
    """
     ARGS: Valores de Calidad, Numero de partidos, Dinero apostado --> list, int, int
     OBJ: Obtiene el beneficio maximo posible de una apuesta por el equipo Grifos de Javi Potter
     RETURN: Devuelve la cantidad máxima posible (float)
    """
    #lista de probabilidades
    probabilidades = calcular_probabilidades_vc(vc) 
     #lista de probabilidad de ganar un partido 
    probabilidades_ganar = calcular_probabilidad_ganar_1_partido(probabilidades)
    #en la lista en la posicion 0 esta la probabilidad de ganar de los grifos 1 partido
    probabilidad_grifos_ganar = math.pow(probabilidades_ganar[0], N) 

    ganancias_maximas = D / probabilidad_grifos_ganar

    return ganancias_maximas

# Ejemplo de uso ejercicio 6
vc = [5, 4, 3, 2]  # Valores de Calidad de los equipos (Grifos, Serpientes, Cuervos, Tejones)
N = 3  # Cantidad de partidos que debe ganar un equipo para ganar el torneo
D = 100  # Cantidad de dinero apostado por Javi Potter

ganancias = calcular_ganancias(vc, N, D)
print("Posibles ganancias si ganan los Grifos:", ganancias)


# CUADERNO TEMA 5: BACKTRACKING Y RECURSIVIDAD

# EJERCICIO 3
"""
Se tiene un número de Tam cifras almacenado en una cadena de texto; por ejemplo, la
cadena dato = 1151451.
Diseñar un algoritmo que mediante técnicas de Backtracking encuentre, de la manera más
eficiente posible, todos los números distintos de N cifras que puedan formarse con los
números de la cadena sin alterar su orden relativo dentro de la misma.
Por ejemplo, si N = 4, son números válidos 1151, 1511 y 1541, pero no 4551 o 5411 que
aunque pueden formarse con los dígitos de la cadena dato implican una reordenación.
"""

def backtracking_numeros(N, cadena):
    """ 
     ARGS:  N, cadena --> int, str
     OBJ: Esta función recibe como parámetros N, que es la longitud de las combinaciones posibles, y la cadena de números
     RETURN: Devuelve un conjunto con las combinaciones posibles combinaciones 
    """
    def backtrack(comb, index):
        """
         ARGS:  comb, index --> str, int
         OBJ: Esta función recibe como parámetros la combinación de string y un índice para añadir y comparar. Dependiendo de 
         cuanta sea la longitud de las subcadenas, y de los que esten ya incluidos en visitados, obtendrá mediante llamadas recursivas sucesivas todas
         las posibles subcadenas ordenadas de números.
         RETURN: Devuelve el conjunto de todas las subcadenas ordenadas válidas de números
        """
        # variable para ambas funciones (nonlocal)
        nonlocal visitados 
        if len(comb) == N:
            # se asegura que no se añadan repetidos (el add para conjuntos no añade duplicados)
            visitados.add(comb) 
            return
        # si el índice coincide con el final de la cadena, ya no se pueden añadir más elementos 
        if index == len(cadena): 
            return
        # en el rango de tantos carácteres numéricos tenga la cadena 
        for i in range(index, len(cadena)): 
            # llamada recursiva añadiendo a la combinación el siguiente carácter y moviendo el índice 1 a la derecha
            backtrack(comb + cadena[i], i + 1) 
    #estableces un conjunto vacío
    visitados = set() 
    #primera llamada recursiva de bakctrack con cadena vacia y el primer índice de la cadena (0)
    backtrack('', 0) 
    return visitados

# Ejemplo de uso ejercicio 3  
N = 4
cadena = '1151451'
resultados = backtracking_numeros(N, cadena)
print("Números válidos de", N, "cifras:", resultados)


# EJERCICIO 6
"""
Se tiene la tabla de sustitución que aparece a continuación:

                | A | B | C | D |
             A  | b | b | a | d |
             B  | c | a | d | a | 
             C  | b | a | c | c | 
             D  | d | c | d | b | 

que se usa de la manera siguiente: en una cadena cualquiera, dos caracteres consecutivos
se pueden sustituir por el valor que aparece en la tabla, utilizando el primer carácter como
fila y el segundo carácter como columna. Por ejemplo, se puede cambiar la secuencia ca
por una b, ya que M[c,a]=b.
Implementar un algoritmo Backtracking que, a partir de una cadena no vacía texto y
utilizando la información almacenada en una tabla de sustitución M, sea capaz de
encontrar la forma de realizar las sustituciones que permite reducir la cadena texto a un
carácter final, si es posible.
Ejemplo: Con la cadena texto=acabada y el carácter final=d, una posible forma de
sustitución es la siguiente (las secuencias que se sustituyen se marcan para mayor
claridad): acabada  acacda  abcda  abcd  bcd  bc  d
"""

def sustituir(cadena, M, final, visitados):
    """
     ARGS:  cadena, Diccionario datos, caracter final, combinaciones visitadas --> str, dict, str o char, map
     OBJ: Recibe como parametros la cadena, el diccionario con la matriz de combinaciones, el caracter objetivo a lograr y las combinaciones hechas (inicialmente no habrá), 
     pero conforme se hagan llamadas habrán combinaciones previamente hechas que gestionar
     RETURN: Devuelve None si no se encuentra solución y si entra en el if devuelve la cadena final (letra objetivo)
    """
    # Si la cadena ya es igual al carácter final, retornamos la cadena
    if cadena == final:
        return cadena
    # Recorremos la cadena
    for i in range(len(cadena)-1):
        # Formamos el par de caracteres a sustituir
        par = cadena[i:i+2] 
        # Verificamos si el par está en la tabla de sustitución
        if par in M:
            # Sustituimos el par por el valor correspondiente en la tabla de sustitución
            nueva_cadena = cadena[:i] + M[par] + cadena[i+2:]
            # Si la nueva cadena no ha sido visitada antes
            if nueva_cadena not in visitados: 
                # Agregamos la nueva cadena a la lista de visitados
                visitados.add(nueva_cadena)
                # Llamamos recursivamente a la función con la nueva cadena
                resultado = sustituir(nueva_cadena, M, final, visitados)
                # Si se encuentra una solución, retornamos la cadena resultante
                if resultado:
                    return resultado
    # Si no se encontró ninguna solución, retornamos None
    return None 

# Ejemplo de uso ejercicio 6
texto = "acabad"
final = "d"
M = {"aa":"b", "ab": "b", "ac": "a", "ad": "d", "ba": "c", "bb": "a", "bc": "d", "bd": "a", "ca": "b", "cb": "a", "cc": "c", "cd": "c", "da": "d", "db": "c", "dc": "d", "dd": "b"}
visitados = set() 
resultado = sustituir(texto, M, final, visitados) 
if resultado:
    print("Cadena reducida a un solo carácter:", resultado)
else:
    print("No se encontró solución")




