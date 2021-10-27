# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

a = int(input('Digite o angulo que voce deseja: '))

rad = math.radians(a)
sn = math.sin(rad)
cs = math.cos(rad)
tg = math.tan(rad)

print(f'O angulo de {a} tem o SENO de {sn:.2f}\nO angulo de {a} tem o COSSENO de {cs:.2f}\nO angulo de {a} tem o TANGENRE de {tg:.2f}')