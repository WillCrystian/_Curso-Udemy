class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        

class Cliente(Pessoa):
    def comprar(self):
        print('Cliente comprando')
        
class Aluno(Pessoa):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade) # como sobrepor um metodo
        #Pessoa.__init__(self, nome, idade) # passa o nome da classe e  self
        self.sobrenome = sobrenome
    
    
c1 = Cliente('Robson', 31)
print(c1.nome, c1.idade)
c1.comprar()

a1 = Aluno('Manuela', 16, 'Ferreira')
print(a1.nome, a1.sobrenome, a1.idade)
