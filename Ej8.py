import time

cadena = input("Introduzca una frase: \t")
cRemplazado = input("Introduzca el caracter que quiere reemplazar: ")
cIntroducido = input("Introduzca el caracter que quiere introducir: ")

if len(cRemplazado) > 1 or len(cIntroducido) > 1:
    time.sleep(3)
    print("Solo puedes introducir un caracter")
else:
    cadena = cadena.replace(cRemplazado, cIntroducido)
    print(cadena)