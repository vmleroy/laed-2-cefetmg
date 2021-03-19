class Page():
    def __init__(self, min_range:int = 0, max_range:int = 0, page:bool = False):
        self.min_range = min_range
        self.max_range = max_range
        self.child = [None] * (self.max_range+1)
        self.keys = [None] * (self.max_range)
        self.n_registers = 0
        self.page = page
        
   
    def search(self, key):
        if self.page: 
            i = 0
            while i < self.n_registers:
                if key == self.keys[i]:
                    return self.keys[i]
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


    def insert_key(self, key, tree_growth, regReturn, i:int = 0):
        pageReturn = None
        if self.page:
            tree_growth[0] = True
            regReturn[0] = key
            #see if in this page have space left on keys
            if self.n_registers < self.max_range: 
                self.insert_key_on_page(key, pageReturn)
                tree_growth[0] = False
                pageReturn = self
            #if page is full we have to split
            else: 
                temp_page = Page(self.min_range, self.max_range)
                temp_page.child[0] = None
                #check in what page the register will be
                if i <= self.min_range:
                    temp_page.insert_key_on_page(self.keys[self.max_range - 1], self.child[self.max_range])
                    self.n_registers -= 1             
                    self.insert_key_on_page(regReturn[0], pageReturn)
                else:
                    temp_page.insert_key_on_page(regReturn[0], pageReturn)
                    #Half and half of the keys to the new pages    
                j = self.min_range + 1
                for j in range(self.max_range):
                    temp_page.insert_key_on_page(self.keys[j], self.child[j+1])
                    self.child[j+1] = None
                self.n_registers = self.min_range
                temp_page.child[0] = self.child[self.min_range+1]
                #change values
                regReturn[0] = self.keys[self.min_range]
                pageReturn = temp_page              
        else:
            i = 0
            while i < self.n_registers and key > self.n_registers:
                i += 1
                if key == self.keys[i]:
                    print("Error: key already on the tree")
                    tree_growth[0] = False
                    return None
            if self.child[i] is not None:
                pageReturn = self.child[i].insert_key(key, tree_growth, regReturn,i)   
        if tree_growth[0]:
            return pageReturn
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


    def split_child(self, i, regReturn, pageReturn):
        temp_page = Page(self.min_range, self.max_range, self.page)
        temp_page.child[0] = None
        #check in what page the register will be
        if i <= self.min_range:
             temp_page.insert_key_on_page(self.keys[self.max_range - 1], self.child[self.max_range])
             self.n_registers -= 1             
             self.insert_key_on_page(regReturn[0], pageReturn)
        else:
            temp_page.insert_key_on_page(regReturn[0], pageReturn)
            #Half and half of the keys to the new pages    
            j = self.min_range + 1
            for j in range(self.max_range):
                temp_page.insert_key_on_page(self.keys[j], self.child[j+1])
                self.child[j+1] = None
            self.n_registers = self.min_range
            temp_page.child[0] = self.child[self.min_range+1]
        #change values
        regReturn[0] = self.keys[self.min_range]
        pageReturn = temp_page
        return pageReturn

        
    def print_node(self):        
        print(f"{self.keys}")
        i = 0
        while i<self.n_registers:
            if self.child[i] is not None:
                print("A esquerda de " + f"{self.keys[i]}")
                self.child[i].print_node()
            i += 1
        if self.child[i] is not None:
            print("A direita de " + f"{self.keys[i-1]}")
            self.child[i].print_node()

    

        
