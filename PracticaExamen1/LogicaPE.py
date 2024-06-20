
from NodoPE import ColaPrioridad

class Medico:
    def __init__(self, id_medico, nombre, especialidad):
        self.id_medico = id_medico
        self.nombre = nombre
        self.especialidad = especialidad
        self.cola_pacientes = ColaPrioridad()

    def __str__(self):
        return f"ID: {self.id_medico}, Nombre: {self.nombre}, Especialidad: {self.especialidad}, Pacientes por atender: {len(self.cola_pacientes._cola)}"

class Paciente:
    def __init__(self, cedula, nombre, edad, prioridad):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        self.prioridad = prioridad
