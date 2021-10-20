# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

t =  float(input('Informe a temperatura em Celsius: '))
c = t
f = ((c/5)*9)+32 # formula para Fahrenheit
k = (c/5)+273 # formula para kelvin

print(f'A temperatura de {c}C corresponde a {f:.1f}F')
