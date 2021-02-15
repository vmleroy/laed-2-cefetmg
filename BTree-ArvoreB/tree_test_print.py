import unittest
from tree import BTree

class TestNode():
    def setUp(self):
        pass

    def teste_pesquisa(self):
        print("TESTE DE PESQUISA")
        keys = [20, 10, 40, 50, 30, 55, 3, 11, 4, 28, 36, 33, 52, 17, 25, 13, 54, 9, 43, 8, 48]
        arvore_b_ordem_2 = BTree(2)
        for i in keys:    
            arvore_b_ordem_2.insert_key(i)
        
        chaves_procuradas = [36,20,100,48]
        for i in chaves_procuradas:
            print("Key:", i)
            no_procura, posicao = arvore_b_ordem_2.search_tree(i)
            if (no_procura is not None and posicao is not None):
                print("Encontrada key no node:", no_procura.keys, " Na posicao:",posicao)
            else:
                print("Nao ha essa chave na arvore") 
        print()

        
    def teste_insercao(self):
        print("TESTE DE INSERCAO NA ARVORE B")
        keys = [20, 10, 40, 50, 30, 55, 3, 11, 4, 28, 36, 33, 52, 17, 25, 13, 54, 9, 43, 8, 48]
        arvore_b_ordem_2 = BTree(2)
        for i in keys:    
            arvore_b_ordem_2.insert_key(i)
        arvore_b_ordem_2.print_tree()
        print()

        
    def teste_delete(self):
        print("TESTE DE DELECAO NA ARVORE B")
        keys = [20, 10, 40, 50, 30, 55, 3, 11, 4, 28, 36, 33, 52, 17, 25, 13, 54, 9, 43, 8, 48]
        arvore_b_ordem_2 = BTree(2)
        for i in keys:    
            arvore_b_ordem_2.insert_key(i)
            
        chave_deletada = [36, 33, 3, 10, 25]
        for i in chave_deletada:
            print("Key retirada:", i)
            arvore_b_ordem_2.delete_key(i)
            arvore_b_ordem_2.print_tree()
        print()

        

if __name__ == "__main__":
    teste_node = TestNode()
    teste_node.teste_insercao()
    teste_node.teste_pesquisa()
    teste_node.teste_delete()
