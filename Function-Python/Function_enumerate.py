lista = ["abacate","bola", "cachorro"]

for i in range(len(lista)):
    print(i, lista[i])

# Ou pode ser feito assim:

lista = ["abacate","bola", "cachorro"]

for i, nome in enumerate(lista):
    print(i, nome)
