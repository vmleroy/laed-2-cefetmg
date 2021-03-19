"""
Node of the b-tree
    attributes: 
        leaf:bool -> defines if its a leaf or not
        keys:list -> list of internal keys of this node
        branches:list -> list of children of this node
"""

class Node():
    def __init__(self, leaf:bool = False, ):
        self.leaf = leaf
        self.keys = []
        self.child = []


    def search_key(self, key):
        is_in_tree:bool = False
        for i in range (len(self.keys)):
            if self.keys[i] < key:
                if self.child[i]:
                    is_in_tree = self.child[i].search_key(key)
            elif self.keys[i] == key:                
                return True
            if is_in_tree == True:
                return is_in_tree
            else:
                if self.child[i+1]:
                    is_in_tree = self.child[i+1].search_key(key)      
        return is_in_tree



    def insert_key(self, key, order):
        if self.leaf: #if it is leaf, verify if the leaf is full
            if len(self.keys) == (order*2):
                print("Arvore cheia")
                i=len(self.keys)-1
                while i>=0 and key < self.keys[i]:
                    i-=1
                i+=1
                self.split_child(self, i, order)
                if key > self.keys[i]:
                    i+=1
                self.child[i+1].insert_key(key, order)                                
            else:
                self.keys.append(None)
                self.insert_key_node_not_full(key, order)
        else:
            for i in range(len(self.keys)):
                if key < self.keys[i]:
                    if self.child[i]:
                        self.child[i].insert_key(key, order)                            
                        break
                if i == (len(self.keys) - 1):
                    if self.child[i+1]:
                        self.child[i+1].insert_key(key, order) 
                        break



    def insert_key_node_not_full(self, key, order):
        i:int = len(self.keys) - 1
        while i > 0 and self.keys[i-1] > key:
            self.keys[i] = self.keys[i-1]
            i -= 1
        self.keys[i] = key



    def split_child(self, node, i, order):
                
        right_node = node.child[i]
        left_node = Node(leaf=right_node.leaf)

        node.child.insert(i+1, left_node)
        node.keys.insert(i, right_node.keys[order-1])

        left_node.keys = right_node.keys[order:(2*order)]
        right_node.keys = right_node.keys[0:(order-1)]

        if not right_node.leaf:
            left_node.child = right_node.child[order:(2*order)]
            right_node.child = right_node.child[0:(order-1)]

    

    def print_node(self):
        for i in range(len(self.keys)):
            print(f"{self.keys[i]}")
            if not self.leaf and len(self.child)>0:
                if self.child[i]:
                    print("A esquerda de " + f"{self.keys[i]}")
                    self.child[i].print_node()
                if i == (len(self.keys) - 1):
                    if self.child[i+1]:
                        print("A direita de " + f"{self.keys[i]}")
                        self.child[i+1].print_node()



        
