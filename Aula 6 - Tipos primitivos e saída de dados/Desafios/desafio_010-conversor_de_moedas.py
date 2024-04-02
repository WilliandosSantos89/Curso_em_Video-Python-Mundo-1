print('=' *20, end=' ')
print('Desafio 010 - Conversor de Moedas $$', end=' ')
print('=' *20)

real = float(input('Insira o valor em Real: R$ '))

dolar = (real * 5.0153)
euro = (real * 5.043)


print('Cotação em Dolar: $ {:.2f}'.format(dolar))
print('Cotação em Euro: EUR {:.2f}'.format(euro))
