from collections import defaultdict
import heapq

# Definimos la clase Grafo
class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)

    # Función para agregar una arista al grafo
    def agregar_arista(self, origen, destino, peso):
        self.grafo[origen].append((destino, peso))
        self.grafo[destino].append((origen, peso))

    # Función para calcular la ruta más corta usando el algoritmo de Dijkstra
    def ruta_mas_corta(self, origen, destino):
        distancias = {nodo: float('inf') for nodo in self.grafo}
        distancias[origen] = 0
        pila = [(0, origen)]

        while pila:
            dist_actual, nodo_actual = heapq.heappop(pila)

            if dist_actual > distancias[nodo_actual]:
                continue

            for vecino, peso in self.grafo[nodo_actual]:
                distancia = dist_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(pila, (distancia, vecino))

        ruta = []
        nodo = destino
        while nodo != origen:
            ruta.append(nodo)
            for vecino, peso in self.grafo[nodo]:
                if distancias[vecino] == distancias[nodo] - peso:
                    nodo = vecino
                    break

        ruta.append(origen)
        ruta.reverse()

        return ruta, distancias[destino]

# caso de uso 
grafo = Grafo()

# Agregamos las aristas (rutas aereas) con sus costos
grafo.agregar_arista('Ciudad A', 'Ciudad B', 5000)
grafo.agregar_arista('Ciudad B', 'Ciudad C', 1500)
grafo.agregar_arista('Ciudad A', 'Ciudad C', 2300)
grafo.agregar_arista('Ciudad A', 'Ciudad D', 1700)
grafo.agregar_arista('Ciudad C', 'Ciudad D', 1150)
grafo.agregar_arista('Ciudad C', 'Ciudad E', 3800)
grafo.agregar_arista('Ciudad D', 'Ciudad E', 1900)

# Calculamos la ruta mas corta de la Ciudad b a la Ciudad d
origen = 'Ciudad B'
destino = 'Ciudad D'
ruta, costo = grafo.ruta_mas_corta(origen, destino)

# Imprimimos la ruta y el costo
print(f"La ruta más corta de {origen} a {destino} es:")
print(' -> '.join(ruta))
print(f"El costo total es: {costo}")