#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('preço do produto'))
precoDescontado = preco - preco * 5 / 100

print(f'novo preço {precoDescontado}')