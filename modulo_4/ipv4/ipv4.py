import re
from tkinter import N

def decimal_binario(numero):
    if isinstance(numero, str):
        numero = int(numero)    
    binario = bin(numero)[2:]
    return binario

def limpar_ip(ip):
    return re.sub(r'[^0-9]', '',ip)


ipv4 = '10.20.12.45/26'

ip = ipv4.split('/')[0]
mascara_sub_rede = int(ipv4.split('/')[1])
hosts = 2 **(32-mascara_sub_rede) - 2

lt_ip = ip.split('.')
lt_bin = []
for i in lt_ip:
    n = str(bin(int(i))[2:])
    
    if len(n) < 8:
        numeros_zeros = 8 - len(n)
        n = (numeros_zeros * '0') + n
        lt_bin.append(n)
        
m = mascara_sub_rede

for lista in lt_bin:
    for i in lista:
        print(i, m)
        
        m -= 1
        if m < 0:
            m = 0

    print()



