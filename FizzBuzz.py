def percentual(n1, porcentagem):
    return (n1 * porcentagem) / 100

print(percentual(80,25))

def divisivel(n1):
    if n1 % 5 == 0 and n1 % 3 == 0:
        return 'FizzBuzz'
    elif  n1 % 3 == 0:
        return 'Fizz'
    elif n1 % 5 == 0:
        return 'Buzz'
    else:
        return n1
    
print(divisivel(7))