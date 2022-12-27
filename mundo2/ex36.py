# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('digite o valor da casa'))
valorSalario = float(input('digite o valor do salário do comprador'))
anos = int(input('digite em quantos anos vai pagar a casa'))

if prestacao > valorSalario * 0.3:
    print('valor negado')
else:
    prestacao = valorCasa / (anos * 2)
    print(f'o valor a ser pago é {prestacao}')