# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiroTermo = int(input('digite o primeiro termo: '))
razao = int(input('digite a razão: '))

n = 1
while n < 11:
    termo = primeiroTermo + (n - 1) * razao
    print(termo)
    n += 1
