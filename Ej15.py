dict_pizzas = {"Barbacoa": 12.5, "Picante": 9.99, "4 quesos": 11}
dict_ingredientes =  {"Peperoni": 0.5, "Chorizo": 0.75, "Bacon": 1, "Esparragos": 0.25}
ingredientes_elegidos = []
cuentaTotal = 0

try:
    saldo = int(input("Introduzca el saldo que tiene: "))
except ValueError:
    print("Valor erroneo")
    exit()

while True:
    if saldo < 0:
        exit()

    print("Bienvenido a Pizzeria La Beata. Esta es nuestra carta:")
    print("1-   Barbacoa    12.5€")
    print("2-   Picante     9.99€")
    print("3-   4 quesos    11€")
    try:
        pizzaElegida = input("Escoga la pizza por su nombre: ").lower().capitalize()
    except ValueError:
        print("Valor erroneo")
        exit()

    if pizzaElegida in dict_pizzas and saldo > dict_pizzas[pizzaElegida]:
        print(f"Has elegido la pizza {pizzaElegida} que vale {dict_pizzas[pizzaElegida]}€")
        saldoProvisional = saldo-dict_pizzas[pizzaElegida]
        cuentaTotal += dict_pizzas[pizzaElegida]
        print(f"Te queda {saldoProvisional}€")
        try:
            quiereIngredientes = input("¿Desea usted ingredientes?: ").lower()
        except ValueError:
            print("Valor erroneo")

        while quiereIngredientes == "si":
            print("Este es nuestro menu de ingredientes: ")
            print("1-   Peperoni    0.5€")
            print("2-   Chorizo    0.75€")
            print("3-   Bacon    1€")
            print("4-   Esparragos    0.25€")
            try:
                ingrediente = input("Introduce el ingrediente que desea: ").lower().capitalize()
            except ValueError:
                print("Valor erroneo")

            if ingrediente in dict_ingredientes :
                if dict_ingredientes[ingrediente] < saldoProvisional:
                    ingredientes_elegidos.append(ingrediente)
                    saldoProvisional -= dict_ingredientes[ingrediente]
                    cuentaTotal += dict_ingredientes[ingrediente]
                    print(f"Ingrediente elegido, te queda {saldoProvisional}")
                    try:
                        quiereIngredientes = input("¿Desea mas ingredientes?: ").lower()
                    except ValueError:
                        print("Valor erroneo")
                else:
                    print("Saldo insuficiente")
                    break
            else:
                print("El ingrediente no se encuentra en nuestro menu")
                try:
                    quiereIngredientes = input("¿Desea mas ingredientes?: ").lower()
                except ValueError:
                    print("Valor erroneo")

    try:
        nuevoPedido = input("¿Desea realizar de nuevo su pedido?:").lower()
    except ValueError:
        print("Valor erroneo")

    if nuevoPedido == "si" or saldo < 0:
        print("Cargando nuevo pedido...")
    else:
        print("\nTicket compra: ")
        print(f"Pizza : {pizzaElegida}      {dict_pizzas[pizzaElegida]}€")
        for i in range(len(ingredientes_elegidos)):
            print(f"Ingrediente: {ingredientes_elegidos[i]}   {dict_ingredientes[ingredientes_elegidos[i]]}€")
        print(f"Total a pagar:  {cuentaTotal}€")
        exit()




