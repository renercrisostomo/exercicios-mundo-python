#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas.
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome.

nomeCompleto = str(input('digite seu nome completo: '))
print(f'maiusculas: {nomeCompleto.upper()}')
print(f'minusculas: {nomeCompleto.lower()}')
print(f'quantidade de letras (sem contar os espaços): {len(nomeCompleto) - nomeCompleto.count(" ")}')
print(f'quantidade de letras no primeiro nome: {len(nomeCompleto.split(" ")[0])}')