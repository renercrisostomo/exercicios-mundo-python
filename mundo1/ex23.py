#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#Ex: Digite um número: 1834
#unidade:4
#dezena:3
#centena:8
#milhar:1
#Tentar fazer como string e matematicamente: Tem as duas possibilidades, ver qual é melhor.

numeros = str(input('digite o numero de quatro algorismos: ')).split()
print('unidade: {numeros[-1]}')
print('dezena: {numeros[-2]}')
print('centena: {numeros[-3]}')
print('milhar: {numeros[-4]}')
