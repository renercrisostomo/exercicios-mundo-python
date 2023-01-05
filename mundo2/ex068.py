# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

cont = 0
while True:
    while True:
        escolha = input('par ou ímpar? [P/I]: ').upper()
        if escolha in 'PIÍ' and len(escolha) == 1:
            break

    computador = randint(0, 10)

    while True:
        pessoa = int(input('digite um número inteiro maior ou igual a zero: '))
        if pessoa >= 0:
            break
        
    soma = computador + pessoa

    resultado = 'P' if soma % 2 == 0 else 'IÍ'

    if escolha in resultado:
        cont += 1
        print(f'acertou! {cont} partidas seguidas.')
    else:
        print(f'errou! conseguiu {cont} partidas seguidas.')

