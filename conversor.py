def conversor(tipoPesos, valorDolar):
    pesos =input("¿Cuantos pesos " + tipoPesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valorDolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas 🤑

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 4808.59)
elif opcion == 2:
    conversor("argentinos", 171.77)
elif opcion == 3:
    conversor("mexicanos", 19.67)
else:
    print("Opcion incorrecta")