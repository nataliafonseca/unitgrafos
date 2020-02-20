from model.grafo import *
from time import sleep

# Grafo de Exemplo - será utilizado se o usuário não cadastrar um grafo.
digrafo = False
valorado = False
q_vertices = 12
arestas = "1-2, 1-3, 2-3, 2-5, 2-6, 3-4, 3-6, 4-7, 5-6, 5-9, 5-10, 6-7," \
          "6-10, 6-11, 7-8, 7-12, 8-12, 9-10, 10-11"

grafo = None
grafo_exemplo = Grafo(digrafo, valorado, q_vertices, arestas)


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
        print(Fore.BLUE + "Deseja salvar seu grafo? digite 1 para sim ou 0 "
                          "para não:" + Fore.RESET)
        cadastrar = bool(input())
        print()
        if cadastrar:
            grafo.cadastrar_grafo()
        print()

    elif resposta == 2:
        print()
        cabecalho("Opção 2 - Resgatar Grafo Salvo")
        grafo = Grafo.resgatar_grafo()
        print()

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
        print(Fore.RED + "ERRO: Por favor, digite um número inteiro entre "
                         "1 e 5" + Fore.RESET)

    sleep(1)
