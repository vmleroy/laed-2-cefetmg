from typing import List, Dict
class Vertice:
	def __init__(self, valor):
		self.valor = valor
		self.adjacencias = {}

	def insere(self, vizinho, peso:int):
		self.adjacencias[vizinho] = peso

	def obtem_valor(self):
		return self.valor

class Grafo:
	def __init__(self):
		self.vertices = {}

	def adiciona_vertice(self, valor_vertice) -> Vertice:
		#importante pois podem haver vertices que não tem arestas
		novo_vertice = Vertice(valor_vertice)
		self.vertices[valor_vertice] = novo_vertice
		return novo_vertice

	def adiciona_aresta(self, valor_origem, valor_destino, peso:int=1):
		vertice_origem = self.obtem_vertice(valor_origem)
		vertice_destino = self.obtem_vertice(valor_destino)
		if not vertice_origem is None and not vertice_destino is None:
			vertice_origem.insere(vertice_destino, peso)

	def obtem_vertice(self, valor_vertice:str) -> Vertice:
		if valor_vertice in self.vertices:
			return self.vertices[valor_vertice]
		else:
			return None

	def e_um_dag_dfs(self, vertice:Vertice, visitados:Dict[Vertice,int]) -> bool:
		"""
		vertice: vertice a ser explorado
		visitados: Dicionário que mapeia, cada vertice explorado. 
				Se visitados[vertice]==1: o vértice ainda sendo explorado ou foi encontrado um ciclo neste vertice explorado
				Se visitados[vertice]==2: o vértice já foi explorado totalmente e não foi encontrado ciclo durante a exploração
		"""
		visitados[vertice] = 1        
        
		for vizinho in vertice.adjacencias:
			if vizinho not in visitados:            
				if self.e_um_dag_dfs(vizinho, visitados) == True:
					return True
			elif visitados[vizinho] == 1:
				return True
            
		visitados[vertice] = 2
		return False              

	def e_um_dag(self) -> bool:
		visitados = {}
		aciclico:bool = False        
		for vertice in self.vertices.values():            
			if vertice not in visitados:
				ciclico = self.e_um_dag_dfs(vertice, visitados)                 
				print(aciclico)
				if  ciclico is True:
					return True
		print(visitados)                
		return False

	def ordenacao_topologica(self) -> List:
		pass

