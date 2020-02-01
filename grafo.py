quantidade_vetores = int(input("Informe a quantidade de vetores do grafo: "))

grafo = []
for i in range(quantidade_vetores):
    grafo.append([0] * quantidade_vetores)

for i in range(quantidade_vetores):
    print(grafo[i])
