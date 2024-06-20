from nodoClase22 import *

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 1
        self.persona_atendida = None

    def encolar(self, persona):
        nuevo_nodo = Nodo(persona, self.contador)
        if self.cola is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.contador += 1
        return nuevo_nodo.ticket

    def desencolar(self):
        if self.cabeza is not None:
            dato = self.cabeza
            self.cabeza = self.cabeza.siguiente
            if self.cabeza is None:
                self.cola = None
            self.persona_atendida = dato
        else:
            dato = None
        return dato

    def recorrer_fila_obtener(self):
        fila_temporal = ListaEnlazada()
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            fila_temporal.encolar_nodo(Nodo(nodo_actual.persona, nodo_actual.ticket))
            nodo_actual = nodo_actual.siguiente
        return fila_temporal

    def encolar_nodo(self, nodo):
        if self.cola is None:
            self.cabeza = nodo
            self.cola = nodo
        else:
            self.cola.siguiente = nodo
            self.cola = nodo

    def recorrer_fila(self, funcion):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            funcion(nodo_actual)
            nodo_actual = nodo_actual.siguiente