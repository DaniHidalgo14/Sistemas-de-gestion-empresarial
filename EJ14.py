lista_paises = ["España", "Argentina", "Perú"]
cont = 0

while True :
    print("MENU. Elija una de las siguientes opciones marcando su numero")
    print("1. Imprimir alfabeticamente en orden ascendente")
    print("2. Imprimir alfabeticamente en orden descendente")
    print("3. Añadir pais")
    print("4. Eliminar pais")
    print("5. Salir")
    try:
        opcion = int(input("Introduce la opcion que quieras: "))
    except ValueError:
        print("ERROR")
        exit()

    if opcion == 1 :
        lista_paises.sort()
        for i in range(len(lista_paises)):
            print(f"- {lista_paises[i]}\n")
    elif opcion == 2:
        for i in range(len(lista_paises)):
            lista_paises.sort(reverse=True)
            print(f"- {lista_paises[i]}\n")
    elif opcion == 3:
        if len(lista_paises) < 6:
            nuevoPais = input("Inserta un pais nuevo: ").lower().capitalize()
            if nuevoPais in lista_paises:
                print("Este pais ya esta metido")
            else:
                lista_paises.append(nuevoPais)
                print("Nuevo pais introducido")
        else:
            print("No se pueden introducir mas paises")
    elif opcion == 4:
        if len(lista_paises) > 0:
            paisABorrar = input("Introduce el pais que desea borrar: ").lower().capitalize()
            if paisABorrar in lista_paises:
                lista_paises.remove(paisABorrar)
                print("Pais borrado")
            else:
                print("No se encontro el pais")
        else:
            print("No se pueden borrar mas paises")
    elif opcion == 5:
        print(f"Numero de ejecuciones: {cont}")
        print("Saliendo. Gracias")
        print("##########################################################################################################################")
        exit()
    else:
        print("Opcion no valida")
    cont += 1