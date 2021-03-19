from typing import List

class Node:
    def __init__(self, key, left:"Node"=None, right:"Node"=None):
        self.key = key
        self.left = left
        self.right = right

        
    def print_tree(self):
        """
        Imprime a arvore a partir do nodo atual
        """
        if self.left:
            self.left.print_tree()
        print(self.key, end=" ")
        if self.right:
            self.right.print_tree()


    def insert(self, key) -> bool:
        """
        Insere um nodo na árvore que a chave "key"
        """
        if key < self.key:
            if self.left:
                return self.left.insert(key)
            else:
                self.left = Node(key)
                return True
        elif key > self.key:
            if self.right:
                return self.right.insert(key)
            else:
                self.right = Node(key)
                return True
        else:
            return False


    def search(self, key) -> bool:
        """
        Retorna verdadeiro caso a chave `key` exista na árvore
        """
        if key < self.key:
            if self.left:
                return self.left.search(key)
        elif key > self.key:
            if self.right:
                return self.right.search(key)
        else:
            return True
        return False


    def to_sorted_array(self, arr_result:List =None) -> List:
        """
        Retorna um vetor das chaves ordenadas.
        arr_result: Parametro com os itens já adicionados.
        """
        if(arr_result == None):
            arr_result = []

        if self.left:
            self.left.to_sorted_array(arr_result)

        arr_result.append(self.key)

        if self.right:
            self.right.to_sorted_array(arr_result)
        return arr_result

    
    def max_depth(self,current_max_depth:int=0) -> int:
        """
        Calcula a maior distancia entre o nodo raiz e a folha
        current_max_depth: Valor representando a maior distancia até então
                           ao chamar pela primeira vez, não é necessário usa-lo
        """
        current_max_depth = current_max_depth +1
        val_left,val_right = current_max_depth,current_max_depth

        if self.left:
            val_left = self.left.max_depth(current_max_depth)
        if self.right:
            val_right = self.right.max_depth(current_max_depth)

        if(val_left>val_right):
            return val_left
        else:
            return val_right

        
    def position_node(self, key, current_position:int=1) -> int:
        """
            Retorna a posição do nodo desejado na árvore
            current_position: representa a posição da árvore naquele momento
                           ao chamar pela primeira vez, não é necessário usa-lo
        """
        if self.search(key):
            if key < self.key:
                if self.left:
                    current_position = current_position * 2
                    return self.left.position_node(key, current_position)
            elif key > self.key:
                if self.right:
                    current_position = (current_position * 2) + 1
                    return self.right.position_node(key, current_position)
            else:
                return current_position
        else:
            return None        
    
    
    def is_balanced(self) -> bool:
        """
            Retorna true caso a árvore seja balanceada, false caso não seja
        """      
        #Verificar se cada filho (esquerdo e direito) sao balanceados
        #Caso nao exista braco esquerdo nem direito, valor padrao = 0
        h_left, h_right = 0, 0
        if self.left:
            h_left = self.left.max_depth()   
        if self.right:
            h_right = self.right.max_depth() 
        if abs(h_left - h_right) > 1:
            return False
        
        #Recursao para passar proxima raiz
        #Caso nao exista braco esquerdo nem direito, valor padrao = True
            #True, pois o lado nao existe, portanto final da arvore
        left_is_balanced, right_is_balanced = True, True
        if self.left:
            left_is_balanced = self.left.is_balanced()
        if self.right:
            right_is_balanced = self.right.is_balanced()     
        
        return left_is_balanced and right_is_balanced
       

    def sorted_array_to_balanced_tree(self, array:List, start:int, end:int) -> "Node":
        if (start > end):
            return None

        pos_raiz_sub_arvore = int(start + (end-start) / 2)
        raiz_sub_arvore = Node(array[pos_raiz_sub_arvore])

        raiz_sub_arvore.left = self.sorted_array_to_balanced_tree(array, start, (pos_raiz_sub_arvore - 1) )
        raiz_sub_arvore.right = self.sorted_array_to_balanced_tree(array, (pos_raiz_sub_arvore + 1), end )

        return raiz_sub_arvore

    
    def to_balanced_tree(self):

        array = self.to_sorted_array()

        return self.sorted_array_to_balanced_tree(array, 0, len(array)-1)
