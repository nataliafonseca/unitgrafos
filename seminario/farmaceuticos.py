from model.grafo import Grafo
from colorama import Fore, init as color

color()

grafo_farmaceuticos = Grafo(False, False,
                     ["F1", "F2", "F3", "F4", "F5", "F6", "F7"],
                     ["F1-F2", "F1-F6", "F1-F7", "F2-F3", "F2-F4", "F3-F4",
                      "F3-F5", "F4-F5", "F4-F6", "F5-F6", "F5-F7", "F6-F7"])

vertices_nao_coloridos = grafo_farmaceuticos._vertices
cores = [[]]

for vertice in vertices_nao_coloridos:
    ha_adjacente = False
    for idx, cor in enumerate(cores):
        ha_adjacente = False
        if vertice in cores[idx]:
            break
        for adjacente in grafo_farmaceuticos.get_adjacentes(vertice):
            if adjacente in cores[idx]:
                ha_adjacente = True
                break
        if not ha_adjacente:
            cor.append(vertice)
            break
    if ha_adjacente:
        cores.append([vertice])

for idx, cor in enumerate(cores):
    print(f"{Fore.YELLOW}COR {idx + 1}:{Fore.RESET} {cor}")

input(f"{Fore.YELLOW}\nENTER para finalizar{Fore.RESET}")
