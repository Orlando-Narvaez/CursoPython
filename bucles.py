def run():
    LIMITE = 1000000

    contador = 0
    potencia2 = 2**contador

    while potencia2 < LIMITE:
        print("2 elevado a " + str(contador) + " es igual a " + str(potencia2))
        contador += 1
        potencia2 = 2**contador


if __name__ == '__main__':
    run()