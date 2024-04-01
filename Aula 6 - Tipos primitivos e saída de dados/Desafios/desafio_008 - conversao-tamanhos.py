print('='*20, end=' ')
print('Desafio 008 - Conversão de Tamanhos', end=' ')
print('='*20)

# Solicita o tamanho em metros
metros = float(input('Informe o tamanho em metros: '))

# Converte o valor em centímetros e milímetros
centimetros = metros * 100
milimetros = metros * 1000

# Exibe os resultados
print('{} metro(s) equivale(m) à {} centímetros'.format(metros, centimetros))
print('{} metro(s) equivale(m) à {} milímetros'.format(metros, milimetros))
