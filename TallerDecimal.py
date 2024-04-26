# Función para verificar si la pila está vacía
def pila_vacia(pila):
    return len(pila) == 0

# Función para insertar elementos en la pila (Push)
def push(pila, elemento):
    pila.append(elemento)
    return pila

# Función para eliminar elementos de la pila (Pop)
def pop(pila):
    if pila_vacia(pila):
        return None
    else:
        return pila.pop()

# Función para convertir un número decimal a binario
def decimal_a_binario(decimal):
    pila = []
    
    while decimal > 0:
        residuo = decimal % 2
        pila = push(pila, residuo)
        decimal = decimal // 2

    binario = ''
    while not pila_vacia(pila):
        binario += str(pop(pila))

    return binario

# Función para convertir un número decimal a octal
def decimal_a_octal(decimal):
    pila = []
    while decimal > 0:
        residuo = decimal % 8
        pila = push(pila, residuo)
        decimal = decimal // 8

    octal = ''
    while not pila_vacia(pila):
        octal += str(pop(pila))

    return octal

# Función para convertir un número decimal a hexadecimal
def decimal_a_hexadecimal(decimal):
    pila = []
    hex_chars = '0123456789ABCDEF'
    while decimal > 0:
        residuo = decimal % 16
        pila = push(pila, residuo)
        decimal = decimal // 16

    hexadecimal = ''
    while not pila_vacia(pila):
        residuo = pop(pila)
        hexadecimal += hex_chars[residuo]

    return hexadecimal

# Menú principal
def main():
    while True:
        print("\nMenú de conversión")
        print("1. Decimal a Binario")
        print("2. Decimal a Octal")
        print("3. Decimal a Hexadecimal")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            decimal = int(input("Ingrese un número decimal: "))
            binario = decimal_a_binario(decimal)
            print(f"El número {decimal} en binario es: {binario}")

        elif opcion == '2':
            decimal = int(input("Ingrese un número decimal: "))
            octal = decimal_a_octal(decimal)
            print(f"El número {decimal} en octal es: {octal}")

        elif opcion == '3':
            decimal = int(input("Ingrese un número decimal: "))
            hexadecimal = decimal_a_hexadecimal(decimal)
            print(f"El número {decimal} en hexadecimal es: {hexadecimal}")

        elif opcion == '4':
            break

        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    main()