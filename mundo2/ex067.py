# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('digite um número inteiro'))
    
    if num > 0:
        for i in range(11):
            print(f'{num} x {i} = {num*i}')
    else:
        print('fim do programa...')
        break
