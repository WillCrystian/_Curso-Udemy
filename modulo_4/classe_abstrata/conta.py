from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia , conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
        
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def conta(self):
        return self._conta
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            print('O SALDO tem que ser númerico')
            
        self._saldo = valor
        
    def depositar(self, deposito):
        self.saldo += deposito
        self.detalhe()
    
    @abstractmethod
    def sacar(self, sacar):
        pass
        
    def detalhe(self):
        print(f'Conta: {self.conta}', end=' ')
        print(f'Agência: {self.agencia}', end=' ')
        print(f'Saldo: {self.saldo}')