# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input("Largura da parede: "))
h = float(input("Altura da parede: "))

a = h*l
m = a/2


print(f'Sua parede tem a dimensão de {l} x {h} e sua parede é de {a}m².')
print(f'Para pintar essa parede, Voce precisa de {m:.2f}L de tinta')