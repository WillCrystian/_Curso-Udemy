
import random
import string

# número inteiro aleatótio
inteiro = random.randint(0, 10)

# número inteiro atraves da função Range
inteiro_range = random.randrange(0, 20, 3)

# número flutuante entre A e B
flutuante = random.uniform(10, 20) 

# número flutuante entre 0 e 1
flutuante_0_e_1 = random.random()

lista = ['william', 'lorena', 'camila', 'joão', 'maria']

# embaralhar lista aleatório, mas não retorna nada
random.shuffle(lista)

# escolher 1 aleatório
sorteio_choice = random.choice(lista)

# escolher aleatório de acordo com 'k'
sorteio_choices = random.choices(lista, k= 2)

#escolher aletório de acordo com segundo parametro, porém não repete
sorteio_sample = random.sample(lista, 2)


#criar senha aleatório
letras = string.ascii_letters
numeros = string.digits
caracteres = '!@#$%&*()=+-_'

geral = letras + numeros + caracteres
senha_aleatorio = ''.join(random.choices(geral, k=10))
        
print(senha_aleatorio)


