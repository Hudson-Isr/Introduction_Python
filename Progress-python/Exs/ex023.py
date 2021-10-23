# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Achar Unidade, Dezena, Centena...de um número em Python

numero = int(input('Informe um numero: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f"""Analisando o numero: {numero}
Unidade:{u}
Dezena:{d}
Centena:{c}
Milhar:{m} """)
