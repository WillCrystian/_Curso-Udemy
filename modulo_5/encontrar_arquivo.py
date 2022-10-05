import os

procura_caminho = input('Digite um caminho: ')
procura_termo = input('Procura por? ')

def transforma_tamanho(tamanho):
    base = 1024
    mega = base ** 2 # 1.048.576 bytes
    giga = base ** 3 # 1.073.741.824 bytes
    tera = base ** 4 # 1.099.511.627.776 byte
    peta = base ** 5
    
    if tamanho < base:
        texto = 'b'
    elif tamanho < mega:
        texto = 'Kb'
        tamanho /= base
    elif tamanho < giga:
        texto = 'Mb'
        tamanho /= mega
    elif tamanho < tera:
        texto = 'Gb'
        tamanho /= giga
    elif tamanho < peta:
        texto = 'Tb'
        tamanho /= tera
     

    tamanho_format = round(tamanho, 2)
    return f'{tamanho_format}{texto}'

cont = 0
for caminhos, b, arquivos in os.walk(procura_caminho):
    for arquivo in arquivos:
        if procura_termo in arquivo:
            caminho_completo = os.path.join(caminhos, arquivo)
            nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
            tamanho_arquivo = os.path.getsize(caminho_completo)
            tamanho_convertido = transforma_tamanho(tamanho_arquivo)
            
            print()
            print('Caminho completo: ', caminho_completo)
            print('Nome arquivo: ', nome_arquivo)
            print('Extensão do arquivo: ', ext_arquivo)
            print('Tamanho do arquivo: ', tamanho_arquivo)
            print('Tamanho convertido: ',tamanho_convertido)
            print()
            cont += 1
            
print(f'{cont} arquivo(s) encontrado(s)')
        
