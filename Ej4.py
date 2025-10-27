try:
    num1 = float(input("Introduce un numero: "))
    num2 = float(input("Introduce un numero: "))
    num3 = float(input("Introduce un numero: "))
except ValueError:
    print("Valor erroneo")

num1 *= 0.15
num2 *= 0.35
num3 *= 0.5

result = num1+num2+num3
print(f"Resultado: {result:f}")