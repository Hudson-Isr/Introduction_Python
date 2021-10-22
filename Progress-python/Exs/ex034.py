# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
s =  float(input('Qual é o salario do funcionario? R$'))

if s <= 1250:
    s1 = s * 1.15
    print(f'Quem ganhava R${s:.2f} passa a ganhar R${s1:.2f} agora. ')
else:
    s2 = s * 1.10
    print(f'Quem ganhava R${s:.2f} passa a ganhar R${s2:.2f} agora. ')