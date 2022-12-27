#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km
#e R$0,45 para viagens mais longas.

distancia = int(input('digite a distância em Km: '))
if distancia > 0:
    precoPassagem = distancia * 0.5 if distancia <= 200 else distancia * 0.45
    print(f'o preço da passagem é igual a R$:{precoPassagem}')
else:
    print('distância menor que zero')
