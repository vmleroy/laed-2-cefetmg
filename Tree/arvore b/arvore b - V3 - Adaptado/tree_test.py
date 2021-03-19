from tree import BTree

arvore_b_ordem_2 = BTree(2)
#keys = ['C','S','D','T','A','M','P','I','B','W','N','G','U','R','K','E','H','O','L','J','Y','Q','Z','F','X','V']
#keys = ['P', 'Q', 'R', 'S', 'T', 'U', 'V']
keys = [20, 10, 40, 50, 30, 55, 3, 11, 4, 28, 36, 33, 52, 17, 25, 13, 54, 9, 43, 8, 48]
for i in keys:    
    #print(i)
    arvore_b_ordem_2.insert_key(i)
    #arvore_b_ordem_2.print_tree()
    #print()
    #print("PROXIMO")
arvore_b_ordem_2.print_tree()
no_procura, posicao = arvore_b_ordem_2.search_tree(36)
print("Encontrada key no node:", no_procura.keys, " Na posicao:",posicao)

print()
arvore_b_ordem_2.delete_key(36)
arvore_b_ordem_2.print_tree()
print()
arvore_b_ordem_2.delete_key(33)
arvore_b_ordem_2.print_tree()


