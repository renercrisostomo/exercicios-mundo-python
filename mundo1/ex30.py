#Crie um programa que leia um número inteiro e mostre na tela se ela é PAR ou ÍMPAR.

num = int(input('digite um número inteiro: '))
print('o número é ')
print('par') if num % 2 == 0 else print('impar')