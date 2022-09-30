string = '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10
comp = [string[v: v + 10] for v in range(0, len(string), n)]

concatenacao = '.'.join(comp)
print(concatenacao)