#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será  negado.
c = float(input('Valor da casa: R$'))
s = float(input('Salário do comprardor: R$'))
f = int(input('Quantos anos de financiamento: R$'))
p = c / (f * 12)
m = 0.3 * s

print(f'Para pagar uma casa de R${c:.2f} em {f} anos', end='')
print(f' a prestação será de R${p:.2f}')
if p <= m:
    print('Empréstimo pode ser Concedido!')
else:
    print('Empréstimo Negado!')


