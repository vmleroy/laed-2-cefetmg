from functools import total_ordering
import math
class MinHeap:

    def __init__(self):
        #inicia com o heap com um elemento sentinela (que nunca será acessado)
        self.arr_heap = [None]

    def __str__(self):
        return str(self.arr_heap[1:])

    def __repr__(self):
        return str(self)
        
    def esquerda(self, i:int) ->int:
        """
            Retorna a posição do filho a esquerda de i
        """
        return 2*i

    def direita(self, i:int) ->int:
        """
            Retorna a posição do filho a direita de i
        """
        return 2*i+1

    def pai(self, i) ->int:
        """
        Retorna a posição do pai do i-ésimo nó
        """
        return math.floor(i/2)



    @property
    def pos_ultimo_item(self):
        return len(self.arr_heap)-1

    def refaz(self, pos_raiz_sub_arvore:int):
        #print("Antes das alteracoes: " + f"{self.arr_heap}")
        
        #maior_filho é inicializado com o da esquerda de pos raiz subarvore
        pos_pai = pos_raiz_sub_arvore
        pos_menor_filho = self.esquerda(pos_pai)
        
        #print("pos_pai: " + f"{pos_pai}")
        #print("pos_menor_filho: " + f"{pos_menor_filho}")

        #obtem o item raiz da subarvore do heap
        val_raiz_sub_arvore = self.arr_heap[pos_raiz_sub_arvore]

        while pos_menor_filho<=self.pos_ultimo_item:
            #se a posição do filho a esquerda não for a ultima do vetor,
            #atualize, se necessario, o pos_menor_filho considerando o filho a direita
            if pos_menor_filho<self.pos_ultimo_item:
                #### SEU CODIGO AQUI ############
                
                #print("Filhos =", self.arr_heap[pos_menor_filho], self.arr_heap[pos_menor_filho+1])
                
                if self.arr_heap[pos_menor_filho] > self.arr_heap[pos_menor_filho + 1]:
                    pos_menor_filho += 1
                    
                    #print("novo pos_menor_filho: " + f"{pos_menor_filho}")
                    
            #caso o valor da  raiz desta subarvore (val_raiz_sub_arvore)
            #possua um valor menor que o de seus filhos, 
            # finaliza o while 
            #### SEU CODIGO AQUI ############
            if val_raiz_sub_arvore <= self.arr_heap[pos_menor_filho]:
                break
                
            #realize a troca conforme especificação
            #### SEU CODIGO AQUI ############
            self.arr_heap[pos_pai] = self.arr_heap[pos_menor_filho]
            
            #print(self.arr_heap)
            
            #prepare as variáveis pos_pai e pos_menor_filho para a proxima iteração
            #substitua os "None" das duas linhas abaixo apropriadamente
            pos_pai = pos_menor_filho
            pos_menor_filho = self.esquerda(pos_pai)
            
            #print("pos_pai: " + f"{pos_pai}")
            #print("pos_menor_filho: " + f"{pos_menor_filho}")

        #atualize a posição pos_pai apropriadamente
        self.arr_heap[pos_pai] = val_raiz_sub_arvore
        
        #print("Apos as alteracoes: " + f"{self.arr_heap}")

    def insere(self,item):
        self.arr_heap.append(None)
        pos_inserir = self.pos_ultimo_item
        pai_pos_inserir = self.pai(pos_inserir)

        #substitua o "None" apropriadamente
        while pos_inserir > 1 and self.arr_heap[pai_pos_inserir] >= item:
            #realiza a atualização (substitua os "None")
            self.arr_heap[pos_inserir] = self.arr_heap[pai_pos_inserir]

            #ajusta para a proxima iteração (substitua os None apropriadamente)
            pos_inserir = pai_pos_inserir
            pai_pos_inserir = self.pai(pos_inserir)

        #finalize o insere apropriadamente
        self.arr_heap[pos_inserir] = item

    def retira_min(self):
        if len(self.arr_heap)<=1:
            raise IndexError("Heap Vazio")
        ## Faça a retirada do máximo conforme especificação/slides da aula teórica
        else:
            #print("Antes das alteracoes: " + f"{self.arr_heap}" + "\n")            
            minimo = self.arr_heap[1]
            aux = self.arr_heap[1]
            self.arr_heap[1] = self.arr_heap[-1]
            self.arr_heap[-1] = aux
            self.arr_heap.pop(-1)           
            #print("Apos pop alteracoes: " + f"{self.arr_heap}" + "\n")
            if len(self.arr_heap)>1:
                self.refaz(1)
            #print("Apos as alteracoes: " + f"{self.arr_heap}" + "\n")

        return minimo

    def __str__(self):
        return str(self.arr_heap)

    def __repr__(self):
        return str(self)