import heapq

# Representación del grafo
grafo = {
    'A': {'B': 1, 'C': 1},
    'B': {'D': 1, 'E': 1},
    'C': {'F': 1, 'G': 1, 'H' : 1},
    'D': {},
    'E': {'I': 1, 'J': 1},
    'F': {},
    'G': {'J': 1},
    'H': {'K': 1},
    'I': {'L': 1},
    'J': {},
    'K': {'L': 1},
    'L': {}
}

# Valores heurísticos
heuristica = {
    'A': 12, 'B': 7, 'C': 6, 'D': 3, 'E': 4,
    'F': 9, 'G': 10, 'H': 8, 'I': 1, 'J': 0,
    'K': 2, 'L': 0
}

# Algoritmo A*
def a_estrella(inicio, objetivos):
    abiertos = []  # Lista de prioridad
    
    # Inserta el nodo de inicio en la lista de abiertos con su valor F(n)
    heapq.heappush(abiertos, (heuristica[inicio], inicio))  # (F(n), nodo) 
    cerrados = set()  
    costos = {inicio: 0}  # g(n): el costo acumulado desde el nodo de inicio
    padres = {inicio: None}  # Para rastrear el camino

    while abiertos:
        f_actual, nodo_actual = heapq.heappop(abiertos)  # Extrae el nodo con menor F(n)
        
        # Si alcanzamos un nodo objetivo, terminamos
        if nodo_actual in objetivos:
            print(f"¡Nodo objetivo alcanzado: {nodo_actual}!")
            camino = []
            while nodo_actual is not None:
                camino.append(nodo_actual)
                nodo_actual = padres[nodo_actual]
            print("Camino: ", ' -> '.join(camino[::-1]))  # Imprime el camino en orden desde el inicio
            print("Costo total: ", costos[camino[0]])  # Costo del nodo objetivo
            return

        cerrados.add(nodo_actual)
        print(f"Nodo explorado: {nodo_actual}, F = {f_actual}")
        
        # Expandir los vecinos
        for vecino, costo_transicion in grafo[nodo_actual].items():
            if vecino in cerrados:
                continue
            
            g_nuevo = costos[nodo_actual] + costo_transicion  # Costo acumulado
            f_nuevo = g_nuevo + heuristica[vecino]  # Cálculo de F(n)
            
            # Si encontramos un camino más barato, lo agregamos
            if vecino not in costos or g_nuevo < costos[vecino]:
                costos[vecino] = g_nuevo
                padres[vecino] = nodo_actual 
                heapq.heappush(abiertos, (f_nuevo, vecino)) 
                print(f"  Nodo agregado a abiertos: {vecino}, F = {f_nuevo}")
        print("")

# Ejecutar
a_estrella('A', {'L', 'J'})
