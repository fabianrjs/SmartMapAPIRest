from busquedaDeRutas.caminoMejorado import Camino
from apiRest.models import Edificio

class Nodo(object):

    def __init__(self, idNodo, peso, tipoEspacio, vecinos, habilitado):
        self.idNodo = idNodo
        self.peso = peso
        self.nodoPadre = None
        self.vecinos = []
        self.vecinos2 = vecinos
        self.habilitado = habilitado
        self.tipoEspacio = tipoEspacio
        self.heuristica = 10000000

    def resetNodo(self):
        self.heuristica = 100000000
        self.nodoPadre = None


def buscarNodo(idNodo, listaNodos) -> Nodo:
    for nodo in listaNodos:
        if nodo.idNodo == idNodo:
            return nodo


def buscarRutaOptima(listaNodos, idNodoInicio, idNodoFinal) -> str:

    edificio = Edificio.objects.get(id_edificio = idNodoFinal)
    for nodo in listaNodos:
        # print(type(nodo.idNodo))
        #print(str(nodo.idNodo) + "--")
        partes = nodo.vecinos2.split(",")
        for p in partes:
            nodo.vecinos.append(int(p))

    # buscarNodo(152, listaNodos).peso = 50

    finder = Camino()
    entradas = edificio.listaDeEntradas.split(",")
    caminoMasCorto = []
    pesoMinimo = 100000

    for entrada in entradas:
        

        print(buscarNodo(entrada, listaNodos))
        caminos = finder.buscarCaminoMasCorto(
            listaNodos, buscarNodo(idNodoInicio, listaNodos), buscarNodo(int(entrada), listaNodos))
        if(caminos[len(caminos) - 1] < pesoMinimo):
            pesoMinimo = caminos[len(caminos) - 1]
            caminos.pop()
            caminoMasCorto = caminos.copy()
    

    rutaStr = ''
    for path in caminoMasCorto:
        rutaStr += str(path.idNodo) + ','
        print(path.idNodo)

    
    return rutaStr[:-1]
    
