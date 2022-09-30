######### Sistemas de perguntas e respostas #########

perguntas = {
    'Pergunta 1:': {
        'pergunta': 'Quanto é 2 + 2? ',
        'respostas': {'a': '8', 'b': '4', 'c': '10'},
        'resposta_certa': 'b'
    },
    'Pergunta 2:': {
        'pergunta': 'Quanto é 5 + 2? ',
        'respostas': {'a': '7', 'b': '3', 'c': '6'},
        'resposta_certa': 'a'
    },    
    'Pergunta 3:': {
        'pergunta': 'Quanto é 7 * 3? ',
        'respostas': {'a': '19', 'b': '20', 'c': '21'},
        'resposta_certa': 'c'
    },   
}

respostas_certas = 0

for pk, pv in perguntas.items():
    print(f'\n{pk} {pv["pergunta"]}')
    
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}] {rv}')
        
    resposta_usuario = input('\nQual é sua resposta? ')
    
    
    if resposta_usuario == pv['resposta_certa']:
        respostas_certas += 1
        print('Parabéns você acertou!!\n')
    else:
        print('Você errou!\n')
    
    
quant_perguntas = len(perguntas)
porcentagem_acerto = (100 * respostas_certas) / quant_perguntas
    
if respostas_certas == 0:
    print(f'Você errou todas as perguntas.')
elif respostas_certas == 1:    
    print(f'Você acertou {respostas_certas} resposta.')
else:
    print(f'Você acertou {respostas_certas} respostas.')
    
print(f'Teve {porcentagem_acerto:.0f} % de acerto.')
        