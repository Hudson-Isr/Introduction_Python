# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Qual é o preço do produto? '))

p1 = p - (p * 5/100)

print(f'O produto que custava {p}, na promoção com desconto de 5% vai custar R${p1:.2f}.')