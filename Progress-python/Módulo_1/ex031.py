# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

v = int(input('Qual é a distancia da sua viagem: '))

if v <= 200:
    print(f'Você está prestes a começar uma viagem de {v:.1f}KM.')
    p1 = v * 0.5
    print(f'E o preço da sua passagem será de R${p1:.2f}')
else:
    print(f'Você está prestes a começar uma viagem de {v:.1f}KM.')
    p2 = v * 0.45
    print(f'E o preço da sua passagem será de R${p2:.2f}')