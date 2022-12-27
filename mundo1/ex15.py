#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

quilometros = float(input('digite os quilometros percorridos'))
diasAlugado = int(input('digite a quantidade dias de aluguel'))

preco = 60 * diasAlugado + 0.15 * quilometros

print(f'O preço a pagar é R$:{preco}')