from prettytable import PrettyTable
from colorama import Fore, init as color

color()


def definir_grafo():
    q_vertices = int(input("Informe a quantidade de vertices do grafo: "))
    arestas = input("Informe as arestas do grafo (deve-se separar os vertices "
                    "adjacentes por traços e cada par de vertices deve ser "
                    "separado por virgula. Por exemplo: '1-2, 1-3, 1-4, "
                    "2-3'): ")
    digrafo = bool(int(input("O grafo é direcionado? "
                             "Digite 1 se sim ou 0 se não: ")))
    return Grafo(q_vertices, arestas, digrafo)


class Grafo:
    def __init__(self, q_vertices, arestas, digrafo):
        self.__q_vertices = q_vertices
        self.__arestas = arestas
        self.__digrafo = digrafo

    def estrutura_adjacencia(self):
        grafo = {}
        for i in range(self.__q_vertices):
            grafo.update({i + 1: []})
        arestas = self.__arestas.split(",")
        for par in arestas:
            i, j = par.split("-")
            i, j = int(i.strip()), int(j.strip())
            grafo[i].append(j)
            if not self.__digrafo:
                grafo[j].append(i)
        return grafo

    def print_estrutura_adjacencia(self):
        grafo = self.estrutura_adjacencia()
        for i in grafo:
            print(f"{Fore.YELLOW}{i} -> {Fore.RESET}{grafo[i]}")

    def matriz_adjacencia(self):
        grafo = []
        for i in range(self.__q_vertices):
            grafo.append([0] * self.__q_vertices)
        arestas = self.__arestas.split(",")
        for par in arestas:
            i, j = par.split("-")
            i, j = (int(i.strip()) - 1), (int(j.strip()) - 1)
            grafo[i][j] = 1
            if not self.__digrafo:
                grafo[j][i] = 1
        return grafo

    def print_matriz_adjacencia(self):
        grafo = self.matriz_adjacencia()

        x = PrettyTable([Fore.YELLOW + "*" + Fore.RESET] +
                        [f"{Fore.YELLOW}{i + 1}{Fore.RESET}"
                         for i in range(self.__q_vertices)])
        x.padding_width = 1
        for i in range(self.__q_vertices):
            x.add_row([f"{Fore.YELLOW}{i + 1}{Fore.RESET}"] + grafo[i])
        print(x)

    def busca_profundidade(self, vertice=1):
        pilha = [vertice]
        vertices_visitados = [vertice]
        grafo = self.estrutura_adjacencia()

        while pilha:
            if grafo[pilha[-1]][0] not in vertices_visitados:
                vertices_visitados.append(grafo[pilha[-1]][0])
                pilha.append(grafo[pilha[-1]][0])
            pilha.pop(-1)

        return vertices_visitados

    def busca_largura(self, vertice=1):
        fila = [vertice]
        vertices_visitados = [vertice]
        grafo = self.estrutura_adjacencia()

        while fila:
            for vertice in grafo[fila[0]]:
                if vertice not in vertices_visitados:
                    vertices_visitados.append(vertice)
                    fila.append(vertice)
            fila.pop(0)

        return vertices_visitados
