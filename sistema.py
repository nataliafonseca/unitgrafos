import os
os.getcwd()
from lib.interface import *
from time import sleep


while True:
    resposta = menu(["Cadastrar Grafo", "Imprimir Grafo", "Sair do sistema"])
    if resposta == 1:
        cabecalho("Opção 1")
    elif resposta == 2:
        cabecalho("Opção 2")
    elif resposta == 3:
        cabecalho("Saindo do sistema... Até logo!")
    else:
        print(Fore.RED + "ERRO: Por favor, digite um número inteiro entre "
                         "1 e 3" + Fore.RESET)
    sleep(1)
