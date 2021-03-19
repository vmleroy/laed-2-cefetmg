from node import BtNode

class BTree():
    def __init__(self, minimum_degree):
        self.root = BtNode(True)
        self.t = minimum_degree


    def print_tree(self, node:"BtNode" = None, j:int = 0):
        """
            Funcao para printar a arvore demonstrando em qual altura esta sendo printada
        """
        if node is not None:
            print("level: ", j, "   ", node.keys)
            if len(node.childs) > 0:                
                j+=1
                for i in node.childs:
                    self.print_tree(i,j)
        else:
            self.print_tree(self.root)


    def search_tree(self, key, node:"BtNode" = None):
        """
            Funcao retorna o node onde foi encontrada a key e a respectiva posicao no node
            Se nao encontrar a key, retorna None
        """
        if node is not None:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            if i < len(node.keys) and key == node.keys[i]:
                return (node, i)
            elif node.leaf:
                return None
            else:
                return self.search_tree(key, node.childs[i])                
        else:
            return self.search_tree(key, self.root)


    def split_child(self, node:"BtNode" = None, i:int = 0):
        """
            Funcao faz o split de um node filho em dois e ajusta o node pai para que tenha
                mais um node filho.
            Recebe um no e a posicao do filho correspondente (posicao tambem equivale a 
                posicao a ser inserido no no pai)
        """
        t = self.t
        y = node.childs[i]
        z = BtNode(y.leaf)
        node.childs.insert(i+1, z)
        node.keys.insert(i, y.keys[t-1])
        z.keys = y.keys[t:2*t]
        y.keys = y.keys[0:t-1]
        if not y.leaf:
            z.childs = y.childs[t:2*t+1]
            y.childs = y.childs[0:t]


    def insert_key(self, key):
        """
            Funcao que insere uma nova key na arvore e verifica se a raiz da arvore esta
                cheia de registros
        """
        r = self.root        
        grow_height = False
        grow_height = self.insert_key_recursive(r, key)
        if grow_height:
            if len(r.keys) == (self.t*2):
                s = BtNode()
                self.root = s
                s.childs.insert(0, r)
                self.split_child(s, 0)


    def insert_key_recursive(self, node, key):
        """
            Metodo recursivo auxiliar para inserir a key na arvore
            Apos encontrar a folha exata para insercao da key, verifica se esta ultrapassou o limite maximo
                de chaves por pagina
        """
        grow_height = False
        i = len(node.keys)-1
        if node.leaf:
            node.keys.append(0)    
            #print(node.keys, node.n)        
            while i >= 0 and key < node.keys[i]:
                node.keys[i+1] = node.keys[i]
                i -= 1
            node.keys[i+1] = key            
            if len(node.keys) == (self.t*2):    
                grow_height = True            
                return grow_height
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1  
            grow_height = self.insert_key_recursive(node.childs[i], key)
            if grow_height:           
                if len(node.childs[i].keys) == (self.t*2):
                    self.split_child(node, i)
                    return grow_height
            else:
                grow_height = False
                return grow_height

    
    def delete_key(self, key):
        """
            Funcao para deletar uma key da arvore e realizar as devidas
                operacoes para reorganizar a arvore
        """
        node_encontrado, posicao = self.search_tree(key)
        if node_encontrado is not None:
            print("Encontrada key no node:", node_encontrado.keys, " Na posicao:",posicao)
            print("E' uma folha:", node_encontrado.leaf)
            if node_encontrado.leaf:
                node_encontrado.keys.pop(posicao)
                self.delete_key_update_tree(key)
                return
            elif node_encontrado.leaf is not True:
                self.delete_key_internal_node(node_encontrado, key, posicao)
                self.delete_key_update_tree(key)
        else:
            return

    def delete_key_internal_node(self, node, key, i):
        """
            Funcao deleta uma key de um no interno e verifica se atende as especificacoes
                da arvore b
        """
        t = self.t
        # Se o no escolhido for uma folha
        if node.leaf:
            if node.keys[i] == key:
                node.keys.pop(i)
                return 
            return 
        # Se o no escolhido nao for uma folha, verificar se filho a esquerda desta posicao esta
        # dentro das especificacoes da arvore b e "puxa" o maior filho deste no anterior
        if len(node.child[i].keys) >= t:
            node.keys[i] = self.delete_key_predecessor(node.child[i])
            return 
        # Se o no escolhido nao for uma folha, verificar se filho a direita desta posicao esta
        # dentro das especificacoes da arvore b e "puxa" o menor filho deste no anterior    
        elif len(node.child[i + 1].keys) >= t:
            node.keys[i] = self.delete_key_sucessor(node.child[i+1])
            return 
        # Se nao, chama por recursao esta mesma funcao une os filhos
        else:
            self.delete_key_merge(node, i, i+1)
            self.delete_key_internal_node(node.child[i], key, self.t - 1)
        

    def delete_key_predecessor(self, node):
        """
            Funcao deleta a ultima key do anterior e verifica se esta dentro das condicoes
                da arvore b
        """
        t = self.t
        if node.leaf:
            return node.keys.pop()
        i = len(node.keys) - 1
        if len(node.child[i].keys) >= t:
            self.delete_key_sibling(node, i + 1, i)
        else:
            self.delete_key_merge(node, i, i+1)
        self.delete_key_predecessor(node.child[i])
    
    def delete_key_sucessor(self, node):
        """
            Funcao deleta a primeira key do sucessor e verifica se esta dentro das condicoes
                da arvore b
        """
        t = self.t
        if node.leaf:
            return node.keys.pop(0)
        if len(node.child[1].keys) >= t:
            self.delete_key_sibling(node, 0, 1)
        else:
            self.delete_key_merge(node, 0, 1)
        self.delete_key_sucessor(node.child[0])

    
    def delete_key_merge(self, node, i, j):
        """
            Funcao une dois filhos de um unico no caso ocorra delecao de uma key
        """
        child_node = node.child[i]
        # Verifica qual filho sera selecionado para serem unidos
        # Filho da direita se une
        if j > i:
            right_child_node = node.childs[j]
            child_node.keys.append(node.keys[i])
            for k in range(len(right_child_node.keys)):
                child_node.keys.append(right_child_node[k])
                if len(right_child_node.childs) > 0:
                    child_node.childs.append(right_child_node.childs[k])
            if len(right_child_node.childs) > 0:
                child_node.childs.append(right_child_node.childs.pop())
            new_child = child_node
            node.keys.pop(i)
            node.childs.pop(j)
        # Filho da esquerda se une
        else:
            left_child_node = node.childs[j]
            left_child_node.keys.append(node.keys[j])
            for i in range(len(child_node.keys)):
                left_child_node.keys.append(child_node.keys[i])
                if len(left_child_node.childs) > 0:
                    left_child_node.append(child_node.childs[i])
            if len(left_child_node.childs) > 0:
                left_child_node.append(child_node.childs.pop())
            new_child = left_child_node
            node.keys.pop(j)
            node.childs.pop(i)
        # Caso o node seja a propria raiz da arvore, transformamos o novo no criado
        # na nova raiz        
        if node == self.root and len(node.keys) == 0:
            self.root = new_child

    def delete_key_sibling(self, node, i, j):
        """
            Funcao para realizar a transferencia de posse de chaves entre filhos
                caso ocorra a delecao de uma key
        """
        child_node = node.childs[i]
        # Caso buscamos a key do filho a direita, pegamos a primeira key e o primeiro filho
        # caso este exista
        if j > i:
            right_child_node = node.childs[j]
            child_node.keys.append(node.keys[i])
            node.keys[i] = right_child_node[0]
            if len(right_child_node.child) > 0:
                child_node.childs.append(right_child_node.child[0])
                right_child_node.childs.pop(0)
            right_child_node.keys.pop(0)
        # Caso buscamos a key do filho a esquerda, pegamos a ultima key e o ultimo filho
        # caso este exista
        else:
            left_child_node = node.childs[j]
            child_node.keys.insert(0, node.keys[i - 1])
            node.keys[i - 1] = left_child_node.keys.pop()
            if len(left_child_node.childs) > 0:
                child_node.childs.insert(0, left_child_node.childs.pop)

    def delete_key_update_tree(self, key, node:"BtNode" = None):
        """
            Atualiza arvore depois que ocorre delecao de elemento
        """
        if node is not None:
            t = self.t
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                    i += 1
            if i != 0 and i + 2 < len(node.childs):
                if len(node.childs[i - 1].keys) >= t:
                    self.delete_key_sibling(node, i, i-1)
                elif  len(node.childs[i + 1].keys) >= t:
                    self.delete_key_sibling(node, i, i+1)
                else:
                    self.delete_key_merge(node, i, i+1)
            elif i == 0:
                if len(node.childs[i + 1].keys) >= t:
                    self.delete_key_sibling(node, i, i+1)
                else:
                    self.delete_key_merge(node, i, i+1)
            elif i + 1 == len(node.childs):
                if len(node.childs[i + 1].keys) >= t:
                    self.delete_key_sibling(node, i, i-1)
                else:
                    self.delete_key_merge(node, i, i-1)
            self.delete_key_update_tree(key, node.childs[i])
        else:
            self.delete_key_update_tree(key, self.root)




                            
            




    

