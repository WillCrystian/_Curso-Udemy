from zipfile import ZipFile
import os

caminho = r'C:\Users\Pos Vendas\Desktop\Teste'

# Compactar arquivos
with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)
    print('Compactado com sucesso.')
    
print('#######################################################')

# Ler arquivos que estão compactados
with ZipFile('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)
        
print('#######################################################')

# extrair arquivos
with ZipFile('arquivo.zip', 'r') as zip:
    zip.extractall(caminho + '\descompactado')
    print('Descompactado com sucesso.')