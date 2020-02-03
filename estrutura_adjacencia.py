# quantidade_vetores = int(input("Informe a quantidade de vetores do grafo: "))
grafo = {}

quantidade_vetores = 6
for i in range(quantidade_vetores):
    grafo.update({i: []})

# arestas = input("Informe as arestas do grafo, separe cada os vertices "
#                 "ligados por virgulas e os pares de vertices por "
#                 "ponto e virgula.")
arestas = "0,1;1,2;1,3;2,4;2,5"
arestas = arestas.split(";")

for par in arestas:
    i, j = par.split(",")
    i, j = int(i.strip()), int(j.strip())
    grafo[i].append(j)

print(grafo)
