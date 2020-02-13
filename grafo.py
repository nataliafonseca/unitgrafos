class Grafo:
    def __init__(self, q_vertices, arestas):
        self.__q_vertices = q_vertices
        self.__arestas = arestas

    def __estrutura_adjacencia(self):
        grafo = {}
        for i in range(self.__q_vertices):
            grafo.update({i+1: []})
        arestas = self.__arestas.split(",")
        for par in arestas:
            i, j = par.split("-")
            i, j = (int(i.strip()) - 1), (int(j.strip()) - 1)
            grafo[i+1].append(j+1)
            grafo[j+1].append(i+1)
        return grafo

    def get_estrutura_adjacencia(self):
        grafo = self.__estrutura_adjacencia()
        for i in grafo:
            print(f"{i} -> {grafo[i]}")

    def __matriz_adjacencia(self):
        grafo = []
        for i in range(self.__q_vertices):
            grafo.append([0] * self.__q_vertices)
        arestas = self.__arestas.split(",")
        for par in arestas:
            i, j = par.split("-")
            i, j = (int(i.strip()) - 1), (int(j.strip()) - 1)
            grafo[i][j] = 1
            grafo[j][i] = 1
        return grafo

    def get_matriz_adjacencia(self):
        grafo = self.__matriz_adjacencia()
        print(f"*  {str([i+1 for i in range(self.__q_vertices)]).strip('[]')}")
        for i in range(self.__q_vertices):
            print(f"{i+1} {grafo[i]}")
