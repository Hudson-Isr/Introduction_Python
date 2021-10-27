# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

f = str(input('Digite uma frase: ')).strip()
f = f.upper()
l = f.find('A') +1
r = f.rfind('A') +1
f = f.count('A')


print(f"""A letra A apareceu {f} Vezes na frase.
A primeira letra A apareceu na posição {l}
A última letra A apareceu na posição {r}""")