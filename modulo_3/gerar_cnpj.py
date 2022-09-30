from random import randint

def gerar_numero_aleatorio():
    numero = randint(100000000000, 999999999999)
    return str(numero)

def achar_digito(qual_digito, cnpj):
    if qual_digito == 1:        
        primeira_volta = 5
    elif qual_digito == 2:
        primeira_volta = 6
    else:
        primeira_volta = 0
        
    soma = 0

    for i in cnpj:
        if primeira_volta < 2:
            primeira_volta = primeira_volta + 8            
        soma = soma + (int(i) * primeira_volta)    
        primeira_volta -= 1

    digito = 11 - (soma % 11)

    if digito > 9:
        digito = 0

    cnpj = cnpj + str(digito)
    
    return cnpj
    
numero_aleatorio = gerar_numero_aleatorio()

cnpj_com_primeiro_digito = achar_digito(1, numero_aleatorio)
cnpj_com_segundo_digito = achar_digito(2, cnpj_com_primeiro_digito)

print(cnpj_com_segundo_digito)
    