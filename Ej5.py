print("Bienvenido a Calculadora. Este es el menu:")
print(" Sumar \n Restar  \n Multiplicar  \n Dividir  \n Salir")

try:
    num1 = float(input("Introduce un numero: "))
    num2 = float(input("Introduce un numero: "))
except ValueError:
    print("Introduce solo numeros")

opcion = input("Introduzca la opcion que desea realizar: ")
opcion = opcion.lower()

while opcion != "salir":
    if opcion == "sumar":
        result = num1 + num2
        print(f"Resultado: {result}")

    elif opcion == "restar":
        result = num1-num2
        print(f"Resultado: {result}")

    elif opcion == "multiplicar":
        result = num1*num2
        print(f"Resultado: {result}")

    elif opcion == "dividir":
        if num2 == 0:
            print("El divisor no puede ser 0")
        else:
            result = num1 / num2
            print(f"Resultado: {result}")
    else:
        print("Valor no reconocido")
    opcion = input("Introduzca la opcion que desea realizar: ")
    opcion = opcion.lower()
    try:
        num1 = float(input("Introduce un numero: "))
        num2 = float(input("Introduce un numero: "))
    except ValueError:
        print("Introduce solo numeros")