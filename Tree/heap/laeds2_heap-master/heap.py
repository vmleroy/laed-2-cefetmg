from functools import total_ordering
import math
class MaxHeap:

    def __init__(self):
        #inicia com o heap com um elemento sentinela (que nunca será acessado)
        self.arr_heap = [None]

    def __str__(self):
        return str(self.arr_heap[1:])

    def __repr__(self):
        return str(self)
    
    #Os metodos esquerda, direita e pai serão usados nos demais metodos do heap
    def esquerda(self, i:int) ->int:
        """
            Retorna a posição do filho a esquerda de i
        """
        left = 2*i
        return left

    def direita(self, i:int) ->int:
        """
            Retorna a posição do filho a direita de i
        """
        right = 2*i + 1
        return right

    def pai(self, i:int) ->int:
        """
        Retorna a posição do pai do i-ésimo nó
        """
        father = math.floor(i/2)
        return father



    @property
    def pos_ultimo_item(self):
        return len(self.arr_heap)-1

    def refaz(self, pos_raiz_sub_arvore:int):
        #print("Antes das alteracoes: " + f"{self.arr_heap}")
        
        #maior_filho é inicializado com o da esquerda de pos raiz subarvore
        pos_pai = pos_raiz_sub_arvore
        pos_maior_filho = self.esquerda(pos_pai)
        
        #print("pos_pai: " + f"{pos_pai}")
        #print("pos_maior_filho: " + f"{pos_maior_filho}")

        #obtem o item raiz da subarvore do heap
        val_raiz_sub_arvore = self.arr_heap[pos_raiz_sub_arvore]


        while pos_maior_filho<=self.pos_ultimo_item:
            #se a posição do filho a esquerda não for a ultima do vetor,
            #atualize, se necessario, o pos_maior_filho considerando o filho a direita
            if pos_maior_filho<self.pos_ultimo_item:
                #### SEU CODIGO AQUI ############
                if self.arr_heap[pos_maior_filho] < self.arr_heap[pos_maior_filho + 1]:
                    pos_maior_filho += 1
                    
                    #print("pos_maior_filho: " + f"{pos_maior_filho}")
                    
            #caso o valor da  raiz desta subarvore (val_raiz_sub_arvore)
            #possua um valor maior que o de seus filhos, 
            # finaliza o while 
            #### SEU CODIGO AQUI ############
            if val_raiz_sub_arvore >= self.arr_heap[pos_maior_filho]:
                break
                
            #realize a troca conforme especificação
            #### SEU CODIGO AQUI ############
            self.arr_heap[pos_pai] = self.arr_heap[pos_maior_filho]
            
            #print(self.arr_heap)
            
            #prepare as variáveis pos_pai e pos_maior_filho para a proxima iteração
            #substitua os "None" das duas linhas abaixo apropriadamente
            pos_pai = pos_maior_filho
            pos_maior_filho = self.esquerda(pos_pai)
            
            #print("pos_pai: " + f"{pos_pai}")
            #print("pos_maior_filho: " + f"{pos_maior_filho}")

        #atualize a posição pos_pai apropriadamente
        self.arr_heap[pos_pai] = val_raiz_sub_arvore
        
        #print("Apos as alteracoes: " + f"{self.arr_heap}" + "\n")

    def retira_max(self):
        if len(self.arr_heap)<=1:
            raise IndexError("Heap Vazio")
        ## Faça a retirada do máximo conforme especificação/slides da aula teórica
        else:
            #print("Antes das alteracoes: " + f"{self.arr_heap}" + "\n")            
            maximo = self.arr_heap[1]
            aux = self.arr_heap[1]
            self.arr_heap[1] = self.arr_heap[-1]
            self.arr_heap[-1] = aux
            self.arr_heap.pop(-1)           
            #print("Apos pop alteracoes: " + f"{self.arr_heap}" + "\n")
            if len(self.arr_heap)>1:
                self.refaz(1)
            #print("Apos as alteracoes: " + f"{self.arr_heap}" + "\n")

        return maximo

    def insere(self, item):
        self.arr_heap.append(None)
        pos_inserir = self.pos_ultimo_item
        pai_pos_inserir = self.pai(pos_inserir)

        #substitua o "None" apropriadamente
        while pos_inserir > 1 and self.arr_heap[pai_pos_inserir] <= item:
            #realiza a atualização (substitua os "None")
            self.arr_heap[pos_inserir] = self.arr_heap[pai_pos_inserir]

            #ajusta para a proxima iteração (substitua os None apropriadamente)
            pos_inserir = pai_pos_inserir
            pai_pos_inserir = self.pai(pos_inserir)

        #finalize o insere apropriadamente
        self.arr_heap[pos_inserir] = item
