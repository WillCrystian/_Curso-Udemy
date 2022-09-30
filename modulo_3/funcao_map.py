from dados import produtos, pessoas, lista

nova_lista = map(lambda i : i * 2, lista)
print(list(nova_lista))

precos = map(lambda p: round(p['preco'] * 1.10, 2), produtos)
print(list(precos))

def letras_maiuscula(nome):
    nome['nome'] = nome['nome'].upper()+'s'
    return nome

novas_pessoas = map(letras_maiuscula, pessoas)

for pessoa in novas_pessoas:
    print(pessoa)