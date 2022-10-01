'''
_ private/protected (consigo acessar fora da classe, porém não é recomendados)
__ private (não consigo usar fora da classe)
'''

class BancoDeDados:
    def __init__(self):
        self.__dados = {}
        
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
            
    def listar_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)
            
    def excluir_cliente(self, id):
        del self.__dados['clientes'][id]
            
            
bd = BancoDeDados()
bd.inserir_cliente(1, 'William')
bd.inserir_cliente(2, 'Camila')
bd.inserir_cliente(3, 'Lorena')
bd.excluir_cliente(2)