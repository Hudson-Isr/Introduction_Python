# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math

comprimentooposto = float(input('Comprimento do cateto oposto: '))
comprimentoadjacente = float(input('Comprimento do cateto adjacente: '))

co = comprimentooposto**2
ca = comprimentoadjacente**2
h = co + ca
h1 = math.sqrt(h)

print(f'A hipotenusa vai medir {h1:.2f}')

# Ou 

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')