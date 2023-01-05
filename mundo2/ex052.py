# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

from math import isqrt

num = int(input('digite um número inteiro: '))

print(primo(num))

def primo(numero):
    if numero == 1:
        return False
    for divisor in range(2, isqrt(numero) + 1):
        if numero % (divisor) == 0:
            return False
    return True