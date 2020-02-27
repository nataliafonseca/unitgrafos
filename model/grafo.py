from lib.interface import *
from prettytable import PrettyTable
from datetime import datetime
from jsonpickle import encode, decode
from colorama import Fore, init as color

color()


class Grafo:

    def __init__(self, digrafo, valorado, q_vertices, arestas):
        self._id_grafo = f"{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self._digrafo = digrafo
        self._valorado = valorado
        self._q_vertices = q_vertices
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
            self._id_grafo = id_grafo_p

        with open("grafos.json", "a") as grafos_json:
            grafos_json.write(encode(self) + "\n")

    def imprimir_informacoes(self):
        cabecalho(Fore.BLUE + f"{self._id_grafo}" + Fore.RESET)
        print(f"{Fore.YELLOW}Quantidade de vertices:{Fore.RESET} "
              f"{self._q_vertices}")
        print(f"{Fore.YELLOW}Arestas:{Fore.RESET} {self._arestas}")
        print(f"{Fore.YELLOW}Digrafo:{Fore.RESET} {self._digrafo}")
        print(f"{Fore.YELLOW}Valorado:{Fore.RESET} {self._valorado}")
        print(f"{Fore.YELLOW}Regular:{Fore.RESET} {self.regular()}")
        print(f"{Fore.YELLOW}Completo:{Fore.RESET} {self.completo()}")
        print(f"{Fore.YELLOW}Conexo:{Fore.RESET} {self.conexo()}")
        if not self.conexo():
            print(f"{Fore.YELLOW}Quantidade de componentes conexos:{Fore.RESET} "
                  f"{self._get_q_componentes()['conexos']}")
        if self._digrafo:
            if not self.fortemente_conexo():
                print(f"{Fore.YELLOW}Quantidade de componentes fortemente "
                      f"conexos:{Fore.RESET} "
                      f"{self._get_q_componentes()['fortes']}")
        print()

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
        for i in range(self._q_vertices):
            grafo.update({i + 1: []})
        arestas = self._arestas.split(",")
        if self._valorado:
            for trio in arestas:
                i, j, p = trio.split("-")
                i, j, p = int(i.strip()), int(j.strip()), int(p.strip())
                grafo[i].append({'vertice_id': j, 'peso': p})
                if not self._digrafo:
                    grafo[j].append({'vertice_id': i, 'peso': p})
                if p > self._max_peso:
                    self._max_peso = p
        else:
            for par in arestas:
                i, j = par.split("-")
                i, j = int(i.strip()), int(j.strip())
                grafo[i].append({'vertice_id': j, 'peso': 1})
                if not self._digrafo:
                    grafo[j].append({'vertice_id': i, 'peso': 1})
        return grafo

    def imprimir_estrutura_adjacencia(self):
        grafo = self.estrutura_adjacencia()
        wg = len(str(max(grafo, key=int)))
        wp = len(str(self._max_peso))
        for i in grafo:
            print(f"{Fore.YELLOW}{i:>{wg}}", end=' -> ')
            for j in grafo[i]:
                print(f"{Fore.RESET}{j['vertice_id']:>{wg}}"
                      f"_P{j['peso']:<{wp}}", end=' | ')
            print()

    def matriz_adjacencia(self):
        grafo = []
        for i in range(self._q_vertices):
            grafo.append([0] * self._q_vertices)
        arestas = self._arestas.split(",")
        if self._valorado:
            for trio in arestas:
                i, j, p = trio.split("-")
                i, j, p = (int(i.strip()) - 1), (int(j.strip()) - 1), \
                          (int(p.strip()))
                grafo[i][j] = p
                if not self._digrafo:
                    grafo[j][i] = p
        else:
            for trio in arestas:
                i, j = trio.split("-")
                i, j = (int(i.strip()) - 1), (int(j.strip()) - 1)
                grafo[i][j] = 1
                if not self._digrafo:
                    grafo[j][i] = 1
        return grafo

    def imprimir_matriz_adjacencia(self):
        grafo = self.matriz_adjacencia()

        x = PrettyTable([Fore.YELLOW + "*" + Fore.RESET] +
                        [f"{Fore.YELLOW}{i + 1}{Fore.RESET}"
                         for i in range(self._q_vertices)])
        x.padding_width = 1
        for i in range(self._q_vertices):
            x.add_row([f"{Fore.YELLOW}{i + 1}{Fore.RESET}"] + grafo[i])
        print(x)

    def get_adjacentes(self, vertice):
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

    def regular(self):
        regular = True
        for i in range(self._q_vertices):
            if len(self.get_adjacentes(1)) != len(self.get_adjacentes(i + 1)):
                regular = False
        return regular

    def completo(self):
        completo = True
        for i in range(self._q_vertices):
            if len(self.get_adjacentes(i + 1)) != self._q_vertices - 1:
                completo = False
        return completo

    def conexo(self):
        conexo = True
        if self._get_q_componentes()['conexos'] > 1:
            conexo = False
        return conexo

    def fortemente_conexo(self):
        fortemente_conexo = True
        if self._get_q_componentes()['fortes'] > 1:
            fortemente_conexo = False
        return fortemente_conexo

    def _busca_profundidade_por_componente(self, vertice_inicial=1):
        pilha = [vertice_inicial]
        vertices_visitados = [vertice_inicial]
        vertices_explorados = []

        while pilha:
            vertice = pilha[-1]
            pilha.pop(-1)
            vertices_explorados.append(vertice)
            for w in self.get_adjacentes(vertice):
                if w not in vertices_visitados:
                    vertices_visitados.append(w)
                    pilha.append(w)

        return vertices_visitados

    def _busca_largura_por_componente(self, vertice_inicial=1):
        fila = [vertice_inicial]
        vertices_visitados = [vertice_inicial]
        vertices_explorados = []

        while fila:
            vertice = fila[0]
            fila.pop(0)
            vertices_explorados.append(vertice)
            for w in self.get_adjacentes(vertice):
                if w not in vertices_visitados:
                    vertices_visitados.append(w)
                    fila.append(w)

        return vertices_visitados

    def _busca_geral(self, busca):
        vertice = 1
        q_componentes = 0
        vertices_visitados = []

        while len(vertices_visitados) < self._q_vertices:
            if q_componentes > 0:
                for i in range(1, self._q_vertices + 1):
                    if i not in vertices_visitados:
                        vertice = i
            if busca == 'largura':
                vertices_visitados += \
                    self._busca_largura_por_componente(vertice)
            elif busca == 'profundidade':
                vertices_visitados += \
                    self._busca_profundidade_por_componente(vertice)
            q_componentes += 1

        return vertices_visitados, q_componentes

    def busca_largura(self):
        return self._busca_geral('largura')[0]

    def busca_profundidade(self):
        return self._busca_geral('profundidade')[0]

    def _get_q_componentes(self):
        q_conexos = self._busca_geral('largura')[1]
        q_fortemente_conexos = q_conexos
        if self._digrafo:
            self._digrafo = False
            q_conexos = self._busca_geral('largura')[1]
            self._digrafo = True
        return {'conexos': q_conexos, 'fortes': q_fortemente_conexos}

    def _dijkstra(self, v_origem):
        vertices = [(i+1) for i in range(self._q_vertices)]
        dist = [float('inf') for i in range(self._q_vertices)]
        path = ['-' for i in range(self._q_vertices)]
        s = [v_origem]
        not_s = [(i+1) for i in range(self._q_vertices)]
        not_s.remove(v_origem)
        dist[v_origem - 1] = 0

        v_atual = v_origem

        while not_s:
            _adj, _p = self._get_adjacentes_e_pesos(v_atual)
            adjacentes, pesos = [], []
            for idx, vertice in enumerate(_adj):
                if vertice in not_s:
                    adjacentes.append(_adj[idx])
                    pesos.append(_p[idx])

            for idx, vertice in enumerate(adjacentes):
                if dist[vertice - 1] > dist[v_atual - 1] + pesos[idx]:
                    dist[vertice - 1] = dist[v_atual - 1] + pesos[idx]
                    path[vertice - 1] = v_atual

            min_dist = float('inf')
            if adjacentes:
                for vertice in adjacentes:
                    if dist[vertice - 1] < min_dist:
                        min_dist = dist[vertice - 1]
                        v_atual = vertice
            else:
                for vertice in not_s:
                    if dist[vertice - 1] < min_dist:
                        min_dist = dist[vertice - 1]
                        v_atual = vertice

            s.append(v_atual)
            not_s.remove(v_atual)

        return vertices, dist, path

    def get_menor_caminho(self, v_origem, v_destino="todos"):
        vertices, dist, path = self._dijkstra(v_origem)
        if v_destino == "todos":
            x = PrettyTable(['vertice', 'dist', 'path'])
            x.padding_width = 1

            for i in range(len(vertices)):
                x.add_row([vertices[i], dist[i], path[i]])
            return x
        else:
            caminho = [v_destino]
            v = v_destino
            while v != v_origem:
                v = path[int(v) - 1]
                caminho.append(v)
            return caminho


