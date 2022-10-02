class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
        
    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))
        
    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(f'{endereco.cidade}/ {endereco.estado}')

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
        
############################################################       
c1 = Cliente('Lorena', 4)
c1.insere_endereco('Diadema', 'SP')
c1.listar_enderecos()

c2 = Cliente('Maria', 50)
c2.insere_endereco('Viçosa', 'MG')
c2.listar_enderecos()