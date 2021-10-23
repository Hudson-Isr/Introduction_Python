# crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Em qual cidade você nasceu: ')).strip()
print(cidade[:5].lower() == 'santo')

#OR

cidade = input('Em qual cidade você nasceu: ').strip()
ci = cidade.lower()
ci = "santo" in ci

print(f'{ci}')