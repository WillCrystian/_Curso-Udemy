class Banco:
    def __init__(self) -> None:
        self._agencia = [1111, 2222, 3333]
        self._conta = []
        self._cliente = []
        
    def adicionar_cliente(self, cliente):
        self._cliente.append(cliente)
        
    def adicionar_conta(self, conta):
        self._conta.append(conta)
    
    def autenticar(self, cliente) -> bool:
        if cliente.conta.agencia not in self._agencia:
            print(f'agencia {cliente.conta.agencia}')
            return False
        
        if cliente.conta not in self._conta:
            print(f'conta {cliente.conta.conta}')
            return False
        
        if cliente not in self._cliente:
            print(f'cliente {cliente}')
            return False
        return True
            