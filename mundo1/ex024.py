#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

palavras = str('digite o nome da cidade').split(' ')

if palavras[0].upper == 'SANTO':
    print('começa com o nome "Santo"')
else:
    print('não começa com o nome "Santo"')