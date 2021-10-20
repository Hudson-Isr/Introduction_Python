# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

x = int(input('Qual o valor: '))

print(f'O numero escolhido é {x}, seu antecessor é {x-1}, e seu sucessor é {x+1}')

# OU Melhor forma por variavel
x = int(input('Qual o valor: '))
a = (x - 1)
s = (x + 1)

print(f'O numero escolhido é {x}, seu antecessor é {a}, e seu sucessor é {s}')