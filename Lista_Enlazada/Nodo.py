class Nodo():
    """
    dato = numeros, objetos, palabras, etc
    siguiente = a el siguiente Nodo
    """
    def __init__(self, dato):
        self.dato= dato
        self.siguiente = None
    
    def get_dato(self):
        return self.dato

    def set_dato(self, nuevo_dato):
        self.dato = nuevo_dato

    def get_siguiente(self):
        return self.siguiente

    def set_siguiente(self, nuevo_siguiente):
        self.siguiente = nuevo_siguiente
    
