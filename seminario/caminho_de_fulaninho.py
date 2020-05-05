from copy import deepcopy
from model.grafo import Grafo
from colorama import Fore, init as color

color()

grafo_caminho = Grafo(True, True,
                      ["v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9",
                       "v10", "v11", "v12", "v13", "v14", "v15", "v16", "v17",
                       "v18", "v19", "v20", "v21", "v22", "v23", "v24", "v25",
                       "v26", "v27", "v28"],
                      ["v2-v1-10", "v1-v4-5", "v2-v3-5", "v3-v2-5", "v4-v3-10",
                       "v3-v6-2.5", "v6-v3-2.5", "v4-v5-2", "v6-v5-10",
                       "v6-v9-3", "v9-v3-6", "v5-v8-0.5", "v5-v7-2",
                       "v7-v13-4", "v13-v14-2", "v14-v13-2", "v14-v15-0.5",
                       "v16-v14-3", "v16-v15-2", "v8-v12-2", "v12-v14-1",
                       "v9-v8-9", "v12-v11-9.5", "v14-v17-8", "v17-v16-4",
                       "v15-v21-1", "v21-v22-2", "v22-v28-2", "v21-v20-6",
                       "v23-v22-5", "v27-v28-5.5", "v28-v27-5.5", "v9-v11-2",
                       "v11-v9-2", "v11-v10-6", "v10-v18-2", "v18-v10-2",
                       "v11-v17-2", "v17-v11-2", "v17-v18-6", "v18-v17-6",
                       "v17-v20-2", "v20-v17-2", "v18-v19-2", "v19-v18-2",
                       "v20-v19-6", "v20-v23-2", "v23-v20-2", "v19-v24-2",
                       "v24-v19-2", "v24-v23-6", "v23-v27-2", "v27-v23-2",
                       "v27-v26-4", "v26-v27-4", "v25-v27-6", "v27-v25-6",
                       "v24-v25-2", "v25-v24-2"])

origem = "v1"
destinos = ["v3", "v4", "v19", "v26", "v28"]
destinos_copy = ["v3", "v4", "v19", "v26", "v28"]


# noinspection PyUnboundLocalVariable
def dijkstra(grafo, vertice_origem, vertices_destino):
    """
    Implementação do algoritmo de dijkstra. Recebe o vértice de
    origem e retorna listas de distância e 'path' para todos os
    vértices do grafo.
    Método adaptado para parar assim que o primeiro dos vértices destino
     entrar em S.
    """
    dist = [float('inf') for i in range(len(grafo._vertices))]
    path = ['-' for i in range(len(grafo._vertices))]
    s = [vertice_origem]
    not_s = deepcopy(grafo._vertices)
    not_s.remove(vertice_origem)
    dist[grafo._vertices.index(origem)] = 0

    v_atual = vertice_origem

    while not_s:
        _adj, _p = grafo._get_adjacentes_e_pesos(v_atual)
        adjacentes, pesos = [], []
        for idx, vertice in enumerate(_adj):
            if vertice in not_s:
                adjacentes.append(_adj[idx])
                pesos.append(_p[idx])

        for idx, vertice in enumerate(adjacentes):
            if dist[grafo._vertices.index(vertice)] > \
                    dist[grafo._vertices.index(v_atual)] + pesos[idx]:
                dist[grafo._vertices.index(vertice)] = \
                    dist[grafo._vertices.index(v_atual)] + pesos[idx]
                path[grafo._vertices.index(vertice)] = v_atual

        min_dist = float('inf')
        for vertice in not_s:
            if dist[grafo._vertices.index(vertice)] < min_dist:
                min_dist = dist[grafo._vertices.index(vertice)]
                v_atual = vertice

        s.append(v_atual)
        not_s.remove(v_atual)
        if v_atual in vertices_destino:
            break

    return dist, path, v_atual


def get_menor_caminho(grafo, vertice_origem, vertice_destino, path_lista):
    """
    Utiliza o retorno do método djikstra para retornar o menor
    caminho completo entre dois vértices. Devem ser informados
    vértice de origem e vértice de destino.
    """
    caminho = [vertice_destino]
    v = vertice_destino
    while v != vertice_origem:
        v = path_lista[grafo._vertices.index(v)]
        caminho.append(v)
    caminho = caminho[::-1]
    return caminho


def _caminho_format(lista_caminho):
    """
    Método que formata o caminho para melhor leitura.
    """
    c_form = f"{Fore.YELLOW}{lista_caminho[0]}{Fore.RESET} > "
    for vertice in lista_caminho[1:-1:]:
        c_form += f"{vertice} > "
    c_form += f"{Fore.YELLOW}{lista_caminho[-1]}{Fore.RESET}"
    return c_form


caminho_completo = ["v1"]
distancia_acumulada = 0
while destinos:
    dist, path, mais_proximo = dijkstra(grafo_caminho, origem, destinos)
    caminho = get_menor_caminho(grafo_caminho, origem, mais_proximo, path)
    caminho_completo += caminho[1::]
    distancia_percorrida = dist[grafo_caminho._vertices.index(mais_proximo)]
    distancia_acumulada += distancia_percorrida

    print(f"{Fore.YELLOW}Fármacia mais proxima: {mais_proximo}{Fore.RESET}")
    print(
        f"Caminho entre {origem} e {mais_proximo}: "
        f"{_caminho_format(caminho)}"
        f"\nDistancia percorrida: {distancia_percorrida}"
        f"\nDistancia acumulada: {distancia_acumulada}")

    destinos.remove(mais_proximo)
    origem = mais_proximo
    print()

print(f"Caminho completo de fulaninho: {_caminho_format(caminho_completo)}")
print(f"Distância total percorrida: {distancia_acumulada}")

input(f"{Fore.YELLOW}\nENTER para finalizar{Fore.RESET}")
