x = input('Digite algo: ')
print('A função primaria é: ', type(x))
print('Só tem espaços?', x.isspace())
print('É um numero?', x.isnumeric())
print('É alfabetico?', x.isalpha())
print('É alfanumerio?', x.isalnum())
print('Está em maiusculas?', x.isupper())
print('Está em minusculas?', x.islower())
print('Está em captalizada?', x.istitle())

# Ou pode ser feito assim:

a = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(a)}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Está em maiúsculas? {a.isupper()}')
print(f'Está em minúsculas? {a.islower()}')
print(f'Está capitalizado? {a.istitle()}')


