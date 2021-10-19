idade = int(input("Digite sua idade: "))

if idade >=18:
    print("Maior de idade")
elif idade < 0: 
    while idade < 0:
        print("Digite um valor valido")
else:
    print("Menor de idade")
