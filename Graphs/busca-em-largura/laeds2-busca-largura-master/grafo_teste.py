import unittest

from typing import List, Dict
from grafo import Grafo,Vertice
class TestGrafo(unittest.TestCase):
    def setUp(self):
        self.arr_tests = []


        self.arr_tests.append(Grafo())
        self.arr_tests[0].adiciona_vertice(0)
        self.arr_tests[0].adiciona_vertice(1)
        self.arr_tests[0].adiciona_vertice(2)
        self.arr_tests[0].adiciona_vertice(3)
        self.arr_tests[0].adiciona_vertice(4)
        self.arr_tests[0].adiciona_vertice(5)
        self.arr_tests[0].adiciona_vertice(6)

        self.arr_tests[0].adiciona_aresta(0, 1)
        self.arr_tests[0].adiciona_aresta(1, 2)
        self.arr_tests[0].adiciona_aresta(1, 3)
        self.arr_tests[0].adiciona_aresta(2, 5)
        self.arr_tests[0].adiciona_aresta(3, 5)
        self.arr_tests[0].adiciona_aresta(4, 5)

        self.arr_tests.append(Grafo())
        self.arr_tests[1].adiciona_vertice(0)
        self.arr_tests[1].adiciona_vertice(1)
        self.arr_tests[1].adiciona_vertice(2)
        self.arr_tests[1].adiciona_vertice(3)

        self.arr_tests[1].adiciona_aresta(0, 1)
        self.arr_tests[1].adiciona_aresta(1, 2)
        self.arr_tests[1].adiciona_aresta(2, 3)
        self.arr_tests[1].adiciona_aresta(3, 1)

    def grau_separacao_result_teste(self,valor_vertice_inicial:str,esperado:Dict[str,int], dict_respostas:Dict[Vertice,int]):
        lst_pessoas_respostas = set([vertice.valor for vertice in dict_respostas.keys()])
        lst_pessoas_esperado = set(esperado.keys())
        
        set_faltou = lst_pessoas_esperado - lst_pessoas_respostas
        set_pessoas_invalidas = lst_pessoas_respostas - lst_pessoas_esperado

        self.assertTrue(len(set_faltou)==0,msg=f"Faltou a distancia das seguintes pessoas: {set_faltou}")
        self.assertTrue(len(set_pessoas_invalidas)==0,msg=f"As pessoas {set_pessoas_invalidas} não deveriam estar inclusas no resultado")

        for vertice,distancia in dict_respostas.items():
            pessoa = vertice.valor
            self.assertEqual(esperado[pessoa],distancia,
                            f"O grau de separação entre {valor_vertice_inicial} e {pessoa} deveria ser {esperado[pessoa]} e foi {distancia}")

    def test_grau_separacao(self):
        grafo = Grafo()
        grafo.adiciona_vertice("Alice")
        grafo.adiciona_vertice("Bob")
        grafo.adiciona_vertice("Carol")
        grafo.adiciona_vertice("Daniel")
        grafo.adiciona_vertice("Elisa")
        grafo.adiciona_vertice("Fabio")
        grafo.adiciona_vertice("Gabriel")
        grafo.adiciona_vertice("Igor")
        grafo.adiciona_vertice("Katia")

        

        grafo.adiciona_aresta("Alice","Carol")
        grafo.adiciona_aresta("Alice","Daniel")
        grafo.adiciona_aresta("Alice","Igor")

        grafo.adiciona_aresta("Bob","Alice")
        grafo.adiciona_aresta("Bob","Carol")

        grafo.adiciona_aresta("Carol","Alice")
        grafo.adiciona_aresta("Carol","Daniel")

        grafo.adiciona_aresta("Daniel","Carol")
        grafo.adiciona_aresta("Daniel","Elisa")

        grafo.adiciona_aresta("Elisa","Gabriel")

        grafo.adiciona_aresta("Igor","Daniel")
        grafo.adiciona_aresta("Igor","Gabriel")

        grafo.adiciona_aresta("Gabriel","Katia")


        distancias_esperadas_por_v_inicial = {"Alice":{
                                        "Alice":0,
                                        "Bob":float("inf"),
                                        "Carol":1,
                                        "Daniel":1,
                                        "Elisa":2,
                                        "Fabio":float("inf"),
                                        "Gabriel":2,
                                        "Igor":1,
                                        "Katia":3 },
                                "Bob":{
                                        "Alice":1,
                                        "Bob":0,
                                        "Carol":1,
                                        "Daniel":2,
                                        "Elisa":3,
                                        "Fabio":float("inf"),
                                        "Gabriel":3,
                                        "Igor":2,
                                        "Katia":4 
                                        },    
                                "Carol":{"Alice":1,
                                        "Bob":float("inf"),
                                        "Carol":0,
                                        "Daniel":1,
                                        "Elisa":2,
                                        "Fabio":float("inf"),
                                        "Gabriel":3,
                                        "Igor":2,
                                        "Katia":4},
                                "Daniel":{
                                        "Alice":2,
                                        "Carol":1,
                                        "Bob":float("inf"),
                                        "Daniel":0,
                                        "Elisa":1,
                                        "Fabio":float("inf"),
                                        "Gabriel":2,
                                        "Igor":3,
                                        "Katia":3
                                        }
                                }            
        for vertice_inicial,distancias_esperadas in  distancias_esperadas_por_v_inicial.items():
            dict_respostas = grafo.grau_separacao(vertice_inicial)
            self.grau_separacao_result_teste(vertice_inicial, distancias_esperadas, dict_respostas)

            
        def test_grau_separacao_victor(self):
            grafo = Grafo()
            grafo.adiciona_vertice("Victor")
            grafo.adiciona_vertice("Gabriel Fallen")
            grafo.adiciona_vertice("Maycon")
            grafo.adiciona_vertice("Leticia")
            grafo.adiciona_vertice("Giovana")
            grafo.adiciona_vertice("Lorena")
            grafo.adiciona_vertice("Felipe")
            grafo.adiciona_vertice("Valentina")
            grafo.adiciona_vertice("Juliana")
            grafo.adiciona_vertice("Rubens")


            grafo.adiciona_aresta("Victor","Maycon")
            grafo.adiciona_aresta("Victor","Leticia")
            grafo.adiciona_aresta("Victor","Lorena")
            grafo.adiciona_aresta("Victor","Felipe")

            grafo.adiciona_aresta("Maycon","Victor")
            grafo.adiciona_aresta("Maycon","Juliana")
            grafo.adiciona_aresta("Maycon","Leticia")

            grafo.adiciona_aresta("Leticia","Giovana")
            grafo.adiciona_aresta("Leticia","Maycon")
            grafo.adiciona_aresta("Leticia","Victor")

            grafo.adiciona_aresta("Giovana","Leticia")

            grafo.adiciona_aresta("Lorena","Victor")
            grafo.adiciona_aresta("Lorena","Valentina")
            grafo.adiciona_aresta("Lorena","Felipe")
            grafo.adiciona_aresta("Lorena","Rubens")

            grafo.adiciona_aresta("Felipe","Victor")
            grafo.adiciona_aresta("Felipe","Lorena")
            grafo.adiciona_aresta("Felipe","Rubens")

            grafo.adiciona_aresta("Valentina","Lorena")

            grafo.adiciona_aresta("Juliana","Maycon")

            grafo.adiciona_aresta("Rubens","Felipe")
            grafo.adiciona_aresta("Rubens","Lorena")

            distancias_esperadas_por_v_inicial = {
                                    "Victor":{
                                            "Victor":0,
                                            "Gabriel Fallen":float("inf"),
                                            "Maycon":1,
                                            "Leticia":1,
                                            "Giovana":2,
                                            "Lorena":1,
                                            "Felipe":1,
                                            "Valentina":2,
                                            "Juliana":2, 
                                            "Rubens":2
                                            },
                                    "Maycon":{
                                            "Victor":1,
                                            "Gabriel Fallen":float("inf"),
                                            "Maycon":0,
                                            "Leticia":1,
                                            "Giovana":2,
                                            "Lorena":2,
                                            "Felipe":2,
                                            "Valentina":3,
                                            "Juliana":1, 
                                            "Rubens":3
                                            },
                                    "Felipe":{
                                            "Victor":1,
                                            "Gabriel Fallen":float("inf"),
                                            "Maycon":2,
                                            "Leticia":2,
                                            "Giovana":3,
                                            "Lorena":1,
                                            "Felipe":0,
                                            "Valentina":2,
                                            "Juliana":3, 
                                            "Rubens":1
                                            }                                
                                    }            
        for vertice_inicial,distancias_esperadas in  distancias_esperadas_por_v_inicial.items():
            dict_respostas = grafo.grau_separacao(vertice_inicial)
            self.grau_separacao_result_teste(vertice_inicial, distancias_esperadas, dict_respostas)
        
if __name__ == "__main__":
    unittest.main()
