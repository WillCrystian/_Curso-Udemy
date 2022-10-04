from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, conta, agencia) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = 0    
    
    def deposito(self, valor):
        self.saldo += valor
        self.extrato()
        
    @abstractmethod
    def sacar(self, valor):
        pass
    
    def extrato(self):
        print(f'Conta: {self.conta} Agência: {self.agencia} Saldo: R${self.saldo:.2f}')
        print()
        
        
class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Seu saldo atual é de R${self.saldo:.2f}, não foi possível fazer o saque de R${valor:.2f}.')
            return
        
        self.saldo -= valor
        self.extrato()
        
class ContaCorrente(Conta):
    def __init__(self, conta, agencia, limite=100) -> None:
        super().__init__(conta, agencia)
        self._limite = limite
        
    @property
    def limite(self):
        return self._limite
    
    def sacar(self, valor):
        if valor > (self.saldo + self.limite):
            print(f'Seu saldo atual é de R${self.saldo:.2f}, não foi possível fazer o saque de R${valor:.2f}.')
            return
        
        self.saldo -= valor
        self.extrato()