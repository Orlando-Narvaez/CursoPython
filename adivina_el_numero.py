import random

def run():
    print("""
    Bienvenido al juego de adivinar el numero, el computador generara un
    numero aletorio entre el 1 y el 100

    Tienes 7 oportunidades de adivinar el numero
    """)
    numerorandom = random.randint(1, 100)
    numeroelegido = int(input("Introduce un numero entre el 1 y el 100: "))
    print("\n")
    vidas = 7
    while numerorandom != numeroelegido:
        if numerorandom < numeroelegido: 
            print("Elige un numero mas pequeño\n")
            vidas -= 1
        elif numerorandom > numeroelegido : 
            print("Elige un numero mas grande\n")
            vidas -= 1

        if vidas == 0 :
            print("GAME OVER")
            break
        print("Tienes", vidas, "vidas\n")
        numeroelegido = int(input("Introduce numero: "))
        print("\n")
    if numerorandom == numeroelegido : 
        print("FELICIDADES GANASTE")


if __name__ == "__main__" : 
    run()