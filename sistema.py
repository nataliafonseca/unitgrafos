from lib.interface import *
from time import sleep
from colorama import init as color
from lib.grafo import Grafo

color()

# Grafo de Exemplo - será utilizado se o usuário não cadastrar um grafo.
q_vertices = 12
arestas = "1-2, 1-3, 2-3, 2-5, 2-6, 3-4, 3-6, 4-7, 5-6, 5-9, 5-10, 6-7," \
          "6-10, 6-11, 7-8, 7-12, 8-12, 9-10, 10-11"
digrafo = False
grafo_exemplo = Grafo(q_vertices, arestas, digrafo)
grafo = False

while True:
    resposta = menu(["Definir Grafo",
                     "Resgatar Grafo Salvo",
                     "Imprimir Matriz de Adjacencia",
                     "Imprimir Estrutura de Adjacencia",
                     "Sair do sistema"])

    if resposta == 1:
        print()
        cabecalho("Opção 1 - Definir Grafo")
        grafo = Grafo.definir_grafo()
        cadastrar = bool(input("Deseja salvar seu grafo? digite 0 para não ou "
                               "1 para sim: "))
        if cadastrar:
            Grafo.cadastrar_grafo(grafo)
        print()

    elif resposta == 2:
        print()
        cabecalho("Opção 2 - Resgatar Grafo Salvo")
        grafo = Grafo.resgatar_grafo()

    elif resposta == 3:
        print()
        cabecalho("Opção 3 - Imprimir Matriz de Adjacencia")
        if not grafo:
            print(Fore.RED + "ATENÇÃO! Você ainda não definiu um grafo, "
                             "será impressa a matriz correspondente ao grafo "
                             "representado em 'grafo_exemplo.png'. Para "
                             "adicionar seu proprio grafo, selecione a opção 1"
                  + Fore.RESET)
            grafo = grafo_exemplo

        grafo.print_matriz_adjacencia()
        print()

    elif resposta == 4:
        print()
        cabecalho("Opção 4 - Imprimir Estrutura de Adjacencia")
        if not grafo:
            print(Fore.RED + "ATENÇÃO! Você ainda não definiu um grafo, "
                             "será impressa a estrutura correspondente ao "
                             "grafo representado em 'grafo_exemplo.png'. Para "
                             "adicionar seu proprio grafo, selecione a opção 1"
                  + Fore.RESET)
            grafo = grafo_exemplo
        grafo.print_estrutura_adjacencia()
        print()

    elif resposta == 5:
        print()
        cabecalho("Saindo do sistema... Até logo!")
        break

    else:
        print('\033[31m' + "ERRO: Por favor, digite um número inteiro entre "
                           "1 e 5" + '\033[m')
    sleep(1)
