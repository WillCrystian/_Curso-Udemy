from dados import pessoas, produtos, lista

nova_lista = list(filter(lambda l: l > 5, lista))
print(nova_lista)
print()

mais_30 = list(filter(lambda p: p['preco'] > 30, produtos))
for m in mais_30:
    print(m)    
print()

def maior_18(idade):
    if idade['idade'] >= 18:
        return True

maiores_idade = list(filter(maior_18, pessoas))

for m in maiores_idade:
    print(m)
