import tkinter
from tkinter import messagebox



from ListaEnlazada import ListaEnlazada
miLista = ListaEnlazada()
numero = 0
opcion = 0

while opcion != 6:

    opcion= int(input("Digite la opción que requiera: \n"
                        "1.Ingresar \n"
                        "2.Mostrar \n"
                        "3.Buscar \n" 
                        "4.Modificar \n"
                        "5.Eliminar \n"
                        "6.Salir\n:"))
    match opcion:
        case 1: 
            numero= int(input("Digite el número que desea inserta:"))
            miLista.insertarNodo(numero)
        case 2:
            print(miLista.mostrarLista())
        case 3:
            numero= int(input("Digite el número que desea buscar:"))
            if (miLista.buscarNodo(numero)):
                print("Número encontrado")

            else:
                print("El número no se encuentra en la lista")
            
        case 4:
            miLista.modificarNodo()
            
        case 5:
            miLista.eliminarNodo()
        case 6:
            print("Saliendo del programa...")

        case _:
            print ("Opción inválida")


