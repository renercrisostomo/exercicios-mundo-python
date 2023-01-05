# Crie um programa que faça o computador jogar Jokempô com você

from random import randint

itens = ['Pedra', 'Papel', 'Tesoura']
escolhaPC = randint(0, 2)
escolhaPessoa = int(input('Digite sua escolha (0: Pedra, 1: Papel, 2: Tesoura)'))

if not (0 < escolhaPessoa < 2):
    if escolhaPessoa == escolhaPC:
        print('empate')
    elif escolhaP
        