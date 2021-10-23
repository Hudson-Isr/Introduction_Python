# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

name = str(input('Digite seu nome completo: ')).strip()
name = name.split()

print(f"""Muito prazer em te conhecer!
Seu Primerio nome é {name[0]}
Seu Último nome é {name[-1]}""")