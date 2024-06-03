from Nodo import Nodo
class ListaEnlazada():
    def __init__(self):
        self.primero=None
        self.ultimo =None

    def get_primero(self):
        return self.primero

    def set_primero(self, nuevo_primero):
        self.primero = nuevo_primero

    def get_ultimo(self):
        return self.ultimo

    def set_ultimo(self, nuevo_ultimo):
        self.ultimo = nuevo_ultimo
    
    def insertarNodo(self, dato):
        nodoNuevo = Nodo(dato)
        if self.get_primero() == None:
            self.primero = nodoNuevo
            self.primero.set_siguiente(None)
            self.ultimo = self.primero
            print("inserte bien 1")
        else:
            self.ultimo.set_siguiente(nodoNuevo)
            nodoNuevo.set_siguiente(None)
            self.ultimo=nodoNuevo
            print("inserte bien 2")

    def mostrarLista(self):
        nodoActual = self.primero
        listaString = ""
        while nodoActual != None:
            listaString = listaString + str(nodoActual.get_dato()) + "\n"
            nodoActual = nodoActual.get_siguiente()
        return listaString

    def buscarNodo(self, dato):
        nodoActual = self.primero
        encontrado= False
        while nodoActual != None:
            if nodoActual.get_dato() == dato:
               encontrado = True
            nodoActual = nodoActual.get_siguiente()
        return encontrado
    
    def modificarNodo(self):
        numero= int(input("Digite el número que desea buscar:"))
        nodoActual = self.primero
        modificado= False
        while nodoActual != None:
            if nodoActual.get_dato() == numero:
                nuevoNumero = int(input("Digite el NUEVO número que desea:"))
                nodoActual.set_dato(nuevoNumero)
                modificado = True
            nodoActual = nodoActual.get_siguiente()
        return modificado
    
    def eliminarNodo(self):
        numero= int(input("Digite el número que desea eliminar:"))
        nodoActual = self.primero

        if nodoActual is not None and nodoActual.get_dato() == numero:
            self.primero = nodoActual.get_siguiente()
            nodoActual = None
            return

        anterior = None
        while nodoActual is not None and nodoActual.get_dato() != numero:
            anterior = nodoActual
            nodoActual = nodoActual.get_siguiente()

        if nodoActual is None:
            return

        anterior.set_siguiente(nodoActual.get_siguiente())
        nodoActual = None