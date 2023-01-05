# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

from rand import randint

numSorteado = randint(0, 5)

num = int(input('qual o número inteiro entre 0 e 5 o commputador escolheu? '))
cont = 0

while num != numSorteado:
    num = str(input('Errou. Tente novamente: '))
    cont += 1

print('Certo.')