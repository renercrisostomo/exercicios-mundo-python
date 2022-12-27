# Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar. Se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoAtual = date.today().year
anoNascimento = int(input('Digite o ano de nascimento: '))
idade = anoAtual - anoNascimento

if idade > 18:
    print(f'Deveria ter se alistado há {idade - 18} anos')
elif idade == 18:
    print('Tem 18 anos. Deve se alistar')
else: 
    print('Menor de idade, não precisa se alistar')

