class Nodo:
    """ Clase que representa un nodo en una lista doblemente enlazada.
    Atributos:
        dato (tuple): Tupla que contiene el nombre y número del atleta.
        anterior (Nodo): Referencia al nodo anterior en la lista.
        siguiente (Nodo): Referencia al nodo siguiente en la lista.
    """
    def __init__(self, dato):
        """ Inicializa un nuevo nodo con el dato proporcionado.
        Args:
            dato (tuple): Tupla que contiene el nombre y número del atleta.
        """
        self.dato = dato
        self.anterior = None
        self.siguiente = None

