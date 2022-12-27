# Crie um programa que leia duas notas de um aluno e calcule sua média. Mostrando uma mensagem no final, de acordo com a média atingida: Média abaixo de 5.0: Reprovado; Média entre 5.0 e 6.9: Recuperação; Média 7.0 ou superior: Aprovado

nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
média = ((nota1+nota2)/2)

print(f'a média é igual a {media}')

if media < 5:
    print('Reprovado')
elif media <= 6.9:
    print('Recuperação')
else:
    print('Aprovado')