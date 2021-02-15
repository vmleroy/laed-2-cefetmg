import unittest
from tree import BTree

class TestNode(unittest.TestCase):
    def setUp(self):
        pass

    def teste_pesquisa(self):
        keys = [20, 10, 40, 50, 30, 55, 3, 11, 4, 28, 36, 33, 52, 17, 25, 13, 54, 9, 43, 8, 48]
        
        chaves_procuradas = [36,20,100,48,200,3,300]
        arr_esperado = [True, True, False, True, False, True, False]
                
        arvore = BTree(2)
        
        for i in keys:    
            arvore.insert_key(i)
                
        existe_chave:bool = False
        for i in range(len(chaves_procuradas)):           
            no_procura, posicao = arvore.search_tree(chaves_procuradas[i])
            if no_procura is not None and posicao is not None:
                existe_chave = True
            else:
                existe_chave = False
            self.assertEqual(existe_chave, arr_esperado[i],f"Erro na árvore de teste: o numero {chaves_procuradas[i]} não foi encontrada")

    def teste_insercao(self):
        keys = [20, 10, 40, 50, 30, 55, 3, 11, 4, 28, 36, 33, 52, 17, 25, 13, 54, 9, 43, 8, 48]
        arr_esperado = [[20], [4, 11], [3], [8, 9, 10], [13, 17], [30, 40, 52], [25, 28], [33, 36], [43, 48, 50], [54, 55]]
        
        arvore = BTree(2)
        for i in keys:    
            arvore.insert_key(i)

        arr_recebido = arvore.get_tree_as_array()
        for i in range(len(arr_esperado)):
            self.assertEqual(arr_recebido[i], arr_esperado[i],f"Erro! Arvore esta diferente do esperado no node {arr_recebido[i]}, o esperado seria {arr_esperado[i]}")
            
    def teste_delecao(self):            
        keys = [20, 10, 40, 50, 30, 55, 3, 11, 4, 28, 36, 33, 52, 17, 25, 13, 54, 9, 43, 8, 48]
        arr_esperado = [[20], [8, 11], [4], [9], [13, 17], [40, 52], [28, 30], [43, 48, 50], [54, 55]]
        
        arvore = BTree(2)
        for i in keys:    
            arvore.insert_key(i)
            
        chave_deletada = [36, 33, 3, 10, 25]
        for i in chave_deletada:
            arvore.delete_key(i)      

        arr_recebido = arvore.get_tree_as_array()
        for i in range(len(arr_esperado)):
            self.assertEqual(arr_recebido[i], arr_esperado[i],f"Erro! Arvore esta diferente do esperado no node {arr_recebido[i]}, o esperado seria {arr_esperado[i]}")


if __name__ == "__main__":
    unittest.main()
