from Main_Nodo import Nodo


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodo):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar(valor, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar(valor, nodo.derecha)

    def buscar(self, valor):
        return self._buscar(valor, self.raiz)

    def _buscar(self, valor, nodo):
        if nodo is None:
            return False
        elif nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._buscar(valor, nodo.izquierda)
        else:
            return self._buscar(valor, nodo.derecha)

    def recorrer_inorden(self):
        self._recorrer_inorden(self.raiz)

    def _recorrer_inorden(self, nodo):
        if nodo:
            self._recorrer_inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            self._recorrer_inorden(nodo.derecha)

# Ejemplo de uso
arbol_busqueda = ArbolBinarioBusqueda()
arbol_busqueda.insertar(5)
arbol_busqueda.insertar(3)
arbol_busqueda.insertar(7)
arbol_busqueda.insertar(1)
arbol_busqueda.insertar(4)

print("Búsqueda de 4:", arbol_busqueda.buscar(4))  # Salida: True
print("Búsqueda de 6:", arbol_busqueda.buscar(6))  # Salida: False

print("Recorrido inorden:")
arbol_busqueda.recorrer_inorden()  # Salida: 1 3 4 5 7