try:
    num = int(input("Introduce un numero: "))
    while num % 2 == 0:
        num = int(input("Introduce un numero: "))
except ValueError:
    print("Valor erroneo")