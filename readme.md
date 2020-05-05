# Teoria dos Grafos

Repositório criado para versionamendo do projeto da disciplina Teoria dos Grafos, ministrada pelo Prof. Adolfo Pinto no primeiro semestre de 2020 na Universidade Tiradentes.

## Requisitos

Para a instalação dos requisitos do projeto abra o promp de comando, navegue até a pasta do projeto e insira o seguinte comando:
```
pip install -r requirements.txt
```

## Inicialização do Programa

Para dar inicio ao programa, execute o arquivo "sistema.py".

Ao abrir o script, você será apresentado com o menu inicial do programa.

## Representação do Grafo

Quando escolher a opção "1 - Definir Grafo" o programa questionará se o mesmo é direcionado (ou digrafo) e, em seguida, se é valorado.
Para estas perguntas, é preciso apenas responder com 1 (para sim) ou 0 (para não).

Então, você será solicitado a informar os vértices do grafo e, em seguida, as arestas.

Para os vértices, deve-se listar em ordem e separando por vírgula (ex.: A, B, C, D, E, ..., L).

Para informar as arestas, deve-se separar os vertices adjacentes por traços e cada par de vertices deve ser separado por virgula (ex.: A-B, A-C, ..., B-C) . Para grafos valorados, separam-se por tracos os vertices iniciais, finais e o peso (ex.: A-B-10, A-C-100, ..., B-C-5).

Por exemplo, para representação do grafo presente na seguinte imagem:

![Exemplo de Grafo](exemplos/simples.png)

Deve-se entrar:

O grafo é direcionado? Digite 1 para sim ou 0 para não: 
```python
0
```
O grafo é valorado? Digite 1 para sim ou 0 para não: 
```python
0
```
Informe os vertices do grafo:
```python
A, B, C, D, E, F, G, H, I, J, K, L
```
Informe as arestas do grafo:
```python
A-B, A-C, B-C, B-E, B-F, C-D, C-F, D-G, E-F, E-I, E-J, F-G, F-J, F-K, G-H, G-L, H-L, I-J, J-K
```

Ao final, o programa perguntará se você deseja salvar o grafo para utilizar posteriormente.

Alternativamente, os valores podem ser incluidos diretamente no arquivo "grafos.json", seguindo o padrão dos exemplos no arquivo, e resgatados utilizando a opção "2 - Resgatar Grafo"

## Implementação dos métodos
Os métodos chamados pelo programas estão implementados no arquivo 'model/grafo.py'. A documentação desses métodos pode ser acessada no arquivo 'model.grafo.html'.
