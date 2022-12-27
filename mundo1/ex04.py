#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

valor = input("digite o valor")
print(f'Você digitou: {valor}')
print(f'O tipo primitivo desse valor é {valor.type()}')
print(f'Só tem espaços? {valor.isspace()}')
print(f'É um número? {valor.isnumeric()}')
print(f'É alfabético? {valor.isalpha()}')
print(f'É alfanumérico {valor.isalnum()}')
print(f'Está em maiúsculas? {valor.isupper()}')
print(f'Está em minúsculas? {valor.islower()}')
print(f'Está capitalizada? {valor.istitle()}')