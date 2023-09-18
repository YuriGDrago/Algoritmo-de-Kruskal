# Kruskal's Minimum Spanning Tree Algorithm

Este é um exemplo de implementação em Python do algoritmo de Kruskal para encontrar a Árvore de Abrangência Mínima (Minimum Spanning Tree - MST) de um grafo conectado, não direcionado e ponderado. A MST é uma subárvore do grafo original que abrange todos os vértices com o menor custo possível. O algoritmo de Kruskal é amplamente utilizado para resolver esse problema de otimização.

### Conteúdo
1. Visão Geral
2. Como Funciona o Código
3. Requisitos
4. Execução
5. Exemplo


### Visão Geral

O código fornece uma implementação do algoritmo de Kruskal em Python para encontrar a MST de um grafo. O algoritmo funciona classificando todas as arestas do grafo em ordem crescente de peso e, em seguida, adicionando as arestas à MST se elas não criarem ciclos. O resultado é uma lista das arestas da MST e o custo total da MST.

### Como Funciona o Código

O código é composto por uma classe Graph que representa o grafo e implementa o algoritmo de Kruskal. Aqui está uma visão geral das principais partes do código:

**__init__(self, vertices):** O construtor da classe inicializa o grafo com um número dado de vértices e uma lista vazia para representar as arestas do grafo.

**addEdge(self, u, v, w):** Este método é usado para adicionar uma aresta ao grafo. Os parâmetros u, v e w representam os vértices de origem, destino e o peso da aresta, respectivamente.

**find(self, parent, i):** Este método implementa a operação "find" com compressão de caminho. Ele é usado para encontrar o conjunto (representado pelo elemento raiz) ao qual um vértice pertence.

**union(self, parent, rank, x, y):** Este método implementa a operação "union" por classificação de rank. Ele é usado para unir dois conjuntos (árvores) em um único conjunto, garantindo que a árvore menor seja anexada à árvore maior.

**KruskalMST(self):** Este é o método principal que encontra a MST usando o algoritmo de Kruskal. Ele classifica todas as arestas do grafo em ordem crescente de peso, inicializa conjuntos individuais para cada vértice e depois começa a adicionar arestas à MST se elas não formarem ciclos.

**if __name__ == '__main__'::** Esta parte do código cria um objeto da classe Graph, adiciona arestas ao grafo e chama o método KruskalMST para encontrar a MST.

### Requisitos
O código foi escrito em Python 3 e não requer bibliotecas externas.

### Execução
Para executar o código, siga estas etapas:

1. Abra um terminal.

2. Navegue até o diretório onde o arquivo Python com o código está localizado.

3. Execute o código Python com o seguinte comando:

```bash
python nome_do_arquivo.py
```
Substitua **nome_do_arquivo.py** pelo nome do arquivo Python que contém o código.

### Exemplo
O código inclui um exemplo de uso onde um grafo é criado com 4 vértices e 5 arestas, e em seguida, a MST é calculada usando o algoritmo de Kruskal. Os resultados são impressos na saída.




