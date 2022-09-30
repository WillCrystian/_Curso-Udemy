from time import time

def velocidade(funcao):
    def slaver(*args, **kwargs):
        print('funcão decorador')
        time_inicio = time()
        resultado = funcao(*args, **kwargs)
        time_fim = time()
        
        time_execucao = (time_fim - time_inicio) * 1000
        print(f'\nTempo para execução do programa foi {time_execucao:.2f}ms')
        
        return resultado
    return slaver
        
@velocidade
def contador():
    for i in range(10000):
        print(i, end='')
    
    
contador()