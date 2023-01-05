# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo; qual é o nome do homem mais velho; quantas mulheres têm menos de 20 anos

pessoas = []
for pessoa in range(4):
    nome = input('digite o nome da {pessoa} pessoa: ')
    idade = int(input('digite a idade da {pessoa} pessoa: '))
    sexo = input('digite o sexo (M ou F) da {pessoa} pessoa: ')
    pessoas.append({'nome': nome, 'idade': idade, 'sexo': sexo})

# Calcula a média de idade do grupo
soma_idades = 0
for pessoa in pessoas:
  soma_idades += pessoa["idade"]
media_idades = soma_idades / len(pessoas)
print("A média de idade do grupo é", media_idades)

# Encontra o nome do homem mais velho
homem_mais_velho = None
idade_homem_mais_velho = 0
for pessoa in pessoas:
  if pessoa["sexo"] == "M" and pessoa["idade"] > idade_homem_mais_velho:
    homem_mais_velho = pessoa["nome"]
    idade_homem_mais_velho = pessoa["idade"]
print("O homem mais velho é", homem_mais_velho)

# Conta quantas mulheres têm menos de 20 anos
contador = 0
for pessoa in pessoas:
  if pessoa["sexo"] == "F" and pessoa["idade"] < 20:
    contador += 1
print("Há", contador, "mulheres com menos de 20 anos")

