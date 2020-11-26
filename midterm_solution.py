#Melanie Andrade Cortés
#Código: T00062025

def solucion():
    estudiantes = {"Pepe Perez":[{"Curso":"Algoritmos",
                                 "Creditos":5,
                                 "Nota":2.8,
                                 "Semestre":"2004-1P"},
                                {"Curso":"Astronomia",
                                 "Creditos":10,
                                 "Nota":3.2,
                                 "Semestre":"2004-2P"}],

                  "Ana Diaz":[{"Curso":"Astronomia",
                                 "Creditos":10,
                                 "Nota":4.0,
                                 "Semestre":"2003-2P"},
                              {"Curso":"Fisica",
                                 "Creditos":10,
                                 "Nota":3.0,
                                 "Semestre":"2003-2P"},
                              {"Curso":"Calculo I",
                                 "Creditos":10,
                                 "Nota":3.5,
                                 "Semestre":"2003-2P"},
                              {"Curso":"Calculo-II",
                                 "Creditos":10,
                                 "Nota":4.0,
                                 "Semestre":"2004-1P"},
                              {"Curso":"Algebra Lineal",
                                 "Creditos":10,
                                 "Nota":2.9,
                                 "Semestre":"2004-1P"},
                              {"Curso":"Fisica I",
                                 "Creditos":10,
                                 "Nota":4.2,
                                 "Semestre":"2004-1P"},
                              {"Curso":"Fisica II",
                                 "Creditos":7,
                                 "Nota":3.6,
                                 "Semestre":"2004-2P"},
                              {"Curso":"Calculo III",
                                 "Creditos":7,
                                 "Nota":2.7,
                                 "Semestre":"2004-2P"},
                              {"Curso":"Programacion",
                                 "Creditos":5,
                                 "Nota":4.3,
                                 "Semestre":"2004-2P"}],

                  "Lina Gomez":[{"Curso":"Calculo I",
                                 "Creditos":10,
                                 "Nota":4.5,
                                 "Semestre":"2004-1P"},
                                {"Curso":"Astronomia",
                                 "Creditos":10,
                                 "Nota":3.1,
                                 "Semestre":"2004-1P"},
                                {"Curso":"Algoritmos",
                                 "Creditos":5,
                                 "Nota":3.9,
                                 "Semestre":"2004-1P"},
                                {"Curso":"Calculo II",
                                 "Creditos":10,
                                 "Nota":2.5,
                                 "Semestre":"2004-2P"},
                                {"Curso":"Programacion",
                                 "Creditos":5,
                                 "Nota":3.2,
                                 "Semestre":"2004-2P"}]}

# Ejercicio 1: Promedio por cada semestre
    promedios = {}
    for key,value in estudiantes.items():
        suma_creditos = 0
        suma_notas = 0

        total_creditos_semestre = 0
        for diccionario_interior in value:
            if diccionario_interior["Semestre"] == "2003-2P":
                suma_creditos = suma_creditos + diccionario_interior["Creditos"]
                promedios[key] = promedios[value] + diccionario_interior["Nota"]

            elif diccionario_interior["Semestre"] == "2004-1P":
                suma_creditos = suma_creditos + diccionario_interior["Creditos"]
                promedios[key] = promedios[value] + diccionario_interior["Nota"]

            elif diccionario_interior["Semestre"] == "2004-2P":
                suma_creditos = suma_creditos + diccionario_interior["Creditos"]
                suma_creditos = suma_creditos + diccionario_interior["Nota"]




            for llave,valor in diccionario_interior.items():
                if valor == "2003-2P":
                    suma_notas =
                elif valor == "2004-1P":

                elif valor== "2003-2P":

                sumatoria = value




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

    #Ejercicio 1-Test

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
    solucion()