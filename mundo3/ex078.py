# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

num = []
for c in range(0, 5):
    num.append(int(input('Digite um número: ')))

print(f'O maior valor digitado foi {max(num)} nas posições ', end='')
for i, v in enumerate(num):
    if v == max(num):
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {min(num)} nas posições ', end='')
for i, v in enumerate(num):
    if v == min(num):
        print(f'{i}...', end='')
print()
