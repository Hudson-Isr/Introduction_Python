"""Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome."""

frase = str(input('Digite seu nome completo: ')).strip()

pn = frase.split()

print(f"""Seu nome em maiúsculas é {frase.upper()}
Seu nome em minúsculas é {frase.lower()}
Seu nome tem ao todo {len(frase) - frase.count(' ')}
Seu primeiro nome é {pn[0]} e ele tem {len(pn[0])} letras.""")