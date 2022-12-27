# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

valor = int(input('Qual o valor a ser sacado? '))

cedulas_50 = valor // 50
resto = valor % 50
cedulas_20 = resto // 20
resto = resto % 20
cedulas_10 = resto // 10
resto = resto % 10
cedulas_1 = resto

print(f'Total de {cedulas_50} cédulas de R$50')
print(f'Total de {cedulas_20} cédulas de R$20')
print(f'Total de {cedulas_10} cédulas de R$10')
print(f'Total de {cedulas_1} cédulas de R$1')
