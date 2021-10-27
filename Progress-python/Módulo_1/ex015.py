# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

diausado = d * 60
kmrodado = km * 0.15

t = diausado + kmrodado

print(f'O total a pagar e de R${t:.2f}')

