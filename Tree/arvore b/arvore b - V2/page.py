class Page():
    def __init__(self, min_range:int = 0, max_range:int = 0, page:bool = False):
        self.min_range = min_range
        self.max_range = max_range
        self.child = []
        self.keys = []
        self.is_page = page
        
   
    def search(self, key):
        if self.is_page: 
            i = 0
            while i < len(self.keys):
                if key == self.keys[i]:
                    return self.keys[i]
            return None 
        else:
            i = 0
            while i < len(self.keys):
                if key == self.keys[i]:
                    return self.keys[i]
                elif key < self.keys[i]:
                    if self.child[i]:
                        return self.child[i].search(key)                
                else:
                    if self.child[i+1]:
                        return self.child[i+1].search(key)


    def insert_key(self, key):
        tree_grow:bool = False
        if self.is_page:
            tree_grow = True
            if len(self.keys) < self.max_range:
                self.insert_key_on_page(key) 
                tree_grow = False
                return tree_grow   
            else:
                return tree_grow
        else:
            i:int = len(self.keys)
            while i > 0 and self.keys[i-1] > key:
                self.keys[i] = self.keys[i-1]
                i -= 1
            child = self.child[i]
            tree_grow = child.insert_key
            if tree_grow:
                if len(child.keys) < self.max_range:
                    child.insert_key_on_page(key) 
                    tree_grow = False
                    return tree_grow
                else: 
                    pass                                   
                        

    def insert_key_on_page(self, key):
        #get the right position to insert the key
        self.keys.append(0)
        i:int = len(self.keys) - 1
        while i > 0 and self.keys[i-1] > key:
            self.keys[i] = self.keys[i-1]
            i -= 1
        self.keys[i] = key 


    def split_child(self, key):
        pass
        
        
    def print_node(self):        
        print(f"{self.keys}")
        i = 0
        if len(self.child) > 0:
            while i<len(self.keys):
                if self.child[i] is not None:
                    print("A esquerda de " + f"{self.keys[i]}")
                    self.child[i].print_node()
                i += 1
            if self.child[i] is not None:
                print("A direita de " + f"{self.keys[i-1]}")
                self.child[i].print_node()

    

        
