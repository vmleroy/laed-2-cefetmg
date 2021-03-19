import unittest

from typing import List, Dict
from arv_geradora_min import Grafo,Vertice
from heap import MinHeap

class TestArvGeradoraMinima(unittest.TestCase):
    def setUp(self):
        self.grafo = Grafo()

        self.grafo.adiciona_vertice("A")
        self.grafo.adiciona_vertice("B")
        self.grafo.adiciona_vertice("C")
        self.grafo.adiciona_vertice("D")
        self.grafo.adiciona_vertice("E")
        self.grafo.adiciona_vertice("F")

        

        self.grafo.adiciona_aresta("A","B",4, bidirecional=True)
        self.grafo.adiciona_aresta("A","C",10, bidirecional=True)
        
        self.grafo.adiciona_aresta("B","C",5, bidirecional=True)
        self.grafo.adiciona_aresta("B","E",2, bidirecional=True)
        self.grafo.adiciona_aresta("C","E",20, bidirecional=True)
        self.grafo.adiciona_aresta("C","D",3, bidirecional=True)
        self.grafo.adiciona_aresta("D","E",7, bidirecional=True)
        self.grafo.adiciona_aresta("E","F",6, bidirecional=True)

    def check_respostas(self, v_origem:str, str_resposta:str, dict_esperado:Dict, dict_respostas:Dict):  
        lst_vertices_respostas = set([vertice.valor for vertice in dict_respostas.keys()])
        lst_vertices_esperado = set(dict_esperado.keys())
        
        set_faltou = lst_vertices_esperado - lst_vertices_respostas
        set_vert_invalidas = lst_vertices_respostas - lst_vertices_esperado

        self.assertTrue(len(set_faltou)==0,msg=f"Faltou a resposta ({str_resposta}) os seguintes vertices: {set_faltou} - vértice origem: {v_origem}")
        self.assertTrue(len(set_vert_invalidas)==0,msg=f"Os vértices {set_vert_invalidas} não deveriam estar inclusos no resultado ({str_resposta})  - vértice origem: {v_origem}")        

    def verifica_caminho_arv_geradora_min(self,valor_vertice_inicial:str, pai_esperado:Dict[Vertice,str], resposta_pai_por_vertice:Dict[Vertice,Vertice]):
        #self.check_respostas(valor_vertice_inicial, "pai",pai_esperado,resposta_pai_por_vertice)
        for vertice,pai_resposta in resposta_pai_por_vertice.items():
            vertice_valor = vertice.valor
            pai_resposta_valor = pai_resposta.valor if not pai_resposta is None else None
            self.assertEqual(pai_esperado[vertice_valor],pai_resposta_valor,
                            f"Arvore geradora minima iniciada {valor_vertice_inicial}: o vértice pai de {vertice_valor} é {pai_esperado[vertice_valor]} e não {pai_resposta_valor}")
    def test_arv_geradora_minima(self):
        pai_esperado_por_v_inicial = {   "A":{
                                                "A":None,
                                                "B":"A",
                                                "C":"B",
                                                "D":"C",
                                                "E":"B",
                                                "F":"E"
                                            },
                                            "B":{
                                                "A":"B",
                                                "B":None,
                                                "C":"B",
                                                "D":"C",
                                                "E":"B",
                                                "F":"E"
                                            },
                                            "C":{
                                                "A":"B",
                                                "B":"C",
                                                "C":None,
                                                "D":"C",
                                                "E":"B",
                                                "F":"E"
                                            },
                                            "D":{
                                                "A":"B",
                                                "B":"C",
                                                "C":"D",
                                                "D":None,
                                                "E":"B",
                                                "F":"E"
                                            }
                                        }         
        for vertice_inicial,pai_esperado in  pai_esperado_por_v_inicial.items():
            dict_resp_pai = self.grafo.cria_arv_geradora_minima(vertice_inicial)
            print(f"RESPOSTA: {dict_resp_pai} pai_esperado: {pai_esperado}")
            self.verifica_caminho_arv_geradora_min(vertice_inicial, pai_esperado, dict_resp_pai)
            
        
if __name__ == "__main__":
    unittest.main()
