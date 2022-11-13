
def buscarNodo(id, nodos):
    for nodo in nodos:
        if nodo.idNodo == id:
            return nodo

class Camino(object):

    def __init__(self):
        self.nodos = []

    def DijkstrasAlgo(self, inicio, final):

        noExplorados = []

        for nod in self.nodos:
            if (nod.habilitado):
                nod.resetNodo()
                noExplorados.append(nod)

        inicio.heuristica = 0

        while len(noExplorados) > 0:

            noExplorados.sort(key=lambda x: x.heuristica)

            actual = noExplorados[0]
            
            # if(actual == final):
            #     return final

            noExplorados.remove(actual)
            vecinosActual = actual.vecinos

            for vecino in vecinosActual:
                # transformar id del vecino en un Nodo

                if buscarNodo(vecino, self.nodos) in noExplorados and buscarNodo(vecino, self.nodos).habilitado == True:
                    vecino = buscarNodo(vecino, self.nodos)
                    distancia = actual.heuristica + (vecino.peso * vecino.tipoEspacio)

                    if distancia < vecino.heuristica:
                        vecino.heuristica = distancia
                        vecino.nodoPadre = actual
                        #print(vecino.numPersonas * vecino.tipoEspacio)

        print("camino completado")
        return final

    def buscarCaminoMasCorto(self, listaNodos, inicio, final):
        self.nodos = listaNodos
        resultado = []

        nodoRespuesta = self.DijkstrasAlgo(inicio, final)
        pesoTotal = nodoRespuesta.heuristica 

        while nodoRespuesta != None:
            resultado.append(nodoRespuesta)
            nodoRespuesta = nodoRespuesta.nodoPadre
        resultado.reverse()
        resultado.append(pesoTotal)
        return resultado
