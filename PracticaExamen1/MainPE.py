from NodoPE import ListaDoblementeEnlazada
from LogicaPE import Medico, Paciente

# Lista de médicos
lista_medicos = ListaDoblementeEnlazada()

# Función para registrar un médico
def registrar_medico():
    id_medico = int(input("Ingrese el ID del médico: "))
    existe_medico = False
    nodo_actual = lista_medicos.cabeza
    while nodo_actual is not None:
        if nodo_actual.dato.id_medico == id_medico:
            existe_medico = True
            break
        nodo_actual = nodo_actual.siguiente

    if existe_medico:
        print("Ya existe un médico registrado con ese ID.")
    else:
        nombre_medico = input("Ingrese el nombre del médico: ")
        especialidad_medico = input("Ingrese la especialidad del médico: ")
        medico = Medico(id_medico, nombre_medico, especialidad_medico)
        lista_medicos.insertar(medico)
        print("Médico registrado exitosamente.")

# Función para registrar un paciente
def registrar_paciente():
    cedula = int(input("Ingrese la cédula del paciente: "))
    nombre = input("Ingrese el nombre completo del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    prioridad = int(input("Ingrese la prioridad del paciente (1-Rojo, 2-Amarillo, 3-Verde): "))
    paciente = Paciente(cedula, nombre, edad, prioridad)

    # Buscar el médico con menos pacientes
    nodo_actual = lista_medicos.cabeza
    medico_con_menos_pacientes = None
    min_pacientes = float('inf')
    while nodo_actual is not None:
        medico = nodo_actual.dato
        if len(medico.cola_pacientes._cola) < min_pacientes and medico.cola_pacientes.buscar(cedula) == -1:
            min_pacientes = len(medico.cola_pacientes._cola)
            medico_con_menos_pacientes = medico
        nodo_actual = nodo_actual.siguiente

    if medico_con_menos_pacientes is not None:
        medico_con_menos_pacientes.cola_pacientes.push(paciente, paciente.prioridad)
        print("Paciente registrado exitosamente.")
    else:
        print("No se pudo registrar al paciente debido a que ya está en la cola de algún médico.")

# Función para consultar un médico
def consultar_medico():
    id_medico = int(input("Ingrese el ID del médico: "))
    nodo_actual = lista_medicos.cabeza
    while nodo_actual is not None:
        if nodo_actual.dato.id_medico == id_medico:
            medico = nodo_actual.dato
            print(medico)
            print(medico.cola_pacientes)
            return
        nodo_actual = nodo_actual.siguiente
    print("No se encontró un médico con ese ID.")

# Función para mostrar el siguiente paciente en atender
def mostrar_siguiente_paciente():
    id_medico = int(input("Ingrese el ID del médico: "))
    nodo_actual = lista_medicos.cabeza
    while nodo_actual is not None:
        if nodo_actual.dato.id_medico == id_medico:
            medico = nodo_actual.dato
            if medico.cola_pacientes._cola:
                paciente_atendido = medico.cola_pacientes.pop()
                print(f"Paciente a atender: Cédula: {paciente_atendido.cedula}, Nombre: {paciente_atendido.nombre}, Edad: {paciente_atendido.edad}, Prioridad: {paciente_atendido.prioridad}")
            else:
                print("No hay pacientes en la cola de este médico.")
            return
        nodo_actual = nodo_actual.siguiente
    print("No se encontró un médico con ese ID.")

# Función para consultar un paciente
def consultar_paciente():
    cedula = int(input("Ingrese la cédula del paciente: "))
    nodo_actual = lista_medicos.cabeza
    while nodo_actual is not None:
        medico = nodo_actual.dato
        posicion = medico.cola_pacientes.buscar(cedula)
        if posicion != -1:
            print(f"El paciente se encuentra en la cola del médico: {medico}")
            print(f"Posición en la cola: {posicion + 1}")
            return
        nodo_actual = nodo_actual.siguiente
    print("No se encontró un paciente con esa cédula.")

# Función para mostrar la lista de médicos del primero al último
def mostrar_medicos_adelante():
    print("Lista de médicos del primero al último:")
    lista_medicos.mostrar_adelante()

# Función para mostrar la lista de médicos del último al primero
def mostrar_medicos_atras():
    print("Lista de médicos del último al primero:")
    lista_medicos.mostrar_atras()

# Función recursiva para calcular el total de pacientes por atender
def calcular_total_pacientes(nodo_actual):
    if nodo_actual is None:
        return 0
    else:
        medico = nodo_actual.dato
        total_pacientes = len(medico.cola_pacientes._cola)
        total_pacientes += calcular_total_pacientes(nodo_actual.siguiente)
        return total_pacientes

# Menú principal
while True:
    print("\nMenú principal:")
    print("1. Registrar Médico")
    print("2. Registrar Paciente")
    print("3. Consultar Médico")
    print("4. Mostrar el siguiente paciente en atender")
    print("5. Consultar Paciente")
    print("6. Mostrar lista de médicos del primero al último")
    print("7. Mostrar lista de médicos del último al primero")
    print("8. Calcular el total de pacientes por atender")
    print("9. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        registrar_medico()
    elif opcion == "2":
        registrar_paciente()
    elif opcion == "3":
        consultar_medico()
    elif opcion == "4":
        mostrar_siguiente_paciente()
    elif opcion == "5":
        consultar_paciente()
    elif opcion == "6":
        mostrar_medicos_adelante()
    elif opcion == "7":
        mostrar_medicos_atras()
    elif opcion == "8":
        total_pacientes = calcular_total_pacientes(lista_medicos.cabeza)
        print(f"El total de pacientes por atender es: {total_pacientes}")
    elif opcion == "9":
        break
    else:
        print("Opción inválida. Por favor, intente nuevamente.")