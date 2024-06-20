
from LogicaClase22 import *
import tkinter as tk
from tkinter import ttk
import time

class InterfazFila(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fila de Personas")
        self.fila = ListaEnlazada()  # Asumimos que la clase ListaEnlazada está importada y disponible
        self.atendidos = 0 # inicializanos en 0 
        self.configurar_interfaz()

    def configurar_interfaz(self):
        # Configurar el frame de entrada
        entrada_frame = tk.Frame(self)
        entrada_frame.pack(pady=10)

        entrada_label = tk.Label(entrada_frame, text="Ingresar persona:")
        entrada_label.pack(side=tk.LEFT)

        self.entrada_persona = tk.Entry(entrada_frame)
        self.entrada_persona.pack(side=tk.LEFT)

        boton_encolar = tk.Button(entrada_frame, text="Encolar", command=self.encolar_persona)
        boton_encolar.pack(side=tk.LEFT)

        # Configurar el frame de la fila
        fila_frame = tk.Frame(self)
        fila_frame.pack(pady=10)

        fila_label = tk.Label(fila_frame, text="Fila:")
        fila_label.pack()

        self.fila_treeview = ttk.Treeview(fila_frame, columns=("Ticket", "Persona"))
        self.fila_treeview.heading("#0", text="")
        self.fila_treeview.heading("Ticket", text="Ticket")
        self.fila_treeview.heading("Persona", text="Persona")
        self.fila_treeview.pack()

        # Configurar el frame de la persona atendida
        atendido_frame = tk.Frame(self)
        atendido_frame.pack(pady=10)

        atendido_label = tk.Label(atendido_frame, text="Persona atendida:")
        atendido_label.pack(side=tk.LEFT)

        self.atendido_texto = tk.Label(atendido_frame, text="")
        self.atendido_texto.pack(side=tk.LEFT)

        self.procesar_fila()

    def encolar_persona(self):
        persona = self.entrada_persona.get()
        if persona:
            ticket = self.fila.encolar(persona)
            self.entrada_persona.delete(0, tk.END)
            print(f"Persona '{persona}' encolada con el ticket {ticket}")
            self.actualizar_fila()

    def actualizar_fila(self):
        self.fila_treeview.delete(*self.fila_treeview.get_children())

        fila_temporal = self.fila.recorrer_fila_obtener()
        nodo_actual = fila_temporal.cabeza
        while nodo_actual is not None:
            self.fila_treeview.insert("", tk.END, text="", values=(nodo_actual.ticket, nodo_actual.persona))
            nodo_actual = nodo_actual.siguiente

    def atender_persona(self, persona, ticket):
        self.atendido_texto.config(text=f"{ticket} - {persona}")

    def procesar_fila(self):
        if self.fila.cabeza is not None:
            persona_atendida = self.fila.desencolar()
            if persona_atendida:
                self.atender_persona(persona_atendida.persona, persona_atendida.ticket)
                self.actualizar_fila()  # Actualizar la fila para eliminar la persona atendida
                self.after(10000, self.eliminar_persona)  # Llamar a método para eliminar persona después de 10 segundos
            else:
                self.after(10000, self.procesar_fila)  # Si no hay persona atendida, continuar con la siguiente
        else:
            self.after(10000, self.procesar_fila)  # Si no hay personas en la fila, continuar con la siguiente

    def eliminar_persona(self):
        self.atendidos += 1  # Incrementar contador de personas atendidas
        self.atendido_texto.config(text=str(self.atendidos))  # Actualizar texto del contador de personas atendidas
        self.actualizar_fila()  # Actualizar la fila para eliminar la persona atendida
        self.procesar_fila()  # Continuar con el procesamiento de la fila
    # Llamar recursivamente después de 10 segundos



app = InterfazFila()
app.mainloop()