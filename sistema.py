from lib.interface import *
from model.grafo import Grafo
from time import sleep

grafo = None

while True:
    resposta = menu(["Definir Grafo",
                     "Resgatar Grafo Salvo",
                     "Imprimir Informações do Grafo",
                     "Imprimir Matriz de Adjacencia",
                     "Imprimir Estrutura de Adjacencia",
                     "Obter Vértices Adjacentes",
                     "Obter Menor Caminho entre Dois Vértices",
                     "Obter Menores Caminhos a partir de um Vértice",
                     "Sair do sistema"])

    if resposta == 1:
        print()
        cabecalho("Opção 1 - Definir Grafo")
        grafo = Grafo.definir_grafo()
        print(Fore.BLUE + "Deseja salvar seu grafo? digite 1 para sim ou 0 "
                          "para não:" + Fore.RESET)
        cadastrar = bool(int(input()))
        if cadastrar:
            print()
            grafo.cadastrar_grafo()
        print()

    elif resposta == 2:
        print()
        cabecalho("Opção 2 - Resgatar Grafo Salvo")
        grafo = Grafo.resgatar_grafo()
        print()

    elif resposta == 3:
        print()
        cabecalho("Opção 3 - Imprimir Informações do Grafo")
        grafo, definido = teste_grafo_definido(grafo)
        grafo.imprimir_informacoes()
        if not definido:
            grafo = None
        print()

    elif resposta == 4:
        print()
        cabecalho("Opção 4 - Imprimir Matriz de Adjacencia")
        grafo, definido = teste_grafo_definido(grafo)
        grafo.imprimir_matriz_adjacencia()
        if not definido:
            grafo = None
        print()

    elif resposta == 5:
        print()
        cabecalho("Opção 5 - Imprimir Estrutura de Adjacencia")
        grafo, definido = teste_grafo_definido(grafo)
        grafo.imprimir_estrutura_adjacencia()
        if not definido:
            grafo = None
        print()

    elif resposta == 6:
        print()
        cabecalho("Opção 6 - Obter Vértices Adjacentes")
        grafo, definido = teste_grafo_definido(grafo)
        vertice = input("Informe o vértice: ")
        print()
        print(grafo.get_adjacentes(vertice))
        if not definido:
            grafo = None
        print()

    elif resposta == 7:
        print()
        cabecalho("Opção 7 - Obter Menor Caminho entre Dois Vértices")
        grafo, definido = teste_grafo_definido(grafo)
        origem = input("Informe o vértice inicial: ")
        destino = input("Informe o vértice final: ")
        print()
        grafo.imprimir_menor_caminho(origem, destino)
        if not definido:
            grafo = None
        print()

    elif resposta == 8:
        print()
        cabecalho("Opção 8 - Obter Menores Caminhos a partir de um Vértice")
        grafo, definido = teste_grafo_definido(grafo)
        origem = input("Informe o vértice inicial: ")
        grafo.imprimir_menor_caminho(origem)
        if not definido:
            grafo = None
        print()

    elif resposta == 9:
        print()
        cabecalho("Saindo do sistema... Até logo!")
        sleep(1)
        break

    else:
        print(Fore.RED + "ERRO: Por favor, digite um número inteiro entre "
                         "1 e 8" + Fore.RESET)

    sleep(1)
