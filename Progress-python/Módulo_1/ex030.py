# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Me diga um número qualquer: '))
p = n %2
if p == 0:
    print(f'O numero {n} é PAR')
else:
    print(f'O número {n} é IMPAR')