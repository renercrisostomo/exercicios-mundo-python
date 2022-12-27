# Refaça o desafio 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('digite um número inteiro'))

for i in range(11):
    print(f'{num} x {i} = {num*i}')
    