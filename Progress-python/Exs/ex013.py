# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sf = float(input("Qual é o salario do funcionario? R$"))

r = sf + (sf * 15/100)

print(f'Um funcionario que ganhava R${sf}, com 15% de aumento, passa a receber R${r:.2f}')