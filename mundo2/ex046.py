# Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos de artigicio indo de 10 até 0. Com uma pausa de 1 segundo entre eles.

for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('BOOM!')