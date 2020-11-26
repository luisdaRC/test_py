def practica():
    goleadores_2014 = {"Miuller": ("Alemania", 5),
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

    mayor=0
    for key, value in goleadores_2014.items():

        if value[1]>mayor:
            mayor=value[1]
            nombre=key

    print(nombre)

"""
Listas: Se puede hacer lo que quiera xD. Se define mi_lista = []
Tuplas: No se pueden eliminar valores. Se define tuplita = ()   >>> b = (5,)  # Es una tupla <<< b = (5) es un int
Conjuntos: No se pueden repetir valores. Se define: conjunto = set()
Diccionarios: Key : Value. Se define diccionario = {}
"""




if __name__ == '__main__':
    practica()