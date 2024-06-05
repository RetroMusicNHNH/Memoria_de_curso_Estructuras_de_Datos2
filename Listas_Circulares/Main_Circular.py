from Logica_Circular import *

miLista = ListaCircula()
numero = 0 
opcion = 0

while opcion != 6:
    try:
        opcion= int(input("Digite la opción que requiera: \n"
                            "1.Ingresar \n"
                            "2.Mostrar \n"
                            "3.Buscar \n" 
                            "4.Modificar \n"
                            "5.Eliminar \n"
                            "6.Salir\n:"))
        match opcion:
            case 1: 
                numero= int(input("Digite el número que desea inserta: "))
                miLista.agregar(numero)
                print("Se ha agregado correctamente...\n")
            case 2:
                print(miLista.mostrar())
            case 3:
                numero= int(input("Digite el número que desea buscar:"))
                if (miLista.buscar(numero)):
                    print("Número encontrado")

                else:
                    print("El número no se encuentra en la lista")
                
            case 4:
                dato = int(input("Ingresa el número a modificar: "))
                nuevo_dato = int(input("Ingresa el nuevo número: "))
                if miLista.modificar(dato, nuevo_dato):
                    print(f"Se ha modificado el número {dato} por {nuevo_dato}")
                else:
                    print(f"No se encontró el número {dato} en la lista")
            case 5:
                numero = int(input("Digite el número a elimiar: "))
                miLista.eliminar(numero)
                print(f"Se ha elimido el numero: {numero} \n")
            case 6:
                print("Saliendo del programa...")
    except ValueError:
        print("Por favor, ingresa un número válido.")
