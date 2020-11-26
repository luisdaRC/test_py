#Changes
def practica():
    goleadores_2014 = {"Muller": ("Alemania", 5),
                       "Dempsey": ("USA", 2),
                       "James": ("Colombia", 6),
                       "Muller": ("Alemania", 5),
                       "Schurrle": ("Alemania", 3),
                       "Messi": ("Argentina", 4),
                       "Suarez": ("Uruguay", 2),
                       "van Persie": ("Holanda", 4),
                       "Benzema": ("Francia", 3),
                       "Klose": ("Alemania", 2),
                       "Robben": ("Holanda", 3),
                       "Valencia": ("Ecuador", 3),
                       "Neymar": ("Brasil", 4),
                       "Shaqiri": ("Suiza", 3),
                       "Kroos": ("Alemania", 2),
                       "Luiz": ("Brasil", 2)
                       }

    #Ejercicio 1
    """
    mayor=0
    for key, value in goleadores_2014.items():

        if value[1]>mayor:
            mayor=value[1]
            nombre=key

    print(nombre)

    #Ejercicio 2
    conjunto = set()
    for value in goleadores_2014.values():
        conjunto.add(value[0])

    print(type(conjunto))
    print(conjunto)

    #Ejercicio 3
    lista = []
    goles_pais = {}

    for i in conjunto:
        acum = 0
        for goles in goleadores_2014.values():
            if i==goles[0]:
                acum=acum+goles[1]
        goles_pais[i]=acum
        lista.append(acum)
    mas_goles = max(goles_pais.values())
    print(goles_pais)

    for key, value in goles_pais.items():
        if mas_goles == value:
            print(key,value)
    tuplita =()
    print(type(tuplita)) """

    #Ejercicio 4 Imprimir los nombres de los jugadores que marcaron entre 3 y 5 goles.
#    for key, value in goleadores_2014.items():
#        if value[1] >= 3 and value[1]<=5:
#            print(key)"""

    #Ejercicio 5. Imprimir los nombres de los jugadores Alemanes.
    for key, value in goleadores_2014.items():
        if value[0] == "Alemania":
            print(key, end="\n\n")

    #Ejercicio 6. Imprimir los nombres de los jugadores que marcaron menos goles.
    for key, value in goleadores_2014.items():
        if value[1] < 3:
            print(key)

    total_goles = 0
    total_jugadores = 0
    #Ejercicio 7.  Imprimir el número total de goles marcados por los jugadores que aparecen en la lista.
    for goles in goleadores_2014.values():
        total_goles += goles[1]
        total_jugadores = total_jugadores+1
    print("Total de goles anotados: ", total_goles)

    #Ejercicio 8. Imprimir el promedio de goles marcados por los jugadores que aparecen en la lista.
    promedio = total_goles/total_jugadores
    print("Promedio de goles anotados: ",promedio)
    print("Aguante el Diego, el más grande")

"""
Listas: Se puede hacer lo que quiera xD. Se define mi_lista = []
Tuplas: No se pueden eliminar valores. Se define tuplita = ()   >>> b = (5,)  # Es una tupla <<< b = (5) es un int
Conjuntos: No se pueden repetir valores. Se define: conjunto = set()
Diccionarios: Key : Value. Se define diccionario = {}
"""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    practica()

