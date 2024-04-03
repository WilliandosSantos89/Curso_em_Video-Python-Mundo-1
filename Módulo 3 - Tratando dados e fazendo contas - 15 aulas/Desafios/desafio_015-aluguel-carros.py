print('=' *20, end=' ')
print('Desafio 015 - Aluguel de Carros', end=' ')
print('=' *20)

"""Programa que pergunte a quantidade de Km percorridos por um carro alugado 
e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 
por Km rodado."""

# Solicitações ao usuário
dias_alugado = float(input('Quantos dias você usou o carro? '))
km_rodados = float(input('Quantos kilômetros foram percorridos? '))

# Calcula os dias usados e os kms rodados
valor_dias = int(dias_alugado * 60)
valor_km = float(km_rodados * 0.15)

# Calcula o valor a ser pago
total_pagar = float(valor_dias + valor_km)

# Exibe os valores
print('Dias alugados: ', dias_alugado)
print('Kms rodados', km_rodados)
print('O total a pagar é de R$ {:.2f}'.format(total_pagar))