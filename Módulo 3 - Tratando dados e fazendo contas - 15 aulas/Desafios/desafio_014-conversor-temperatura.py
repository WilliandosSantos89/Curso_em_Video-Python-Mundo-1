print('=' *20, end=' ')
print('Desafio 014 - Conversor de Temperatura', end=' ')
print('=' *20)

celsios = float(input('Informe a temperatura em °C: '))

fahrenheit = (celsios * 1.8) + 32

print('A temperatura de {:.1f}°C corresponde a {:.1f}°F!'.format(celsios, fahrenheit))