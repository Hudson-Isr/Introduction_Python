# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

x = float(input("Uma distancia em metros: "))
km = x/1000
hm = x/100
dam = x/10
dm = x*10
cm = x*100
mm = x*1000

# para formatar a o 0 apos a virgula, utilizar (:.0f)

print(f'A medida de {x} corresponde a\n{km}km\n{hm}hm\n{dam}dam\n{dm:.0f}dm\n{cm:.0f}cm\n{mm:.0f}mm')
