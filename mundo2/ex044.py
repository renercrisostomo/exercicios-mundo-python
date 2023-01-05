# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e consição de pagamento:
# à vista dinheiro/cheque: 10% de desconto; à vista no cartão: 5% de desconto; em até 2x no cartão: preço normal; 3x ou mais no cartão: 20% de juros

precoNormal = float(input('digite o preço do produto: '))
tipoPagamento = int(input('digite o tipo de pagamento: '))

if tipoPagamento == 1:
    print(f'a vista dinheiro ou cheque: R$: {precoNormal - precoNormal * 0.1}')
elif tipoPagamento == 2:
    print(f'à vista no cartão: R$: {precoNormal - precoNormal * 0.05}')    
elif tipoPagamento == 3:
    print(f'em até 2x no cartão: R$: {precoNormal}')    
elif tipoPagamento == 4:
    print(f'3x ou mais no cartão: R$: {precoNormal + precoNormal * 0.2}')    
else:
    print(f'tipo inválido')    