class Meta(type):
    def __ini__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        
        if 'b_fala' not in  namespace:
            print(f'Oi, você precisa criar método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método, não atributo em {name}')
        return type.__new__(msc, name, bases, namespace)
    
class A(metaclass= Meta):
    def fala(self):
        self.b_fala()
        
class B(A):
    def b_fala(self):
        print('oi')
        
b = B()
b.fala()