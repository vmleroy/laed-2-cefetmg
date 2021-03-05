import unittest

from typing import List, Dict
from grafo import Grafo,Vertice, DistanciaVerticeOrigem
from heap import MinHeap
class TestHeap(unittest.TestCase):
    def test_refaz(self):
        #refaz um heap simples de 3 nodos
        obj_heap = MinHeap()
        #heap que nao precisa alteração
        obj_heap.arr_heap = [None,-12,-9,-6]
        obj_heap.refaz(1)
        self.assertListEqual(obj_heap.arr_heap, [None,-12,-9,-6], f"A operação refaz não foi realizada corretamente. Lista de entrada: {[None,12,9,6]}")
        #heap pequeno, faz uma alteração a esquerda
        obj_heap.arr_heap = [None,-12,-15,-6]
        obj_heap.refaz(1)
        self.assertListEqual(obj_heap.arr_heap, [None,-15,-12,-6], f"A operação refaz não foi realizada corretamente. Lista de entrada: {[None,12,15,6]}")

        #heap pequeno, faz uma alteração a direita
        obj_heap.arr_heap = [None,-12,-9,-15]
        obj_heap.refaz(1)
        self.assertListEqual(obj_heap.arr_heap, [None,-15,-9,-12], f"A operação refaz não foi realizada corretamente. Lista de entrada: {[None,12,9,15]}")


        #heap grande, a partir do filho a esquerda faz uma alteração a direita e depois a esquerda
        obj_heap.arr_heap = [None,-12,-2,-6,-4,-5,3,0,-1,1, -3, 2]
        obj_heap.refaz(2)
        self.assertListEqual(obj_heap.arr_heap, [None,-12,-5,-6,-4,-3,3,0,-1,1, -2, 2], f"A operação refaz não foi realizada corretamente. Resultado esperado: {[None,12,5,6,4,3,-3,0,1,-1, 2, -2]} resultado obtido: {obj_heap.arr_heap}. Lista de entrada: {[None,12,2,6,4,5,-3,0,1,-1, 3, -2]}")

        #heap grande, a partir do filho a esquerda faz uma alteração a esquerda e depois a direita
        print("-------------")
        obj_heap.arr_heap = [None,-12,-2,-4,-6,-5,3,0,1,-3, -3, 2]
        obj_heap.refaz(2)
        self.assertListEqual(obj_heap.arr_heap, [None,-12,-6,-4,-3,-5,3,0,1,-2, -3, 2], f"A operação refaz não foi realizada corretamente. Resultado esperado: {[None,12,6,4,3,5,-3,0,-1,2, 3, -2]} resultado obtido: {obj_heap.arr_heap}. Lista de entrada: {[None,12,2,4,6,5,-3,0,-1,3, 3, -2]}")

    def test_insere(self):
        arr_test = [1,-8,-11,-14]
        arr_heap_esperado = [[None,-12,-9,-6,-4,-3,-5,-2,-1,1],
                             [None,-12,-9,-6,-8,-3,-5,-2,-1,-4],
                             [None,-12,-11,-6,-9,-3,-5,-2,-1,-4],
                             [None,-14,-12,-6,-9,-3,-5,-2,-1,-4],
                            ]
    
        #testa inserção no heap vazio
        for val_inserir in arr_test:
            objHeap = MinHeap()
            objHeap.insere(val_inserir)
            self.assertListEqual([None,val_inserir],objHeap.arr_heap,f"Inserção incorreta ao inserir o valor {val_inserir} no heap vazio, esperado: {[None,val_inserir]} obtido: {objHeap.arr_heap}")

        for i,val_inserir in enumerate(arr_test):
            objHeap = MinHeap()
            objHeap.arr_heap = [None,-12,-9,-6,-4,-3,-5,-2,-1]
            objHeap.insere(val_inserir)
            self.assertListEqual(arr_heap_esperado[i],objHeap.arr_heap,f"Inserção incorreta ao inserir o valor {val_inserir} no heap {[None,-12,-9,-6,-4,-3,-5,-2,-1]}, esperado: {arr_heap_esperado[i]} obtido: {objHeap.arr_heap}")


    def test_retira_min(self):
        obj_heap = MinHeap()
        obj_heap.arr_heap = [None,-12,-9,-4,-7,-5,3,0,1,-2, -3, 2]

        min_val = obj_heap.retira_min()
        self.assertEqual(min_val, -12, f"Não foi retirado o menor valor (-12) e sim {min_val} ")
        self.assertListEqual(obj_heap.arr_heap, [None,-9,-7,-4,-2,-5,3,0,1,2, -3], f"A operação test_retira_min não finalizou com o Heap esperado. ")

        obj_heap.arr_heap = [None,-12]
        min_val = obj_heap.retira_min()
        self.assertEqual(min_val, -12, f"Não foi retirado o menor valor (-12) e sim {min_val} ")
        self.assertListEqual(obj_heap.arr_heap, [None], f"A operação test_retira_min não finalizou com o Heap esperado. ")

