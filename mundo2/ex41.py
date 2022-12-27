# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta a mostre sua categoria, de acordo com a idade.
# Até 9 anos: mirim; até 14 anos: infantil; até 19 anos: junior; até 25 anos: sénior; acima: master

from datetime import date

anoAtual = date.today().year
anoNascimento = int(input('Digite o ano de nascimento: '))
idade = anoAtual - anoNascimento

print('categoria: ')
if idade < 9:
    print('mirim')
elif idade < 14:
    print('infantil')
elif idade < 19:
    print('junior') 
elif idade < 25:
    print('sénior')
else:
    print('master')