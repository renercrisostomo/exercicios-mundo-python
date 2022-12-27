#Escreva um programa que leia a velocidade de um carro.

#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. 
#A multa vai custar R$7,00 por cada km acima do limite.

velocidade = 88
print(f'multado no valor de R$:{(velocidade - 80)*7}') if velocidade > 80 else print('não multado')