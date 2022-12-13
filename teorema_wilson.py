def esPrimo(numero):
    contador = 1
    for i in range(1,numero):
        contador = contador * i

    if (contador + 1) % numero == 0:
        return True
    else:
        return False
        

def run():
    numero = int(input("Ingrese el numero que desea saber si es primo: "))

    if esPrimo(numero):
        print("Es primo")
    else:
        print("No es primo")


if __name__ == '__main__':
    run()