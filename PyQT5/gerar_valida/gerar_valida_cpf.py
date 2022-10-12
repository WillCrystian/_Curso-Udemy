from gerar_cpf import gera_cpf
from valida_cpf import validar_cpf
from designer import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit

class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent= None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        
        self.btnValidar.clicked.connect(self.validar)
        self.btnGerar.clicked.connect(self.gerar)
        
    def validar(self):
        cpf = self.inputValidar.text()
        if validar_cpf(cpf):
            self.labelValida.setStyleSheet('color: green')
            self.labelValida.setText('CPF Válido')
        else:
            self.labelValida.setStyleSheet('color: red')
            self.labelValida.setText('CPF Inválido')
            
    def gerar(self):
        cpf = gera_cpf()
        self.labelGerar.setText(cpf)
        
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
