# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) qual é o total gasto na compra; B) quantos produtos custam mais de R$1000; C) qual é o nome do produto mais barato.

produtos = []
total = 0
menor = None
for produto in range(4):
    nome = input('digite o nome (M ou F) da {produto} produto: ')
    preco = int(input('digite a preco da {produto} produto: '))
    produtos.append({'nome': nome, 'preco': preco})
    total += preco
    if menor == None or preco < menor:
        menor = nome

print(f'total gasto R$: {total}')

# Conta quantas produtos têm mais de 1000 reais
contador = 0
for produto in produtos:
  if produto["preco"] < 1000:
    contador += 1
print(f"Há {contador} produtos com mais de 1000 reais")

print(f'menor preço: R$: {menor}')
