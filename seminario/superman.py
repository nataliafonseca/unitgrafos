from model.grafo import Grafo
from colorama import Fore, init as color

color()

superman = Grafo(True, False, ["1", "2", "3", "4", "5", "6", "7", "8"],
                 ["1-2", "2-6", "3-2", "5-7", "8-5"])

lista_de_listas = []
while superman._vertices:
    graus_entrada_por_vertice = {}
    for vertice in superman._vertices:
        graus_entrada_por_vertice[vertice] = \
            superman.obter_grau_de_entrada(vertice)
    lista_de_saida = []
    for vertice, grau_de_entrada in graus_entrada_por_vertice.items():
        if grau_de_entrada == 0:
            lista_de_saida.append(vertice)
            superman.remover_do_grafo(vertice)
    lista_de_listas.append(lista_de_saida)

for idx, lista in enumerate(lista_de_listas):
    print(f"{Fore.YELLOW}LISTA {idx}:{Fore.RESET} {lista}")

input(f"{Fore.YELLOW}\nENTER para finalizar{Fore.RESET}")
