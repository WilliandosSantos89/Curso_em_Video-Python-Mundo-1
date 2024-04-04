import math

print('=' *20, end=' ')
print('Desafio 018 - Seno e Coseno', end=' ')
print('=' *20)

angulo = float(input('Informe o valor do ângulo: '))

print('Seno - {:.2f}'.format(math.sin(angulo)))
print('Coseno - {:.2f}'.format(math.cos(angulo)))
print('Tangente - {:.2f}'.format(math.tan(angulo)))