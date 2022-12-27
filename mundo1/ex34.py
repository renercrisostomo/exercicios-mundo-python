#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('digite o salário'))

if salario >= 0:
    if salario > 1250:
        salarioNovo = salario + salario * 10/100
    else:
        salarioNovo = salario + salario * 15/100
    print(f'salario novo igual a {salarioNovo}')
else:
    print('Salario negativo')