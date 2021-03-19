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
        aux_page = self
        if self.is_page:
            aux_list = self.keys
            self.insert_key_on_page(aux_list, key)
            if len(aux_list) > self.max_range:
                if len(self.child) > 0:
                    i=0
                    while i < len(self.keys) and key > self.keys[i]:
                        i += 1
                    aux_page = self.split_child(self, aux_list, i)
                    print("aux page " f"{aux_page.keys, aux_page.child[0].keys, aux_page.child[1].keys}")
                else:
                    aux_page = self.create_child(self, aux_list)
                    print("aux page " f"{aux_page.keys, aux_page.child[0].keys, aux_page.child[1].keys}")
            else:
                aux_page.keys = aux_list
        else:
            #search for the page
            i = 0
            while i < len(self.keys) and key > self.keys[i]:
                if key == self.keys[i]:
                    print("JA EXISTE KEY NA ARVORE")
                    return None
                i += 1
            #if there is a child
            if self.child[i]:
               self.child[i].insert_key(key)
        return aux_page
                        

    def insert_key_on_page(self, aux_list, key):
        #get the right position to insert the key
        aux_list.append(0)
        i:int = len(aux_list) - 1
        while i > 0 and aux_list[i-1] > key:
            aux_list[i] = aux_list[i-1]
            i -= 1
        aux_list[i] = key 


    def create_child(self, actual_node, aux_list):
        aux_page = actual_node
        aux_page.keys = aux_list
        temp_page = Page(actual_node.min_range, actual_node.max_range)
        temp_page.child.insert(0, aux_page)
        temp_page.split_child(temp_page, aux_list, 0)   
        actual_node = temp_page
        print("actual node " f"{actual_node.keys, actual_node.child[0].keys, actual_node.child[1].keys}")
        return actual_node


    def split_child(self, actual_node, aux_list, i):
        half_aux_list = int(len(aux_list)/2)
        newRoot = aux_list[half_aux_list]
        left_page = actual_node.child[i]
        right_page = Page(actual_node.min_range, actual_node.max_range, left_page.is_page)

        actual_node.child.insert(i + 1, right_page)
        actual_node.keys.insert(i, newRoot)

        right_page.keys = left_page.keys[actual_node.min_range + 1 : actual_node.max_range + 1]
        left_page.keys = left_page.keys[0 : actual_node.min_range]

        if left_page.is_page is False:
            left_page.child = left_page.child[0 : actual_node.min_range]
            right_page.child = left_page.child[actual_node.min_range : actual_node.max_range]
        
        print("actual node " f"{actual_node.keys, actual_node.child[i].keys, actual_node.child[i+1].keys}")
        return actual_node
        
        
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

    

        
