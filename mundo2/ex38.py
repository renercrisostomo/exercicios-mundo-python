# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem.
# o primeiro valor é maior; o segundo valor é maior; não eciste valor maior. os dois são iguais.

num1 = int(input('digite o primeiro número: '))
num2 = int(input('digite o segundo número: '))

if num1 > num2:
    print('o primeiro número é maior')
elif num1 < num2:
    print('o segundo número é maior')
else:
    print('os números são iguais')
