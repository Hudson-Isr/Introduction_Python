# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
v =  float(input('Qual é a velocidade atual do carro: '))

if v > 80:
    print("Multado! Você excedeu o limite permitido que é 80Km/h")
    m = (v - 80) * 7
    print(f'você deve pagar uma multa de R${m:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')