def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(saudacao, nome):
    return f'{saudacao} {nome}'

def soma(n1, n2, n3):
    return n1 + n2 + n3
    
executando = mestre(fala_oi, 'william')
print(executando)

executando2 = mestre(saudacao, 'Bom dia', 'Camila')
print(executando2)

executando3 = mestre(soma, 5, 5, 5)
print(executando3)