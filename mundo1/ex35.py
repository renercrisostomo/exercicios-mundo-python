#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

A = int(input("Lado A = "))
B = int(input("Lado B = "))
C = int(input("Lado C = "))

if A + B >= C and A + C >= B and B + C >= A and A > 0 and B > 0 and C > 0:
    print("\nFormam um triangulo ")
else: print ("\nEssas medidas nao formam um triangulo.")
