# 'w' escreve no inicio do arquivo
# 'r' Lê arquivo desde o inicio
# 'a' escreve no final do arquivo

with open('teste.txt', 'a+') as arquivo:
    arquivo.write("'w' escreve no inicio do arquivo\n")
    arquivo.write("'r' Le arquivo desde o inicio\n")
    arquivo.write("'r' Le arquivo desde o inicio\n")