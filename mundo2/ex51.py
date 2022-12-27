# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

primeiroTermo = int(input('digite o primeiro termo: '))
razao = int(input('digite a razão: '))

for n in range(1, 11):
    termo = primeiroTermo + (n - 1) * razao
    print(termo)
