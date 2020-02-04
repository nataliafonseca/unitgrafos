# quantidade_vetores = int(input("Informe a quantidade de vetores do grafo: "))
quantidade_vetores = 6

grafo = []
for i in range(quantidade_vetores):
    grafo.append([0] * quantidade_vetores)

# arestas = input("Informe as arestas do grafo, separe cada os vertices "
#                 "ligados por traços e os pares de vertices por "
#                 "ponto e virgula.")
arestas = "0-1;1-2;1-3;2-4;2-5"
arestas = arestas.split(";")

for par in arestas:
    i, j = par.split("-")
    i, j = int(i.strip()), int(j.strip())
    grafo[i][j] = 1

for i in range(quantidade_vetores):
    print(grafo[i])
