from datetime import date

class Pessoa:
    ano_atual = date.today().year
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        ano_nascimento = self.ano_atual - self.idade
        return ano_nascimento
    
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimto):
        idade = cls.ano_atual - ano_nascimto
        return idade
        
    
p1 = Pessoa('william', 31)

print(p1.get_ano_nascimento())


######## Class Method ##########
print(p1.por_ano_nascimento('Lorena', 2018))
