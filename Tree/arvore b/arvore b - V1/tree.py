from node import Node

class Tree():
    def __init__(self, order:int = 0):
        self.root = Node(True)
        self.order:int =  order



    def search_key(self, key):
        discoveredKey:bool = False
        discoveredKey = self.root.search_key(key)
        return discoveredKey



    def insert_key(self, key):
        aux = self.root
        if len(self.root.keys) == (self.order*2):
            new_node = Node()
            self.root = new_node #empty new node
            new_node.child.insert(0, aux)
            self.root.split_child(new_node, 0, self.order)
            self.root.insert_key(key, self.order)
            pass
        else:
            #print("Inserindo key")
            self.root.insert_key(key, self.order) #insert new key

    

    def print_tree(self):
        print("Printando arvore")
        self.root.print_node()
    