#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import choice

quantidade = int(input('quantidade de alunos'))

nomes = []
for i in range(quantidade):
    nomes.append(input('nome do aluno {i}'))

sortiado = choice(nomes)

print(f'nome sortiado: {sortiado}')