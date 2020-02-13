from grafo import Grafo

# q_vertices = int(input("Informe a quantidade de vertices do grafo: "))
# arestas = input("Informe as arestas do grafo (deve-se separar os vertices "
#                 "adjacentes por traços e cada par de vertices deve ser "
#                 "separado por virgula. Por exemplo: '1-2, 1-3, 1-4, 2-3'): ")
# digrafo = bool(int(input("O grafo é direcionado? "
#                          "Digite 1 se sim ou 0 se não.")))

q_vertices = 12
arestas = "1-2, 1-3, 2-3, 2-5, 2-6, 3-4, 3-6, 4-7, 5-6, 5-9, 5-10, 6-7," \
          "6-10, 6-11, 7-8, 7-12, 8-12, 9-10, 10-11"
digrafo = False

grafo = Grafo(q_vertices, arestas, digrafo)

print()
print("****************** MATRIZ DE ADJACENCIA *******************")
print()
grafo.print_matriz_adjacencia()
print()
print("***************** ESTRUTURA DE ADJACENCIA *****************")
print()
grafo.print_estrutura_adjacencia()

print()
input("Entre ENTER para finalizar.")
