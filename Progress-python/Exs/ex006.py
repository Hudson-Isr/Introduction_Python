# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math

x = int(input("Digite um número: "))

d = (x*2)
t = (x*3)
r = float(x)**0.5  #raiz quadrada
#r = math.pow(x, 1/2)
#r = x ** (1/2)

print(f'O dobro de {x} vale {d}\nO dobro de {x} vale {t}\nO dobro de {x} vale {r}')