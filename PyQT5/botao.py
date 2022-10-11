import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QWidget, QGridLayout

class App(QMainWindow):
    def __init__(self, parent= None) -> None:
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.btn = QPushButton('Texto do botão')
        
        # modificando o tamanho da fonte do botão
        self.btn.setStyleSheet('font-size: 15px')
        
        # botão fazendo a função de um método
        self.btn.clicked.connect(self.fala)
        
        # adicionando o botão na grid
        self.grid.addWidget(self.btn, 0, 0, 1, 1)
        self.setCentralWidget(self.cw)
        
    def fala(self):
        print('Olá mundo')
        
        
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()