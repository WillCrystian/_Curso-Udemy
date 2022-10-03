from cp import ContaPoupanca
from cc import ContaCorrente

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(100)
cp.depositar(20)
cp.sacar(50)
cp.sacar(71)

print()

cc = ContaCorrente(1111, 3333, 0, 100)
cc.depositar(20)
cc.sacar(80)
cc.sacar(80)
cc.sacar(50)