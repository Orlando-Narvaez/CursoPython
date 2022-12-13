import random

def run():
    numerorandom = random.randint(1, 100)
    numeroelegido = int(input("Introduce un numero entre el 1 y el 100: "))
    vidas = 5
    while numerorandom != numeroelegido :
        if numerorandom < numeroelegido : 
            print("Elige un numero mas pequeño.")
            vidas -= 1
        elif numerorandom > numeroelegido : 
            print("Elige un numero mas grande.")
            vidas -= 1
        if vidas == 0 :
            print("GAME OVER")
            break
        print("Tienes", vidas, "vidas")
        numeroelegido = int(input("Introduce numero: "))
    if numerorandom == numeroelegido : 
        print("FELICIDADES GANASTE")


if __name__ == "__main__" : 
    run()