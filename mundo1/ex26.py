#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.

frase = str(input('digite uma frase')).upper()
print(f'letras "A": {frase.count("A")}')
print(f'posição da primeira aparição: {frase.find("A")}')
print(f'posição da ultima aparição: {frase.rfind("A")}')