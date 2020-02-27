from model.grafo import *

color()


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(Fore.RED + "ERRO: por favor, digite um número inteiro"
                  + Fore.RESET)
        except KeyboardInterrupt:
            print(Fore.RED + "Usuário preferiu não digitar esse número" +
                  Fore.RESET)
            return 0
        else:
            return n


def linha(tam=50):
    return "-" * tam


def cabecalho(txt):
    print(linha())
    print(txt)
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    for i, item in enumerate(lista):
        print(Fore.YELLOW + f"{i + 1} - " + Fore.BLUE + f"{item}" + Fore.RESET)
    print(linha())
    opc = leiaint("Sua opção: ")
    return opc


def teste_grafo_definido(grafo):
    digrafo = False
    valorado = False
    q_vertices = 12
    arestas = "1-2, 1-3, 2-3, 2-5, 2-6, 3-4, 3-6, 4-7, 5-6, 5-9, 5-10, 6-7," \
              "6-10, 6-11, 7-8, 7-12, 8-12, 9-10, 10-11"
    grafo_exemplo = Grafo(digrafo, valorado, q_vertices, arestas)
    if not grafo:
        print(Fore.RED + "ATENÇÃO! Você ainda não definiu um grafo, "
                         "serão impressas as informações correspondentes "
                         "ao grafo representado em 'exemplo/simples.png'. "
                         "Para adicionar seu proprio grafo, selecione a "
                         "opção 1."
              + Fore.RESET)
        return grafo_exemplo
    return grafo
