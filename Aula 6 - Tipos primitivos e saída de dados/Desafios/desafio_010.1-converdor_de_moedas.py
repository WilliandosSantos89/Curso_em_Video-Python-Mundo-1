import requests
import json

requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')

cotacao = requisicao.json()

print('Moeda: ' + cotacao['USD']['name'])
print('Data: ' + cotacao['USD']['create_data'])
print('Valor atual: R$' + cotacao['USD']['bid'])