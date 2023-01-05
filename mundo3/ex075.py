# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.

numero = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print ('Você digitou os valores', numero)

pares = []
posicoesTres = []

contNoves = 0
for n in numero:
    if n == 9:
        contNoves = contNoves + 1
    if n == 3:
        posicoesTres.append(numero.index(n) + 1)
    if n % 2 == 0:
        pares.append(n)

if contNoves == 0:
    print('O valor 9 não foi digitado')
else:
    print(f'O valor 9 foi digitado {contNoves} vezes')

if len(posicoesTres) == 0:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print('O valor 3 foi digitado na(s) posição(ões)', posicoesTres)

if len(pares) == 0:
    print('Não foram digitados números pares')
else:
    print('Os números pares digitados foram', pares)
