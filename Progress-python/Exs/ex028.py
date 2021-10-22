# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random as ra
print('-=-' * 20)
number = int(input('Em que número eu pensei: '))
print('-=-' * 20)
ra =  ra.randrange(5)
print('Processando...')
if number == ra:
    print('PARABENS! Você conseguiu me vencer!')
else:
    print(f'Ganhei! Eu pensei no número {ra} e não no {number}')

# OR

import random as ra
from time import sleep

print('-=-' * 20)
n1 = int(input('Em que número eu pensei: '))
print('-=-' * 20)
n2 = ra.randrange(5)
print('Processando...')
sleep(2)
print('PARABENS'if n2 == n1 else f'Ganhei! Eu pensei no número {n2} e não no {n1}')