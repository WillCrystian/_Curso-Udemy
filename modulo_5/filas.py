from time import sleep
from collections import deque

"""
Tamanho máximo da fila  é 5
e vai removendo o primeiro que entrou na fila
"""
fila = deque(maxlen=5)

for i in range(100):
    fila.append(i)
    sleep(1)
    print(fila)