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
    lista = [0,0,0]
    for key,value in estudiantes.items():
        suma_creditos = 0
        suma_notas = 0

        total_creditos_semestre = 0
        for diccionario_interior in value:
            if diccionario_interior["Semestre"] == "2003-2P":
                suma_creditos = suma_creditos + diccionario_interior["Creditos"]
                lista[0] = lista[0] + diccionario_interior["Nota"]

            elif diccionario_interior["Semestre"] == "2004-1P":
                suma_creditos = suma_creditos + diccionario_interior["Creditos"]
                lista[0] = lista[0] + diccionario_interior["Nota"]

            elif diccionario_interior["Semestre"] == "2004-2P":
                suma_creditos = suma_creditos + diccionario_interior["Creditos"]
                lista[0] = lista[0] + diccionario_interior["Nota"]


                sumatoria = value
    print(promedios)







if __name__ == '__main__':
    solucion()