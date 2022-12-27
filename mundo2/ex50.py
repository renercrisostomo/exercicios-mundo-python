# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o

numeros = []
for x in range(0, 6):
    numeros.append(int(input(f'digite o {x + 1}º número: ')))

soma = sum([x for x in numeros if x % 2 == 0])

print(f'soma = {soma}')
