from conta import Conta

class ContaPoupanca(Conta):
    
    def sacar(self, sacar):
        if sacar > self.saldo:
            print('Saldo insulficiente')
            return
        
        self.saldo -= sacar
        self.detalhe()