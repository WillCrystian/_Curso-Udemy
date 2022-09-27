from audioop import mul


lista = [
    ['p1', 13],
    ['p3', 33],
    ['p4', 21],
    ['p2', 26]
]

ordenado = sorted(lista, key=lambda i: i[1])
print(ordenado)


soma = lambda a, b, c: a + b + c
mult = lambda a, b: a * b

print(soma(3, 8, 55))
print(mult(3, 8))