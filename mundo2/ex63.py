# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0, 1, 1 ,2, 3, 5, 8...

fibonacci = [0, 1]  #Considerando 1 como a 1ª posicao
qtdTermos = int(input('Digite o número de termos: '))
for posicao in range(2, qtdTermos):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(fibonacci)
