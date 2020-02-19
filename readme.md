# Teoria dos Grafos

Repositório criado para versionamendo do projeto da disciplina Teoria dos Grafos, ministrada pelo Prof. Adolfo Pinto no primeiro semestre de 2020 na Universidade Tiradentes.

## Requisitos

Para a instalação dos requisitos do projeto abra o promp de comando, navegue até a pasta do projeto e insira o seguinte comando:
```
pip install -r requirements.txt
```

## Inicialização do Programa
Para dar inicio ao programa, execute o arquivo "sistema.py"
Ao abrir o script, você será apresentado com o menu inicial do programa.

## Representação do Grafo
Quando escolher a opção "1 - Definir Grafo" você será solicitado a informar a quantidade de vértices do grafo e, em seguida, as arestas. Por ultimo, deve ser informado se o grafo em questão é direcionado ou não.

Para a quantidade de vértices, deve-se considerar o primeiro vertice do grafo como vértice '1'.

Para informar as arestas, deve-se separar os vertices adjacentes por traços e cada par de vertices deve ser separado por virgula.

Para definir se o grafo é um digrafo, é preciso apenas responder com 1 (para sim) ou 0 (para não).

Por exemplo, para representação do grafo presente na seguinte imagem:

![Exemplo de Grafo](grafo_exemplo.png)

Deve-se entrar:

Informe a quantidade de vertices do grafo:
```python
12
```
Informe as arestas do grafo:

```python
1-2, 1-3, 2-3, 2-5, 2-6, 3-4, 3-6, 4-7, 5-6, 5-9, 5-10, 6-7, 6-10, 6-11, 7-8, 7-12, 8-12, 9-10, 10-11
```

O grafo é direcionado? Digite 1 para sim ou 0 para não: 
```python
0
```

Alternativamente, os valores podem ser incluidos diretamente no arquivo "grafos.txt" e resgatados utilizando a opção "2 - Resgatar Grafo"

## Autores:
* Felipe Carvalho de Gois
* Natália Braga da Fonseca
* Sande Andrade de Souza Costa
