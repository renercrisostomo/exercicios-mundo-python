# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = 0
cont = 0
maior = None 
menor = None

while True:
    num = int(input('digite um número inteiro: '))
    
    soma += num
    cont += 1

    if menor == None or num < menor:
        menor = num
    if maior == None or num > maior:
        maior = num

    escolha = str(input('você quer parar? [S ou N]: ')).upper()[0]
    if escolha == 'N':
        break

media = soma/cont
print(f'média = {media}')
print(f'menor valor = {menor}')
print(f'maior valor = {maior}')