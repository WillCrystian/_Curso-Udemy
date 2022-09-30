import re

def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

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
    
cnpj = input('Digite o CNPJ: ')
cnpj_limpo = remover_caracteres(cnpj)
cnpj_sem_digitos = cnpj_limpo[0:12]

cnpj_com_primeiro_digito = achar_digito(1, cnpj_sem_digitos)
cnpj_com_segundo_digito = achar_digito(2, cnpj_com_primeiro_digito)

if cnpj_limpo == cnpj_com_segundo_digito:
    print(f'O CNPJ {cnpj} é VÁLIDO')
else:
    print(f'O CNPJ {cnpj} é INVÁLIDO')
    
print()  
    
    