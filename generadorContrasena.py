import random


def generarContrasena():
    mayusculas = ["A","B","C","D","E"]
    minusculas = ["a","b","c","d","e"]
    simbolos = ["!","·","$","&","/","(",")","="]
    numeros = ["1","2","3", "4","5","6","7","8","9","0"]

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        caracter_randon = random.choice(caracteres)
        contrasena.append(caracter_randon)

    contrasena = "".join(contrasena)
    return contrasena

def run():
    contrasena = generarContrasena()
    print("Tu nueva contraseña es: " + contrasena)



if __name__ == "__main__" : 
    run()