lt_tarefas = []
lt_desfazer = []
last_todo = ''

while True:
    tarefa = input('Nova Tarefa: ').lower()
    
    if tarefa not in lt_tarefas:
        # desfazer
        if tarefa == 'undo' and len(lt_tarefas) > 0:
            lt_desfazer.append(lt_tarefas[-1])
            lt_tarefas.pop()
        
        #refazer
        elif tarefa == 'redo' and len(lt_desfazer) > 0:
            lt_tarefas.append(lt_desfazer[-1])
            lt_desfazer.pop()
            
        # adicionar na lista
        elif tarefa != 'redo' and tarefa != 'undo':
            lt_tarefas.append(tarefa)
    
    last_todo = tarefa
    
    print(f'Tarefas: {lt_tarefas}\n')
    #print(f'Lista desfazer {lt_desfazer}')
