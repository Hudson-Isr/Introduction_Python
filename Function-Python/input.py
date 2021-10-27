# Desafio 1

nome = input('Qual é seu nome: ')

print (f'E um prazer em conhecer, {nome}!')

# Desafio 2 

Dia = input('Dia = ')
Mes = input('Mês = ')
Ano = input('Ano = ')

print('Você nasceu no dia',Dia,'de',Mes,'de',Ano,'. correto?')

# Desafio 3
# Como é a soma de duas variaveis é necessario converter elas em numeros.
n1 = int(input('Primeiro numero: ')) #ou n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: ')) #ou n2 = int(input('Segundo numero: '))
s = n1 + n2

print(f'A soma entre {n1} e {n2} vale {s}') # Novo metodo de usar .format