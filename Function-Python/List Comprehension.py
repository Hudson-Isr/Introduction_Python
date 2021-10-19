x = [1,2,3,4,5]
y = [i**2 for i in x]

for i in x:
    y.append(i**2)

print(x)
print(y)

# ou pode ser feito assim com list comprehension

x = [1,2,3,4,]
# y = [valor_a_adicionar laço]
y = [i**6 for i in x]
# z = [valor_a_adicionar laço condição]
# z = [i for i in x if i%2==1] i%2==1 abstrair apenas numeros impares, se fosse numeros pares seria i%2==0 
z = [i for i in x if i%2==0]

print(y)
print(z)