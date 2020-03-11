from lib.interface import *
from lib.arvore import Arvore
from prettytable import PrettyTable
from datetime import datetime
from jsonpickle import encode, decode
from colorama import Fore, init as color
from copy import deepcopy

color()


class Grafo:

    def __init__(self, digrafo, valorado, vertices, arestas):
        self._id_grafo = f"{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self._digrafo = digrafo
        self._valorado = valorado
        self._vertices = vertices
        self._arestas = arestas
        self._max_peso = 1

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

        print(Fore.BLUE + "Informe os vértices do grafo, separando por "
                          "vírgula: " + Fore.RESET)
        vertices = list(input().replace(" ", "").upper().split(','))
        print()

        if valorado:
            print(
                Fore.BLUE + "Informe as arestas do grafo (deve-se separar os "
                            "vertices adjacentes e peso por traços e cada "
                            "par de vertices deve ser separado por virgula, "
                            "obtendo o formato: "
                + Fore.YELLOW + "vinicial-vfinal-peso, vinicial-vfinal-peso, "
                + Fore.YELLOW + "vinicial-vfinal-peso, vinicial-vfinal-peso, "
                                "..., vinicial-vfinal-peso"
                + Fore.BLUE + ". Por exemplo: "
                + Fore.YELLOW + "A-B-4, A-C-10, A-D-20, B-C-5"
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
                + Fore.YELLOW + "A-B, A-C, A-D, B-C" + Fore.BLUE + "):"
                + Fore.RESET)
        arestas = list(input().replace(" ", "").upper().split(','))
        print()

        return Grafo(digrafo, valorado, vertices, arestas)

    def cadastrar_grafo(self):
        print(
            Fore.BLUE + "Se desejar, informe uma id para o seu grafo, se "
                        "não, aperte ENTER e ele será salvo com um nome "
                        "genérico:" + Fore.RESET)
        id_grafo_p = input()
        if id_grafo_p:
            self._id_grafo = id_grafo_p

        with open("grafos.json", "a") as grafos_json:
            grafos_json.write(encode(self) + "\n")

    def imprimir_informacoes(self):
        cabecalho(Fore.BLUE + f"{self._id_grafo}" + Fore.RESET)
        print(f"{Fore.YELLOW}vertices:{Fore.RESET} {self._vertices}")
        print(f"{Fore.YELLOW}Arestas:{Fore.RESET} {self._arestas}")
        print(f"{Fore.YELLOW}Digrafo:{Fore.RESET} {self._digrafo}")
        print(f"{Fore.YELLOW}Valorado:{Fore.RESET} {self._valorado}")
        print(f"{Fore.YELLOW}Regular:{Fore.RESET} {self.ehRegular()}")
        print(f"{Fore.YELLOW}Completo:{Fore.RESET} {self.ehCompleto()}")
        print(f"{Fore.YELLOW}Conexo:{Fore.RESET} {self.ehConexo()}")
        if not self.ehConexo():
            print(f"{Fore.YELLOW}Quantidade de componentes conexos: "
                  f"{Fore.RESET}{self._get_q_componentes()['conexos']}")
        if self._digrafo:
            if not self.fortemente_conexo():
                print(f"{Fore.YELLOW}Quantidade de componentes fortemente "
                      f"conexos:{Fore.RESET} "
                      f"{self._get_q_componentes()['fortes']}")

    @staticmethod
    def listar_grafos_salvos():
        with open("grafos.json", "r") as grafos_json:
            for line in grafos_json:
                grafo = decode(line)
                grafo.imprimir_informacoes()

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
                if grafo._id_grafo == id_r:
                    return grafo
            print()
            print(Fore.RED + "Grafo não encontrado, tente novamente."
                  + Fore.RESET)

    def estrutura_adjacencia(self):
        grafo = {}
        for i in range(len(self._vertices)):
            grafo.update({self._vertices[i]: []})
        arestas = self._arestas
        if self._valorado:
            for trio in arestas:
                i, j, p = trio.replace(" ", "").split("-")
                p = int(p)
                grafo[i].append({'vertice_id': j, 'peso': p})
                if not self._digrafo:
                    grafo[j].append({'vertice_id': i, 'peso': p})
                if p > self._max_peso:
                    self._max_peso = p
        else:
            for par in arestas:
                i, j = par.replace(" ", "").split("-")
                grafo[i].append({'vertice_id': j, 'peso': 1})
                if not self._digrafo:
                    grafo[j].append({'vertice_id': i, 'peso': 1})
        return grafo

    def imprimir_estrutura_adjacencia(self):
        grafo = self.estrutura_adjacencia()
        wg = len((max(grafo, key=len)))
        wp = len(str(self._max_peso))
        for i in grafo:
            print(f"{Fore.YELLOW}{i:<{wg}}", end=' -> ')
            for j in grafo[i]:
                print(f"{Fore.RESET}{j['vertice_id']:<{wg}}"
                      f"_P{j['peso']:<{wp}}", end=' | ')
            print()

    def matriz_adjacencia(self):
        grafo = []
        for i in range(len(self._vertices)):
            grafo.append([0] * len(self._vertices))
        arestas = self._arestas
        if self._valorado:
            for trio in arestas:
                i, j, p = trio.replace(" ", "").split("-")
                i, j = self._vertices.index(i), self._vertices.index(j)
                p = int(p)
                grafo[i][j] = p
                if not self._digrafo:
                    grafo[j][i] = p
        else:
            for par in arestas:
                i, j = par.replace(" ", "").split("-")
                i, j = self._vertices.index(i), self._vertices.index(j)
                grafo[i][j] = 1
                if not self._digrafo:
                    grafo[j][i] = 1
        return grafo

    def imprimir_matriz_adjacencia(self):
        grafo = self.matriz_adjacencia()

        x = PrettyTable([Fore.YELLOW + "*" + Fore.RESET] +
                        [f"{Fore.YELLOW}{vertice}{Fore.RESET}"
                         for vertice in self._vertices])
        for idx, vertice in enumerate(self._vertices):
            x.add_row([f"{Fore.YELLOW}{vertice}{Fore.RESET}"] + grafo[idx])
        print(x)

    def getAdjacentes(self, vertice):
        grafo = self.estrutura_adjacencia()
        adjacentes = []
        for i in grafo[vertice]:
            adjacentes.append(i['vertice_id'])
        return adjacentes

    def _get_adjacentes_e_pesos(self, vertice):
        grafo = self.estrutura_adjacencia()
        adjacentes = []
        pesos = []
        for i in grafo[vertice]:
            adjacentes.append(i['vertice_id'])
            pesos.append(i['peso'])
        return adjacentes, pesos

    def ehRegular(self):
        regular = True
        for idx, vertice in enumerate(self._vertices):
            if len(self.getAdjacentes(self._vertices[0])) != \
                    len(self.getAdjacentes(self._vertices[idx])):
                regular = False
        return regular

    def ehCompleto(self):
        completo = True
        for vertice in self._vertices:
            if len(self.getAdjacentes(vertice)) != len(self._vertices) - 1:
                completo = False
        return completo

    def ehConexo(self):
        conexo = True
        if self._get_q_componentes()['conexos'] > 1:
            conexo = False
        return conexo

    def fortemente_conexo(self):
        fortemente_conexo = True
        if self._get_q_componentes()['fortes'] > 1:
            fortemente_conexo = False
        return fortemente_conexo

    def _profundidade(self, vertice_inicial):
        pilha = [vertice_inicial]
        vertices_visitados = Arvore(vertice_inicial)

        while pilha:
            vertice = pilha[-1]
            pilha.pop(-1)
            for w in self.getAdjacentes(vertice):
                if not vertices_visitados.localizar_nodo(w):
                    vertices_visitados.inserir_nodo(vertice, w)
                    pilha.append(w)

        return vertices_visitados

    def _largura(self, vertice_inicial):
        fila = [vertice_inicial]
        vertices_visitados = Arvore(vertice_inicial)

        while fila:
            vertice = fila[0]
            fila.pop(0)
            for w in self.getAdjacentes(vertice):
                if not vertices_visitados.localizar_nodo(w):
                    vertices_visitados.inserir_nodo(vertice, w)
                    fila.append(w)

        return vertices_visitados

    def _busca_geral(self, busca, vertice_inicial="nao_informado"):
        if vertice_inicial == "nao_informado":
            vertice = self._vertices[0]
        else:
            vertice = vertice_inicial
        q_componentes = 0
        vertices_visitados = []
        vv_quantidade = 1

        def vv_busca(vertice_buscado):
            for arvore in vertices_visitados:
                if arvore.localizar_nodo(vertice_buscado):
                    return True
            return False

        while vv_quantidade < len(self._vertices):
            if q_componentes > 0:
                for v in self._vertices:
                    if not vv_busca(v):
                        vertice = v
            if busca == 'largura':
                vertices_visitados.append(self._largura(vertice))
            elif busca == 'profundidade':
                vertices_visitados.append(self._profundidade(vertice))
            q_componentes += 1
            vv_quantidade += vertices_visitados[-1].quantidade

        return vertices_visitados, q_componentes

    def busca_largura(self, vertice_inicial="nao_informado"):
        vertices_visitados = self._busca_geral('largura', vertice_inicial)[0]
        if len(vertices_visitados) == 1:
            vertices_visitados[0].imprimir()
        else:
            for i in range(len(vertices_visitados)):
                vertices_visitados[i].imprimir()

    def busca_profundidade(self, vertice_inicial="nao_informado"):
        vertices_visitados = self._busca_geral('profundidade', vertice_inicial)[0]
        if len(vertices_visitados) == 1:
            vertices_visitados[0].imprimir()
        else:
            for i in range(len(vertices_visitados)):
                vertices_visitados[i].imprimir()

    def _get_q_componentes(self):
        q_conexos = self._busca_geral('largura')[1]
        q_fortemente_conexos = q_conexos
        if self._digrafo:
            self._digrafo = False
            q_conexos = self._busca_geral('largura')[1]
            self._digrafo = True
        return {'conexos': q_conexos, 'fortes': q_fortemente_conexos}

    def _dijkstra(self, v_origem):
        dist = [float('inf') for i in range(len(self._vertices))]
        path = ['-' for i in range(len(self._vertices))]
        s = [v_origem]
        not_s = deepcopy(self._vertices)
        not_s.remove(v_origem)
        dist[self._vertices.index(v_origem)] = 0

        v_atual = v_origem

        while not_s:
            _adj, _p = self._get_adjacentes_e_pesos(v_atual)
            adjacentes, pesos = [], []
            for idx, vertice in enumerate(_adj):
                if vertice in not_s:
                    adjacentes.append(_adj[idx])
                    pesos.append(_p[idx])

            for idx, vertice in enumerate(adjacentes):
                if dist[self._vertices.index(vertice)] > \
                        dist[self._vertices.index(v_atual)] + pesos[idx]:
                    dist[self._vertices.index(vertice)] = \
                        dist[self._vertices.index(v_atual)] + pesos[idx]
                    path[self._vertices.index(vertice)] = v_atual

            min_dist = float('inf')
            for vertice in not_s:
                if dist[self._vertices.index(vertice)] < min_dist:
                    min_dist = dist[self._vertices.index(vertice)]
                    v_atual = vertice

            s.append(v_atual)
            not_s.remove(v_atual)

        return dist, path

    def _get_caminho(self, v_origem, v_destino):
        path = self._dijkstra(v_origem)[1]
        caminho = [v_destino]
        v = v_destino
        while v != v_origem:
            v = path[self._vertices.index(v)]
            caminho.append(v)
        caminho = caminho[::-1]
        return caminho

    def _caminho_format(self, v_origem, v_destino):
        caminho = self._get_caminho(v_origem, v_destino)
        c_form = f"{Fore.YELLOW}{caminho[0]}{Fore.RESET} > "
        for vertice in caminho[1:-1:]:
            c_form += f"{vertice} > "
        c_form += f"{Fore.YELLOW}{caminho[-1]}{Fore.RESET}"
        return c_form

    def imprimir_menor_caminho(self, v_origem, v_destino="todos"):
        dist, path = self._dijkstra(v_origem)

        if v_destino == "todos":
            x = PrettyTable([f"{Fore.BLUE}vertice{Fore.RESET}",
                             f"{Fore.BLUE}distância{Fore.RESET}",
                             f"{Fore.BLUE}caminho{Fore.RESET}"])
            x.align[f"{Fore.BLUE}caminho{Fore.RESET}"] = "l"

            x.add_row([f"{Fore.YELLOW}{v_origem}{Fore.RESET}",
                       f"{Fore.YELLOW}0{Fore.RESET}",
                       f"{Fore.YELLOW}-{Fore.RESET}"])
            for idx, vertice in enumerate(self._vertices):
                if vertice != v_origem:
                    x.add_row([f"{Fore.YELLOW}{self._vertices[idx]}"
                               f"{Fore.RESET}", dist[idx],
                               f"{self._caminho_format(v_origem, vertice)}"])

            print(x)
        else:
            print(self._caminho_format(v_origem, v_destino))
            print(f"Distância = {dist[self._vertices.index(v_destino)]}")
