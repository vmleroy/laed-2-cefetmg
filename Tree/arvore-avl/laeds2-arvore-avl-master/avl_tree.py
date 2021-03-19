class No:
    def __init__(self, chave=None):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1

    @property
    def altura_subarvore_esquerda(self):
        if self.esquerda is None:
            return 0
        return self.esquerda.altura

    @property
    def altura_subarvore_direita(self):
        if self.direita is None:
            return 0

        return self.direita.altura

    @property
    def equilibrio(self):
        return self.altura_subarvore_esquerda-self.altura_subarvore_direita

    def atualiza_altura(self):
        self.altura = 1 + max(self.altura_subarvore_esquerda,
                                    self.altura_subarvore_direita)

class AVL:
    def __init__(self,raiz):
        self.raiz = raiz
                
    def imprime(self):
        self._imprime(self.raiz)        
        
    def _imprime(self, raiz_sub_arvore):
        print(raiz_sub_arvore.chave, end="\n")
        if raiz_sub_arvore.esquerda:
            print(f"---------Esquerda de {raiz_sub_arvore.chave}-------")
            self._imprime(raiz_sub_arvore.esquerda)

        if raiz_sub_arvore.direita:
            print(f"---------Direita  de {raiz_sub_arvore.chave}-------")
            self._imprime(raiz_sub_arvore.direita)

            
            
    def rotacao_esquerda(self, raiz_sub_arvore):
        print("\nRotacao esquerda")
#         self._imprime(raiz_sub_arvore)
        
        # nova raiz
        nova_raiz_sub_arvore = raiz_sub_arvore.direita 
        
        # caso exista um numero menor que a nova raiz
        if nova_raiz_sub_arvore.esquerda: 
            raiz_sub_arvore.direita = nova_raiz_sub_arvore.esquerda
        else: # se nao existir setar valor nulo na raiz
            raiz_sub_arvore.direita = None
        nova_raiz_sub_arvore.esquerda = raiz_sub_arvore # realizando a rotacao

        nova_raiz_sub_arvore.atualiza_altura() # altera altura da raiz nova
        raiz_sub_arvore.atualiza_altura() # altera altura da raiz antiga     
        
#         print("Depois")
        self._imprime(nova_raiz_sub_arvore)
        
        return nova_raiz_sub_arvore

        
    def rotacao_direita(self, raiz_sub_arvore):   
        print("\nRotacao direita")
        self._imprime(raiz_sub_arvore)
        
        # nova raiz
        nova_raiz_sub_arvore = raiz_sub_arvore.esquerda
        
        # caso exista um numero maior que a nova raiz
        if nova_raiz_sub_arvore.direita: 
            raiz_sub_arvore.esquerda = nova_raiz_sub_arvore.direita
        else: # se nao existir setar valor nulo na raiz
            raiz_sub_arvore.esquerda = None
        nova_raiz_sub_arvore.direita = raiz_sub_arvore # realizando a rotacao
              
        nova_raiz_sub_arvore.atualiza_altura() # altera altura da raiz nova
        raiz_sub_arvore.atualiza_altura() # altera altura da raiz antiga
        
        print("Depois")
        self._imprime(nova_raiz_sub_arvore)
        
        return nova_raiz_sub_arvore

        
    def rotacao_dupla_esquerda(self,raiz_sub_arvore):
        print("\nROTACAO DUPLA ESQUERDA")
        self._imprime(raiz_sub_arvore)
        
        # rotacao da sub arvore a direita da raiz recebida
        raiz_sub_arvore.direita = self.rotacao_direita(raiz_sub_arvore.direita)
        #rotacao da arvore principal
        nova_raiz_sub_arvore = self.rotacao_esquerda(raiz_sub_arvore)
        
        if raiz_sub_arvore.direita:
            raiz_sub_arvore.direita.atualiza_altura()
        nova_raiz_sub_arvore.atualiza_altura()
        
        print("Depois")
        self._imprime(nova_raiz_sub_arvore)
        
        return nova_raiz_sub_arvore
    
    
    def rotacao_dupla_direita(self, raiz_sub_arvore):
        print("\nROTACAO DUPLA DIREITA")
        self._imprime(raiz_sub_arvore)
        
        # rotacao da sub arvore a direita da raiz recebida
        raiz_sub_arvore.esquerda = self.rotacao_esquerda(raiz_sub_arvore.esquerda)
        #rotacao da arvore principal
        nova_raiz_sub_arvore = self.rotacao_direita(raiz_sub_arvore)
        
        if raiz_sub_arvore.esquerda:
            raiz_sub_arvore.esquerda.atualiza_altura()
        nova_raiz_sub_arvore.atualiza_altura()
        
        print("Depois")
        self._imprime(nova_raiz_sub_arvore)
        
        return nova_raiz_sub_arvore

    
    
    def insere(self,chave):
        self.raiz = self._insere(chave, self.raiz)
                
    def _insere(self, chave, raiz_sub_arvore):
        #Inserção - alterando subarvores se necessario
        if not raiz_sub_arvore:
            return No(chave)
        elif chave < raiz_sub_arvore.chave:
            raiz_sub_arvore.esquerda = self._insere(chave,raiz_sub_arvore.esquerda)
        elif chave > raiz_sub_arvore.chave:
            raiz_sub_arvore.direita = self._insere(chave,raiz_sub_arvore.direita)
        else:
            #raiz desta subarvore não é modificada quando a chave é a mesma - e não realiza inserção
            return raiz_sub_arvore

        # altura atualizada
        raiz_sub_arvore.atualiza_altura()

        #Rebalanceia a árvore de tal forma que o equilibrio sempre fique entre -1 e 1
        # Caso 1 - Rotacao direita
        if raiz_sub_arvore.equilibrio > 1 and chave < raiz_sub_arvore.esquerda.chave:       
            return self.rotacao_direita(raiz_sub_arvore)
        
        # Caso 2 - Rotacao esquerda
        if raiz_sub_arvore.equilibrio < -1 and chave > raiz_sub_arvore.direita.chave:
            return self.rotacao_esquerda(raiz_sub_arvore)

        # Caso 3 - Rotacao dupla direita
        if raiz_sub_arvore.equilibrio > 1 and chave > raiz_sub_arvore.esquerda.chave:      
            return self.rotacao_dupla_direita(raiz_sub_arvore)

        # Caso 4 - Rotacao dupla esquerda
        if raiz_sub_arvore.equilibrio < -1 and chave < raiz_sub_arvore.direita.chave:
            return self.rotacao_dupla_esquerda(raiz_sub_arvore)



        #caso já esteja equilibrado, a raiz subarvore não é modificada
        return raiz_sub_arvore
