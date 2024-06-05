from Logica_DE import ListaAtletas

def main():
    lista_atletas = ListaAtletas()
    while True:
        try:
            mostrar_menu()
            opcion = input("---> ")
            if opcion == "1":
                nombre = input("Ingrese el nombre del atleta: ")
                numero = int(input("Ingrese el número del atleta: "))
                lista_atletas.agregar_atleta(nombre, numero)
            elif opcion == "2":
                numero = int(input("Ingrese el número del atleta a buscar: "))
                nodo = lista_atletas.buscar_atleta(numero)
                if nodo is not None:
                    print(f"Atleta encontrado: {nodo.dato}")
                else:
                    print(f"No se encontró el atleta con número {numero}")
            elif opcion == "3":
                if lista_atletas.cabeza is None:
                    print("La lista de atletas está vacía.")
                else:
                    lista_atletas.mostrar_posiciones()
            elif opcion == "4":
                numero = int(input("Ingrese el número del atleta a modificar: "))
                nuevo_nombre = input("Ingrese el nuevo nombre del atleta: ")
                lista_atletas.modificar_atleta(numero, nuevo_nombre)
            elif opcion == "5":
                numero = int(input("Ingrese el número del atleta a eliminar: "))
                lista_atletas.eliminar_atleta(numero)
            elif opcion == "6":
                lista_atletas.correr()
            elif opcion == "7":
                numero_origen = int(input("Ingrese el número del atleta de origen: "))
                numero_destino = int(input("Ingrese el número del atleta de destino: "))
                lista_atletas.pasar_competidor(numero_origen, numero_destino)
                print("Posiciones actualizadas:")
                lista_atletas.mostrar_posiciones()
            elif opcion == "8":
                vueltas = int(input("Ingrese el número de vueltas a simular: "))
                lista_atletas.simular_carrera(vueltas)
                ganador = lista_atletas.obtener_ganador()
                if ganador is not None:
                    print(f"\n¡El ganador es {ganador[0]} con el número {ganador[1]}!")

            elif opcion == "9":
                exit(0)
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")
        except Exception as e:
            print(f"Error: {e}")

def mostrar_menu():
    """ Muestra el menú de opciones. """
    print("Seleccione una opción:")
    print("1. Agregar atleta")
    print("2. Buscar atleta")
    print("3. Mostrar posiciones")
    print("4. Modificar atleta")
    print("5. Eliminar atleta")
    print("6. Correr")
    print("7. Pasar competidor")
    print("8. Simular carrera")
    print("9. Salir")

if __name__ == "__main__":
    main()
