from PIL import Image
import os
        
def main(image_folder, new_width = 800):
    # verificando se o diretório existe.
    if not os.path.isdir(image_folder):
        print('Diretório não encontrado!')
        return
        
    for roots, dirs, files in os.walk(image_folder):
        for file in files:
            full_path = os.path.join(roots, file)
            file_name, extension = os.path.splitext(file)
            
            converted_tag = '_CONVERTED'
            new_file = file_name + converted_tag + extension
            new_file_full_path = os.path.join(image_folder, new_file)
            
            # Remover os arquivos criados
            #if converted_tag in full_path:
            #    os.remove(full_path)  
            #   print(f'O arquivo {full_path} foi removido com sucesso.')              
            #continue            
            
            # verificando se o arquivo a ser criado já existe na pasta
            if os.path.isfile(new_file_full_path):
                print(f'A imagem {new_file_full_path} já existe.')
                continue
            
            #  se arquivo já está convertido return
            if converted_tag in full_path:
                print(f'O {full_path} já está convertido.')
                continue
            
            # abrindo imagem
            img_pillow = Image.open(full_path)
            
            # obtendo tamanho da imagem
            width, height = img_pillow.size
            # obtendo valores do redimensionando da imagem
            new_height= round((new_width * height) / width)
            # redimencionando imagem
            new_img = img_pillow.resize((new_width, new_height), Image.LANCZOS)
            
            # salvando imagem
            new_img.save(new_file_full_path, optimize= True, quality= 70) # exif= img_pillow.info['exif']
            
            new_img.close()
            
            # fechando imagem
            img_pillow.close()
            print(f'{file} convertido com sucesso.')
            
            
if __name__== '__main__':
    image_folder = r'C:\Users\Pos Vendas\Desktop\cachorros'
    main(image_folder, new_width= 1200)