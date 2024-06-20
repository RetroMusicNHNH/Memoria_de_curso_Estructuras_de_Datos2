import heapq

# Nodo para lsita doblemnte enlazada.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def eliminar(self, dato):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.dato == dato:
                if nodo_actual == self.cabeza:
                    self.cabeza = nodo_actual.siguiente
                    if self.cabeza is not None:
                        self.cabeza.anterior = None
                else:
                    if nodo_actual == self.cola:
                        self.cola = nodo_actual.anterior
                        self.cola.siguiente = None
                    else:
                        nodo_anterior = nodo_actual.anterior
                        nodo_siguiente = nodo_actual.siguiente
                        nodo_anterior.siguiente = nodo_siguiente
                        nodo_siguiente.anterior = nodo_anterior
                return
            nodo_actual = nodo_actual.siguiente

    def mostrar_adelante(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente

    def mostrar_atras(self):
        nodo_actual = self.cola
        while nodo_actual is not None:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.anterior

# Nodo para colas de prioridad.

class ColaPrioridad:
    def __init__(self):
        self._cola = []
        self._indice = 0

    def push(self, dato, prioridad):
        heapq.heappush(self._cola, (-prioridad, self._indice, dato))
        self._indice += 1

    def pop(self):
        return heapq.heappop(self._cola)[-1]

    def buscar(self, cedula):
        for i, (_, _, paciente) in enumerate(self._cola):
            if paciente.cedula == cedula:
                return i
        return -1

    def __str__(self):
        cadena = ""
        for _, _, paciente in self._cola:
            cadena += f"Cédula: {paciente.cedula}, Nombre: {paciente.nombre}, Edad: {paciente.edad}, Prioridad: {paciente.prioridad}\n"
        return cadena
