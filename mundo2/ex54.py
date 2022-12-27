# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

anoAtual = date.today().year

qtdMaiores = 0
for pessoa in range(7):
    ano = int(input(f'Digite o ano de nascimento do {pessoa + 1}ª pessoa: '))
    idade = anoAtual - anoNascimento
    if idade >= 18:
        qtdMaiores += 1

