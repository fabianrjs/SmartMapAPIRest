
import random as rr

def calcularAforo(idEdificio, numPisos):

    x = []
    for i in range(7, 20):
        x.append(i)

    listaY = []
    for i in range(0, numPisos):

        y = [rr.randint(10, 30), rr.randint(20, 40), rr.randint(30, 60), rr.randint(50, 70), rr.randint(60, 80),
             rr.randint(80, 100), rr.randint(50, 70), rr.randint(60, 80), rr.randint(50, 80), rr.randint(50, 70), rr.randint(30, 60), rr.randint(20, 40), rr.randint(10, 30)]
        listaY.append(y)

    totalHoras = []

    for i in range(0, len(listaY[0])):
        acumulado = 0
        for j in range(0, len(listaY)):
            acumulado += listaY[j][i]
        totalHoras.append(acumulado)

    return totalHoras

