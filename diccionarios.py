def run():
    miDiccionario = {
        "Llave1": 1,
        "Llave2": 2,
        "Llave3": 3,
    }
    #print(miDiccionario["Llave1"])
    #print(miDiccionario["Llave2"])
    #print(miDiccionario["Llave3"])

    poblacionPaises = {
        "Argentina": 44938712,
        "Brasil": 210147125,
        "Colombia": 50372424,
    }

    #print(poblacionPaises["Argentina"])

    #for pais in poblacionPaises.keys():
    #    print(pais)

    #for pais in poblacionPaises.values():
    #    print(pais)

    for pais, poblacion in poblacionPaises.items():
        print(pais + " Tiene " + str(poblacion) +  " Habitantes<")    



if __name__ == "__main__" : 
    run()