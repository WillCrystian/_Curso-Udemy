""" comando para converter arquivo do QT Designer em .py
-> pyuic5 nome_do_projeto.ui -o nome_do_arquivo.py 
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QFileDialog
from PyQt5.QtGui import QPixmap
from designer import *

class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent= None ) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherImagem.clicked.connect(self.abrir_imagem)
        self.btnRedimensionar.clicked.connect(self.redimensionar)
        self.btnSalvar.clicked.connect(self.salvar_imagem)
        
    def abrir_imagem(self):
        # caminho da imagem
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Imagem',
            r'C:\Users\Pos Vendas\Desktop\cachorros',            
        )
        
        # passando o nome da imagem para o input
        self.inputNomeArquivo.setText(imagem)
        # Armazenando o caminho da imagem
        self.original_img = QPixmap(imagem)
        # mandar imagem para o label do formulario
        self.labelImg.setPixmap(self.original_img)
        # pegar largura e passar para input
        self.inputLargura.setText(str(self.original_img.width()))
        # pegar altura e passar para input
        self.inputAltura.setText(str(self.original_img.height()))
        
    def redimensionar(self):
        try:
            # armazenando o valor da largura
            largura = int(self.inputLargura.text())
            # com base na largura redimensiona altura
            self.nova_imagem = self.original_img.scaledToWidth(largura)
            # passa para o label Imagem a nova imagem
            self.labelImg.setPixmap(self.nova_imagem)
            # pegar largura e passar para input
            self.inputLargura.setText(str(self.nova_imagem.width()))
            # pegar altura e passar para input        
            self.inputAltura.setText(str(self.nova_imagem.height()))
        except ValueError as e:
            print('Erro:', e)
            print('Escolha uma imagem antes de redimensiona-lá')
        
    def salvar_imagem(self):
        # caminho da imagem 
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar Imagem',
            r'C:\Users\Pos Vendas\Desktop',            
        )
        try:
            self.nova_imagem.save(imagem, 'PNG')
        except AttributeError as e:
            print('Erro:', e)
            print('Para salvar a imagem precisa redimensiona-lá')

        
        
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()

