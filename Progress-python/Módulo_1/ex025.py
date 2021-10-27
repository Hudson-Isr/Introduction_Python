# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

name = str(input('Diga seu nome completo: ')).strip()
name = name.lower()
name = "silva" in name
print(f'Seu nome tem silva?{name}')
