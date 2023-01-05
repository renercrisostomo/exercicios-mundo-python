# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário; 2 para octal; 3 para hexadecimal

num = int(input('digite um número inteiro: '))
base = input('digite a base de conversão: ')

if base == '1':
    print(f'valor convertido em binário: {bin(num)}')
elif base == '2':
    print(f'valor convertido em octal: {hex(num)}')
elif base == '3':
    print(f'valor convertido em hexadecimal: {hex(num)}')
else:
    print('valor inválido')
