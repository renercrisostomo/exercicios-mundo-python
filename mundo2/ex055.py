# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

num = []
for i in range(5):
    num.append(float(input(f"Peso {i + 1}: ")))
print(f"Maior Valor = {max(num)}\nMenor Valor = {min(num)}")