print('=' *20, end=' ')
print('Desafio 017 - Calculando a hipotenusa', end=' ')
print('=' *20)

# Solicitação de dados ao usuário
cateto_oposto = float(input('Informe o cateto oposto: '))
cateto_adjaceste = float(input('Informe o cateto adijascente: '))

# Calculo da hipotenusa - **= potência (2 - ao quadrado)
hipotenusa = (cateto_oposto ** 2 + cateto_adjaceste ** 2) ** 0.5

print('{:.2f}'.format(hipotenusa))
