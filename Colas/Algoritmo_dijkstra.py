import heapq

def dijkstra(grafo, nodo_inicial):
    # Crear un diccionario para almacenar las distancias más cortas
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[nodo_inicial] = 0

    # Crear un diccionario para almacenar los nodos previos en la ruta más corta
    previos = {nodo: None for nodo in grafo}

    # Crear una cola de prioridad para ordenar los nodos por distancia
    cola_prioridad = [(0, nodo_inicial)]

    while cola_prioridad:
        # Extraer el nodo con la distancia mínima de la cola de prioridad
        dist_actual, nodo_actual = heapq.heappop(cola_prioridad)

        # Si la distancia en la cola de prioridad es mayor que la distancia actual,
        # significa que ya se encontró una ruta más corta, por lo que se ignora
        if dist_actual > distancias[nodo_actual]:
            continue

        # Visitar cada vecino del nodo actual
        for vecino, peso in grafo[nodo_actual].items():
            # Calcular la distancia tentativa al vecino
            distancia_tentativa = distancias[nodo_actual] + peso

            # Si la distancia tentativa es menor que la distancia actual del vecino,
            # actualizar la distancia y el previo, y agregar el vecino a la cola de prioridad
            if distancia_tentativa < distancias[vecino]:
                distancias[vecino] = distancia_tentativa
                previos[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia_tentativa, vecino))

    return distancias, previos

# Ejemplo de uso
grafo = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

nodo_inicial = 'A'
distancias, previos = dijkstra(grafo, nodo_inicial)

print(f"Distancias desde el nodo '{nodo_inicial}':")
for nodo, distancia in distancias.items():
    print(f"{nodo}: {distancia}")

print("\nRutas más cortas:")
for nodo in grafo:
    if nodo != nodo_inicial:
        ruta = [nodo]
        previo = previos[nodo]
        while previo is not None:
            ruta.append(previo)
            previo = previos[previo]
        ruta.reverse()
        print(f"{nodo_inicial} -> {' -> '.join(ruta)}")