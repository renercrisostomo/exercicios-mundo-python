# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos

primeiroTermo = int(input('digite o primeiro termo: '))
razao = int(input('digite a razão: '))

n = 1
while True:
    termo = primeiroTermo + (n - 1) * razao
    print(termo)
    n += 1

    qtdTermos = int(input('Quantos termos a mais você deseja ver? '))
    if qtdTermos == 0:
        break

