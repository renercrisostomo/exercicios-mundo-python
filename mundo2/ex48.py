# Faça um programa que calcula a soma entre todos os números impates que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = sum([x for x in range(1, 501) if x % 3 == 0])
print(f'soma: {soma}')
