# Crie um programa que leia dois valores e mostre um menu como ao lado na tela:
# Seu programa deverá realizar a operação solicitada em cadea caso.
# 1 - somar; 2 - multiplicar; 3 - maior; 4 - novos números; 5 - sair do programa

valor1 = int(input('digite o primeiro valor: '))
valor2 = int(input('digite o segundo valor: '))

print('Menu:'
'1 - somar'
'2 - multiplicar'
'3 - maior'
'4 - novos números'
'5 - sair do programa')

opcao = 0
while opcao != 5:
    opcao = str(input('Digite um número de opção: '))
    while 0 > opcao > 5:
        opcao = str(input('Valor inválido. Digite um número das opções do menu: '))
    if opcao == 1:
        print(valor1 + valor2)
    elif opcao == 2:
        print(valor1 * valor2)
    elif opcao == 3:
        print(valor1 > valor2)
    elif opcao == 4:
        print('Novos valores:')
        valor1 = int(input('digite o primeiro valor: '))
        valor2 = int(input('digite o segundo valor: '))
    elif opcao == 5:
        print('saindo do programa...')
    

