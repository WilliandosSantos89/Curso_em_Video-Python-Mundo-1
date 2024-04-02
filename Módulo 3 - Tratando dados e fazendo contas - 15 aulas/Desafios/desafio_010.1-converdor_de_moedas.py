print('=' *20, end=' ')
print('Conversor de Moedas em tempo real', end=' ')
print('=' *20)

#Neste código você pode saber a cotação do dolar em tempo real
#através do consumo de uma API

import requests
import json

# Requisição da API
requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')

# Retorno da API
cotacao = requisicao.json()

# Obtem a data e converte para o formato Brasileiro
data = cotacao['USD']['create_date']
data_formatada = data.split()[0] #Pega apenas a parte da data (sem o horário)
dia, mes, ano = data_formatada.split('-')
data_brasileira = f'{ano}/{mes}/{dia}' #A ordem foi alterada para forçar o formato brasileiro

# Obtem o valor da cotação do dolar
dolar_atual = float(cotacao['USD']['bid'])

# Solicitação ao usuário
real = float(input('Digite o valor em reais: R$ '))

# Calcula o equivalente em dólar
dolar = real * dolar_atual

# Mostra a cotação formatada
print(f'Moeda: {cotacao['USD']['name']}')
print(f'Data: {data_brasileira}')
print(f'Valor atual: R$ {dolar:.2f}') #Duas casas decimais