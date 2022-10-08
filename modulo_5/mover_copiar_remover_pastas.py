import os
import shutil

caminho_original = r'C:\Users\Pos Vendas\Desktop\Teste'
caminho_novo = r'C:\Users\Pos Vendas\Desktop\Teste2'

try:
    os.mkdir(caminho_novo) # criando uma pasta
except FileExistsError as e:
    print(f'O {caminho_novo} já existe.')
    
def mover_arquivos(caminho_atual, caminho_novo):
    for caminhos, diretorios, arquivos in os.walk(caminho_atual):
        for arquivo in arquivos:
            caminho_completo = os.path.join(caminhos, arquivo)
            
            shutil.move(caminho_completo, caminho_novo)
            print(f'O {arquivo} foi movido com sucesso.')
            
def copiar_arquivos(caminho_atual, caminho_novo):
    for caminhos, diretorios, arquivos in os.walk(caminho_atual):
        for arquivo in arquivos:
            caminho_completo = os.path.join(caminhos, arquivo)
            shutil.copy(caminho_completo, caminho_novo)
            print(f'O {arquivo} foi copiado com sucesso.')
            
def remover_arquivos(caminho_atual):
    for caminhos, diretorios, arquivos in os.walk(caminho_atual):
        for arquivo in arquivos:
            caminho_completo = os.path.join(caminhos, arquivo)
            os.remove(caminho_completo)
            print(f'O {arquivo} foi removido com sucesso.')
            
            
if __name__ == '__main__':
    # mover_arquivos(caminho_original, caminho_novo)
    # copiar_arquivos(caminho_original, caminho_novo)
    # remover_arquivos(caminho_novo)
    pass