class TestGrafo(unittest.TestCase):
    def setUp(self):
        self.grafo = Grafo()

        self.grafo.adiciona_vertice("A")
        self.grafo.adiciona_vertice("B")
        self.grafo.adiciona_vertice("C")
        self.grafo.adiciona_vertice("D")
        self.grafo.adiciona_vertice("E")
        self.grafo.adiciona_vertice("F")

        

        self.grafo.adiciona_aresta("A","B",4)
        self.grafo.adiciona_aresta("B","D",2)
        self.grafo.adiciona_aresta("B","C",4)
        self.grafo.adiciona_aresta("B","E",1)  
        self.grafo.adiciona_aresta("C","D",1)
        self.grafo.adiciona_aresta("D","C",10)
        self.grafo.adiciona_aresta("D","A",1)
        self.grafo.adiciona_aresta("E","C",1)
        self.grafo.adiciona_aresta("E","A",1)

    def test_distancia_vertice(self):
        vertice_a = self.grafo.obtem_vertice("A")
        vertice_b = self.grafo.obtem_vertice("B")

        distancia_b_10 = DistanciaVerticeOrigem(vertice_b, 10)        
        distancia_10 = DistanciaVerticeOrigem(vertice_a, 10)
        distancia_10_igual = DistanciaVerticeOrigem(vertice_a, 10)
        distancia_15 = DistanciaVerticeOrigem(vertice_a, 15)
        distancia_9 = DistanciaVerticeOrigem(vertice_a, 9)

        self.assertTrue(distancia_b_10 != distancia_10, msg="Os vertices devem ser os mesmos para que um objeto distancia seja igual ao outro")
        self.assertTrue(distancia_10 == distancia_10_igual, msg="Se o vertice  e a distancia são iguais, a distancia deveria ser igual")
        self.assertTrue(distancia_15 > distancia_10, msg="Uma distancia de 15 deveria ser maior do que uma distancia 10")
        self.assertTrue(distancia_9 < distancia_10, msg="Uma distancia de 9 deveria ser menor do que uma distancia 10") 

    def relax_teste(self, distancias:Dict[Vertice, DistanciaVerticeOrigem], pai:Dict[Vertice,Vertice],vertice:Vertice):
        str_msg = "O caminhamento de  A para C, passando por E, tem um custo menor (6). " 
        str_msg += f"O Custo atual é  {distancias[vertice].distancia} passando por {pai[vertice].valor}"
        self.assertEqual(pai[vertice].valor, "E", msg=str_msg)
        self.assertEqual(distancias[vertice].distancia, 6, msg=str_msg)

    def test_dijkstra_relax(self):
        vertice_a = self.grafo.obtem_vertice("A")
        vertice_c = self.grafo.obtem_vertice("C")
        vertice_b = self.grafo.obtem_vertice("B")
        vertice_e = self.grafo.obtem_vertice("E")
        heap = MinHeap()
        #caminhamentos considrando no A como origem
        distancias = {vertice_c: DistanciaVerticeOrigem(vertice_c, 8),
                      vertice_b: DistanciaVerticeOrigem(vertice_b, 4),
                      vertice_e: DistanciaVerticeOrigem(vertice_e, 5)}
        pai = { vertice_a:None,
                vertice_b:vertice_a,
                vertice_e:vertice_b,
                vertice_c:vertice_b}
        
        self.grafo.dijkstra_relax(heap,vertice_e, vertice_c, distancias,pai)
        
        #verifica se as distancias e o caminho foram modificadas apropriadamente
        #Fazemos o caminhamento de  A para C, passando por E, em um custo menor (6)
        self.relax_teste(distancias, pai, vertice_c)
        self.assertEqual(len(heap.arr_heap),2,"Sempre quando seja alterado a distancia deve-se adicionar no heap esta distancia")
        self.assertEqual(heap.arr_heap[1].vertice.valor,"C","O vértice adicionado no heap deveria ser o vértice C")
        #depois de modificado, o caminho de A para C passando por B não pode modificar o menor
        #caminho encontrado até então
        self.grafo.dijkstra_relax(heap,vertice_e, vertice_c, distancias,pai)
        self.relax_teste(distancias, pai, vertice_c)
        self.assertEqual(len(heap.arr_heap),2,"O heap não deveria ser modificado neste caso")

    def check_respostas(self, v_origem:str, str_resposta:str, dict_esperado:Dict, dict_respostas:Dict):  
        lst_vertices_respostas = set([vertice.valor for vertice in dict_respostas.keys()])
        lst_vertices_esperado = set(dict_esperado.keys())
        
        set_faltou = lst_vertices_esperado - lst_vertices_respostas
        set_vert_invalidas = lst_vertices_respostas - lst_vertices_esperado

        self.assertTrue(len(set_faltou)==0,msg=f"Faltou a resposta ({str_resposta}) os seguintes vertices: {set_faltou} - vértice origem: {v_origem}")
        self.assertTrue(len(set_vert_invalidas)==0,msg=f"Os vértices {set_vert_invalidas} não deveriam estar inclusos no resultado ({str_resposta})  - vértice origem: {v_origem}")        

    def dijkstra_result_teste(self,valor_vertice_inicial:str,dist_esperada:Dict[str,int], resposta_distancia:Dict[Vertice,DistanciaVerticeOrigem], 
                                                            pai_esperado:Dict[Vertice,str], resposta_pai:Dict[Vertice,Vertice]):

        self.check_respostas(valor_vertice_inicial, "distancias",dist_esperada,resposta_distancia)
        self.check_respostas(valor_vertice_inicial, "pai",pai_esperado,resposta_pai)
        for vertice,distancia in resposta_distancia.items():
            
            vertice_valor = vertice.valor
            self.assertEqual(dist_esperada[vertice_valor],distancia.distancia,
                            f"A distancia entre {valor_vertice_inicial} e {vertice_valor} deveria ser {dist_esperada[vertice_valor]} e foi {distancia.distancia}")


            pai_resposta = resposta_pai[vertice].valor if resposta_pai[vertice] is not None else None 
            self.assertEqual(pai_esperado[vertice_valor],pai_resposta,
                            f"No caminho mínimo de {valor_vertice_inicial} para {vertice_valor}, o vértice pai de {vertice_valor} é {pai_esperado[vertice_valor]} e não a {pai_resposta}")
    def test_dijkstra(self):



        distancias_esperadas_por_v_inicial = {
                                                "C":{
                                                    "A":2,
                                                    "B":6,
                                                    "C":0,
                                                    "D":1,
                                                    "E":7,
                                                    "F":float("inf"),
                                                    }
                                                }  
        pai_esperado_por_v_inicial = {   "A":{
                                                "A":None,
                                                "B":"A",
                                                "C":"E",
                                                "D":"B",
                                                "E":"B",
                                                "F":None
                                            },
                                            "B":{
                                                "A":"E",
                                                "B":None,
                                                "C":"E",
                                                "D":"B",
                                                "E":"B",
                                                "F":None
                                            },
                                            "C":{
                                                "A":"D",
                                                "B":"A",
                                                "C":None,
                                                "D":"C",
                                                "E":"B",
                                                "F":None
                                            },
                                            "D":{
                                                "A":"D",
                                                "B":"A",
                                                "C":"E",
                                                "D":None,
                                                "E":"B",
                                                "F":None
                                            }
                                        }         
        for vertice_inicial,distancias_esperadas in  distancias_esperadas_por_v_inicial.items():
            pai_esperado = pai_esperado_por_v_inicial[vertice_inicial]
            dict_resp_distancias,dict_resp_pai = self.grafo.dijkstra(vertice_inicial)
            self.dijkstra_result_teste(vertice_inicial, distancias_esperadas, dict_resp_distancias,pai_esperado, dict_resp_pai)
            
        
if __name__ == "__main__":
    unittest.main()
