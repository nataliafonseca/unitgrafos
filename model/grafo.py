from lib.interface import *
from prettytable import PrettyTable
from datetime import datetime
from jsonpickle import encode, decode
from colorama import Fore, init as color

color()


class Grafo:

    def __init__(self, digrafo, valorado, q_vertices, arestas):
        self.__id_grafo = f"{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.__digrafo = digrafo
        self.__valorado = valorado
        self.__q_vertices = q_vertices
        self.__arestas = arestas

    @staticmethod
    def definir_grafo():
        print(Fore.BLUE + "O grafo é direcionado? Digite 1 para sim ou 0 para "
                          "não:" + Fore.RESET)
        digrafo = bool(int(input()))
        print()

        print(Fore.BLUE + "O grafo é valorado? Digite 1 para sim ou 0 para "
                          "não:" + Fore.RESET)
        valorado = bool(int(input()))
        print()

        print(Fore.BLUE + "Informe a quantidade de vertices do grafo:"
              + Fore.RESET)
        q_vertices = int(input())
        print()

        if valorado:
            print(
                Fore.BLUE + "Informe as arestas do grafo (deve-se separar os "
                            "vertices adjacentes e peso por traços e cada "
                            "par de vertices deve ser separado por virgula, "
                            "obtendo o formato: "
                + Fore.YELLOW + "vinicial-vfinal-peso, vinicial-vfinal-peso, "
                                "..., vinicial-vfinal-peso"
                + Fore.BLUE + ". Por exemplo: "
                + Fore.YELLOW + "1-2-4, 1-3-10, 1-4-20, 2-3-5"
                + Fore.BLUE + "):"
                + Fore.RESET)
        else:
            print(
                Fore.BLUE + "Informe as arestas do grafo (deve-se separar os "
                            "vertices adjacentes por traços e cada par de "
                            "vertices deve ser separado por virgula, obtendo "
                            "o formato: "
                + Fore.YELLOW + "vinicial-vfinal, vinicial-vfinal, ..., "
                                "vinicial-vfinal"
                + Fore.BLUE + ". Por exemplo: "
                + Fore.YELLOW + " 1-2, 1-3, 1-4, 2-3" + Fore.BLUE + "):"
                + Fore.RESET)
        arestas = input()
        print()

        return Grafo(digrafo, valorado, q_vertices, arestas)

    def cadastrar_grafo(self):
        print(
            Fore.BLUE + "Se desejar, informe uma id para o seu grafo, se "
                        "não, aperte ENTER e ele será salvo com um nome "
                        "genérico:" + Fore.RESET)
        id_grafo_p = input()
        if id_grafo_p:
            self.__id_grafo = id_grafo_p

        with open("grafos.json", "a") as grafos_json:
            grafos_json.write(encode(self) + "\n")

    @staticmethod
    def listar_grafos_salvos():
        with open("grafos.json", "r") as grafos_json:
            for line in grafos_json:
                grafo = decode(line)
                cabecalho(Fore.BLUE + f"{grafo.__id_grafo}" + Fore.RESET)
                print(f"Digrafo: {grafo.__digrafo}")
                print(f"Digrafo: {grafo.__valorado}")
                print(f"Quantidade de vertices: {grafo.__q_vertices}")
                print(f"Arestas: {grafo.__arestas}")
                print()

    @staticmethod
    def resgatar_grafo():
        Grafo.listar_grafos_salvos()
        with open("grafos.json", "r") as grafos_json:
            print(
                Fore.BLUE + "Informe a id do grafo que deseja resgatar ("
                            "para"
                            " evitar erros, copie da lista acima): "
                + Fore.RESET)
            id_r = input().strip()

            for line in grafos_json:
                grafo = decode(line)
                if grafo.__id_grafo == id_r:
                    return grafo
            print()
            print(Fore.RED + "Grafo não encontrado, tente novamente."
                  + Fore.RESET)

    def estrutura_adjacencia(self):
        grafo = {}
        for i in range(self.__q_vertices):
            grafo.update({i + 1: []})
        arestas = self.__arestas.split(",")
        if self.__valorado:
            for trio in arestas:
                i, j, p = trio.split("-")
                i, j, p = int(i.strip()), int(j.strip()), int(p.strip())
                grafo[i].append((j, p))
                if not self.__digrafo:
                    grafo[j].append((i, p))
        else:
            for par in arestas:
                i, j = par.split("-")
                i, j = int(i.strip()), int(j.strip())
                grafo[i].append((j, 1))
                if not self.__digrafo:
                    grafo[j].append((i, 1))
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
        if self.__valorado:
            for trio in arestas:
                i, j, p = trio.split("-")
                i, j, p = (int(i.strip()) - 1), (int(j.strip()) - 1), \
                          (int(p.strip()))
                grafo[i][j] = p
                if not self.__digrafo:
                    grafo[j][i] = p
        else:
            for trio in arestas:
                i, j = trio.split("-")
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

    # TODO: revisar e consertar as funções de busca
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
