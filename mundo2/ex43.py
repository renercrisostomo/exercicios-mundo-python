# Desenvolva uma lógica que leia o peso e a altura de uma pessoa e calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# abaixo de 18.5: abaixo do peso; entre 18.5 e 25: peso ideal; 25 até 30: sobrepeso; 30 até 40: obesidade; acima de 40: obesidade mórbida 

peso = float(input('qual é seu peso? '))
altura = float(input('qual é sua altura? '))

imc = peso / (altura ** 2)

print("\nClassificacao:")
if imc >= 40:
	print("Obesidade Mórbida")
elif imc >= 30:
	print("Obesidade")
elif imc >= 25:
	print("Sobrepeso")
elif imc >= 18.5:
	print("Peso Ideal")
else:
	print("Abaixo do Peso")
    