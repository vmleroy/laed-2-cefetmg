class Page():
    def __init__(self, max_range, page:bool = False):
        self.child = [None] * (max_range+1)
        self.keys = [None] * (max_range)
        self.n_registers = 0
        self.page = page

    
    def search(self, key):
        if self is None: 
            return None 
        else:
            i = 0
            while i < self.n_registers:
                if key == self.keys[i]:
                    return self.keys[i]
                elif key < self.keys[i]:
                    if self.child[i]:
                        return self.child[i].search(key)                
                else:
                    if self.child[i+1]:
                        return self.child[i+1].search(key)


    def insert_key(self, key, return_register:list = [None], tree_growth:list = [False], max_range:int = 0):
        #verify if this is the page where the key have to be inserted
        if self.page is True:
            tree_growth[0] = True
            return_register[0] = key                        
        else:
            return_page = None
            i = 0
            #search for the right position to insert the key
            while i < self.n_registers and key < self.keys[i]:
                i += 1
            #verify if the key is the same    
            if key == self.keys[i]:
                print("Error: Key already exist on the tree\n")
                tree_growth[0] = False
            else:
                return_page = self.child[i].insert_key(key, return_register, tree_growth, max_range)    
                if tree_growth[0]:
                    #verify if this page have space left
                    if self.n_registers < len(self.keys):
                        self.insert_key_on_page(return_register[0], return_page)
                        tree_growth[0] = False
                        return_page = self
                    #page have to be splited
                    else:
                        temp_page = Page(max_range)
                        temp_page.child[0] = None
                        #verify where the new register have to be placed and split the keys between 
                        if i <= max_range/2:
                            temp_page.insert_key_on_page(self.keys[max_range-1], self.child[max_range])
                            self.n_registers -= 1
                            self.insert_key_on_page(return_register[0], return_page)
                        else:
                            temp_page.insert_key_on_page(return_register, return_page)
                            j = ((max_range/2) + 1)
                            for j in range(max_range):
                                temp_page.insert_key_on_page(self.keys[j], self.child[j+1])
                                self.child[j+1] = None
                        self.n_registers = (max_range/2)
                        temp_page.child[0] = self.child[(max_range/2)+1]
                        #what key is gonna go up on the tree
                        return_register[0] = self.keys[max_range/2]
                        #new reference on the upper page
                        return_page = temp_page
        if tree_growth[0]:
             return return_page
        else:
            return self
                        

    def insert_key_on_page(self, key, page_right:"Page" = None):
        #get the right position to insert the key
        k = self.n_registers - 1
        while (k >= 0) and (key < self.keys[k]):
            self.keys[k+1] = self.keys[k]
            self.child[k+2] = self.child[k+1]
            k -= 1
        #set the key and the page     
        self.keys[k+1] = key
        self.child[k+2] = page_right
        self.n_registers += 1


    def print_node(self):
        for i in range(len(self.keys)):
            print(f"{self.keys[i]}")
            if self.child[i]:
                print("A esquerda de " + f"{self.keys[i]}")
                self.child[i].print_node()
            if i == (len(self.keys) - 1):
                 if self.child[i+1]:
                    print("A direita de " + f"{self.keys[i]}")
                    self.child[i+1].print_node()    

    

        
