def es_valida(expresion):
    # Definir un diccionario que mapea los paréntesis de apertura con los de cierre
    pares = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    # Crear una pila vacía para almacenar los paréntesis de apertura
    pila = []

    # Verificar si la expresión contiene al menos uno de los tipos de paréntesis
    tiene_parentesis = any(char in pares.keys() or char in pares.values() for char in expresion)
    if not tiene_parentesis:
        return False

    # Iterar sobre cada carácter de la expresión
    for caracter in expresion:
        # Si el carácter es un paréntesis de apertura, agregarlo a la pila
        if caracter in pares:
            pila.append(caracter)
        # Si el carácter es un paréntesis de cierre
        elif caracter in pares.values():
            # Si la pila está vacía, la expresión no es válida
            if not pila:
                return False
            # Si el paréntesis de cierre no coincide con el último de la pila, la expresión no es válida
            if pares[pila.pop()] != caracter:
                return False

    # Si la pila está vacía después de recorrer toda la expresión, es válida
    return not pila

while True:
    expresion = input("Ingresa una expresión con operaciones dentro de paréntesis, corchetes o llaves (ejemplo: (a+b), [c*d], {e/f}): ")

    if expresion.strip() == "":
        print("No ingresaste ninguna expresión. Inténtalo nuevamente.")
        continue

    if es_valida(expresion):
        print(f"La expresión '{expresion}' es válida.")
        break
    else:
        print(f"La expresión '{expresion}' no es válida. Verifica que los paréntesis, corchetes o llaves estén balanceados e inténtalo nuevamente.")