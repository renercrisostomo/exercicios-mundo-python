#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
#OBS: pode ter silva em qualquer lugar - o resultado é True ou False

nomeCompleto = str('digite o nome completo').split(' ')

print(f"nome é silva? {nomeCompleto[0].upper == 'SILVA'}")