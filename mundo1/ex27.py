#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.
#Ex: Ana Maria de Souza
#primeiro = Ana
#último = Souza
#Obs: programa tem que funcionar pra qualquer tamanho de string.

nomes = str(input('digite seu nome completo: ')).split()
print(f'primeiro nome: {nomes[0]+1}')
print(f'último nome: {nomes[-1]+1}')
