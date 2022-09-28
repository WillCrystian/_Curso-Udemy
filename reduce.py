from dados import lista, pessoas, produtos
from functools import reduce

######## Fazer somas em listas, dicionarios ########

soma_lista = reduce(lambda ac, i: ac + i, lista, 0)
print(soma_lista)

soma_preco = reduce(lambda ac, p: ac + p['preco'], produtos, 0)
print(soma_preco)

soma_idade = reduce(lambda ac, i: ac + i['idade'], pessoas, 0)
print(soma_idade)