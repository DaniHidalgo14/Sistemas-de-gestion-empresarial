cadena = input("Introduce una frase: ")
cadena.lower()

cadena.replace(" ", "")

caracteres_contados = []

for caracter in cadena:
    if caracter not in caracteres_contados:
        cont = 0
        for c in cadena:
            if c == caracter:
                cont +=1
        print(f"El caracter {caracter} se repite {cont}")
        caracteres_contados.append(caracter)