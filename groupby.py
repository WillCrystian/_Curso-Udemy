from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'Anderson', 'nota': 'B'},
]

ordena_nota = lambda i : i['nota']

alunos.sort(key= ordena_nota)
alunos_agrupados = groupby(alunos, ordena_nota)

for nota, grupos in alunos_agrupados:
    print(f'Alunos com nota {nota}.')
    for grupo in grupos:        
        print(grupo)
    print()
