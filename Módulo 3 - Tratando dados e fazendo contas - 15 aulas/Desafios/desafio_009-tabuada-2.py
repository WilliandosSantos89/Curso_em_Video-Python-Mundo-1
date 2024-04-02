n = int(input('Digite um número: '))


# Tabuada de soma
print('-' *20)
print('Tabuada de Soma + ')
print('-' *20)

for count in range(1,11):
    resultado = n + count
    print('{} + {} = {}'.format(n, count, resultado))
print('-' *20)

#Tabuada de subtração
print('Tabuada de Subtração - ')
print('-' *20)

for count in range(1,11):
    resultado = count - n
    print('{} - {} = {}'.format(count, n, resultado))
print('-' *20)

#Tabuada de multiplicação
print('Tabuada de Multiplicação * ')
print('-' *20)

for count in range(1,11):
    resultado = n * count
    print('{} * {} = {}'.format(n, count, resultado))
print('-' *20)

#Tabuada de divisão
print('Tabuada de Divisão / ')
print('-' *20)

for count in range(1,11):
    resultado = n / count
    print('{} / {} = {:3f}'.format(n, count, resultado))
print('-' *20)