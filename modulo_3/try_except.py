def converte_numero(numero):
    try:
        return int(numero)
    except ValueError:
        
        try:
            return float(numero)           
        except ValueError:
            pass        

def soma(numero):
    return 10 + numero

numero = input('Digite um número: ')
numero = converte_numero(numero)

if numero == None:
    print('Não é um número.')
else:
    print(soma(numero))
