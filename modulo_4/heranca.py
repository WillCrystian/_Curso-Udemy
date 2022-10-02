class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        

class Cliente(Pessoa):
    def comprar(self):
        print('Cliente comprando')
    
    
c1 = Cliente('Robson', 31)
print(c1.nome, c1.idade)
c1.comprar()
#a1 = Aluno('Manuela', 16)