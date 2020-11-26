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
    matriz = [[0 for i in range(3)] for j in range(3)]
    notas = [0,0,0]
    creditos = [0,0,0]
    iterador = 0
    for key,value in estudiantes.items():

        for diccionario_interior in value:
            if diccionario_interior["Semestre"] == "2003-2P":
                creditos[0] = creditos[0] + diccionario_interior["Creditos"]
                notas[0] = notas[0] + diccionario_interior["Nota"]*diccionario_interior["Creditos"]
                matriz[iterador][0]=notas[0]

            elif diccionario_interior["Semestre"] == "2004-1P":
                creditos[1] = creditos[1] + diccionario_interior["Creditos"]
                notas[1] = notas[1] + diccionario_interior["Nota"]*diccionario_interior["Creditos"]
                matriz[iterador][1]=notas[1]

            elif diccionario_interior["Semestre"] == "2004-2P":
                creditos[2] = creditos[2] + diccionario_interior["Creditos"]
                notas[2] = notas[2] + diccionario_interior["Nota"]*diccionario_interior["Creditos"]
                matriz[iterador][2]=notas[2]

        for x in range(3):
            if creditos[0] != 0:
                print(key)
                print(matriz[iterador][x]/creditos[x])

        iterador = iterador + 1

#    print(promedios)

# Ejercicio 2



if __name__ == '__main__':
    solucion()