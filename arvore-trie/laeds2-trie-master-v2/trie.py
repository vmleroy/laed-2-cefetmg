from typing import List
class NoTrie:
	def __init__(self, letra="", fim_palavra:bool=False):
		self.filhos = dict()
		self.fim_palavra = fim_palavra
		self.letra = letra

	##@property
	def insere(self, letra:str, fim_palavra:bool):
		self.filhos[letra] = NoTrie(letra, fim_palavra)

	def existe_letra(self, letra:str) -> bool:
		return letra in self.filhos

	def obtem_no_filho(self,letra:str) -> "NoTrie":       
		return self.filhos[letra]

	def nos_filhos(self) -> List[str]:
		return self.filhos.keys()

class Trie:
	def __init__(self, raiz=None):
		if not raiz:
			raiz = NoTrie()
		self.raiz = raiz

	def insere(self, palavra:str):
		no_atual = self.raiz

		for i,letra in enumerate(palavra):
			if not no_atual.existe_letra(letra):
				no_atual.insere(letra, i == len(palavra)-1)

			no_atual = no_atual.obtem_no_filho(letra)
		no_atual.fim_palavra = True

	def pesquisa(self, palavra:str) -> bool:
		raiz = self.raiz
		for letra in palavra:
			if not raiz.existe_letra(letra):
				return False
			raiz = raiz.obtem_no_filho(letra)
		return raiz != None and raiz.fim_palavra

	def preditor_palavras(self, no_atual:"NoTrie", palavra:str = None, palavra_list:list = None):
		#Se encontrar o final da palavra, vamos adicionar na lista a palavra nova        
		if no_atual.fim_palavra:
			palavra_list.append(palavra)
            
		#Caso nao seja a ultima palavra, vamos procurar os filhos do no_atual, juntamente com a letra que o representa.
		#Vamos realizar tambem uma recursao utilizando a (letra encontrada + palavra atual) e o no que da letra que  representa
		for letra, i in no_atual.filhos.items():
			self.preditor_palavras(i, palavra + letra, palavra_list)          
            
	def preditor(self, prefixo_palavra:str) -> List[str]:		
		#obtem a ultima letra do prefixo
		no_ult_letra_prefixo = self.raiz
		for letra in prefixo_palavra:
			if not no_ult_letra_prefixo.existe_letra(letra):
				return []

			no_ult_letra_prefixo = no_ult_letra_prefixo.obtem_no_filho(letra)

		#por meio da ultima letra do prefixo, faz a predição das possiveis palavras
		#Para isso, você poderá precisar de fazer um método recursivo
		### SEU Código aqui      
		palavras_preditor = []
		self.preditor_palavras(no_ult_letra_prefixo, prefixo_palavra, palavras_preditor)             
                    
		return palavras_preditor

def main():
	pass
	# palavras criadas
	#palavras = ["teste", "a", "texto", "aresta", "ano",
	#		  "zebra", "trabalho",]

	# arvore Trie
	#arvore = Trie()

	# insere palavras
	#print("Insercao:")
	#for palavra in palavras:
	#	arvore.insere(palavra)
	#	print(f"palavra -{palavra}- inserida")

	#print("\n")
	# pesquisa
	#print("Pesquisa:")
	#print(f'-{"ano"}-: {arvore.pesquisa("ano")}')
	#print(f'-{"ana"}-: {arvore.pesquisa("ana")}')
	#print(f'-{"teste"}-: {arvore.pesquisa("teste")}')
	#print(f'-{"testa"}-: {arvore.pesquisa("testa")}')
	#print(f'-{"texto"}-: {arvore.pesquisa("texto")}')
	#print(f'-{"trabalho"}-: {arvore.pesquisa("trabalho")}')

if __name__ == '__main__':
	main()
