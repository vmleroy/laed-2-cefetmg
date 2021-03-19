import unittest

from lcs import LCS


class TestNode(unittest.TestCase):
    def lcs_setup(self):  
        self.lcs = LCS()   

        self.lcs_strings = []
        self.lcs_strings.append("TZAQWIBDCXE")
        self.lcs_strings.append("HXTBUWAICE")
        self.lcs_strings.append("ACADB")
        self.lcs_strings.append("CBDA")
        self.lcs_strings.append("BCDAACD")
        self.lcs_strings.append("ACDBAC")

        self.lcs_strings_solution = []
        self.lcs_strings_solution.append(5)
        self.lcs_strings_solution.append(2)
        self.lcs_strings_solution.append(4)

        self.lcs_strings_solution_2 = []
        self.lcs_strings_solution_2.append("TWICE")
        self.lcs_strings_solution_2.append("CB")
        self.lcs_strings_solution_2.append("CDAC")

        #for i in range(len(lcs_strings)):
            #print(lcs_strings[i])                

    def lcs_test_tamanho(self):
        self.lcs_setup()        
        
        arr_recebido = []        
        i = 0        

        while i < len(self.lcs_strings):
            j = i + 1
            matriz, valor = self.lcs.lcs(self.lcs_strings[i], self.lcs_strings[j])
            arr_recebido.append(valor)
            
            i += 2
        
        for i in range(len(arr_recebido)):    
            #print(arr_recebido[i], self.lcs_strings_solution[i])                 
            self.assertEqual(arr_recebido[i], self.lcs_strings_solution[i], f"Erro! o lcs recebido {arr_recebido[i]} esta diferente do esperado. O esperado seria {self.lcs_strings_solution[i]}")


    def lcs_test_string(self):
        self.lcs_setup()        
        
        arr_recebido = []        
        i = 0        

        while i < len(self.lcs_strings):
            j = i + 1
            matriz, valor = self.lcs.lcs(self.lcs_strings[i], self.lcs_strings[j])
            arr_recebido.append(self.lcs.printing_lcs(matriz, self.lcs_strings[i], self.lcs_strings[j]))
            i += 2
            
           
        for i in range(len(arr_recebido)):
            #print(arr_recebido[i], self.lcs_strings_solution[i])                 
            self.assertEqual(arr_recebido[i], self.lcs_strings_solution_2[i], f"Erro! o lcs recebido {arr_recebido[i]} esta diferente do esperado. O esperado seria {self.lcs_strings_solution_2[i]}")            


        
        
if __name__ == "__main__":
    unittest.main()