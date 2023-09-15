# Programa Python para o algoritmo de Kruskal encontrar
# Árvore geradora mínima de um determinado conectado,
# gráfico não direcionado e ponderado


# Classe para representar um gráfico
class Graph:

	def __init__(self, vertices):
		self.V = vertices
		self.graph = []

	# Função para adicionar uma aresta ao gráfico
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	# Uma função de utilidade para encontrar o conjunto de um elemento i
	# (realmente usa técnica de compactação de caminho)
	def find(self, parent, i):
		if parent[i] != i:

			# Reatribuição do pai do nó
			# para o nó raiz como
			# compactação de caminho requer
			parent[i] = self.find(parent, parent[i])
		return parent[i]

	# Uma função que faz a união de dois conjuntos de x e y
	# (usa união por classificação)
	def union(self, parent, rank, x, y):

		# Anexe uma árvore de classificação menor na raiz de
		# árvore de classificação alta (União por Classificação)
		if rank[x] < rank[y]:
			parent[x] = y
		elif rank[x] > rank[y]:
			parent[y] = x

		# Se as classificações forem iguais, crie uma como root
		# e aumentar sua classificação em um
		else:
			parent[y] = x
			rank[x] += 1

	# A principal função para construir o MST
	# using Kruskal's algorithm
	def KruskalMST(self):

		# Isso armazenará o MST resultante
		result = []

		# Uma variável de índice, usada para arestas classificadas
		i = 0

		# Uma variável de índice, usada para resultado[]
		e = 0

		# Classifique todas as arestas em
		# ordem não decrescente de seus
		# pesos
		self.graph = sorted(self.graph,
							key=lambda item: item[2])

		parent = []
		rank = []

		# Crie subconjuntos V com elementos únicos
		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		# O número de arestas a serem obtidas é menor que V-1
		while e < self.V - 1:

			# Escolha a menor aresta e incremente
			# o índice para a próxima iteração
			u, v, w = self.graph[i]
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent, v)

		   # Se incluir esta aresta não
           # ciclo de causa e, em seguida, inclua-o no resultado
           # e incrementar o índice de resultado
           # para a próxima borda
			if x != y:
				e = e + 1
				result.append([u, v, w])
				self.union(parent, rank, x, y)
			# Caso contrário, descarte a borda

		minimumCost = 0
		print("Bordas no MST construído")
		for u, v, weight in result:
			minimumCost += weight
			print("%d -- %d == %d" % (u, v, weight))
		print("Árvore de abrangência mínima", minimumCost)


# Código do motorista
if __name__ == '__main__':
	g = Graph(4)
	g.addEdge(0, 1, 10)
	g.addEdge(0, 2, 6)
	g.addEdge(0, 3, 5)
	g.addEdge(1, 3, 15)
	g.addEdge(2, 3, 4)

	# Function call
	g.KruskalMST()