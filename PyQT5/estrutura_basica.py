import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class App(QMainWindow):
    def __init__(self, parent= None) -> None:
        super().__init__(parent)
        
        
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()