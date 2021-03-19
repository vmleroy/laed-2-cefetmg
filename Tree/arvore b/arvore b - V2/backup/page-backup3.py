class Page():
    def __init__(self, min_range:int = 0, max_range:int = 0, page:bool = False):
        self.min_range = min_range
        self.max_range = max_range
        self.child = []
        self.keys = []
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


    def insert_key(self, key):
        if self.page:
            #verify if page is full
            if self.n_registers < self.max_range:
                self.keys.append(None)
                self.insert_key_on_page(key)
            else:
                #search for the right child to insert new number
                i = 0
                while i<self.n_registers and key > self.keys[i]:   
                    i += 1  
                #split old childs bcs page is full
                if self.child[i].n_registers == self.child[i].max_range: 
                    self.split_child(self, i)
                #insert new key
                self.child[i].insert_key(key)
        else:
            #search for the page
            i = 0
            while i < self.n_registers and key > self.keys[i]:
                if key == self.keys[i]:
                    print("JA EXISTE KEY NA ARVORE")
                    return None
                i += 1
            #if there is a child
            if self.child[i]:
                self.child[i].insert_key(key)
                        

    def insert_key_on_page(self, key):
        #get the right position to insert the key
        k = self.n_registers - 1
        while (k >= 0) and (key < self.keys[k]):
            self.keys[k+1] = self.keys[k]
            k -= 1
            #set the key and the page     
        self.keys[k+1] = key
        self.n_registers += 1


    def split_child(self, x, i):
        #separating new childs and selecting new root  
        t = self.min_range  
        y = x.child[i]
        z = Page(x.min_range, x.max_range, y.page)

        #setting new childs
        x.child.insert(i+1, z)
        x.keys.insert(i, y.keys[t - 1])
        x.n_registers = len(x.keys)

        #setting keys to new childs (gonna get from left_child bcs is old root)
        z.keys = y.keys[t:(2*t-1)]
        y.keys = y.keys[0:(t-1)]    
        z.n_registers = len(z.keys)    
        y.n_registers = len(y.keys)    

        #if those new childs arent pages, we promote them
        if not y.page:
            z.child = y.child[t : (2*t)]
            y.child = y.child[0 : (t-1)]
        
        

        
    def print_node(self):        
        print(f"{self.keys}")
        i = 0
        if len(self.child) > 0:
            while i<self.n_registers:
                if self.child[i] is not None:
                    print("A esquerda de " + f"{self.keys[i]}")
                    self.child[i].print_node()
                i += 1
            if self.child[i] is not None:
                print("A direita de " + f"{self.keys[i-1]}")
                self.child[i].print_node()

    

        
