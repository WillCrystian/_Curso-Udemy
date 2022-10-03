from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite = 100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite
        
    @property
    def limite(self):
        return self._limite
    
    def sacar(self, sacar):
        if sacar > (self.limite + self.saldo):
            print('Saldo insulficiente')
            return
        
        self.saldo -= sacar
        self.detalhe()
        
        