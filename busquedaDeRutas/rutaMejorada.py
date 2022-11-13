from busquedaDeRutas.caminoMejorado import Camino

def buscarNodo(id, nodos):
    for nodo in nodos:
        if nodo.idNodo == id:
            return nodo


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


def buscarNodo(idNodo, listaNodos):
    for nodo in listaNodos:
        if nodo.idNodo == idNodo:
            return nodo


def buscarRutaOptima(listaNodos, idNodoInicio, idNodoFinal) -> str:

    for nodo in listaNodos:
        # print(type(nodo.idNodo))
        #print(str(nodo.idNodo) + "--")
        partes = nodo.vecinos2.split(",")
        for p in partes:
            nodo.vecinos.append(int(p))

    # buscarNodo(152, listaNodos).peso = 50

    finder = Camino()
    caminos = finder.buscarCaminoMasCorto(
        listaNodos, buscarNodo(idNodoInicio, listaNodos), buscarNodo(idNodoFinal, listaNodos))

    rutaStr = ''
    for path in caminos:
        rutaStr += str(path.idNodo) + ','
        print(path.idNodo)

    return rutaStr[:-1]
    
