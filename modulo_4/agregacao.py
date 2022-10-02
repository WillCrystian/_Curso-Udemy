class CarrinhoDeCompra:
    def __init__(self):
        self.produtos = []
        
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        
    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.preco)
            
    def somar_preco(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total
            
            
class Produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    
carrinho = CarrinhoDeCompra()
p1 = Produtos('Camiseta', 50)
p2 = Produtos('Shorts', 70)

carrinho.adicionar_produto(p1)
carrinho.adicionar_produto(p2)
carrinho.listar_produtos()
print(carrinho.somar_preco())