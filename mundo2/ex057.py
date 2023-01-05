# Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitaçã novamente até ter um valor correto.

sexo = str(input('informe seu sexo (M ou F): ')).upper()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo (M ou F): '))

print('Dados válidos.')