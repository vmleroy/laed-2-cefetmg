class LCS:
    def __init__(self):
        pass

    def lcs (self, string_1:str, string_2:str):
        """
            Esta funcao monta a matriz contendo a maior sequencia possivel entre as duas
            strings utilizando a tecninca de programacao dinamica. Retorna a matriz e a maior posicao
        """
        
        size_string_1 = len(string_1)
        size_string_2 = len(string_2)    

        # A matriz possui tamanho size_string + 1, pois a posicao [0][0] nao contem a informacao
        # da primeira letra da string. Alem disso, as posicoes [n][0] e [0][n] serao todas none
        lcs_matrix = [ [0 for x in range(size_string_2 + 1)] for x in range(size_string_1 + 1) ]

        # Construindo a matriz lcs preenchendo ela no estilo "Bottom Up" (de baixo pra cima)
        # Cada posicao (i,j) contem o tamanho do LCS de string_1[0...i-1] e string_2[0...j-1]
        for i in range(size_string_1 + 1):
            for j in range(size_string_2 + 1):
                # Primeira linha da matriz e' sempre 0
                if i == 0 or j == 0:
                    lcs_matrix[i][j] = 0
                # Caso seja encontrado um caractere igual entre as strings
                elif string_1[i-1] == string_2[j-1]: 
                    lcs_matrix[i][j] = lcs_matrix[i-1][j-1] + 1
                # Caso contrario, buscar a maior posicao entre as posicoes esquerdas e a cima do bloco estudado
                else:
                    lcs_matrix[i][j] = max(lcs_matrix[i-1][j], lcs_matrix[i][j-1])
        
        # Retorno da funcao, sendo "matriz, tamanho sub sequencia"
        return lcs_matrix, lcs_matrix[size_string_1][size_string_2]

    def printing_lcs (self, lcs_matrix, string_1, string_2):
        """
            Esta funcao printa a solucao do problema lcs
        """
        
        size_string_1 = len(string_1)
        size_string_2 = len(string_2) 
        
        # Array de caracteres para armazenar a resposta do problema
        index = lcs_matrix[size_string_1][size_string_2]
        lcs_solution         = [""] * (index)
        
        #lcs_solution        = [""] * (index+1)
        #lcs_solution[index] = ""

        # Comecar a printar da posicao inferior direita da matriz, pois ela contem
        # O maior valor possivel da sub sequencia        
        i = size_string_1
        j = size_string_2
        while i > 0 and j > 0:
            # Se os caracteres nas strings forem iguais, entao fazem parte da solucao do lcs
            if string_1[i - 1] == string_2[j - 1]: 
                lcs_solution[index - 1] = string_1[i - 1] 
                i = i - 1
                j = j - 1
                index = index - 1
            # Se nao for igual, entao procurar o maior entre eles e segue na direcao do maior valor
            elif lcs_matrix[i-1][j] > lcs_matrix[i][j-1]: 
                i = i - 1
            else: 
                j = j - 1
                
        #print(lcs_solution)
        # Printando as sequencias
        #print("S1 : " + string_1 + "\nS2 : " + string_2)
        #print("LCS: " + "".join(lcs_solution) + "\n")

        lcs_solution = "".join(lcs_solution)
        return lcs_solution