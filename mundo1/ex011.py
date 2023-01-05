#Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2.

largura = float(input('digite largura em metros'))
altura = float(input('digite altura em metros'))

area = largura * altura
litros = area/2

print(f'precisa de {litros} litros de tinta')