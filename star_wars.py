from model.grafo import Grafo
from lib.arvore import Arvore

grafo_starwars = Grafo(False, False, ["YODA", "COUNT DOOKU", "QUIN GON JINN",
                                      "OBI WAN KENOBI", "CLIEGG LARS",
                                      "SHMI SKYWALKER", "OWEN LARS",
                                      "BERU LARS", "ANAKIN SKYWALKER",
                                      "RUWEE NABERRIE", "JOBAL NABERRIE",
                                      "PADME AMIDALA", "BAIL ORGANA",
                                      "BREHA ORGANA", "DARTH MAUL",
                                      "EMPEROR PALPATINE", "LUKE SKYWALKER",
                                      "PRINCESS LEIA ORGANA", "HAN SOLO",
                                      "SUPREME LEADER SNOKE", "REY",
                                      "BEN SOLO", "DARTH PLAGUEIS"],
                       ["YODA-COUNT DOOKU", "YODA-LUKE SKYWALKER",
                        "COUNT DOOKU-EMPEROR PALPATINE",
                        "COUNT DOOKU-QUIN GON JINN",
                        "QUIN GON JINN-OBI WAN KENOBI",
                        "OBI WAN KENOBI-LUKE SKYWALKER",
                        "OBI WAN KENOBI-ANAKIN SKYWALKER",
                        "CLIEGG LARS-SHMI SKYWALKER", "CLIEGG LARS-OWEN LARS",
                        "SHMI SKYWALKER-ANAKIN SKYWALKER",
                        "OWEN LARS-BERU LARS", "OWEN LARS-LUKE SKYWALKER",
                        "BERU LARS-LUKE SKYWALKER",
                        "ANAKIN SKYWALKER-LUKE SKYWALKER",
                        "ANAKIN SKYWALKER-PRINCESS LEIA ORGANA",
                        "ANAKIN SKYWALKER-PADME AMIDALA",
                        "ANAKIN SKYWALKER-EMPEROR PALPATINE",
                        "RUWEE NABERRIE-JOBAL NABERRIE",
                        "RUWEE NABERRIE-PADME AMIDALA",
                        "JOBAL NABERRIE-PADME AMIDALA",
                        "BAIL ORGANA-BREHA ORGANA",
                        "BAIL ORGANA-PRINCESS LEIA ORGANA",
                        "BREHA ORGANA-PRINCESS LEIA ORGANA",
                        "DARTH MAUL-EMPEROR PALPATINE",
                        "EMPEROR PALPATINE-DARTH PLAGUEIS",
                        "LUKE SKYWALKER-PRINCESS LEIA ORGANA",
                        "LUKE SKYWALKER-REY", "LUKE SKYWALKER-BEN SOLO",
                        "PRINCESS LEIA ORGANA-BEN SOLO",
                        "PRINCESS LEIA ORGANA-HAN SOLO", "HAN SOLO-BEN SOLO",
                        "SUPREME LEADER SNOKE-BEN SOLO"])

vertice_origem = "YODA"
vertice_destino = "PRINCESS LEIA ORGANA"

fila = [vertice_origem]
vertices_visitados = Arvore(vertice_origem)

while fila:
    if vertices_visitados.localizar_nodo(vertice_destino):
        break
    vertice = fila[0]
    fila.pop(0)
    for w in grafo_starwars.get_adjacentes(vertice):
        if not vertices_visitados.localizar_nodo(w):
            vertices_visitados.inserir_nodo(vertice, w)
            fila.append(w)
    vertices_visitados.imprimir()
    print()

vertices_visitados.imprimir()

input()
