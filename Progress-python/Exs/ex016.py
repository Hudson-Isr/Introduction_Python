# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc
v = float(input('Digite um valor: '))
q = trunc(v)

print(f'O valor digitado foi {v}, a sua porção interia é {q}')