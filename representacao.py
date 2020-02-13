from grafo import Grafo

q_vertices = int(input("Informe a quantidade de vertices do grafo: "))
arestas = input("Informe as arestas do grafo (deve-se separar os vertices "
                "adjacentes por traços e cada par de vertices deve ser "
                "separado por virgula. Por exemplo: '1-2, 1-3, 1-4, 2-3'): ")

# q_vertices = 8
# arestas = "1-2, 1-3, 2-4, 2-5, 3-4, 4-5, 4-6, 6-7, 6-8, 7-8"

grafo = Grafo(q_vertices, arestas)

print()
print("****************** MATRIZ DE ADJACENCIA *******************")
print()
grafo.get_matriz_adjacencia()
print()
print("***********************************************************")

print()
print("***************** ESTRUTURA DE ADJACENCIA *****************")
print()
grafo.get_estrutura_adjacencia()
print()
print("***********************************************************")

print()
input("Entre ENTER para finalizar.")
