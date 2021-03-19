from page import Page

class BTree():
    def __init__(self, min_range:int):
        self.min_range = min_range
        self.max_range = min_range * 2
        self.root = Page(self.min_range, self.max_range, True)


    def search(self, key):
        self.root.search(key)


    def insert_key(self, key):
        self.root.insert_key(key)


    def print_tree(self):
        print("Printando arvore")
        self.root.print_node()        
