from eletronico import Eletronico
from log import LogMixes

class Smartphone(Eletronico, LogMixes):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False
    
    def conectar(self):
        if not self._ligado:
            self.log_error(f'{self._nome} está desligado')
            return
        
        if self._conectado:
            self.log_error(f'{self._nome} já está conectado')
            return
        
        self.log_info(f'{self._nome} conectando.')
        self._conectado = True
        
    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} já está desconectado'
            self.log_error(error)
            return
        
        self.log_info(f'{self._nome} desconectando')
        self._conectado = False
        
    