from Nodo_Circular import Nodo 

class ListaCircula():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def es_vacia(self):
        return self.primero is None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.es_vacia():
            self.primero = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
        self.ultimo = nuevo_nodo
        self.ultimo.siguiente = self.primero

    def mostrar(self):
        if self.es_vacia():
            print("La lista esta vacia")
            return
        nodo_actual = self.primero
        while True:
            print(nodo_actual.dato, end="->")
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                break
        print()

    def buscar(self, dato):
        if self.primero is None:
            return False
        
        nodo_actual = self.primero
        while True:
            if nodo_actual.dato == dato:
                return True
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                return False

    def modificar(self, dato, nuevo_dato):
        if self.primero is None:
            return False
        nodo_actual = self.primero
        while True:
            if nodo_actual.dato == dato:
                nodo_actual.dato = nuevo_dato
                return True
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                return False

    def eliminar(self, dato):
        if self.primero is None:
            return

        if self.primero.dato == dato:
            if self.primero.siguiente == self.primero:
                self.primero = None
                return
            ultimo_nodo = self.primero
            while ultimo_nodo.siguiente != self.primero:
                ultimo_nodo = ultimo_nodo.siguiente
            ultimo_nodo.siguiente = self.primero.siguiente
            self.primero = self.primero.siguiente
            return

        nodo_actual = self.primero
        while nodo_actual.siguiente != self.primero:
            if nodo_actual.siguiente.dato == dato:
                nodo_actual.siguiente = nodo_actual.siguiente
                return
            nodo_actual = nodo_actual.siguiente