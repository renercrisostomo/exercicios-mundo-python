#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import suffle

quantidade = int(input('quantidade de alunos'))

nomes = []
for i in range(quantidade):
    nomes.append(input('nome do aluno {i}'))

embaralhado = suffle(nomes)

print(f'ordem: {embaralhado}')