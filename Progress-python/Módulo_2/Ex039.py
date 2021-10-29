# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

year = int(input('Ano de nascimento: '))
anos = date.today().year
a = anos - year
print(f'Quem nasceu em {year} tem {a} anos em {anos}.')
if a == 18:
    print(f'Você tem que se alistar IMEDIATAMENTE!')
elif a < 18:
    s = 18 - a 
    print(f'Ainda falta {s} anos para o alistamento')
    alis = anos - s
    print(f'Seu alistamento será em {alis}')
elif a > 18:
    s = a - 18
    print(f'Você já deveria ter se alistado há {s} anos')
    alis = anos - s
    print(f'Seu alistamento será em {alis}')

