# 'w' escreve no inicio do arquivo
# 'r' Lê arquivo desde o inicio
# 'a' escreve no final do arquivo

from cgi import test
import json
from dados import pessoas

p = pessoas
p_jason = json.dumps(p, indent= True) # convertendo para json

escrever_arquivo = True

if escrever_arquivo:
    with open('teste.json', 'w+') as arquivo:
        arquivo.write(p_jason)
else: 
    with open('./teste.json', 'r') as arquivo:
        p_jason = arquivo.read()
        p = json.loads(p_jason) # convertendo para txt