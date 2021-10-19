
# Nesse modelo nao é possivel fazer o resultado de uma lista de numero
def dobro(x):
    return x*2

valor = 2
print(dobro(valor))

# OU
def dobro(x):
    return x*2

valor = [1,2,3,4,5]

valor_dobrado = map(dobro, valor)


for v in valor_dobrado: #ou de forma mais simplis pode ser usando "valor_dobrado = list(valor_dobrado)"
    print(v) 