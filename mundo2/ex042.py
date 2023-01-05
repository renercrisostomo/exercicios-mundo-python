# Refaça o desafio 35 dos triângulos, acrecentando o recurso de mostrar que tipo de triângulo será formado:
# equilátero: todos os lados iguais; isósceles: dois lados iguais; escaleno: todos os lados diferentes

A = int(input("Lado A = "))
B = int(input("Lado B = "))
C = int(input("Lado C = "))

if A + B >= C and A + C >= B and B + C >= A and A > 0 and B > 0 and C > 0:
    print("\nTipo do triangulo: ")
    if A == B and B == C:
        print("Equilatero (Todos os lados iguais)") 
    elif A != B and A != C and B != C:
        print("Escaleno (Todos os lados diferentes)")
    else: print("Isosceles (2 lados iguais)")       
else: print ("\nEssas medidas nao formam um triangulo.")