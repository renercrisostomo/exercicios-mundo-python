# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos; B) quantos homens foram cadastrados; C) quantas mulheres tem menos de 20 anos.

pessoas = []
for pessoa in range(4):
    idade = int(input('digite a idade da {pessoa} pessoa: '))
    sexo = input('digite o sexo (M ou F) da {pessoa} pessoa: ')
    pessoas.append({'idade': idade, 'sexo': sexo})

# Conta quantos homens foram cadastrados
contador = 0
for pessoa in pessoas:
  if pessoa["sexo"] == "M":
    contador += 1
print(f"Há {contador} homens")

# Conta quantas pessoas têm mais de 18 anos
contador = 0
for pessoa in pessoas:
  if pessoa["idade"] > 18:
    contador += 1
print(f"Há {contador} pessoas com mais de 18 anos")

# Conta quantas mulheres têm menos de 20 anos
contador = 0
for pessoa in pessoas:
  if pessoa["sexo"] == "F" and pessoa["idade"] < 20:
    contador += 1
print(f"Há {contador} mulheres com menos de 20 anos")
