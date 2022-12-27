#Faça um programa que leia o comprimento do cateto oposo e do cateto adjacente de um triâncgulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.

#Quanto temos um triangulo retangulo temos: cateto oposto, cateto adjacente, angulo de 90 graus e hipotenusa
#Princípio matemático:
#O quadrado da hipotenusa é igual a soma do quadrado dos catetos

catetoOposto = int(input('digite o cateto oposto'))
catetoAdjacente = int(input('digite o cateto adjacente'))

hipotenusa = (catetoAdjacente**2 + catetoOposto**2) ** (1/2)

print(f'hipotenusa: {hipotenusa}')

#ou
#from math import hypot
# hipotenusa = hypot(catetoAdjacente, catetoOposto)