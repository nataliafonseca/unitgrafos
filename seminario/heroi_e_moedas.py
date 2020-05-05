from model.grafo import Grafo
from lib.arvore import Arvore
from colorama import Fore, init as color

color()

grafo_heroi = Grafo(False, False,
                    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11",
                     "12", "13", "14", "15", "16", "17", "18", "19", "20",
                     "21", "22", "23", "24", "25", "26", "27", "28"],
                    ["1-2", "1-6", "2-3", "2-10", "3-4", "3-16", "4-5", "6-7",
                     "6-13", "7-8", "7-15", "8-9", "10-11", "11-12", "11-13",
                     "12-14", "14-15", "14-16", "14-21", "16-17", "17-19",
                     "18-19", "19-20", "20-24", "21-22", "22-27", "23-24",
                     "23-25", "24-26", "26-27", "26-28"])

vertice_origem = "1"
moedas = ["5", "9", "12", "15", "16", "18", "21", "25", "28"]

pilha = [vertice_origem]
vertices_visitados = Arvore(vertice_origem)

while pilha and moedas:
    vertice = pilha[-1]
    explorado = True
    for w in grafo_heroi.get_adjacentes(vertice):
        if not vertices_visitados.localizar_nodo(w):
            explorado = False
            break
    if explorado:
        pilha.pop(-1)
    for w in grafo_heroi.get_adjacentes(vertice):
        if not vertices_visitados.localizar_nodo(w):
            vertices_visitados.inserir_nodo(vertice, w)
            if w in moedas:
                moedas.remove(w)
            pilha.append(w)
            break

vertices_visitados.imprimir()

input(f"{Fore.YELLOW}\nENTER para finalizar{Fore.RESET}")

