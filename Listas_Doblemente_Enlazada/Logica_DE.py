import random
from Nodo_DE import Nodo

class ListaAtletas:
    """ Clase que representa una lista doblemente enlazada de atletas.
    Atributos:
        cabeza (Nodo): Referencia al primer nodo de la lista.
        cola (Nodo): Referencia al último nodo de la lista.
    """
    def __init__(self):
        """ Inicializa una lista doblemente enlazada vacía. """
        self.cabeza = None
        self.cola = None
        self.cantidad = 0
        self.correr_realizado = False

    def agregar_atleta(self, nombre, numero):
        """ Agrega un nuevo atleta al final de la lista.
        Args:
            nombre (str): Nombre del atleta.
            numero (int): Número del atleta.
        """
        nuevo_nodo = Nodo((nombre, numero))
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def buscar_atleta(self, numero):
        """ Busca un atleta por su número en la lista.
        Args:
            numero (int): Número del atleta.
        Returns:
            Nodo: Nodo que contiene los datos del atleta, o None si no se encuentra.
        """
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.dato[1] == numero:
                return nodo_actual
            nodo_actual = nodo_actual.siguiente
        return None

    def mostrar_posiciones(self):
        """ Muestra las posiciones de los atletas en la lista. """
        if self.cabeza is None:
            print("La lista de atletas está vacía.")
            return

        nodo_actual = self.cabeza
        while nodo_actual is not None:
            atras = self.cola.dato[1] if nodo_actual.anterior is None else nodo_actual.anterior.dato[1]
            delante = self.cabeza.dato[1] if nodo_actual.siguiente is None else nodo_actual.siguiente.dato[1]
            print(f"Detrás del atleta {nodo_actual.dato[1]} va el {atras}, delante del {nodo_actual.dato[1]} va el {delante}.")
            nodo_actual = nodo_actual.siguiente


    def modificar_atleta(self, numero, nuevo_nombre):
        """ Modifica el nombre de un atleta en la lista.
        Args:
            numero (int): Número del atleta.
            nuevo_nombre (str): Nuevo nombre del atleta.
        """
        nodo_actual = self.buscar_atleta(numero)
        if nodo_actual is not None:
            nodo_actual.dato = (nuevo_nombre, numero)
        else:
            print(f"No se encontró el atleta con número {numero}")

    def eliminar_atleta(self, numero):
        """ Elimina un atleta de la lista.
        Args:
            numero (int): Número del atleta.
        """
        nodo_actual = self.buscar_atleta(numero)
        if nodo_actual is not None:
            if nodo_actual.anterior is None:
                self.cabeza = nodo_actual.siguiente
                if self.cabeza is not None:
                    self.cabeza.anterior = None
            else:
                nodo_actual.anterior.siguiente = nodo_actual.siguiente
                if nodo_actual.siguiente is not None:
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
        else:
            print(f"No se encontró el atleta con número {numero}")

    def correr(self):
        """ Mueve a todos los atletas a la siguiente posición en la lista. """
        if self.cabeza is None:
            return
        self.correr_realizado = True

        # Obtener el último nodo y desconectarlo de la lista
        ultimo_nodo = self.cola
        self.cola = ultimo_nodo.anterior
        self.cola.siguiente = None

        # Conectar el último nodo al principio de la lista
        ultimo_nodo.anterior = None
        ultimo_nodo.siguiente = self.cabeza
        self.cabeza.anterior = ultimo_nodo
        self.cabeza = ultimo_nodo

    def pasar_competidor(self, numero_origen, numero_destino):
        """ Intercambia las posiciones de dos atletas en la lista.
        Args:
            numero_origen (int): Número del atleta de origen.
            numero_destino (int): Número del atleta de destino.
        """

        if not self.correr_realizado:
            print("Debe correr al menos una vez antes de pasar competidor.")
            return

        nodo_origen = self.buscar_atleta(numero_origen)
        nodo_destino = self.buscar_atleta(numero_destino)
        if nodo_origen is not None and nodo_destino is not None:
            # Intercambiar las posiciones de los nodos
            if nodo_origen.anterior is None:
                self.cabeza = nodo_destino
            else:
                nodo_origen.anterior.siguiente = nodo_destino
            if nodo_destino.siguiente is None:
                self.cola = nodo_origen
            else:
                nodo_destino.siguiente.anterior = nodo_origen
            nodo_origen.siguiente, nodo_destino.anterior = nodo_destino.anterior, nodo_origen.siguiente
            nodo_origen.anterior, nodo_destino.siguiente = nodo_destino, nodo_origen
            print(f"El atleta {numero_origen} pasa al {numero_destino} corriendo, entonces se intercambian las posiciones: El atleta {numero_origen} pasa a la posición {numero_destino} y el {numero_destino} a la posición {numero_origen}.")
            
            # Actualizar las posiciones después de pasar el competidor
            self.actualizar_posiciones()
            

        else:
            print(f"No se encontraron los atletas con números {numero_origen} y {numero_destino}")

    def actualizar_posiciones(self):
        """ Actualiza las posiciones de los atletas en la lista. """
        nodo_actual = self.cabeza
        posicion = 0
        while nodo_actual is not None:
            nodo_actual.dato = (nodo_actual.dato[0], posicion)
            nodo_actual = nodo_actual.siguiente
            posicion += 1

    def simular_carrera(self, vueltas):
            """ Simula una carrera entre los atletas en la lista.
            Args:
                vueltas (int): Número de vueltas que se realizarán en la carrera.
            """
            if self.cabeza is None:
                print("La lista de atletas está vacía.")
                return

            for vuelta in range(vueltas):
                print(f"\nVuelta {vuelta + 1}:")
                nodo_actual = self.cabeza
                while nodo_actual is not None:
                    avance = random.randint(1, 10)  # Avance aleatorio entre 1 y 10
                    print(f"Atleta {nodo_actual.dato[0]} ({nodo_actual.dato[1]}): Avanza {avance} metros.")
                    nodo_actual = nodo_actual.siguiente

            print("\n¡Carrera terminada!")
            self.mostrar_posiciones()

    def obtener_ganador(self):
        """ Obtiene al ganador de la carrera simulada de forma aleatoria entre los tres atletas.
        Returns:
            tuple: Tupla que contiene el nombre y número del atleta ganador.
        """
        if self.cabeza is None:
            print("La lista de atletas está vacía.")
            return None

        atletas = []
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            atletas.append(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente

        ganador = random.choice(atletas)
        return ganador