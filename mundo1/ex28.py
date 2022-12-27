#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

#O programa deverá escrever na tela se o usuário venceu ou perdeu

from rand import randint

numSorteado = randint(0, 5)

num = int(input('qual o número inteiro entre 0 e 5 o commputador escolheu? '))
print(num == numSorteado)
