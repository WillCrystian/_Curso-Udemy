from pessoa import Cliente
from contas import ContaCorrente, ContaPoupanca
from banco import Banco

b1 = Banco()
cliente1 = Cliente('William', 30)
conta1 = ContaCorrente(123456, 1111)

cliente1.adicionar_conta(conta1)
b1.adicionar_cliente(cliente1)
b1.adicionar_conta(conta1)

if b1.autenticar(cliente1):
    cliente1.conta.deposito(50)
    cliente1.conta.sacar(20)
    cliente1.conta.sacar(131)
    
else:
    print('Autenticação inválida')