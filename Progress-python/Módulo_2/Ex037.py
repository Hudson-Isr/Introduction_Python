#  Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input('Digite um numero inteiro: '))
print("""Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")
n2 = int(input('Sua opção: '))
bin = bin(n)
oct = oct(n)
hex = hex(n)

if n2 == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin[2:]}')
elif n2 == 2:
    print(f'{n} convertido para OCTAL é igual a {oct[2:]}')
else:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex[2:]}')