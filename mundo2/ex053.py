# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

frase = list(str(input('digite a frase: ')).upper())
fraseRevertida = frase[::-1]
if frase == fraseRevertida:
    print('É palíndromo')
else:
    print('Não é palíndromo')
