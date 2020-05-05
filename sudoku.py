from random import shuffle
from model.grafo import Grafo

grafo_sudoku = Grafo(False, False,
                     ["v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9",
                      "v10", "v11", "v12", "v13", "v14", "v15", "v16"],
                     ["v1-v2", "v1-v3", "v1-v4", "v1-v5", "v1-v9", "v1-v13",
                      "v1-v6", "v2-v3", "v2-v4", "v2-v6", "v2-v10", "v2-v14",
                      "v2-v5", "v3-v4", "v3-v7", "v3-v11", "v3-v15", "v3-v8",
                      "v4-v8", "v4-v12", "v4-v16", "v4-v7", "v5-v6", "v5-v7",
                      "v5-v8", "v5-v9", "v5-v13", "v6-v7", "v6-v8", "v6-v10",
                      "v6-v14", "v7-v8", "v7-v11", "v7-v15", "v8-v12",
                      "v8-v16", "v9-v10", "v9-v11", "v9-v12", "v9-v13",
                      "v9-v14", "v10-v11", "v10-v12", "v10-v13", "v10-v14",
                      "v11-v12", "v11-v15", "v11-v16", "v12-v15", "v12-v16",
                      "v13-v14", "v13-v15", "v13-v16", "v14-v15", "v14-v16",
                      "v15-v16"])


def coloracao(grafo):
    cores = [["v1", "v10"], ["v7"], ["v16"], []]

    for vertice in grafo_sudoku._vertices:
        ha_adjacente = False
        for idx, cor in enumerate(cores):
            ha_adjacente = False
            if vertice in cores[idx]:
                break
            for adjacente in grafo.get_adjacentes(vertice):
                if adjacente in cores[idx]:
                    ha_adjacente = True
                    break
            if not ha_adjacente:
                cor.append(vertice)
                break
        if ha_adjacente:
            cores.append([vertice])

    return cores


lista_cores = grafo_sudoku._coloracao([["v1", "v10"], ["v7"], ["v16"]])
while len(lista_cores) > 4:
    shuffle(grafo_sudoku._vertices)
    lista_cores = coloracao(grafo_sudoku)

for i in range(4):
    print(f"COR {i + 1}: {lista_cores[i]}")

input()
