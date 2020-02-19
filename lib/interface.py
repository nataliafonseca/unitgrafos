from colorama import init as color, Fore


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


def linha(tam=42):
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
